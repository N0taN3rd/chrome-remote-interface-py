from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.debugger import types as Debugger
from cripy.async.protocol.profiler.types import *

__all__ = [
    "ConsoleProfileFinishedEvent",
    "ConsoleProfileStartedEvent",
    "PROFILER_EVENTS_TO_CLASS",
    "PROFILER_EVENTS_NS"
]

class ConsoleProfileFinishedEvent(object):

    event = "Profiler.consoleProfileFinished"

    __slots__ = ["id", "location", "profile", "title"]

    def __init__(self, id: str, location: Union[Debugger.Location, dict], profile: Union[Profile, dict], title: Optional[str] = None) -> None:
        """
        Create a new instance of ConsoleProfileFinishedEvent

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
        return "ConsoleProfileFinishedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleProfileFinishedEvent', dict]]:
        """
        Safely create ConsoleProfileFinishedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ConsoleProfileFinishedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ConsoleProfileFinishedEvent if creation did not fail
        :rtype: Optional[Union[dict, ConsoleProfileFinishedEvent]]
        """
        if init is not None:
            try:
                ourselves = ConsoleProfileFinishedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ConsoleProfileFinishedEvent', dict]]]:
        """
        Safely create a new list ConsoleProfileFinishedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ConsoleProfileFinishedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ConsoleProfileFinishedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ConsoleProfileFinishedEvent]]]
        """
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

    __slots__ = ["id", "location", "title"]

    def __init__(self, id: str, location: Union[Debugger.Location, dict], title: Optional[str] = None) -> None:
        """
        Create a new instance of ConsoleProfileStartedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.location is not None:
            repr_args.append("location={!r}".format(self.location))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        return "ConsoleProfileStartedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleProfileStartedEvent', dict]]:
        """
        Safely create ConsoleProfileStartedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ConsoleProfileStartedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ConsoleProfileStartedEvent if creation did not fail
        :rtype: Optional[Union[dict, ConsoleProfileStartedEvent]]
        """
        if init is not None:
            try:
                ourselves = ConsoleProfileStartedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ConsoleProfileStartedEvent', dict]]]:
        """
        Safely create a new list ConsoleProfileStartedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ConsoleProfileStartedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ConsoleProfileStartedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ConsoleProfileStartedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleProfileStartedEvent.safe_create(it))
            return list_of_self
        else:
            return init


PROFILER_EVENTS_TO_CLASS = {
   "Profiler.consoleProfileFinished": ConsoleProfileFinishedEvent,
   "Profiler.consoleProfileStarted": ConsoleProfileStartedEvent,
}

ProfilerNS = namedtuple("ProfilerNS", ["ConsoleProfileFinished", "ConsoleProfileStarted"])

PROFILER_EVENTS_NS = ProfilerNS(
  ConsoleProfileFinished="Profiler.consoleProfileFinished",
  ConsoleProfileStarted="Profiler.consoleProfileStarted",
)
