from types import SimpleNamespace
try:
    from cripy.sync.protocol.inspector.types import *
except ImportError:
    pass

__all__ = [
    "DetachedEvent",
    "TargetCrashedEvent",
    "TargetReloadedAfterCrashEvent",
]


class DetachedEvent(object):
    """
    Fired when remote debugging connection is about to be terminated.
	Contains detach reason.
    """

    event = "Inspector.detached"

    def __init__(self, reason):
        """
        :param reason: The reason why connection has been terminated.
        :type reason: str
        """
        super().__init__()
        self.reason = reason

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        return "DetachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DetachedEvent(**init)
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
                list_of_self.append(DetachedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetCrashedEvent(dict):
    """
    Fired when debugging target has crashed
    """

    event = "Inspector.targetCrashed"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "TargetCrashedEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = TargetCrashedEvent(**init)
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
                list_of_self.append(TargetCrashedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TargetReloadedAfterCrashEvent(dict):
    """
    Fired when debugging target has reloaded after crash
    """

    event = "Inspector.targetReloadedAfterCrash"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "TargetReloadedAfterCrashEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = TargetReloadedAfterCrashEvent(**init)
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
                list_of_self.append(TargetReloadedAfterCrashEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Inspector.detached": DetachedEvent,
   "Inspector.targetCrashed": TargetCrashedEvent,
   "Inspector.targetReloadedAfterCrash": TargetReloadedAfterCrashEvent,
}

EVENT_NS = SimpleNamespace(
  Detached="Inspector.detached",
  TargetCrashed="Inspector.targetCrashed",
  TargetReloadedAfterCrash="Inspector.targetReloadedAfterCrash",
)
