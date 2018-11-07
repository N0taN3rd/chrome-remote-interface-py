# -*- coding: utf-8 -*-
import asyncio
import logging
import traceback
import ujson as json
from asyncio import Future, AbstractEventLoop, Task
from typing import Callable, Optional, Dict, ClassVar, Union, TYPE_CHECKING

import attr
import websockets
import websockets.protocol
from pyee import EventEmitter
from websockets import WebSocketClientProtocol

from .errors import NetworkError

if TYPE_CHECKING:
    from .client import Client, TargetSession

__all__ = ["Connection", "CDPSession", "ConnectionEvents", "createProtocolError"]

logger = logging.getLogger(__name__)


def createProtocolError(method: str, msg: Dict) -> str:
    error = msg["error"]
    data = error.get("data")
    emsg = f"Protocol Error ({method}): {error.get('message')}"
    if data:
        emsg += f" {data}"
    return emsg


@attr.dataclass
class ConnectionEvents(object):
    Disconnected: str = attr.ib(default="Disconnected")


class Connection(EventEmitter):
    """Chrome DevTools Protocol Connection Class.

    This class provides the websocket communication for using the CDP.
    """

    Events: ClassVar[ConnectionEvents] = ConnectionEvents()

    def __init__(self, ws_url: str, loop: Optional[AbstractEventLoop] = None) -> None:
        """Construct a new instance of the CDP Client.

        :param ws_url: The WS endpoint of the remote instance
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        super().__init__(loop=loop)
        self.connected: bool = False
        self._url: str = ws_url
        self._lastId: int = 0
        self._callbacks: Dict[int, Future] = dict()
        self._ws: WebSocketClientProtocol = None
        self._recv_task: Optional[Task] = None
        self._closeCallback: Optional[Callable[[], None]] = None
        self._sessions: Dict[str, Union[CDPSession, "TargetSession"]] = dict()
        self._closed: bool = False

    @property
    def loop(self) -> AbstractEventLoop:
        return self._loop

    @property
    def url(self) -> str:
        """Get connected WebSocket url."""
        return self._url

    async def connect(self) -> None:
        """Connect to the remote websocket endpoint"""
        self._ws = await websockets.client.connect(
            self._url,
            ping_interval=None,  # chrome no ping pong and websockets closes down on no pong :'(
            max_size=None,
            compression=None,
            max_queue=2 ** 7,
            loop=self._loop,
        )
        self._recv_task = self._loop.create_task(self._recv_loop())

    async def createSession(self, targetId: str) -> "CDPSession":
        """Attach to the target specified by target id and create new TargetSession for direct communication to it."""
        resp = await self.send("Target.attachToTarget", {"targetId": targetId})
        sessionId = resp.get("sessionId")
        session = CDPSession(self, targetId, sessionId)
        self._sessions[sessionId] = session
        return session

    def set_close_callback(self, callback: Callable[[], None]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    def send(self, method: str, params: Optional[Dict] = None) -> Future:
        """Send a protocol msg to the remote chrome instance.

        :param method: The method to be used
        :param params: The optional parameters (arguments) for the command
        :return: A future that resolves once the commands response is received
        """
        if self._lastId and not self.connected:
            raise NetworkError("Connection is closed")
        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(method=method, params=params, id=_id))
        callback: Future = self._loop.create_future()
        callback.method = method  # type: ignore
        self._callbacks[_id] = callback
        self._loop.create_task(self._send_async(msg, _id))
        return callback

    async def dispose(self) -> None:
        """Close all connection."""
        self.connected = False
        await self._on_close()

    async def _recv_loop(self) -> None:
        """Loop that listens for messages from the remote chrome instance and handles them.

        When a msg is received, the _on_message method is called with the raw msg contents.
        """
        self.connected = True
        while self.connected:
            try:
                resp = await self._ws.recv()
                if resp:
                    self._on_message(resp)
            except (websockets.ConnectionClosed, ConnectionResetError) as e:
                logger.info("connection closed")
                break
            await asyncio.sleep(0)
        if self.connected:
            self._loop.create_task(self.dispose())

    async def _send_async(self, msg: str, callback_id: int) -> None:
        """Actually send the msg to remote instance.

        :param msg: The msg to send
        :param callback_id: The id identifying the callback associated with the msg
        """
        while not self.connected:
            await asyncio.sleep(0)

        try:
            await self._ws.send(msg)
        except websockets.ConnectionClosed:
            logger.error("connection unexpectedly closed")
            callback = self._callbacks.get(callback_id, None)
            if callback and not callback.done():
                callback.set_result(None)
                await self.dispose()

    def _on_message(self, message: str) -> None:
        """Handles a message received from the remote browser instance.

        If the message contains a callback id, _on_response is called with the parsed message.
        Otherwise _on_unsolicited is called with the parsed message.
        :param message: The JSON message string.
        """
        msg = json.loads(message)
        _id = msg.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(msg.get("id", -1))
            if callback and not callback.done():
                if "error" in msg:
                    callback.set_exception(
                        NetworkError(createProtocolError(callback.method, msg))
                    )
                else:
                    callback.set_result(msg.get("result"))
        else:
            params = msg.get("params", {})
            method = msg.get("method", "")
            sessionId = params.get("sessionId")
            try:
                if method == "Target.receivedMessageFromTarget":
                    session = self._sessions.get(sessionId)
                    if session:
                        session.on_message(params.get("message"))
                elif method == "Target.detachedFromTarget":
                    session = self._sessions.get(sessionId)
                    if session:
                        session.on_closed()
                        del self._sessions[sessionId]
                else:
                    self.emit(method, params)
            except Exception as e:
                traceback.print_exc()
                print(f"_on_unsolicited error {method}", e)
                print(f"_on_unsolicited error {method}", params)

    async def _on_close(self) -> None:
        """Closes the websocket connection and cleans up internals.

        All pending protocol method callbacks are canceled and the receive loop is stopped.
        Calls the on close callback if it was supplied and the "connection-closed" method is emitted
        """
        if self._closed:
            return
        self._closed = True
        if self._closeCallback:
            self._closeCallback()
            self._closeCallback = None

        for cb in self._callbacks.values():
            if not cb.done():
                cb.set_exception(
                    NetworkError(f"Protocol error {cb.method}: Target closed.")
                )
        self._callbacks.clear()

        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()

        # close connection
        if not self._ws.closed:
            try:
                await self._ws.close()
            except Exception:
                pass

        if self._recv_task is not None and not self._recv_task.done():
            self._recv_task.cancel()

        self.emit(self.Events.Disconnected)

    def __await__(self) -> "Connection":
        yield from self.connect().__await__()
        return self

    def __str__(self) -> str:
        return f"Connection(wsurl={self._url}, connected={self.connected})"

    def __repr__(self) -> str:
        return self.__str__()


class CDPSession(EventEmitter):
    def __init__(
        self, connection: Union[Connection, "Client"], targetId: str, sessionId: str
    ) -> None:
        """Make new session."""
        super().__init__(loop=connection.loop)
        self._lastId: int = 0
        self._callbacks: Dict[int, Future] = dict()
        self._connection: Union[Connection, "Client"] = connection
        self._targetId: str = targetId
        self._sessionId: str = sessionId
        self._sessions: Dict[str, Union[CDPSession, "TargetSession"]] = dict()

    @property
    def loop(self) -> AbstractEventLoop:
        return self._loop

    def send(self, method: str, params: Optional[dict] = None) -> Future:
        """Send message to the connected session.
        :arg str method: Protocol method name.
        :arg dict params: Optional method parameters.
        """
        if not self._connection:
            raise NetworkError(
                f"Protocol Error ({method}): Session closed. Most likely the "
                f"target has been closed."
            )

        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(id=_id, method=method, params=params))
        callback: Future = self._connection._loop.create_future()
        self._callbacks[_id] = callback
        callback.method = method
        try:
            self._connection.send(
                "Target.sendMessageToTarget",
                {"sessionId": self._sessionId, "message": msg},
            )
        except Exception as e:
            # The response from target might have been already dispatched
            if _id in self._callbacks:
                cb = self._callbacks[_id]
                del self._callbacks[_id]
                if not cb.done():
                    cb.set_exception(NetworkError(e.args[0]))
        return callback

    async def detach(self) -> None:
        """Detach session from target.
        Once detached, session won't emit any events and can't be used to send
        messages.
        """
        if not self._connection:
            raise NetworkError("TargetSession already closed.")
        await self._connection.send(
            "Target.detachFromTarget", {"sessionId": self._sessionId}
        )

    def create_session(self, targetId: str, sessionId: str) -> "CDPSession":
        sesh = CDPSession(self._connection, targetId, sessionId)
        self._sessions[sessionId] = sesh
        return sesh

    def on_message(self, message: str) -> None:
        obj = json.loads(message)
        _id = obj.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if "error" in obj:
                callback.set_exception(
                    NetworkError(createProtocolError(callback.method, obj))
                )
            else:
                result = obj.get("result")
                if callback and not callback.done():
                    callback.set_result(result)
        else:
            method = obj.get("method")
            params = obj.get("params")
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(params.get("sessionId"))
                if session is not None:
                    session.on_message(params.get("message"))
            elif method == "Target.detachedFromTarget":
                sessionId = params.get("sessionId")
                session = self._sessions.get(sessionId)
                if session is not None:
                    session.on_closed()
                    del self._sessions[sessionId]
            self.emit(method, params)

    def on_closed(self) -> None:
        for cb in self._callbacks.values():
            if not cb.done():
                cb.set_exception(
                    NetworkError(
                        f"Protocol error {cb.method}: Target closed."  # type: ignore
                    )
                )
        self._callbacks.clear()
        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()
        self._connection = None

    def __str__(self) -> str:
        return f"CDPSession(targetId={self._targetId}, sessionId={self._sessionId})"

    def __repr__(self) -> str:
        return self.__str__()
