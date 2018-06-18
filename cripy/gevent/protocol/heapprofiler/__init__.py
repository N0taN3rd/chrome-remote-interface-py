from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.heapprofiler import events as Events
from cripy.gevent.protocol.heapprofiler import types as Types

__all__ = ["HeapProfiler"] + Events.__all__ + Types.__all__


class HeapProfiler(object):
    dependencies = ["Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    def addInspectedHeapObject(self, heapObjectId):
        """
        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :type heapObjectId: str
        """
        msg_dict = dict()
        if heapObjectId is not None:
            msg_dict["heapObjectId"] = heapObjectId
        wres = self.chrome.send("HeapProfiler.addInspectedHeapObject", msg_dict)
        return wres.get()

    def collectGarbage(self):
        wres = self.chrome.send("HeapProfiler.collectGarbage")
        return wres.get()

    def disable(self):
        wres = self.chrome.send("HeapProfiler.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("HeapProfiler.enable")
        return wres.get()

    def getHeapObjectId(self, objectId):
        """
        :param objectId: Identifier of the object to get heap object id for.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        wres = self.chrome.send("HeapProfiler.getHeapObjectId", msg_dict)
        res = wres.get()
        return res

    def getObjectByHeapObjectId(self, objectId, objectGroup=None):
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
        wres = self.chrome.send("HeapProfiler.getObjectByHeapObjectId", msg_dict)
        res = wres.get()
        res["result"] = Runtime.RemoteObject.safe_create(res["result"])
        return res

    def getSamplingProfile(self):
        wres = self.chrome.send("HeapProfiler.getSamplingProfile")
        res = wres.get()
        res["profile"] = Types.SamplingHeapProfile.safe_create(res["profile"])
        return res

    def startSampling(self, samplingInterval=None):
        """
        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
        :type samplingInterval: Optional[float]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict["samplingInterval"] = samplingInterval
        wres = self.chrome.send("HeapProfiler.startSampling", msg_dict)
        return wres.get()

    def startTrackingHeapObjects(self, trackAllocations=None):
        """
        :param trackAllocations: The trackAllocations
        :type trackAllocations: Optional[bool]
        """
        msg_dict = dict()
        if trackAllocations is not None:
            msg_dict["trackAllocations"] = trackAllocations
        wres = self.chrome.send("HeapProfiler.startTrackingHeapObjects", msg_dict)
        return wres.get()

    def stopSampling(self):
        wres = self.chrome.send("HeapProfiler.stopSampling")
        res = wres.get()
        res["profile"] = Types.SamplingHeapProfile.safe_create(res["profile"])
        return res

    def stopTrackingHeapObjects(self, reportProgress=None):
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        wres = self.chrome.send("HeapProfiler.stopTrackingHeapObjects", msg_dict)
        return wres.get()

    def takeHeapSnapshot(self, reportProgress=None):
        """
        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :type reportProgress: Optional[bool]
        """
        msg_dict = dict()
        if reportProgress is not None:
            msg_dict["reportProgress"] = reportProgress
        wres = self.chrome.send("HeapProfiler.takeHeapSnapshot", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
