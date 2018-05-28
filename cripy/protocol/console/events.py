from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class MessageAddedEvent(BaseEvent):
    """Issued when new console message is added."""

    event: str = "Console.messageAdded"

    def __init__(self) -> None:
        """
        :param message: Console message that has been added.
        :type ConsoleMessage:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

