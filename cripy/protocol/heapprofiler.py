# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["HeapProfiler"]


class HeapProfiler(object):
    dependencies: ClassVar[List[str]] = ["Runtime"]

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def addInspectedHeapObject(self, heapObjectId: str) -> Optional[dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict["heapObjectId"] = heapObjectId
        res = await self.client.send("HeapProfiler.addInspectedHeapObject", msg_dict)
        return res

    async def collectGarbage(self) -> Optional[dict]:
        res = await self.client.send("HeapProfiler.collectGarbage")
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.client.send("HeapProfiler.disable")
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.client.send("HeapProfiler.enable")
        return res

    async def getHeapObjectId(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("HeapProfiler.getHeapObjectId", msg_dict)
        return res

    async def getObjectByHeapObjectId(
        self, objectId: str, objectGroup: Optional[str] = None
    ) -> Optional[dict]:
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
        res = await self.client.send("HeapProfiler.getObjectByHeapObjectId", msg_dict)
        return res

    async def getSamplingProfile(self) -> Optional[dict]:
        res = await self.client.send("HeapProfiler.getSamplingProfile")
        return res

    async def startSampling(
        self, samplingInterval: Optional[float] = None
    ) -> Optional[dict]:
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict["samplingInterval"] = samplingInterval
        res = await self.client.send("HeapProfiler.startSampling", msg_dict)
        return res

    async def startTrackingHeapObjects(
        self, trackAllocations: Optional[bool] = None
    ) -> Optional[dict]:
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict["trackAllocations"] = trackAllocations
        res = await self.client.send("HeapProfiler.startTrackingHeapObjects", msg_dict)
        return res

    async def stopSampling(self) -> Optional[dict]:
        res = await self.client.send("HeapProfiler.stopSampling")
        return res

    async def stopTrackingHeapObjects(
        self, reportProgress: Optional[bool] = None
    ) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        res = await self.client.send("HeapProfiler.stopTrackingHeapObjects", msg_dict)
        return res

    async def takeHeapSnapshot(
        self, reportProgress: Optional[bool] = None
    ) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        res = await self.client.send("HeapProfiler.takeHeapSnapshot", msg_dict)
        return res

    def addHeapSnapshotChunk(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("HeapProfiler.addHeapSnapshotChunk", fn)
        else:
            self.client.on("HeapProfiler.addHeapSnapshotChunk", fn)

    def heapStatsUpdate(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        If heap objects tracking has been started then backend may send update for one or more fragments
        """
        if once:
            self.client.once("HeapProfiler.heapStatsUpdate", fn)
        else:
            self.client.on("HeapProfiler.heapStatsUpdate", fn)

    def lastSeenObjectId(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        If heap objects tracking has been started then backend regularly sends a current value for last
        seen object id and corresponding timestamp. If the were changes in the heap since last event
        then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.
        """
        if once:
            self.client.once("HeapProfiler.lastSeenObjectId", fn)
        else:
            self.client.on("HeapProfiler.lastSeenObjectId", fn)

    def reportHeapSnapshotProgress(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        if once:
            self.client.once("HeapProfiler.reportHeapSnapshotProgress", fn)
        else:
            self.client.on("HeapProfiler.reportHeapSnapshotProgress", fn)

    def resetProfiles(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("HeapProfiler.resetProfiles", fn)
        else:
            self.client.on("HeapProfiler.resetProfiles", fn)

    def __repr__(self):
        return f"HeapProfiler()"
