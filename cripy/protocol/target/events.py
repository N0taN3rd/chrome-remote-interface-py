from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.target.types import (
    TargetInfo,
    SessionID,
    TargetID,
)


class AttachedToTargetEvent(BaseEvent):
    """
    Issued when attached to target because of auto-attach or `attachToTarget` command.
    """

    event = "Target.attachedToTarget"

    def __init__(self, sessionId: SessionID, targetInfo: Union[TargetInfo, dict], waitingForDebugger: bool) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AttachedToTargetEvent']:
        if init is not None:
            return AttachedToTargetEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AttachedToTargetEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttachedToTargetEvent(**it))
            return list_of_self
        else:
            return init


class DetachedFromTargetEvent(BaseEvent):
    """
    Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it.
    """

    event = "Target.detachedFromTarget"

    def __init__(self, sessionId: SessionID, targetId: Optional[TargetID] = None) -> None:
        """
        :param sessionId: Detached session identifier.
        :type sessionId: str
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        super().__init__()
        self.sessionId = sessionId
        self.targetId = targetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DetachedFromTargetEvent']:
        if init is not None:
            return DetachedFromTargetEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DetachedFromTargetEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DetachedFromTargetEvent(**it))
            return list_of_self
        else:
            return init


class ReceivedMessageFromTargetEvent(BaseEvent):
    """
    Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event).
    """

    event = "Target.receivedMessageFromTarget"

    def __init__(self, sessionId: SessionID, message: str, targetId: Optional[TargetID] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ReceivedMessageFromTargetEvent']:
        if init is not None:
            return ReceivedMessageFromTargetEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ReceivedMessageFromTargetEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReceivedMessageFromTargetEvent(**it))
            return list_of_self
        else:
            return init


class TargetCreatedEvent(BaseEvent):
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TargetCreatedEvent']:
        if init is not None:
            return TargetCreatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetCreatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCreatedEvent(**it))
            return list_of_self
        else:
            return init


class TargetDestroyedEvent(BaseEvent):
    """
    Issued when a target is destroyed.
    """

    event = "Target.targetDestroyed"

    def __init__(self, targetId: TargetID) -> None:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        super().__init__()
        self.targetId = targetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TargetDestroyedEvent']:
        if init is not None:
            return TargetDestroyedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetDestroyedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetDestroyedEvent(**it))
            return list_of_self
        else:
            return init


class TargetInfoChangedEvent(BaseEvent):
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TargetInfoChangedEvent']:
        if init is not None:
            return TargetInfoChangedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetInfoChangedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfoChangedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Target.attachedToTarget": AttachedToTargetEvent,
   "Target.detachedFromTarget": DetachedFromTargetEvent,
   "Target.receivedMessageFromTarget": ReceivedMessageFromTargetEvent,
   "Target.targetCreated": TargetCreatedEvent,
   "Target.targetDestroyed": TargetDestroyedEvent,
   "Target.targetInfoChanged": TargetInfoChangedEvent,
}

