from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AttachedToTargetEvent(BaseEvent):
    """Issued when attached to target because of auto-attach or `attachToTarget` command."""

    event: str = "Target.attachedToTarget"

    def __init__(self) -> None:
        """
        :param sessionId: Identifier assigned to the session used to send/receive messages.
        :type SessionID:
        :param targetInfo: The targetInfo
        :type TargetInfo:
        :param waitingForDebugger: The waitingForDebugger
        :type bool:
        """
        super().__init__()


class DetachedFromTargetEvent(BaseEvent):
    """Issued when detached from target for any reason (including `detachFromTarget` command).
	Can be issued multiple times per target if multiple sessions have been attached to it."""

    event: str = "Target.detachedFromTarget"

    def __init__(self) -> None:
        """
        :param sessionId: Detached session identifier.
        :type SessionID:
        :param targetId: Deprecated.
        :type TargetID:
        """
        super().__init__()


class ReceivedMessageFromTargetEvent(BaseEvent):
    """Notifies about a new protocol message received from the session (as reported in `attachedToTarget` event)."""

    event: str = "Target.receivedMessageFromTarget"

    def __init__(self) -> None:
        """
        :param sessionId: Identifier of a session which sends a message.
        :type SessionID:
        :param message: The message
        :type str:
        :param targetId: Deprecated.
        :type TargetID:
        """
        super().__init__()


class TargetCreatedEvent(BaseEvent):
    """Issued when a possible inspection target is created."""

    event: str = "Target.targetCreated"

    def __init__(self) -> None:
        """
        :param targetInfo: The targetInfo
        :type TargetInfo:
        """
        super().__init__()


class TargetDestroyedEvent(BaseEvent):
    """Issued when a target is destroyed."""

    event: str = "Target.targetDestroyed"

    def __init__(self) -> None:
        """
        :param targetId: The targetId
        :type TargetID:
        """
        super().__init__()


class TargetInfoChangedEvent(BaseEvent):
    """Issued when some information about a target has changed.
	This only happens between `targetCreated` and `targetDestroyed`."""

    event: str = "Target.targetInfoChanged"

    def __init__(self) -> None:
        """
        :param targetInfo: The targetInfo
        :type TargetInfo:
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

