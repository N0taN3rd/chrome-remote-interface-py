from types import SimpleNamespace

try:
    from cripy.gevent.protocol.headlessexperimental.types import *
except ImportError:
    pass

__all__ = ["NeedsBeginFramesChangedEvent"]


class NeedsBeginFramesChangedEvent(object):
    """
    Issued when the target starts or stops needing BeginFrames.
    """

    event = "HeadlessExperimental.needsBeginFramesChanged"

    def __init__(self, needsBeginFrames):
        """
        :param needsBeginFrames: True if BeginFrames are needed, false otherwise.
        :type needsBeginFrames: bool
        """
        super().__init__()
        self.needsBeginFrames = needsBeginFrames

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.needsBeginFrames is not None:
            repr_args.append("needsBeginFrames={!r}".format(self.needsBeginFrames))
        return "NeedsBeginFramesChangedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NeedsBeginFramesChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent
}

EVENT_NS = SimpleNamespace(
    NeedsBeginFramesChanged="HeadlessExperimental.needsBeginFramesChanged"
)
