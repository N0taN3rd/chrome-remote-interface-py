from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.emulation.types import *
except ImportError:
    pass


class VirtualTimeAdvancedEvent(BaseEvent):
    """
    Notification sent after the virtual time has advanced.
    """

    event = "Emulation.virtualTimeAdvanced"

    def __init__(self, virtualTimeElapsed: float) -> None:
        """
        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was first enabled.
        :type virtualTimeElapsed: float
        """
        super().__init__()
        self.virtualTimeElapsed = virtualTimeElapsed

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['VirtualTimeAdvancedEvent']:
        if init is not None:
            return VirtualTimeAdvancedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['VirtualTimeAdvancedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimeAdvancedEvent(**it))
            return list_of_self
        else:
            return init


class VirtualTimeBudgetExpiredEvent(BaseEvent, dict):
    """
    Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.
    """

    event = "Emulation.virtualTimeBudgetExpired"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['VirtualTimeBudgetExpiredEvent']:
        if init is not None:
            return VirtualTimeBudgetExpiredEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['VirtualTimeBudgetExpiredEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimeBudgetExpiredEvent(**it))
            return list_of_self
        else:
            return init


class VirtualTimePausedEvent(BaseEvent):
    """
    Notification sent after the virtual time has paused.
    """

    event = "Emulation.virtualTimePaused"

    def __init__(self, virtualTimeElapsed: float) -> None:
        """
        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was first enabled.
        :type virtualTimeElapsed: float
        """
        super().__init__()
        self.virtualTimeElapsed = virtualTimeElapsed

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['VirtualTimePausedEvent']:
        if init is not None:
            return VirtualTimePausedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['VirtualTimePausedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimePausedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Emulation.virtualTimeAdvanced": VirtualTimeAdvancedEvent,
   "Emulation.virtualTimeBudgetExpired": VirtualTimeBudgetExpiredEvent,
   "Emulation.virtualTimePaused": VirtualTimePausedEvent,
}

