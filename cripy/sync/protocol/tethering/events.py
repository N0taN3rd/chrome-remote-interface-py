from types import SimpleNamespace
try:
    from cripy.sync.protocol.tethering.types import *
except ImportError:
    pass

__all__ = [
    "AcceptedEvent",
]


class AcceptedEvent(object):
    """
    Informs that port was successfully bound and got a specified connection id.
    """

    event = "Tethering.accepted"

    def __init__(self, port, connectionId):
        """
        :param port: Port number that was successfully bound.
        :type port: int
        :param connectionId: Connection id to be used.
        :type connectionId: str
        """
        super().__init__()
        self.port = port
        self.connectionId = connectionId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.port is not None:
            repr_args.append("port={!r}".format(self.port))
        if self.connectionId is not None:
            repr_args.append("connectionId={!r}".format(self.connectionId))
        return "AcceptedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = AcceptedEvent(**init)
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
                list_of_self.append(AcceptedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Tethering.accepted": AcceptedEvent,
}

EVENT_NS = SimpleNamespace(
  Accepted="Tethering.accepted",
)
