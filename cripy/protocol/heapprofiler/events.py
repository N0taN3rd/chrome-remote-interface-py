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
    def safe_create(init: Optional[dict]) -> Optional[Union['AddHeapSnapshotChunkEvent', dict]]:
        if init is not None:
            try:
                ourselves = AddHeapSnapshotChunkEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AddHeapSnapshotChunkEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AddHeapSnapshotChunkEvent.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['HeapStatsUpdateEvent', dict]]:
        if init is not None:
            try:
                ourselves = HeapStatsUpdateEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['HeapStatsUpdateEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(HeapStatsUpdateEvent.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['LastSeenObjectIdEvent', dict]]:
        if init is not None:
            try:
                ourselves = LastSeenObjectIdEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['LastSeenObjectIdEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LastSeenObjectIdEvent.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['ReportHeapSnapshotProgressEvent', dict]]:
        if init is not None:
            try:
                ourselves = ReportHeapSnapshotProgressEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ReportHeapSnapshotProgressEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ReportHeapSnapshotProgressEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResetProfilesEvent(BaseEvent, dict):

    event = "HeapProfiler.resetProfiles"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ResetProfilesEvent', dict]]:
        if init is not None:
            try:
                ourselves = ResetProfilesEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ResetProfilesEvent', dict]]]:
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

