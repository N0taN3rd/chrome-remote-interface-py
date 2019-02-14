# -*- coding: utf-8 -*-
import asyncio
import logging
from asyncio import (
    AbstractEventLoop,
    Future,
    Task,
    get_event_loop as aio_get_event_loop,
    sleep as aio_sleep,
)
from typing import Callable, Optional, Dict, ClassVar, Union, TYPE_CHECKING
from ujson import loads as ujson_loads, dumps as ujson_dumps

from async_timeout import timeout
from pyee2 import EventEmitter
from websockets import WebSocketClientProtocol, ConnectionClosed, connect as wsconnect

from .errors import NetworkError, ConnectionClosedError
from .events import ConnectionEvents, SessionEvents

if TYPE_CHECKING:  # pragma: no cover
    from .client import Client, TargetSession  # noqa: F401

__all__ = ["CDPResultFuture", "CDPSession", "Connection", "create_protocol_error"]

logger = logging.getLogger(__name__)


def create_protocol_error(method: str, msg: Dict) -> str:
    error = msg["error"]
    data = error.get("data")
    emsg = f"Protocol Error ({method}): {error.get('message')}"
    if data:
        emsg += f" {data}"
    return emsg


class CDPResultFuture(Future):
    """A subclass of asyncio.Future to make linting happy about adding method to it"""

    def __init__(self, method: str, loop: Optional[AbstractEventLoop] = None) -> None:
        super().__init__(loop=loop)
        self.method: str = method


