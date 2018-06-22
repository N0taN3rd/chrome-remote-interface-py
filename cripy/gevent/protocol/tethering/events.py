from collections import namedtuple

__all__ = [
    "AcceptedEvent",
    "TETHERING_EVENTS_TO_CLASS",
    "TETHERING_EVENTS_NS"
]


class AcceptedEvent(object):
    """
    Informs that port was successfully bound and got a specified connection id.
    """

    __slots__ = ["port", "connectionId"]

    def __init__(self, port, connectionId):
        """
        Create a new instance of AcceptedEvent

        :param port: Port number that was successfully bound.
        :type port: int
        :param connectionId: Connection id to be used.
        :type connectionId: str
        """
        super(AcceptedEvent, self).__init__()
        self.port = port
        self.connectionId = connectionId

    def __repr__(self):
        repr_args = []
        if self.port is not None:
            repr_args.append("port={!r}".format(self.port))
        if self.connectionId is not None:
            repr_args.append("connectionId={!r}".format(self.connectionId))
        return "AcceptedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AcceptedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AcceptedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AcceptedEvent if creation did not fail
        :rtype: Optional[Union[dict, AcceptedEvent]]
        """
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
        """
        Safely create a new list AcceptedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AcceptedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AcceptedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AcceptedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AcceptedEvent.safe_create(it))
            return list_of_self
        else:
            return init


TETHERING_EVENTS_TO_CLASS = {
   "Tethering.accepted": AcceptedEvent,
}

TetheringNS = namedtuple("TetheringNS", ["Accepted"])

TETHERING_EVENTS_NS = TetheringNS(
  Accepted="Tethering.accepted",
)
