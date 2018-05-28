from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class ConsoleProfileFinishedEvent(BaseEvent):

    event: str = "Profiler.consoleProfileFinished"

    def __init__(self) -> None:
        """
        :param id: The id
        :type str:
        :param location: Location of console.profileEnd().
        :type Debugger.Location:
        :param profile: The profile
        :type Profile:
        :param title: Profile title passed as an argument to console.profile().
        :type str:
        """
        super().__init__()


class ConsoleProfileStartedEvent(BaseEvent):
    """Sent when new profile recording is started using console.profile() call."""

    event: str = "Profiler.consoleProfileStarted"

    def __init__(self) -> None:
        """
        :param id: The id
        :type str:
        :param location: Location of console.profile().
        :type Debugger.Location:
        :param title: Profile title passed as an argument to console.profile().
        :type str:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Profiler.consoleProfileFinished": ConsoleProfileFinishedEvent,
   "Profiler.consoleProfileStarted": ConsoleProfileStartedEvent,
}

