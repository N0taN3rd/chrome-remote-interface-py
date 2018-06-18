from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.async.protocol.emulation.types import *
except ImportError:
    pass


class VirtualTimeAdvancedEvent(object):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.virtualTimeElapsed is not None:
            repr_args.append("virtualTimeElapsed={!r}".format(self.virtualTimeElapsed))
        return "VirtualTimeAdvancedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["VirtualTimeAdvancedEvent", dict]]:
        if init is not None:
            try:
                ourselves = VirtualTimeAdvancedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["VirtualTimeAdvancedEvent", dict]]]:
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
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["VirtualTimeBudgetExpiredEvent", dict]]:
        if init is not None:
            try:
                ourselves = VirtualTimeBudgetExpiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["VirtualTimeBudgetExpiredEvent", dict]]]:
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

    def __init__(self, virtualTimeElapsed: float) -> None:
        """
        :param virtualTimeElapsed: The amount of virtual time that has elapsed in milliseconds since virtual time was first enabled.
        :type virtualTimeElapsed: float
        """
        super().__init__()
        self.virtualTimeElapsed = virtualTimeElapsed

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.virtualTimeElapsed is not None:
            repr_args.append("virtualTimeElapsed={!r}".format(self.virtualTimeElapsed))
        return "VirtualTimePausedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["VirtualTimePausedEvent", dict]]:
        if init is not None:
            try:
                ourselves = VirtualTimePausedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["VirtualTimePausedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VirtualTimePausedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Emulation.virtualTimeAdvanced": VirtualTimeAdvancedEvent,
    "Emulation.virtualTimeBudgetExpired": VirtualTimeBudgetExpiredEvent,
    "Emulation.virtualTimePaused": VirtualTimePausedEvent,
}

EVENT_NS = SimpleNamespace(
    VirtualTimeAdvanced="Emulation.virtualTimeAdvanced",
    VirtualTimeBudgetExpired="Emulation.virtualTimeBudgetExpired",
    VirtualTimePaused="Emulation.virtualTimePaused",
)
