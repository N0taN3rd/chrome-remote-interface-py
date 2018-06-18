from types import SimpleNamespace

try:
    from cripy.gevent.protocol.log.types import *
except ImportError:
    pass

__all__ = ["EntryAddedEvent"]


class EntryAddedEvent(object):
    """
    Issued when new message was logged.
    """

    event = "Log.entryAdded"

    def __init__(self, entry):
        """
        :param entry: The entry.
        :type entry: dict
        """
        super().__init__()
        self.entry = LogEntry.safe_create(entry)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.entry is not None:
            repr_args.append("entry={!r}".format(self.entry))
        return "EntryAddedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = EntryAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {"Log.entryAdded": EntryAddedEvent}

EVENT_NS = SimpleNamespace(EntryAdded="Log.entryAdded")
