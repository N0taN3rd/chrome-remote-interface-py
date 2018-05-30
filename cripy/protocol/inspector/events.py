from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent


class DetachedEvent(BaseEvent):
    """
    Fired when remote debugging connection is about to be terminated.
	Contains detach reason.
    """

    event = "Inspector.detached"

    def __init__(self, reason: str) -> None:
        """
        :param reason: The reason why connection has been terminated.
        :type reason: str
        """
        super().__init__()
        self.reason = reason

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DetachedEvent']:
        if init is not None:
            return DetachedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DetachedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DetachedEvent(**it))
            return list_of_self
        else:
            return init


class TargetCrashedEvent(BaseEvent):
    """
    Fired when debugging target has crashed
    """

    event = "Inspector.targetCrashed"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TargetCrashedEvent']:
        if init is not None:
            return TargetCrashedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetCrashedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCrashedEvent(**it))
            return list_of_self
        else:
            return init


class TargetReloadedAfterCrashEvent(BaseEvent):
    """
    Fired when debugging target has reloaded after crash
    """

    event = "Inspector.targetReloadedAfterCrash"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TargetReloadedAfterCrashEvent']:
        if init is not None:
            return TargetReloadedAfterCrashEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetReloadedAfterCrashEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetReloadedAfterCrashEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Inspector.detached": DetachedEvent,
   "Inspector.targetCrashed": TargetCrashedEvent,
   "Inspector.targetReloadedAfterCrash": TargetReloadedAfterCrashEvent,
}

