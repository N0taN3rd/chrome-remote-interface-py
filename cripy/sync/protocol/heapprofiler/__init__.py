from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.heapprofiler import events as Events
from cripy.sync.protocol.heapprofiler import types as Types

__all__ = ["HeapProfiler"] + Events.__all__ + Types.__all__ 


class HeapProfiler(object):
    dependencies = ['Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def addInspectedHeapObject(self, heapObjectId):
        """
        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict['heapObjectId'] = heapObjectId
        self.chrome.send('HeapProfiler.addInspectedHeapObject', params=msg_dict)


    def collectGarbage(self):
        self.chrome.send('HeapProfiler.collectGarbage')


    def disable(self):
        self.chrome.send('HeapProfiler.disable')


    def enable(self):
        self.chrome.send('HeapProfiler.enable')


    def getHeapObjectId(self, objectId):
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        def cb(res):
            self.chrome.emit('HeapProfiler.getHeapObjectId', res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('HeapProfiler.getHeapObjectId', params=msg_dict, cb=cb)


    def getObjectByHeapObjectId(self, objectId, objectGroup):
        """
        :param objectId: The objectId
        :type objectId: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        def cb(res):
            res['result'] = Runtime.RemoteObject.safe_create(res['result'])
            self.chrome.emit('HeapProfiler.getObjectByHeapObjectId', res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        self.chrome.send('HeapProfiler.getObjectByHeapObjectId', params=msg_dict, cb=cb)


    def getSamplingProfile(self):
        def cb(res):
            res['profile'] = Types.SamplingHeapProfile.safe_create(res['profile'])
            self.chrome.emit('HeapProfiler.getSamplingProfile', res)
        self.chrome.send('HeapProfiler.getSamplingProfile', cb=cb)


    def startSampling(self, samplingInterval):
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict['samplingInterval'] = samplingInterval
        self.chrome.send('HeapProfiler.startSampling', params=msg_dict)


    def startTrackingHeapObjects(self, trackAllocations):
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict['trackAllocations'] = trackAllocations
        self.chrome.send('HeapProfiler.startTrackingHeapObjects', params=msg_dict)


    def stopSampling(self):
        def cb(res):
            res['profile'] = Types.SamplingHeapProfile.safe_create(res['profile'])
            self.chrome.emit('HeapProfiler.stopSampling', res)
        self.chrome.send('HeapProfiler.stopSampling', cb=cb)


    def stopTrackingHeapObjects(self, reportProgress):
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        self.chrome.send('HeapProfiler.stopTrackingHeapObjects', params=msg_dict)


    def takeHeapSnapshot(self, reportProgress):
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict['reportProgress'] = reportProgress
        self.chrome.send('HeapProfiler.takeHeapSnapshot', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

