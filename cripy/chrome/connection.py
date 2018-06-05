import asyncio
import ujson as json
import logging
from typing import Optional, List, Dict, Union, Callable, Any
from pyee import EventEmitter
import websockets
import websockets.protocol

from cripy.protocol import ProtocolMixin

logger = logging.getLogger(__name__)

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
TIMEOUT_S = 25
MAX_PAYLOAD_SIZE_BYTES = 2 ** 30
MAX_PAYLOAD_SIZE_MB = MAX_PAYLOAD_SIZE_BYTES / 1024 ** 2  # ~ 1GB


class NetworkError(Exception):  # noqa: D204
    """Network/Protocol related exception."""

    pass


class Connection(ProtocolMixin, EventEmitter):

    def __init__(self, url: str, delay: int = 0, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._url = url
        self._message_id = 0
        self._callbacks: Dict[int, asyncio.Future] = dict()
        self._delay = delay
        self._sessions: Dict[str, CDPSession] = dict()
        self.connected = False
        self._ws = None
        self._recv_fut = None
        self._closeCallback: Optional[Callable[[], None]] = None

    @staticmethod
    async def createForWebSocket(url: str, delay: int = 0) -> "Connection":
        con = Connection(url, delay)
        await con.connect()
        return con

    async def connect(self):
        self._ws = await websockets.client.connect(
            self._url, compression=None, max_queue=0, timeout=20
        )
        self._recv_fut = asyncio.ensure_future(self._recv_loop())

    @property
    def url(self) -> str:
        """Get connected WebSocket url."""
        return self._url

    async def send(self, method: str = None, params: dict = None) -> None:
        if params is None:
            params = dict()
        self._message_id += 1
        _id = self._message_id
        msg = json.dumps(dict(method=method, params=params, id=_id))
        asyncio.ensure_future(self._send_async(msg))
        callback = asyncio.get_event_loop().create_future()
        self._callbacks[_id] = callback
        callback.method = method  # type: ignore
        return callback

    async def dispose(self) -> None:
        """Close all connection."""
        self.connected = False
        await self._on_close()

    async def createSession(self, targetId: str) -> "CDPSession":
        """Create new session."""
        resp = await self.Target.attachToTarget(targetId)
        sessionId = resp.get("sessionId")
        session = CDPSession(self, targetId, sessionId)
        self._sessions[sessionId] = session
        return session

    def set_close_callback(self, callback: Callable[[], None]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    async def _recv_loop(self):
        self.connected = True
        while self.connected:
            try:
                resp = await self._ws.recv()
                # print(resp)
                if resp:
                    self._on_message(resp)
            except (websockets.ConnectionClosed, ConnectionResetError) as e:
                print("websocket dead", e)
                logger.info("connection closed")
                break
        print("disposing")

    def _on_message(self, message: str) -> None:
        msg = json.loads(message)
        if msg.get("id") in self._callbacks:
            self._on_response(msg)
        else:
            self._on_unsolicited(msg)

    def _on_response(self, msg: dict) -> None:
        callback = self._callbacks.pop(msg.get("id", -1))
        if "error" in msg:
            error = msg["error"]
            callback.set_exception(NetworkError(f"Protocol Error: {error}"))
        else:
            callback.set_result(msg.get("result"))

    def _on_unsolicited(self, msg: dict) -> None:
        params = msg.get("params", {})
        method = msg.get("method", "")
        if method in self.protocol_events:
            params = self.protocol_events[method].safe_create(params)
        try:
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(params.sessionId)
                if session:
                    session.on_message(params.message)
            elif method == "Target.detachedFromTarget":
                session = self._sessions.get(params.sessionId)
                if session:
                    session.on_closed()
                    del self._sessions[params.sessionId]
            else:
                self.emit(method, params)
        except Exception as e:
            print(e)
            print(params)

    async def _send_async(self, msg: str) -> None:
        while not self.connected:
            await asyncio.sleep(0)
        await self._ws.send(msg)

    async def _on_close(self) -> None:
        if self._closeCallback:
            self._closeCallback()
            self._closeCallback = None

        for cb in self._callbacks.values():
            cb.cancel()
        self._callbacks.clear()

        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()

        # close connection
        if not self._recv_fut.done():
            self._recv_fut.cancel()
        if not self._ws.closed:
            await self._ws.close()


class CDPSession(ProtocolMixin, EventEmitter):

    def __init__(
        self, connection: Connection, targetId: str, sessionId: str, *args, **kwargs
    ) -> None:
        """Make new session."""
        super().__init__(*args, **kwargs)
        self._lastId = 0
        self._callbacks: Dict[int, asyncio.Future] = {}
        self._connection: Optional[Connection] = connection
        self._targetId = targetId
        self._sessionId = sessionId
        self._sessions: Dict[str, CDPSession] = dict()

    async def send(self, method: str, params: dict = None) -> Any:
        """Send message to the connected session.
        :arg str method: Protocol method name.
        :arg dict params: Optional method parameters.
        """
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(id=_id, method=method, params=params))

        callback = asyncio.get_event_loop().create_future()
        self._callbacks[_id] = callback
        callback.method: str = method  # type: ignore

        if not self._connection:
            raise NetworkError("Connection closed.")
        await self._connection.Target.sendMessageToTarget(
            msg, sessionId=self._sessionId
        )
        return await callback

    async def detach(self) -> None:
        """Detach session from target.
        Once detached, session won't emit any events and can't be used to send
        messages.
        """
        if not self._connection:
            raise NetworkError("Connection already closed.")
        await self._connection.Target.detachFromTarget(self._sessionId)

    def create_session(self, targetId: str, sessionId: str) -> "CDPSession":
        sesh = CDPSession(self._connection, targetId, sessionId)
        self._sessions[sessionId] = sesh
        return sesh

    def on_message(self, message: str) -> None:
        # print('CDPSession.on_message', message)
        msg = json.loads(message)
        _id = msg.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if "error" in msg:
                error = msg["error"]
                msg = error.get("message")
                data = error.get("data")
                callback.set_exception(NetworkError(f"Protocol Error: {msg} {data}"))
            else:
                result = msg.get("result")
                callback.set_result(result)
        else:
            method = msg.get("method")
            params = msg.get("params")
            if method in self.protocol_events:
                params = self.protocol_events[method].safe_create(params)
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(params.sesionId)
                if session:
                    session.on_message(params.message)
            elif method == "Target.detachedFromTarget":
                session = self._sessions.get(params.sesionId)
                if session:
                    session.on_closed()
                    del self._sessions[params.sesionId]
            else:
                self.emit(method, params)

    def on_closed(self) -> None:
        for cb in self._callbacks.values():
            cb.cancel()
        self._callbacks.clear()
        self._connection = None
