from collections import namedtuple
from cripy.gevent.protocol.heapprofiler.types import *

__all__ = [
    "AddHeapSnapshotChunkEvent",
    "HeapStatsUpdateEvent",
    "LastSeenObjectIdEvent",
    "ReportHeapSnapshotProgressEvent",
    "ResetProfilesEvent",
    "HEAPPROFILER_EVENTS_TO_CLASS",
    "HEAPPROFILER_EVENTS_NS"
]


class AddHeapSnapshotChunkEvent(object):
    __slots__ = ["chunk"]

    def __init__(self, chunk):
        """
        Create a new instance of AddHeapSnapshotChunkEvent

        :param chunk: The chunk
        :type chunk: str
        """
        super(AddHeapSnapshotChunkEvent, self).__init__()
        self.chunk = chunk

    def __repr__(self):
        repr_args = []
        if self.chunk is not None:
            repr_args.append("chunk={!r}".format(self.chunk))
        return "AddHeapSnapshotChunkEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AddHeapSnapshotChunkEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AddHeapSnapshotChunkEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AddHeapSnapshotChunkEvent if creation did not fail
        :rtype: Optional[Union[dict, AddHeapSnapshotChunkEvent]]
        """
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
        """
        Safely create a new list AddHeapSnapshotChunkEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AddHeapSnapshotChunkEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AddHeapSnapshotChunkEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AddHeapSnapshotChunkEvent]]]
        """
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

    __slots__ = ["statsUpdate"]

    def __init__(self, statsUpdate):
        """
        Create a new instance of HeapStatsUpdateEvent

        :param statsUpdate: An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment.
        :type statsUpdate: List[int]
        """
        super(HeapStatsUpdateEvent, self).__init__()
        self.statsUpdate = statsUpdate

    def __repr__(self):
        repr_args = []
        if self.statsUpdate is not None:
            repr_args.append("statsUpdate={!r}".format(self.statsUpdate))
        return "HeapStatsUpdateEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create HeapStatsUpdateEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of HeapStatsUpdateEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of HeapStatsUpdateEvent if creation did not fail
        :rtype: Optional[Union[dict, HeapStatsUpdateEvent]]
        """
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
        """
        Safely create a new list HeapStatsUpdateEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list HeapStatsUpdateEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of HeapStatsUpdateEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, HeapStatsUpdateEvent]]]
        """
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

    __slots__ = ["lastSeenObjectId", "timestamp"]

    def __init__(self, lastSeenObjectId, timestamp):
        """
        Create a new instance of LastSeenObjectIdEvent

        :param lastSeenObjectId: The lastSeenObjectId
        :type lastSeenObjectId: int
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super(LastSeenObjectIdEvent, self).__init__()
        self.lastSeenObjectId = lastSeenObjectId
        self.timestamp = timestamp

    def __repr__(self):
        repr_args = []
        if self.lastSeenObjectId is not None:
            repr_args.append("lastSeenObjectId={!r}".format(self.lastSeenObjectId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "LastSeenObjectIdEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LastSeenObjectIdEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LastSeenObjectIdEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LastSeenObjectIdEvent if creation did not fail
        :rtype: Optional[Union[dict, LastSeenObjectIdEvent]]
        """
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
        """
        Safely create a new list LastSeenObjectIdEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LastSeenObjectIdEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LastSeenObjectIdEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LastSeenObjectIdEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LastSeenObjectIdEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ReportHeapSnapshotProgressEvent(object):
    __slots__ = ["done", "total", "finished"]

    def __init__(self, done, total, finished=None):
        """
        Create a new instance of ReportHeapSnapshotProgressEvent

        :param done: The done
        :type done: int
        :param total: The total
        :type total: int
        :param finished: The finished
        :type finished: Optional[bool]
        """
        super(ReportHeapSnapshotProgressEvent, self).__init__()
        self.done = done
        self.total = total
        self.finished = finished

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
        """
        Safely create ReportHeapSnapshotProgressEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ReportHeapSnapshotProgressEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ReportHeapSnapshotProgressEvent if creation did not fail
        :rtype: Optional[Union[dict, ReportHeapSnapshotProgressEvent]]
        """
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
        """
        Safely create a new list ReportHeapSnapshotProgressEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ReportHeapSnapshotProgressEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ReportHeapSnapshotProgressEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ReportHeapSnapshotProgressEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReportHeapSnapshotProgressEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResetProfilesEvent(dict):
    def __repr__(self):
        return "ResetProfilesEvent(dict)"

    @staticmethod
    def safe_create(init):
        """
        Safely create ResetProfilesEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ResetProfilesEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ResetProfilesEvent if creation did not fail
        :rtype: Optional[Union[dict, ResetProfilesEvent]]
        """
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
        """
        Safely create a new list ResetProfilesEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ResetProfilesEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ResetProfilesEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ResetProfilesEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResetProfilesEvent.safe_create(it))
            return list_of_self
        else:
            return init


HEAPPROFILER_EVENTS_TO_CLASS = {
   "HeapProfiler.addHeapSnapshotChunk": AddHeapSnapshotChunkEvent,
   "HeapProfiler.heapStatsUpdate": HeapStatsUpdateEvent,
   "HeapProfiler.lastSeenObjectId": LastSeenObjectIdEvent,
   "HeapProfiler.reportHeapSnapshotProgress": ReportHeapSnapshotProgressEvent,
   "HeapProfiler.resetProfiles": ResetProfilesEvent,
}

HeapProfilerNS = namedtuple("HeapProfilerNS", ["AddHeapSnapshotChunk", "HeapStatsUpdate", "LastSeenObjectId", "ReportHeapSnapshotProgress", "ResetProfiles"])

HEAPPROFILER_EVENTS_NS = HeapProfilerNS(
  AddHeapSnapshotChunk="HeapProfiler.addHeapSnapshotChunk",
  HeapStatsUpdate="HeapProfiler.heapStatsUpdate",
  LastSeenObjectId="HeapProfiler.lastSeenObjectId",
  ReportHeapSnapshotProgress="HeapProfiler.reportHeapSnapshotProgress",
  ResetProfiles="HeapProfiler.resetProfiles",
)
