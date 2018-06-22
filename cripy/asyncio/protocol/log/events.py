from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.log.types import *

__all__ = [
    "EntryAddedEvent",
    "LOG_EVENTS_TO_CLASS",
    "LOG_EVENTS_NS"
]

class EntryAddedEvent(object):
    """
    Issued when new message was logged.
    """

    event = "Log.entryAdded"

    __slots__ = ["entry"]

    def __init__(self, entry: Union[LogEntry, dict]) -> None:
        """
        Create a new instance of EntryAddedEvent

        :param entry: The entry.
        :type entry: dict
        """
        super().__init__()
        self.entry = LogEntry.safe_create(entry)

    def __repr__(self) -> str:
        repr_args = []
        if self.entry is not None:
            repr_args.append("entry={!r}".format(self.entry))
        return "EntryAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['EntryAddedEvent', dict]]:
        """
        Safely create EntryAddedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of EntryAddedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of EntryAddedEvent if creation did not fail
        :rtype: Optional[Union[dict, EntryAddedEvent]]
        """
        if init is not None:
            try:
                ourselves = EntryAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['EntryAddedEvent', dict]]]:
        """
        Safely create a new list EntryAddedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list EntryAddedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of EntryAddedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, EntryAddedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


LOG_EVENTS_TO_CLASS = {
   "Log.entryAdded": EntryAddedEvent,
}

LogNS = namedtuple("LogNS", ["EntryAdded"])

LOG_EVENTS_NS = LogNS(
  EntryAdded="Log.entryAdded",
)
