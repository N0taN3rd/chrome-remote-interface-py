import logging
from asyncio import AbstractEventLoop, Event, Task, get_event_loop, sleep
from inspect import isawaitable
from typing import Any, Callable, ClassVar, Dict, Optional, TYPE_CHECKING, Type, Union

from async_timeout import timeout
from pyee2 import EventEmitterS
from ujson import dumps, loads
from websockets import ConnectionClosed, WebSocketClientProtocol, connect

from .cdp_result_future import CDPResultFuture
from .cdp_session import CDPSession
from .errors import NetworkError, create_protocol_error
from .events import ConnectionEvents

if TYPE_CHECKING:  # pragma: no cover
    from cripy import ConnectionType, SessionType  # noqa: F401

__all__ = ["Connection"]

logger = logging.getLogger(__name__)


class Connection(EventEmitterS):
    """Chrome DevTools Protocol Connection Class.

    This class provides the websocket communication for using the CDP.
    """

    __slots__ = [
        "_callbacks",
        "_closeCallback",
        "_closed",
        "_connected",
        "_flatten_sessions",
        "_lastId",
        "_recv_task",
        "_sessions",
        "_ws",
        "_ws_url",
    ]

    Events: ClassVar[Type[ConnectionEvents]] = ConnectionEvents

    def __init__(
        self,
        ws_url: Optional[str] = None,
        flatten_sessions: bool = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        """Construct a new instance of the CDP Client.

        :param ws_url: The WS endpoint of the remote instance.
        If a ws url is not supplied it is expected to be supplied via connect.
        :param flatten_sessions: Enables "flat" access to the session via specifying sessionId
        attribute in the commands
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        """
        if loop is None:
            loop = get_event_loop()
        super().__init__(loop=loop)
        self._connected: bool = False
        self._closed: bool = False
        self._flatten_sessions: bool = flatten_sessions
        self._ws_url: str = ws_url
        self._lastId: int = 0
        self._callbacks: Dict[int, CDPResultFuture] = {}
        self._sessions: Dict[str, "SessionType"] = {}
        self._ws: Optional[WebSocketClientProtocol] = None
        self._recv_task: Optional[Task] = None
        self._closeCallback: Optional[Callable[[], Any]] = None

    @staticmethod
    def from_session(session: "SessionType") -> "ConnectionType":
        """Returns the underlying connection given a session

        :param session: The session to retrieve the underlying connection
        :return: The underlying connection
        """
        if session.flat_session:
            return session._connection
        conn = session._connection
        while not isinstance(conn, Connection):
            conn = conn._connection
        return conn

    @property
    def loop(self) -> AbstractEventLoop:
        """Returns the event loop the connection is using"""
        return self._loop

    @property
    def ws_url(self) -> str:
        """Get connected WebSocket url"""
        return self._ws_url

    @property
    def closed(self) -> bool:
        """Returns T/F indicating if the connection is closed"""
        return self._closed

    def add_session(self, session: "SessionType") -> None:
        """Adds the supplied session to the tracked sessions

        :param session: The session to be tracked
        """
        self._sessions[session.session_id] = session

    def set_close_callback(self, callback: Callable[[], Any]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    def session(self, session_id: str) -> Optional[CDPSession]:
        """Returns the session instance associated with the supplied
        session id.

        :param session_id: The id of the session to be retrieved
        :return: The session instance associated with the id if it exists
        """
        return self._sessions.get(session_id)

    def send(self, method: str, params: Optional[Dict] = None) -> CDPResultFuture:
        """Send a command to the remote chrome instance.

        :param str method: The method to be used
        :param dict params: The optional parameters (arguments) for the command
        :return: A future that resolves once the commands response is received
        """
        if self._lastId and not self._connected:
            raise NetworkError("Connection is closed")
        if params is None:
            params = {}
        _id = self._raw_send({"method": method, "params": params})
        callback = CDPResultFuture(method, loop=self._loop)
        self._callbacks[_id] = callback
        return callback

    async def connect(
        self, ws_url: Optional[str] = None, flatten_sessions: Optional[bool] = None
    ) -> None:
        """Connect to the remote websocket endpoint

        :param ws_url: The websocket URL to connect to
        :param flatten_sessions: Should flat session mode be used
        """
        if ws_url is not None:
            self._ws_url = ws_url
        if flatten_sessions is not None:
            self._flatten_sessions = flatten_sessions
        self._ws = await connect(
            self._ws_url,
            ping_interval=None,  # chrome no ping pong and websockets closes down on no pong :'(
            ping_timeout=None,
            max_size=None,
            compression=None,
            max_queue=2 ** 7,
            loop=self._loop,
        )
        self._closed = False
        # ensure that _recv_loop gets going
        ready_event = Event(loop=self._loop)
        self._recv_task = self._loop.create_task(self._recv_loop())
        self.once(ConnectionEvents.Ready, lambda: ready_event.set())
        await ready_event.wait()

    async def create_session(self, target_id: str) -> CDPSession:
        """Attach to the target specified by the supplied target id and creates new CDPSession for
        direct communication to it

        :param target_id: The id of the target connecting to
        :return: A new session connected to the target
        """
        params: Dict[str, Union[str, bool]] = {"targetId": target_id}
        if self._flatten_sessions:
            params["flatten"] = self._flatten_sessions
        resp = await self.send("Target.attachToTarget", params)
        session_id = resp.get("sessionId")
        if self._flatten_sessions:
            session = self._sessions.get(session_id)
            if session:
                return session
        session = self._new_session(resp.get("type", "unknown"), session_id)
        self._sessions[session_id] = session
        return session

    async def dispose(self) -> None:
        """Close all open connections"""
        self._connected = False
        await self._on_close()

    async def _recv_loop(self) -> None:
        """Loop that listens for messages from the remote chrome instance and handles them.

        When a msg is received, the _on_message method is called with the raw msg contents.
        """
        self._connected = True
        self.emit(ConnectionEvents.Ready)
        self_ws_recv = self._ws.recv
        self_on_message = self._on_message
        logger_info = logger.info
        connected = self.__connected

        while 1:
            try:
                resp = await self_ws_recv()
                if resp:
                    self_on_message(resp)
            except (ConnectionClosed, ConnectionResetError):
                logger_info("connection closed")
                break
            if not connected():
                break

        if self._connected:
            await self.dispose()  # pragma: no cover

    def __connected(self) -> bool:
        """Helper method for _recv_loop
        :return: T/F indicating if we are still connected
        """
        return self._connected

    async def _send_async(self, msg: str, callback_id: int) -> None:
        """Actually send the msg to remote instance.

        :param msg: The msg to send
        :param callback_id: The id identifying the callback associated with the msg
        """
        while not self._connected:
            await sleep(0)  # pragma: no cover

        try:
            await self._ws.send(msg)
        except ConnectionClosed:
            logger.error("connection unexpectedly closed")
            callback = self._callbacks.get(callback_id, None)
            if callback and not callback.done():
                callback.set_result(None)
                await self.dispose()

    async def _on_close(self) -> None:
        """Closes the websocket connection and cleans up internals.

        All pending protocol method callbacks are canceled and the receive loop is stopped.
        Calls the on close callback if it was supplied and the "connection-closed" method
        is emitted
        """
        if self._closed:  # pragma: no cover
            return
        self._closed = True

        for cb in self._callbacks.values():
            if not cb.done():  # pragma: no cover
                cb.set_exception(NetworkError(f"{cb.method}: Target closed."))
        self._callbacks.clear()

        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()

        # close connection
        if self._ws and not self._ws.closed:
            try:
                async with timeout(15, loop=self._loop):
                    await self._ws.close()
            except Exception:  # pragma: no cover
                pass

        if self._recv_task is not None and not self._recv_task.done():
            self._recv_task.cancel()
            try:
                async with timeout(15, loop=self._loop):
                    await self._recv_task
            except Exception:  # pragma: no cover
                pass

        if self._closeCallback:
            ret = self._closeCallback()
            if isawaitable(ret):
                try:
                    await ret
                except Exception:
                    pass
            self._closeCallback = None

        self.emit(ConnectionEvents.Disconnected)

    def _raw_send(self, msg: Dict) -> int:
        """Sends a message to the remote browser returning
        the id of the message

        :param msg: The message to be sent
        :return: The id of the message sent
        """
        self._lastId += 1
        _id = self._lastId
        msg["id"] = _id
        self._loop.create_task(self._send_async(dumps(msg), _id))
        return _id

    def _on_message(self, message: str) -> None:
        """Handles a message received from the remote browser instance.

        If the message contains a callback id, the future associated with the id has
        its result set or exception set if the command was unsuccessful.
        Otherwise the if the method is for a target the message is forwarded to the CDPSession
        and if it is not for a target it is emitted.

        :param message: The JSON message string.
        """
        msg = loads(message)
        self._log_msg(msg)
        if not self._flatten_sessions:
            return self._on_message_non_flat(msg)
        _id = msg.get("id")
        params = msg.get("params", {})
        method = msg.get("method", "")
        if method == "Target.attachedToTarget":
            session_id = params.get("sessionId")
            self._sessions[session_id] = self._new_session(
                params.get("targetInfo", {}).get("type", "unknown"), session_id
            )
        elif method == "Target.detachedFromTarget":
            session_id = params.get("sessionId", None)
            session = self._sessions.get(session_id)
            if session:
                session.on_closed()
                del self._sessions[session_id]

        session_id = msg.get("sessionId", None)
        if session_id:
            session = self._sessions.get(session_id)
            if session:
                session.on_message(msg)
            return
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if not callback.done():
                if "error" in msg:
                    callback.set_exception(create_protocol_error(callback.method, msg))
                else:
                    callback.set_result(msg.get("result"))
            return
        self.emit(method, params)

    def _on_message_non_flat(self, msg: Dict) -> None:
        """Handles a message received from the remote browser instance when
        flat sessions are not used.

        If the message contains a callback id, the future associated with the id has
        its result set or exception set if the command was unsuccessful.
        Otherwise the if the method is for a target the message is forwarded to the CDPSession
        and if it is not for a target it is emitted.

        :param msg: The JSON message string.
        """
        _id = msg.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if callback and not callback.done():
                if "error" in msg:
                    callback.set_exception(create_protocol_error(callback.method, msg))
                else:
                    callback.set_result(msg.get("result"))
            return
        params = msg.get("params", {})
        method = msg.get("method", "")
        session_id = params.get("sessionId")
        if method == "Target.receivedMessageFromTarget":
            session = self._sessions.get(session_id)
            if session:
                session.on_message(params.get("message"))
            return
        if method == "Target.detachedFromTarget":
            session = self._sessions.get(session_id)
            if session:
                session.on_closed()
                del self._sessions[session_id]
            return
        self.emit(method, params)

    def _new_session(self, target_type: str, session_id: str) -> CDPSession:
        """Creates a new session connected to the target

        :param target_type: The type of the session
        :param session_id: The id of the session
        :return: A CDPSession connected to the target
        """
        return CDPSession(
            self, target_type, session_id, flat_session=self._flatten_sessions
        )

    def _log_msg(self, msg: Dict) -> None:
        """Utility function to log all received messages IFF someone is listening

        :param msg: The message to maybe be emitted
        """
        if self.has_listeners(ConnectionEvents.AllMessages):
            self.emit(ConnectionEvents.AllMessages, msg)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(wsurl={self._ws_url}, connected={self._connected})"

    def __repr__(self) -> str:
        return self.__str__()
