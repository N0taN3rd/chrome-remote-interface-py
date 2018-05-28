from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.target.types import (
    TargetInfo,
    TargetID,
    SessionID,
)


class AttachedToTargetEvent(BaseEvent):
    """Issued when attached to target because of auto-attach or `attachToTarget` command."""

    event: str = "Target.attachedToTarget"

    def __init__(self, sessionId: SessionID, targetInfo: TargetInfo, waitingForDebugger: bool) -> None:
        """
        :param sessionId: Identifier assigned to the session used to send/receive messages.
        :type sessionId: SessionID
        :param targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        :param waitingForDebugger: The waitingForDebugger
        :type waitingForDebugger: bool
        """
        super().__init__()
        self.sessionId: SessionID = sessionId
        self.targetInfo: TargetInfo = targetInfo
        self.waitingForDebugger: bool = waitingForDebugger


class DetachedFromTargetEvent(BaseEvent):
    """Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it."""

    event: str = "Target.detachedFromTarget"

    def __init__(self, sessionId: SessionID, targetId: Optional[TargetID] = None) -> None:
        """
        :param sessionId: Detached session identifier.
        :type sessionId: SessionID
        :param targetId: Deprecated.
        :type targetId: TargetID
        """
        super().__init__()
        self.sessionId: SessionID = sessionId
        self.targetId: Optional[TargetID] = targetId


class ReceivedMessageFromTargetEvent(BaseEvent):
    """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""

    event: str = "Target.receivedMessageFromTarget"

    def __init__(self, sessionId: SessionID, message: str, targetId: Optional[TargetID] = None) -> None:
        """
        :param sessionId: Identifier of a session which sends a message.
        :type sessionId: SessionID
        :param message: The message
        :type message: str
        :param targetId: Deprecated.
        :type targetId: TargetID
        """
        super().__init__()
        self.sessionId: SessionID = sessionId
        self.message: str = message
        self.targetId: Optional[TargetID] = targetId


class TargetCreatedEvent(BaseEvent):
    """Issued when a possible inspection target is created."""

    event: str = "Target.targetCreated"

    def __init__(self, targetInfo: TargetInfo) -> None:
        """
        :param targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        """
        super().__init__()
        self.targetInfo: TargetInfo = targetInfo


class TargetDestroyedEvent(BaseEvent):
    """Issued when a target is destroyed."""

    event: str = "Target.targetDestroyed"

    def __init__(self, targetId: TargetID) -> None:
        """
        :param targetId: The targetId
        :type targetId: TargetID
        """
        super().__init__()
        self.targetId: TargetID = targetId


class TargetInfoChangedEvent(BaseEvent):
    """Issued when some information about a target has changed.
	This only happens between `targetCreated` and `targetDestroyed`."""

    event: str = "Target.targetInfoChanged"

    def __init__(self, targetInfo: TargetInfo) -> None:
        """
        :param targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        """
        super().__init__()
        self.targetInfo: TargetInfo = targetInfo


EVENT_TO_CLASS = {
   "Target.attachedToTarget": AttachedToTargetEvent,
   "Target.detachedFromTarget": DetachedFromTargetEvent,
   "Target.receivedMessageFromTarget": ReceivedMessageFromTargetEvent,
   "Target.targetCreated": TargetCreatedEvent,
   "Target.targetDestroyed": TargetDestroyedEvent,
   "Target.targetInfoChanged": TargetInfoChangedEvent,
}

