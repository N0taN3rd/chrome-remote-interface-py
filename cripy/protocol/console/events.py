from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.console.types import (
    ConsoleMessage,
)


class MessageAddedEvent(BaseEvent):
    """Issued when new console message is added."""

    event: str = "Console.messageAdded"

    def __init__(self, message: ConsoleMessage) -> None:
        """
        :param message: Console message that has been added.
        :type message: ConsoleMessage
        """
        super().__init__()
        self.message: ConsoleMessage = message


EVENT_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

