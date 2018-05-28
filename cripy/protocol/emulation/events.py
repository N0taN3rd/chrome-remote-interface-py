from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class VirtualTimeAdvancedEvent(BaseEvent):
    """Notification sent after the virtual time has advanced."""

    event: str = "Emulation.virtualTimeAdvanced"

    def __init__(self) -> None:
        """
        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was
        first enabled.
        :type float:
        """
        super().__init__()


class VirtualTimeBudgetExpiredEvent(BaseEvent):
    """Notification sent after the virtual time budget for the current VirtualTimePolicy has run out."""

    event: str = "Emulation.virtualTimeBudgetExpired"

    def __init__(self) -> None:
        super().__init__()


class VirtualTimePausedEvent(BaseEvent):
    """Notification sent after the virtual time has paused."""

    event: str = "Emulation.virtualTimePaused"

    def __init__(self) -> None:
        """
        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was
        first enabled.
        :type float:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Emulation.virtualTimeAdvanced": VirtualTimeAdvancedEvent,
   "Emulation.virtualTimeBudgetExpired": VirtualTimeBudgetExpiredEvent,
   "Emulation.virtualTimePaused": VirtualTimePausedEvent,
}

