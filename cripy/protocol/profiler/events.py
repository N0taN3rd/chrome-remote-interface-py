from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.debugger import types as Debugger
from cripy.protocol.profiler.types import (
    Profile,
)


class ConsoleProfileFinishedEvent(BaseEvent):

    event: str = "Profiler.consoleProfileFinished"

    def __init__(self, id: str, location: Debugger.Location, profile: Profile, title: Optional[str] = None) -> None:
        """
        :param id: The id
        :type id: str
        :param location: Location of console.profileEnd().
        :type location: Debugger.Location
        :param profile: The profile
        :type profile: Profile
        :param title: Profile title passed as an argument to console.profile().
        :type title: str
        """
        super().__init__()
        self.id: str = id
        self.location: Debugger.Location = location
        self.profile: Profile = profile
        self.title: Optional[str] = title


class ConsoleProfileStartedEvent(BaseEvent):
    """Sent when new profile recording is started using console.profile() call."""

    event: str = "Profiler.consoleProfileStarted"

    def __init__(self, id: str, location: Debugger.Location, title: Optional[str] = None) -> None:
        """
        :param id: The id
        :type id: str
        :param location: Location of console.profile().
        :type location: Debugger.Location
        :param title: Profile title passed as an argument to console.profile().
        :type title: str
        """
        super().__init__()
        self.id: str = id
        self.location: Debugger.Location = location
        self.title: Optional[str] = title


EVENT_TO_CLASS = {
   "Profiler.consoleProfileFinished": ConsoleProfileFinishedEvent,
   "Profiler.consoleProfileStarted": ConsoleProfileStartedEvent,
}

