from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class MessageAddedEvent(BaseEvent):
    """Issued when new console message is added."""

    event: str = "Console.messageAdded"

    def __init__(self) -> None:
        """
        :param ConsoleMessage message: Console message that has been added.
        :type message: ConsoleMessage
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

