"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["HeapProfiler"]


@attr.dataclass(slots=True, cmp=False)
class HeapProfiler(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def addInspectedHeapObject(self, heapObjectId: str) -> Awaitable[Dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict["heapObjectId"] = heapObjectId
        return self.client.send("HeapProfiler.addInspectedHeapObject", msg_dict)

    def collectGarbage(self) -> Awaitable[Dict]:
        return self.client.send("HeapProfiler.collectGarbage")

    def disable(self) -> Awaitable[Dict]:
        return self.client.send("HeapProfiler.disable")

    def enable(self) -> Awaitable[Dict]:
        return self.client.send("HeapProfiler.enable")

    def getHeapObjectId(self, objectId: str) -> Awaitable[Dict]:
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        return self.client.send("HeapProfiler.getHeapObjectId", msg_dict)

    def getObjectByHeapObjectId(
        self, objectId: str, objectGroup: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        :param objectId: The objectId
        :type objectId: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        return self.client.send("HeapProfiler.getObjectByHeapObjectId", msg_dict)

    def getSamplingProfile(self) -> Awaitable[Dict]:
        return self.client.send("HeapProfiler.getSamplingProfile")

    def startSampling(
        self, samplingInterval: Optional[float] = None
    ) -> Awaitable[Dict]:
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict["samplingInterval"] = samplingInterval
        return self.client.send("HeapProfiler.startSampling", msg_dict)

    def startTrackingHeapObjects(
        self, trackAllocations: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict["trackAllocations"] = trackAllocations
        return self.client.send("HeapProfiler.startTrackingHeapObjects", msg_dict)

    def stopSampling(self) -> Awaitable[Dict]:
        return self.client.send("HeapProfiler.stopSampling")

    def stopTrackingHeapObjects(
        self, reportProgress: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        return self.client.send("HeapProfiler.stopTrackingHeapObjects", msg_dict)

    def takeHeapSnapshot(
        self, reportProgress: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        return self.client.send("HeapProfiler.takeHeapSnapshot", msg_dict)

    def addHeapSnapshotChunk(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeapProfiler.addHeapSnapshotChunk", _cb)

            return future

        self.client.on("HeapProfiler.addHeapSnapshotChunk", cb)
        return lambda: self.client.remove_listener(
            "HeapProfiler.addHeapSnapshotChunk", cb
        )

    def heapStatsUpdate(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        If heap objects tracking has been started then backend may send update for one or more fragments
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeapProfiler.heapStatsUpdate", _cb)

            return future

        self.client.on("HeapProfiler.heapStatsUpdate", cb)
        return lambda: self.client.remove_listener("HeapProfiler.heapStatsUpdate", cb)

    def lastSeenObjectId(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        If heap objects tracking has been started then backend regularly sends a current value for last
        seen object id and corresponding timestamp. If the were changes in the heap since last event
        then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeapProfiler.lastSeenObjectId", _cb)

            return future

        self.client.on("HeapProfiler.lastSeenObjectId", cb)
        return lambda: self.client.remove_listener("HeapProfiler.lastSeenObjectId", cb)

    def reportHeapSnapshotProgress(
        self, cb: Optional[Callable[..., Any]] = None
    ) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeapProfiler.reportHeapSnapshotProgress", _cb)

            return future

        self.client.on("HeapProfiler.reportHeapSnapshotProgress", cb)
        return lambda: self.client.remove_listener(
            "HeapProfiler.reportHeapSnapshotProgress", cb
        )

    def resetProfiles(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeapProfiler.resetProfiles", _cb)

            return future

        self.client.on("HeapProfiler.resetProfiles", cb)
        return lambda: self.client.remove_listener("HeapProfiler.resetProfiles", cb)
