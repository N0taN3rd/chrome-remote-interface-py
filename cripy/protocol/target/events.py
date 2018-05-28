from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AttachedToTargetEvent(BaseEvent):
    """Issued when attached to target because of auto-attach or `attachToTarget` command."""

    event: str = "Target.attachedToTarget"

    def __init__(self) -> None:
        """
        :param SessionID sessionId: Identifier assigned to the session used to send/receive messages.
        :type sessionId: SessionID
        :param TargetInfo targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        :param bool waitingForDebugger: The waitingForDebugger
        :type waitingForDebugger: bool
        """
        super().__init__()


class DetachedFromTargetEvent(BaseEvent):
    """Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it."""

    event: str = "Target.detachedFromTarget"

    def __init__(self) -> None:
        """
        :param SessionID sessionId: Detached session identifier.
        :type sessionId: SessionID
        :param TargetID targetId: Deprecated.
        :type targetId: TargetID
        """
        super().__init__()


class ReceivedMessageFromTargetEvent(BaseEvent):
    """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""

    event: str = "Target.receivedMessageFromTarget"

    def __init__(self) -> None:
        """
        :param SessionID sessionId: Identifier of a session which sends a message.
        :type sessionId: SessionID
        :param str message: The message
        :type message: str
        :param TargetID targetId: Deprecated.
        :type targetId: TargetID
        """
        super().__init__()


class TargetCreatedEvent(BaseEvent):
    """Issued when a possible inspection target is created."""

    event: str = "Target.targetCreated"

    def __init__(self) -> None:
        """
        :param TargetInfo targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        """
        super().__init__()


class TargetDestroyedEvent(BaseEvent):
    """Issued when a target is destroyed."""

    event: str = "Target.targetDestroyed"

    def __init__(self) -> None:
        """
        :param TargetID targetId: The targetId
        :type targetId: TargetID
        """
        super().__init__()


class TargetInfoChangedEvent(BaseEvent):
    """Issued when some information about a target has changed.
	This only happens between `targetCreated` and `targetDestroyed`."""

    event: str = "Target.targetInfoChanged"

    def __init__(self) -> None:
        """
        :param TargetInfo targetInfo: The targetInfo
        :type targetInfo: TargetInfo
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Target.attachedToTarget": AttachedToTargetEvent,
   "Target.detachedFromTarget": DetachedFromTargetEvent,
   "Target.receivedMessageFromTarget": ReceivedMessageFromTargetEvent,
   "Target.targetCreated": TargetCreatedEvent,
   "Target.targetDestroyed": TargetDestroyedEvent,
   "Target.targetInfoChanged": TargetInfoChangedEvent,
}

