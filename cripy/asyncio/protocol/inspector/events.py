from typing import Any, List, Optional, Union
from collections import namedtuple

__all__ = [
    "DetachedEvent",
    "TargetCrashedEvent",
    "TargetReloadedAfterCrashEvent",
    "INSPECTOR_EVENTS_TO_CLASS",
    "INSPECTOR_EVENTS_NS"
]


class DetachedEvent(object):
    """
    Fired when remote debugging connection is about to be terminated.
	Contains detach reason.
    """


    __slots__ = ["reason"]

    def __init__(self, reason: str) -> None:
        """
        Create a new instance of DetachedEvent

        :param reason: The reason why connection has been terminated.
        :type reason: str
        """
        super().__init__()
        self.reason = reason

    def __repr__(self) -> str:
        repr_args = []
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        return "DetachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DetachedEvent', dict]]:
        """
        Safely create DetachedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DetachedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DetachedEvent if creation did not fail
        :rtype: Optional[Union[dict, DetachedEvent]]
        """
        if init is not None:
            try:
                ourselves = DetachedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DetachedEvent', dict]]]:
        """
        Safely create a new list DetachedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DetachedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DetachedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DetachedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DetachedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetCrashedEvent(dict):
    """
    Fired when debugging target has crashed
    """


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "TargetCrashedEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TargetCrashedEvent', dict]]:
        """
        Safely create TargetCrashedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetCrashedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetCrashedEvent if creation did not fail
        :rtype: Optional[Union[dict, TargetCrashedEvent]]
        """
        if init is not None:
            try:
                ourselves = TargetCrashedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TargetCrashedEvent', dict]]]:
        """
        Safely create a new list TargetCrashedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetCrashedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetCrashedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetCrashedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetCrashedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetReloadedAfterCrashEvent(dict):
    """
    Fired when debugging target has reloaded after crash
    """


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "TargetReloadedAfterCrashEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TargetReloadedAfterCrashEvent', dict]]:
        """
        Safely create TargetReloadedAfterCrashEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetReloadedAfterCrashEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetReloadedAfterCrashEvent if creation did not fail
        :rtype: Optional[Union[dict, TargetReloadedAfterCrashEvent]]
        """
        if init is not None:
            try:
                ourselves = TargetReloadedAfterCrashEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TargetReloadedAfterCrashEvent', dict]]]:
        """
        Safely create a new list TargetReloadedAfterCrashEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetReloadedAfterCrashEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetReloadedAfterCrashEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetReloadedAfterCrashEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetReloadedAfterCrashEvent.safe_create(it))
            return list_of_self
        else:
            return init


INSPECTOR_EVENTS_TO_CLASS = {
   "Inspector.detached": DetachedEvent,
   "Inspector.targetCrashed": TargetCrashedEvent,
   "Inspector.targetReloadedAfterCrash": TargetReloadedAfterCrashEvent,
}

InspectorNS = namedtuple("InspectorNS", ["Detached", "TargetCrashed", "TargetReloadedAfterCrash"])

INSPECTOR_EVENTS_NS = InspectorNS(
  Detached="Inspector.detached",
  TargetCrashed="Inspector.targetCrashed",
  TargetReloadedAfterCrash="Inspector.targetReloadedAfterCrash",
)
