from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.log.types import *
except ImportError:
    pass


class EntryAddedEvent(object):
    """
    Issued when new message was logged.
    """

    event = "Log.entryAdded"

    def __init__(self, entry: Union[LogEntry, dict]) -> None:
        """
        :param entry: The entry.
        :type entry: dict
        """
        super().__init__()
        self.entry = LogEntry.safe_create(entry)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.entry is not None:
            repr_args.append("entry={!r}".format(self.entry))
        return "EntryAddedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["EntryAddedEvent", dict]]:
        if init is not None:
            try:
                ourselves = EntryAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["EntryAddedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {"Log.entryAdded": EntryAddedEvent}

EVENT_NS = SimpleNamespace(EntryAdded="Log.entryAdded")
