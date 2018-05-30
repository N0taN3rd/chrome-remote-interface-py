from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.heapprofiler.types import *
except ImportError:
    pass


class AddHeapSnapshotChunkEvent(BaseEvent):

    event = "HeapProfiler.addHeapSnapshotChunk"

    def __init__(self, chunk: str) -> None:
        """
        :param chunk: The chunk
        :type chunk: str
        """
        super().__init__()
        self.chunk = chunk

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AddHeapSnapshotChunkEvent']:
        if init is not None:
            return AddHeapSnapshotChunkEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AddHeapSnapshotChunkEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AddHeapSnapshotChunkEvent(**it))
            return list_of_self
        else:
            return init


class HeapStatsUpdateEvent(BaseEvent):
    """
    If heap objects tracking has been started then backend may send update for one or more fragments
    """

    event = "HeapProfiler.heapStatsUpdate"

    def __init__(self, statsUpdate: List[int]) -> None:
        """
        :param statsUpdate: An array of triplets. Each triplet describes a fragment. The first integer is the fragment index, the second integer is a total count of objects for the fragment, the third integer is a total size of the objects for the fragment.
        :type statsUpdate: List[int]
        """
        super().__init__()
        self.statsUpdate = statsUpdate

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['HeapStatsUpdateEvent']:
        if init is not None:
            return HeapStatsUpdateEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['HeapStatsUpdateEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(HeapStatsUpdateEvent(**it))
            return list_of_self
        else:
            return init


class LastSeenObjectIdEvent(BaseEvent):
    """
    If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp.
	If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
    """

    event = "HeapProfiler.lastSeenObjectId"

    def __init__(self, lastSeenObjectId: int, timestamp: float) -> None:
        """
        :param lastSeenObjectId: The lastSeenObjectId
        :type lastSeenObjectId: int
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.lastSeenObjectId = lastSeenObjectId
        self.timestamp = timestamp

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LastSeenObjectIdEvent']:
        if init is not None:
            return LastSeenObjectIdEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LastSeenObjectIdEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LastSeenObjectIdEvent(**it))
            return list_of_self
        else:
            return init


class ReportHeapSnapshotProgressEvent(BaseEvent):

    event = "HeapProfiler.reportHeapSnapshotProgress"

    def __init__(self, done: int, total: int, finished: Optional[bool] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ReportHeapSnapshotProgressEvent']:
        if init is not None:
            return ReportHeapSnapshotProgressEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ReportHeapSnapshotProgressEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReportHeapSnapshotProgressEvent(**it))
            return list_of_self
        else:
            return init


class ResetProfilesEvent(BaseEvent, dict):

    event = "HeapProfiler.resetProfiles"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ResetProfilesEvent']:
        if init is not None:
            return ResetProfilesEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ResetProfilesEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResetProfilesEvent(**it))
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

