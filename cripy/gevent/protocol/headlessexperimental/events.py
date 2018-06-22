from collections import namedtuple
from cripy.gevent.protocol.headlessexperimental.types import *

__all__ = [
    "NeedsBeginFramesChangedEvent",
    "HEADLESSEXPERIMENTAL_EVENTS_TO_CLASS",
    "HEADLESSEXPERIMENTAL_EVENTS_NS"
]


class NeedsBeginFramesChangedEvent(object):
    """
    Issued when the target starts or stops needing BeginFrames.
    """

    __slots__ = ["needsBeginFrames"]

    def __init__(self, needsBeginFrames):
        """
        Create a new instance of NeedsBeginFramesChangedEvent

        :param needsBeginFrames: True if BeginFrames are needed, false otherwise.
        :type needsBeginFrames: bool
        """
        super(NeedsBeginFramesChangedEvent, self).__init__()
        self.needsBeginFrames = needsBeginFrames

    def __repr__(self):
        repr_args = []
        if self.needsBeginFrames is not None:
            repr_args.append("needsBeginFrames={!r}".format(self.needsBeginFrames))
        return "NeedsBeginFramesChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create NeedsBeginFramesChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NeedsBeginFramesChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NeedsBeginFramesChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, NeedsBeginFramesChangedEvent]]
        """
        if init is not None:
            try:
                ourselves = NeedsBeginFramesChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list NeedsBeginFramesChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NeedsBeginFramesChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NeedsBeginFramesChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, NeedsBeginFramesChangedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NeedsBeginFramesChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


HEADLESSEXPERIMENTAL_EVENTS_TO_CLASS = {
   "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent,
}

HeadlessExperimentalNS = namedtuple("HeadlessExperimentalNS", ["NeedsBeginFramesChanged"])

HEADLESSEXPERIMENTAL_EVENTS_NS = HeadlessExperimentalNS(
  NeedsBeginFramesChanged="HeadlessExperimental.needsBeginFramesChanged",
)
