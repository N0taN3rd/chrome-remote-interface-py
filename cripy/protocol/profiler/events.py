from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.debugger import types as Debugger
try:
    from cripy.protocol.profiler.types import *
except ImportError:
    pass


class ConsoleProfileFinishedEvent(BaseEvent):

    event = "Profiler.consoleProfileFinished"

    def __init__(self, id: str, location: Union[Debugger.Location, dict], profile: Union[Profile, dict], title: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleProfileFinishedEvent', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleProfileFinishedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ConsoleProfileStartedEvent(BaseEvent):
    """
    Sent when new profile recording is started using console.profile() call.
    """

    event = "Profiler.consoleProfileStarted"

    def __init__(self, id: str, location: Union[Debugger.Location, dict], title: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleProfileStartedEvent', dict]]:
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