class Connection(EventEmitter):
    """Chrome DevTools Protocol Connection Class.

    This class provides the websocket communication for using the CDP.
    """

    Events: ClassVar[ConnectionEvents] = ConnectionEvents()

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
            loop = aio_get_event_loop()
        super().__init__(loop=loop)
        self._connected: bool = False
        self._ws_url: str = ws_url
        self._lastId: int = 0
        self._closed: bool = False
        self._flatten_sessions: bool = flatten_sessions
        self._callbacks: Dict[int, CDPResultFuture] = dict()
        self._sessions: Dict[str, Union[CDPSession, "TargetSession"]] = dict()
        self._ws: WebSocketClientProtocol = None
        self._recv_task: Optional[Task] = None
        self._closeCallback: Optional[Callable[[], None]] = None

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
        return self._closed

    def add_session(self, session: Union["CDPSession", "TargetSession"]) -> None:
        self._sessions[session.session_id] = session

    def set_close_callback(self, callback: Callable[[], None]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    async def connect(
        self, ws_url: Optional[str] = None, flatten_sessions: Optional[bool] = None
    ) -> None:
        """Connect to the remote websocket endpoint"""
        if ws_url is not None:
            self._ws_url = ws_url
        if flatten_sessions is not None:
            self._flatten_sessions = flatten_sessions
        self._ws = await wsconnect(
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
        ready_event = asyncio.Event(loop=self._loop)
        self._recv_task = self._loop.create_task(self._recv_loop())
        self.once(Connection.Events.Ready, lambda: ready_event.set())
        await ready_event.wait()

    async def create_session(self, target_id: str) -> "CDPSession":
        """Attach to the target specified by the supplied target id and creates new CDPSession for
        direct communication to it

        :param target_id: The id of the target connecting to
        :return: A new session connected to the target
        """
        params = {"targetId": target_id}
        if self._flatten_sessions:
            params["flatten"] = self._flatten_sessions
        resp = await self.send("Target.attachToTarget", params)
        session_id = resp.get("sessionId")
        if self._flatten_sessions:
            session = self._sessions.get(session_id)
            if session:
                return session
        session = CDPSession(
            self, resp.get("type", "unknown"), session_id, self._flatten_sessions
        )
        self._sessions[session_id] = session
        return session

    def send(self, method: str, params: Optional[Dict] = None) -> Future:
        """Send a command to the remote chrome instance.

        :param str method: The method to be used
        :param dict params: The optional parameters (arguments) for the command
        :return: A future that resolves once the commands response is received
        """
        if self._lastId and not self._connected:
            raise NetworkError("Connection is closed")
        if params is None:
            params = dict()
        _id = self._raw_send(method, params)
        callback = CDPResultFuture(method, loop=self._loop)
        self._callbacks[_id] = callback
        return callback

    async def dispose(self) -> None:
        """Close all connection."""
        self._connected = False
        await self._on_close()

    async def _recv_loop(self) -> None:
        """Loop that listens for messages from the remote chrome instance and handles them.

        When a msg is received, the _on_message method is called with the raw msg contents.
        """
        self._connected = True
        self.emit(Connection.Events.Ready)
        self_ws_recv = self._ws.recv
        self_on_message = self._on_message
        logger_info = logger.info
        while self._connected:
            try:
                resp = await self_ws_recv()
                if resp:
                    self_on_message(resp)
            except (ConnectionClosed, ConnectionResetError):
                logger_info("connection closed")
                break
        if self._connected:
            await self.dispose()  # pragma: no cover

    async def _send_async(self, msg: str, callback_id: int) -> None:
        """Actually send the msg to remote instance.

        :param msg: The msg to send
        :param callback_id: The id identifying the callback associated with the msg
        """
        while not self._connected:
            await aio_sleep(0)  # pragma: no cover

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
                cb.set_exception(ConnectionClosedError(f"{cb.method}: Target closed."))
        self._callbacks.clear()

        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()

        # close connection
        if self._ws and not self._ws.closed:
            try:
                async with timeout(10, loop=self._loop):
                    await self._ws.close()
            except Exception:  # pragma: no cover
                pass

        if self._recv_task is not None and not self._recv_task.done():
            self._recv_task.cancel()
            try:
                async with timeout(10, loop=self._loop):
                    await self._recv_task
            except Exception:  # pragma: no cover
                pass

        if self._closeCallback:
            self._closeCallback()
            self._closeCallback = None

        self.emit(Connection.Events.Disconnected)

    def _raw_send(self, method: str, params: Dict) -> int:
        self._lastId += 1
        _id = self._lastId
        msg = ujson_dumps(dict(method=method, params=params, id=_id))
        self._loop.create_task(self._send_async(msg, _id))
        return _id

    def _on_message(self, message: str) -> None:
        """Handles a message received from the remote browser instance.

        If the message contains a callback id, the future associated with the id has
        its result set or exception set if the command was unsuccessful.
        Otherwise the if the method is for a target the message is forwarded to the CDPSession
        and if it is not for a target it is emitted.

        :param message: The JSON message string.
        """
        if not self._flatten_sessions:
            return self._on_message_non_flat(message)
        msg = ujson_loads(message)
        _id = msg.get("id")
        params = msg.get("params", {})
        method = msg.get("method", "")
        session_id = params.get("sessionId", None)
        if method == "Target.attachedToTarget":
            pass
        elif method == "Target.detachedFromTarget":
            session = self._sessions.get(session_id)
            if session:
                session.on_closed()
                del self._sessions[session_id]

        if session_id:
            session = self._sessions.get(session_id)
            if session:
                session.on_message(msg)
        elif _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if not callback.done():
                if "error" in msg:
                    callback.set_exception(
                        NetworkError(create_protocol_error(callback.method, msg))
                    )
                else:
                    callback.set_result(msg.get("result"))
        else:
            self.emit(method, params)

    def _on_message_non_flat(self, message: str) -> None:
        msg = ujson_loads(message)
        _id = msg.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if callback and not callback.done():
                if "error" in msg:
                    callback.set_exception(
                        NetworkError(create_protocol_error(callback.method, msg))
                    )
                else:
                    callback.set_result(msg.get("result"))
        else:
            params = msg.get("params", {})
            method = msg.get("method", "")
            session_id = params.get("sessionId")
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(session_id)
                if session:
                    session.on_message(params.get("message"))
            elif method == "Target.detachedFromTarget":
                session = self._sessions.get(session_id)
                if session:
                    session.on_closed()
                    del self._sessions[session_id]
            else:
                self.emit(method, params)

    def _new_session(self, target_type: str, session_id: str) -> "CDPSession":
        return CDPSession(self, )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(wsurl={self._ws_url}, connected={self._connected})"

    def __repr__(self) -> str:
        return self.__str__()


class CDPSession(EventEmitter):
    Events: ClassVar[SessionEvents] = SessionEvents()

    def __init__(
        self,
        connection: Union[Connection, "Client", "CDPSession", "TargetSession"],
        target_type: str,
        session_id: str,
        flat_session: bool = False,
    ) -> None:
        """Make new session."""
        _loop = (
            connection.loop if connection.loop is not None else aio_get_event_loop()
        )  # pragma: no cover
        super().__init__(loop=_loop)
        self._lastId: int = 0
        self._connection: Union[
            Connection, "Client", "CDPSession", "TargetSession"
        ] = connection
        self._target_type: str = target_type
        self._session_id: str = session_id
        self._flat_session: bool = flat_session
        self._callbacks: Dict[int, CDPResultFuture] = dict()
        self._sessions: Dict[str, Union[CDPSession, "TargetSession"]] = dict()

    @property
    def loop(self) -> AbstractEventLoop:
        return self._loop

    @property
    def flat_session(self) -> bool:
        return self._flat_session

    @property
    def session_id(self) -> str:
        return self._session_id

    @property
    def target_type(self) -> str:
        return self._target_type

    def send(self, method: str, params: Optional[dict] = None) -> Future:
        """Send message to the connected session.
        :arg str method: Protocol method name.
        :arg dict params: Optional method parameters.
        """
        if not self._connection:  # pragma: no cover
            raise ConnectionClosedError(
                f"Protocol Error ({method}): Session closed. Most likely the "
                f"target {self._target_type} has been closed."
            )
        if self._flat_session:
            _id = self._connection._raw_send(method, params)
            callback = CDPResultFuture(method, self._loop)
            self._callbacks[_id] = callback
            return callback
        return self._send_non_flat(method, params)

    async def detach(self) -> None:
        """Detach session from target. Once detached, session won't emit any events and
        can't be used to send messages.
        """
        if not self._connection:
            raise NetworkError(f"CDPSession for {self._target_type} already closed.")
        await self._connection.send(
            "Target.detachFromTarget", {"sessionId": self._session_id}
        )

    def create_session(self, target_type: str, session_id: str) -> "CDPSession":
        """Creates a new session for the target being connected to specified
        by the session_id

        :param target_type: The type of the target being connected to
        :param session_id: The session id used to communicate to the target
        :return: A new session connected to the target
        """
        connection = self._connection if self._flat_session else self
        session = CDPSession(connection, target_type, session_id, self._flat_session)
        if self._flat_session:
            self._connection.add_session(session)
        else:
            self._sessions[session_id] = session
        return session

    def on_message(self, message: str) -> None:
        obj = ujson_loads(message)
        _id = obj.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if "error" in obj:
                callback.set_exception(
                    NetworkError(create_protocol_error(callback.method, obj))
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
                    ConnectionClosedError(
                        f"Protocol error {cb.method}: {self._target_type} closed."
                    )
                )
        self._callbacks.clear()
        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()
        self._connection = None
        self.emit(CDPSession.Events.Disconnected)

    def _send_non_flat(self, method: str, params: Optional[dict] = None) -> Future:
        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = ujson_dumps(dict(id=_id, method=method, params=params))
        callback = CDPResultFuture(method, self._loop)
        self._callbacks[_id] = callback
        try:
            self._connection.send(
                "Target.sendMessageToTarget",
                {"sessionId": self._session_id, "message": msg},
            )
        except Exception as e:
            # The response from target might have been already dispatched
            if _id in self._callbacks:
                cb = self._callbacks[_id]
                del self._callbacks[_id]
                if not cb.done():
                    cb.set_exception(NetworkError(e.args[0]))
        return callback

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(target={self._target_type}, sessionId={self._session_id})"

    def __repr__(self) -> str:
        return self.__str__()
