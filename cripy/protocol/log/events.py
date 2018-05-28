from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.log.types import (
    LogEntry,
)


class EntryAddedEvent(BaseEvent):
    """Issued when new message was logged."""

    event: str = "Log.entryAdded"

    def __init__(self, entry: LogEntry) -> None:
        """
        :param entry: The entry.
        :type entry: LogEntry
        """
        super().__init__()
        self.entry: LogEntry = entry


EVENT_TO_CLASS = {
   "Log.entryAdded": EntryAddedEvent,
}

