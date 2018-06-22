from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.runtime import types as Runtime
from cripy.asyncio.protocol.heapprofiler import events as Events
from cripy.asyncio.protocol.heapprofiler import types as Types

__all__ = ["HeapProfiler"]


class HeapProfiler(object):
    dependencies = ['Runtime']

    events = Events.HEAPPROFILER_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new HeapProfiler object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def addInspectedHeapObject(self, heapObjectId: str) -> Optional[dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict['heapObjectId'] = heapObjectId
        mayberes = await self.chrome.send('HeapProfiler.addInspectedHeapObject', msg_dict)
        return mayberes

    async def collectGarbage(self) -> Optional[dict]:
        mayberes = await self.chrome.send('HeapProfiler.collectGarbage')
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send('HeapProfiler.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send('HeapProfiler.enable')
        return mayberes

    async def getHeapObjectId(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        mayberes = await self.chrome.send('HeapProfiler.getHeapObjectId', msg_dict)
        res = await mayberes
        return res

    async def getObjectByHeapObjectId(self, objectId: str, objectGroup: Optional[str] = None) -> Optional[dict]:
        """
        :param objectId: The objectId
        :type objectId: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        mayberes = await self.chrome.send('HeapProfiler.getObjectByHeapObjectId', msg_dict)
        res = await mayberes
        res['result'] = Runtime.RemoteObject.safe_create(res['result'])
        return res

    async def getSamplingProfile(self) -> Optional[dict]:
        mayberes = await self.chrome.send('HeapProfiler.getSamplingProfile')
        res = await mayberes
        res['profile'] = Types.SamplingHeapProfile.safe_create(res['profile'])
        return res

    async def startSampling(self, samplingInterval: Optional[float] = None) -> Optional[dict]:
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict['samplingInterval'] = samplingInterval
        mayberes = await self.chrome.send('HeapProfiler.startSampling', msg_dict)
        return mayberes

    async def startTrackingHeapObjects(self, trackAllocations: Optional[bool] = None) -> Optional[dict]:
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict['trackAllocations'] = trackAllocations
        mayberes = await self.chrome.send('HeapProfiler.startTrackingHeapObjects', msg_dict)
        return mayberes

    async def stopSampling(self) -> Optional[dict]:
        mayberes = await self.chrome.send('HeapProfiler.stopSampling')
        res = await mayberes
        res['profile'] = Types.SamplingHeapProfile.safe_create(res['profile'])
        return res

    async def stopTrackingHeapObjects(self, reportProgress: Optional[bool] = None) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        mayberes = await self.chrome.send('HeapProfiler.stopTrackingHeapObjects', msg_dict)
        return mayberes

    async def takeHeapSnapshot(self, reportProgress: Optional[bool] = None) -> Optional[dict]:
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        mayberes = await self.chrome.send('HeapProfiler.takeHeapSnapshot', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.HEAPPROFILER_EVENTS_TO_CLASS

