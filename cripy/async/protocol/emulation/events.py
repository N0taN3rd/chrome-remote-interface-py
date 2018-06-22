from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.emulation.types import *

__all__ = [
    "VirtualTimeAdvancedEvent",
    "VirtualTimeBudgetExpiredEvent",
    "VirtualTimePausedEvent",
    "EMULATION_EVENTS_TO_CLASS",
    "EMULATION_EVENTS_NS"
]

class VirtualTimeAdvancedEvent(object):
    """
    Notification sent after the virtual time has advanced.
    """

    event = "Emulation.virtualTimeAdvanced"

    __slots__ = ["virtualTimeElapsed"]

    def __init__(self, virtualTimeElapsed: float) -> None:
        """
        Create a new instance of VirtualTimeAdvancedEvent

        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was first enabled.
        :type virtualTimeElapsed: float
        """
        super().__init__()
        self.virtualTimeElapsed = virtualTimeElapsed

    def __repr__(self) -> str:
        repr_args = []
        if self.virtualTimeElapsed is not None:
            repr_args.append("virtualTimeElapsed={!r}".format(self.virtualTimeElapsed))
        return "VirtualTimeAdvancedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['VirtualTimeAdvancedEvent', dict]]:
        """
        Safely create VirtualTimeAdvancedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of VirtualTimeAdvancedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of VirtualTimeAdvancedEvent if creation did not fail
        :rtype: Optional[Union[dict, VirtualTimeAdvancedEvent]]
        """
        if init is not None:
            try:
                ourselves = VirtualTimeAdvancedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['VirtualTimeAdvancedEvent', dict]]]:
        """
        Safely create a new list VirtualTimeAdvancedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list VirtualTimeAdvancedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of VirtualTimeAdvancedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, VirtualTimeAdvancedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimeAdvancedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class VirtualTimeBudgetExpiredEvent(dict):
    """
    Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.
    """

    event = "Emulation.virtualTimeBudgetExpired"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "VirtualTimeBudgetExpiredEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['VirtualTimeBudgetExpiredEvent', dict]]:
        """
        Safely create VirtualTimeBudgetExpiredEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of VirtualTimeBudgetExpiredEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of VirtualTimeBudgetExpiredEvent if creation did not fail
        :rtype: Optional[Union[dict, VirtualTimeBudgetExpiredEvent]]
        """
        if init is not None:
            try:
                ourselves = VirtualTimeBudgetExpiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['VirtualTimeBudgetExpiredEvent', dict]]]:
        """
        Safely create a new list VirtualTimeBudgetExpiredEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list VirtualTimeBudgetExpiredEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of VirtualTimeBudgetExpiredEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, VirtualTimeBudgetExpiredEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimeBudgetExpiredEvent.safe_create(it))
            return list_of_self
        else:
            return init


class VirtualTimePausedEvent(object):
    """
    Notification sent after the virtual time has paused.
    """

    event = "Emulation.virtualTimePaused"

    __slots__ = ["virtualTimeElapsed"]

    def __init__(self, virtualTimeElapsed: float) -> None:
        """
        Create a new instance of VirtualTimePausedEvent

        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was first enabled.
        :type virtualTimeElapsed: float
        """
        super().__init__()
        self.virtualTimeElapsed = virtualTimeElapsed

    def __repr__(self) -> str:
        repr_args = []
        if self.virtualTimeElapsed is not None:
            repr_args.append("virtualTimeElapsed={!r}".format(self.virtualTimeElapsed))
        return "VirtualTimePausedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['VirtualTimePausedEvent', dict]]:
        """
        Safely create VirtualTimePausedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of VirtualTimePausedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of VirtualTimePausedEvent if creation did not fail
        :rtype: Optional[Union[dict, VirtualTimePausedEvent]]
        """
        if init is not None:
            try:
                ourselves = VirtualTimePausedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['VirtualTimePausedEvent', dict]]]:
        """
        Safely create a new list VirtualTimePausedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list VirtualTimePausedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of VirtualTimePausedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, VirtualTimePausedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimePausedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EMULATION_EVENTS_TO_CLASS = {
   "Emulation.virtualTimeAdvanced": VirtualTimeAdvancedEvent,
   "Emulation.virtualTimeBudgetExpired": VirtualTimeBudgetExpiredEvent,
   "Emulation.virtualTimePaused": VirtualTimePausedEvent,
}

EmulationNS = namedtuple("EmulationNS", ["VirtualTimeAdvanced", "VirtualTimeBudgetExpired", "VirtualTimePaused"])

EMULATION_EVENTS_NS = EmulationNS(
  VirtualTimeAdvanced="Emulation.virtualTimeAdvanced",
  VirtualTimeBudgetExpired="Emulation.virtualTimeBudgetExpired",
  VirtualTimePaused="Emulation.virtualTimePaused",
)
