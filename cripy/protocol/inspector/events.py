from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DetachedEvent(BaseEvent):
    """Fired when remote debugging connection is about to be terminated.
	Contains detach reason."""

    event: str = "Inspector.detached"

    def __init__(self) -> None:
        """
        :param reason: The reason why connection has been terminated.
        :type str:
        """
        super().__init__()


class TargetCrashedEvent(BaseEvent):
    """Fired when debugging target has crashed"""

    event: str = "Inspector.targetCrashed"

    def __init__(self) -> None:
        super().__init__()


class TargetReloadedAfterCrashEvent(BaseEvent):
    """Fired when debugging target has reloaded after crash"""

    event: str = "Inspector.targetReloadedAfterCrash"

    def __init__(self) -> None:
        super().__init__()


EVENT_TO_CLASS = {
   "Inspector.detached": DetachedEvent,
   "Inspector.targetCrashed": TargetCrashedEvent,
   "Inspector.targetReloadedAfterCrash": TargetReloadedAfterCrashEvent,
}

