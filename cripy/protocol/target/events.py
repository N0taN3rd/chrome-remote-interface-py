from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.target.types import *
except ImportError:
    pass


class AttachedToTargetEvent(object):
    """
    Issued when attached to target because of auto-attach or `attachToTarget` command.
    """

    event = "Target.attachedToTarget"

    def __init__(
        self,
        sessionId: str,
        targetInfo: Union[TargetInfo, dict],
        waitingForDebugger: bool,
    ) -> None:
        """
        :param sessionId: Identifier assigned to the session used to send/receive messages.
        :type sessionId: str
        :param targetInfo: The targetInfo
        :type targetInfo: dict
        :param waitingForDebugger: The waitingForDebugger
        :type waitingForDebugger: bool
        """
        super().__init__()
        self.sessionId = sessionId
        self.targetInfo = TargetInfo.safe_create(targetInfo)
        self.waitingForDebugger = waitingForDebugger

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        if self.waitingForDebugger is not None:
            repr_args.append("waitingForDebugger={!r}".format(self.waitingForDebugger))
        return "AttachedToTargetEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["AttachedToTargetEvent", dict]]:
        if init is not None:
            try:
                ourselves = AttachedToTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AttachedToTargetEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttachedToTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DetachedFromTargetEvent(object):
    """
    Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it.
    """

    event = "Target.detachedFromTarget"

    def __init__(self, sessionId: str, targetId: Optional[str] = None) -> None:
        """
        :param sessionId: Detached session identifier.
        :type sessionId: str
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        super().__init__()
        self.sessionId = sessionId
        self.targetId = targetId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "DetachedFromTargetEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["DetachedFromTargetEvent", dict]]:
        if init is not None:
            try:
                ourselves = DetachedFromTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DetachedFromTargetEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DetachedFromTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ReceivedMessageFromTargetEvent(object):
    """
    Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event).
    """

    event = "Target.receivedMessageFromTarget"

    def __init__(
        self, sessionId: str, message: str, targetId: Optional[str] = None
    ) -> None:
        """
        :param sessionId: Identifier of a session which sends a message.
        :type sessionId: str
        :param message: The message
        :type message: str
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        super().__init__()
        self.sessionId = sessionId
        self.message = message
        self.targetId = targetId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "ReceivedMessageFromTargetEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ReceivedMessageFromTargetEvent", dict]]:
        if init is not None:
            try:
                ourselves = ReceivedMessageFromTargetEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ReceivedMessageFromTargetEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReceivedMessageFromTargetEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetCreatedEvent(object):
    """
    Issued when a possible inspection target is created.
    """

    event = "Target.targetCreated"

    def __init__(self, targetInfo: Union[TargetInfo, dict]) -> None:
        """
        :param targetInfo: The targetInfo
        :type targetInfo: dict
        """
        super().__init__()
        self.targetInfo = TargetInfo.safe_create(targetInfo)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        return "TargetCreatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["TargetCreatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = TargetCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["TargetCreatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetDestroyedEvent(object):
    """
    Issued when a target is destroyed.
    """

    event = "Target.targetDestroyed"

    def __init__(self, targetId: str) -> None:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        super().__init__()
        self.targetId = targetId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "TargetDestroyedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["TargetDestroyedEvent", dict]]:
        if init is not None:
            try:
                ourselves = TargetDestroyedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["TargetDestroyedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetDestroyedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetCrashedEvent(object):
    """
    Issued when a target has crashed.
    """

    event = "Target.targetCrashed"

    def __init__(self, targetId: str, status: str, errorCode: int) -> None:
        """
        :param targetId: The targetId
        :type targetId: str
        :param status: Termination status type.
        :type status: str
        :param errorCode: Termination error code.
        :type errorCode: int
        """
        super().__init__()
        self.targetId = targetId
        self.status = status
        self.errorCode = errorCode

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        if self.errorCode is not None:
            repr_args.append("errorCode={!r}".format(self.errorCode))
        return "TargetCrashedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["TargetCrashedEvent", dict]]:
        if init is not None:
            try:
                ourselves = TargetCrashedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["TargetCrashedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCrashedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetInfoChangedEvent(object):
    """
    Issued when some information about a target has changed.
	This only happens between `targetCreated` and `targetDestroyed`.
    """

    event = "Target.targetInfoChanged"

    def __init__(self, targetInfo: Union[TargetInfo, dict]) -> None:
        """
        :param targetInfo: The targetInfo
        :type targetInfo: dict
        """
        super().__init__()
        self.targetInfo = TargetInfo.safe_create(targetInfo)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.targetInfo is not None:
            repr_args.append("targetInfo={!r}".format(self.targetInfo))
        return "TargetInfoChangedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["TargetInfoChangedEvent", dict]]:
        if init is not None:
            try:
                ourselves = TargetInfoChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["TargetInfoChangedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfoChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Target.attachedToTarget": AttachedToTargetEvent,
    "Target.detachedFromTarget": DetachedFromTargetEvent,
    "Target.receivedMessageFromTarget": ReceivedMessageFromTargetEvent,
    "Target.targetCreated": TargetCreatedEvent,
    "Target.targetDestroyed": TargetDestroyedEvent,
    "Target.targetCrashed": TargetCrashedEvent,
    "Target.targetInfoChanged": TargetInfoChangedEvent,
}

EVENT_NS = SimpleNamespace(
    AttachedToTarget="Target.attachedToTarget",
    DetachedFromTarget="Target.detachedFromTarget",
    ReceivedMessageFromTarget="Target.receivedMessageFromTarget",
    TargetCreated="Target.targetCreated",
    TargetDestroyed="Target.targetDestroyed",
    TargetCrashed="Target.targetCrashed",
    TargetInfoChanged="Target.targetInfoChanged",
)
