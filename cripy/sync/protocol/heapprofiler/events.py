from types import SimpleNamespace
try:
    from cripy.sync.protocol.heapprofiler.types import *
except ImportError:
    pass

__all__ = [
    "AddHeapSnapshotChunkEvent",
    "HeapStatsUpdateEvent",
    "LastSeenObjectIdEvent",
    "ReportHeapSnapshotProgressEvent",
    "ResetProfilesEvent",
]


class AddHeapSnapshotChunkEvent(object):

    event = "HeapProfiler.addHeapSnapshotChunk"

    def __init__(self, chunk):
        """
        :param chunk: The chunk
        :type chunk: str
        """
        super().__init__()
        self.chunk = chunk

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.chunk is not None:
            repr_args.append("chunk={!r}".format(self.chunk))
        return "AddHeapSnapshotChunkEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = AddHeapSnapshotChunkEvent(**init)
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
                list_of_self.append(AddHeapSnapshotChunkEvent.safe_create(it))
            return list_of_self
        else:
            return init


class HeapStatsUpdateEvent(object):
    """
    If heap objects tracking has been started then backend may send update for one or more fragments
    """

    event = "HeapProfiler.heapStatsUpdate"

    def __init__(self, statsUpdate):
        """
        :param statsUpdate: An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment.
        :type statsUpdate: List[int]
        """
        super().__init__()
        self.statsUpdate = statsUpdate

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.statsUpdate is not None:
            repr_args.append("statsUpdate={!r}".format(self.statsUpdate))
        return "HeapStatsUpdateEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = HeapStatsUpdateEvent(**init)
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
                list_of_self.append(HeapStatsUpdateEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LastSeenObjectIdEvent(object):
    """
    If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp.
	If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
    """

    event = "HeapProfiler.lastSeenObjectId"

    def __init__(self, lastSeenObjectId, timestamp):
        """
        :param lastSeenObjectId: The lastSeenObjectId
        :type lastSeenObjectId: int
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.lastSeenObjectId = lastSeenObjectId
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.lastSeenObjectId is not None:
            repr_args.append("lastSeenObjectId={!r}".format(self.lastSeenObjectId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "LastSeenObjectIdEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = LastSeenObjectIdEvent(**init)
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
                list_of_self.append(LastSeenObjectIdEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ReportHeapSnapshotProgressEvent(object):

    event = "HeapProfiler.reportHeapSnapshotProgress"

    def __init__(self, done, total, finished):
        """
        :param done: The done
        :type done: int
        :param total: The total
        :type total: int
        :param finished: The finished
        :type finished: Optional[bool]
        """
        super().__init__()
        self.done = done
        self.total = total
        self.finished = finished

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.done is not None:
            repr_args.append("done={!r}".format(self.done))
        if self.total is not None:
            repr_args.append("total={!r}".format(self.total))
        if self.finished is not None:
            repr_args.append("finished={!r}".format(self.finished))
        return "ReportHeapSnapshotProgressEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ReportHeapSnapshotProgressEvent(**init)
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
                list_of_self.append(ReportHeapSnapshotProgressEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResetProfilesEvent(dict):

    event = "HeapProfiler.resetProfiles"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "ResetProfilesEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ResetProfilesEvent(**init)
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
                list_of_self.append(ResetProfilesEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "HeapProfiler.addHeapSnapshotChunk": AddHeapSnapshotChunkEvent,
   "HeapProfiler.heapStatsUpdate": HeapStatsUpdateEvent,
   "HeapProfiler.lastSeenObjectId": LastSeenObjectIdEvent,
   "HeapProfiler.reportHeapSnapshotProgress": ReportHeapSnapshotProgressEvent,
   "HeapProfiler.resetProfiles": ResetProfilesEvent,
}

EVENT_NS = SimpleNamespace(
  AddHeapSnapshotChunk="HeapProfiler.addHeapSnapshotChunk",
  HeapStatsUpdate="HeapProfiler.heapStatsUpdate",
  LastSeenObjectId="HeapProfiler.lastSeenObjectId",
  ReportHeapSnapshotProgress="HeapProfiler.reportHeapSnapshotProgress",
  ResetProfiles="HeapProfiler.resetProfiles",
)
