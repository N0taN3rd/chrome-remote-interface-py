from asyncio import AbstractEventLoop, get_event_loop
from typing import ClassVar, Dict, Optional, TYPE_CHECKING, Type, Union

from ujson import dumps, loads
from pyee2 import EventEmitterS

from .cdp_result_future import CDPResultFuture
from .errors import NetworkError, create_protocol_error
from .events import SessionEvents

if TYPE_CHECKING:  # pragma: no cover
    from cripy import ConnectionType, SessionType  # noqa: F401


class CDPSession(EventEmitterS):
    __slots__ = [
        "_lastId",
        "_connection",
        "_target_type",
        "_session_id",
        "_flat_session",
        "_callbacks",
        "_sessions",
    ]

    Events: ClassVar[Type[SessionEvents]] = SessionEvents

    def __init__(
        self,
        connection: Union["ConnectionType", "SessionType"],
        target_type: str,
        session_id: str,
        flat_session: bool = False,
    ) -> None:
        """Make new session

        :param connection: The connection to use
        :param target_type: The type of the target connected to
        :param session_id: The id of the session being connected to
        :param flat_session: Should any sessions created from this session
        using flat session mode
        """
        _loop: AbstractEventLoop = (
            connection.loop if connection.loop is not None else get_event_loop()
        )  # pragma: no cover
        super().__init__(loop=_loop)
        self._lastId: int = 0
        self._connection: Union["ConnectionType", "SessionType"] = connection
        self._target_type: str = target_type
        self._session_id: str = session_id
        self._flat_session: bool = flat_session
        self._callbacks: Dict[int, CDPResultFuture] = {}
        self._sessions: Dict[str, SessionType] = {}

    @property
    def loop(self) -> AbstractEventLoop:
        """Returns the instance of event loop"""
        return self._loop

    @property
    def flat_session(self) -> bool:
        """Returns T/F indicating if flat session mode is enabled"""
        return self._flat_session

    @property
    def session_id(self) -> str:
        """Returns the id of the session"""
        return self._session_id

    @property
    def target_type(self) -> str:
        """Returns the type of the target"""
        return self._target_type

    def send(self, method: str, params: Optional[Dict] = None) -> CDPResultFuture:
        """Send message to the connected session.

        :param method: Protocol method name
        :param params: Optional method parameters
        :return: A future that resolves once a response has been received
        """
        if not self._connection:  # pragma: no cover
            raise NetworkError(
                f"Protocol Error ({method}): Session closed. Most likely the "
                f"target {self._target_type} has been closed."
            )
        if params is None:
            params = {}
        if self._flat_session:
            _id = self._connection._raw_send(
                {"method": method, "params": params, "sessionId": self.session_id}
            )
            callback = CDPResultFuture(method, self._loop)
            self._callbacks[_id] = callback
            return callback
        self._lastId += 1
        _id = self._lastId
        msg = dumps({"id": _id, "method": method, "params": params})
        callback = CDPResultFuture(method, self._loop)
        self._callbacks[_id] = callback
        self._connection.send(
            "Target.sendMessageToTarget",
            {"sessionId": self._session_id, "message": msg},
        )
        return callback

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
        session = CDPSession(
            connection, target_type, session_id, flat_session=self._flat_session
        )
        if self._flat_session:
            self._connection.add_session(session)
        else:
            self._sessions[session_id] = session
        return session

    def on_message(self, maybe_str_or_dict: Union[str, Dict]) -> None:
        """Handles the recite of a message. Depending on if flat session
        mode is enabled the message supplied to this method will be either
        a string (non-flat more) or a dict (flat mode).

        :param maybe_str_or_dict: The message received
        """
        if isinstance(maybe_str_or_dict, str):
            obj = loads(maybe_str_or_dict)
        else:
            obj = maybe_str_or_dict
        _id = obj.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if "error" in obj:
                # Checking state of the future object.
                # It can be canceled.
                if callback and not callback.done():
                    callback.set_exception(create_protocol_error(callback.method, obj))
            else:
                result = obj.get("result")
                if callback and not callback.done():
                    callback.set_result(result)
            return
        method = obj.get("method")
        params = obj.get("params")
        if not self._flat_session:
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(params.get("sessionId"))
                if session is not None:
                    session.on_message(params.get("message"))
                return
            if method == "Target.detachedFromTarget":
                session_id = params.get("sessionId")
                session = self._sessions.get(session_id)
                if session is not None:
                    session.on_closed()
                    del self._sessions[session_id]
            return
        self.emit(method, params)

    def on_closed(self) -> None:
        """Close this session"""
        for cb in self._callbacks.values():
            if not cb.done():
                cb.set_exception(
                    NetworkError(
                        f"Network error {cb.method}: {self._target_type} closed."
                    )
                )
        self._callbacks.clear()
        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()
        self._connection = None
        self.emit(SessionEvents.Disconnected)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(target={self._target_type}, sessionId={self._session_id})"

    def __repr__(self) -> str:
        return self.__str__()
