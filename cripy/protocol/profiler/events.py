from typing import Any, List, Optional, Union
from types import SimpleNamespace
from cripy.protocol.debugger import types as Debugger

try:
    from cripy.protocol.profiler.types import *
except ImportError:
    pass


class ConsoleProfileFinishedEvent(object):

    event = "Profiler.consoleProfileFinished"

    def __init__(
        self,
        id: str,
        location: Union[Debugger.Location, dict],
        profile: Union[Profile, dict],
        title: Optional[str] = None,
    ) -> None:
        """
        :param id: The id
        :type id: str
        :param location: Location of console.profileEnd().
        :type location: dict
        :param profile: The profile
        :type profile: dict
        :param title: Profile title passed as an argument to console.profile().
        :type title: Optional[str]
        """
        super().__init__()
        self.id = id
        self.location = Debugger.Location.safe_create(location)
        self.profile = Profile.safe_create(profile)
        self.title = title

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.location is not None:
            repr_args.append("location={!r}".format(self.location))
        if self.profile is not None:
            repr_args.append("profile={!r}".format(self.profile))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        return "ConsoleProfileFinishedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ConsoleProfileFinishedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ConsoleProfileFinishedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ConsoleProfileFinishedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleProfileFinishedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ConsoleProfileStartedEvent(object):
    """
    Sent when new profile recording is started using console.profile() call.
    """

    event = "Profiler.consoleProfileStarted"

    def __init__(
        self,
        id: str,
        location: Union[Debugger.Location, dict],
        title: Optional[str] = None,
    ) -> None:
        """
        :param id: The id
        :type id: str
        :param location: Location of console.profile().
        :type location: dict
        :param title: Profile title passed as an argument to console.profile().
        :type title: Optional[str]
        """
        super().__init__()
        self.id = id
        self.location = Debugger.Location.safe_create(location)
        self.title = title

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.location is not None:
            repr_args.append("location={!r}".format(self.location))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        return "ConsoleProfileStartedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ConsoleProfileStartedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ConsoleProfileStartedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ConsoleProfileStartedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleProfileStartedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Profiler.consoleProfileFinished": ConsoleProfileFinishedEvent,
    "Profiler.consoleProfileStarted": ConsoleProfileStartedEvent,
}

EVENT_NS = SimpleNamespace(
    ConsoleProfileFinished="Profiler.consoleProfileFinished",
    ConsoleProfileStarted="Profiler.consoleProfileStarted",
)
