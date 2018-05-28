from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class EntryAddedEvent(BaseEvent):
    """Issued when new message was logged."""

    event: str = "Log.entryAdded"

    def __init__(self) -> None:
        """
        :param entry: The entry.
        :type LogEntry:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Log.entryAdded": EntryAddedEvent,
}

