from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.layertree import events as Events
from cripy.gevent.protocol.layertree import types as Types

__all__ = ["LayerTree"] + Events.__all__ + Types.__all__


class LayerTree(object):
    dependencies = ["DOM"]

    def __init__(self, chrome):
        self.chrome = chrome

    def compositingReasons(self, layerId):
        """
        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        wres = self.chrome.send("LayerTree.compositingReasons", msg_dict)
        res = wres.get()
        return res

    def disable(self):
        wres = self.chrome.send("LayerTree.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("LayerTree.enable")
        return wres.get()

    def loadSnapshot(self, tiles):
        """
        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        msg_dict = dict()
        if tiles is not None:
            msg_dict["tiles"] = tiles
        wres = self.chrome.send("LayerTree.loadSnapshot", msg_dict)
        res = wres.get()
        return res

    def makeSnapshot(self, layerId):
        """
        :param layerId: The id of the layer.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        wres = self.chrome.send("LayerTree.makeSnapshot", msg_dict)
        res = wres.get()
        return res

    def profileSnapshot(
        self, snapshotId, minRepeatCount=None, minDuration=None, clipRect=None
    ):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        :param minRepeatCount: The maximum number of times to replay the snapshot (1, if not specified).
        :type minRepeatCount: Optional[int]
        :param minDuration: The minimum duration (in seconds) to replay the snapshot.
        :type minDuration: Optional[float]
        :param clipRect: The clip rectangle to apply when replaying the snapshot.
        :type clipRect: Optional[dict]
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        if minRepeatCount is not None:
            msg_dict["minRepeatCount"] = minRepeatCount
        if minDuration is not None:
            msg_dict["minDuration"] = minDuration
        if clipRect is not None:
            msg_dict["clipRect"] = clipRect
        wres = self.chrome.send("LayerTree.profileSnapshot", msg_dict)
        res = wres.get()
        return res

    def releaseSnapshot(self, snapshotId):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        wres = self.chrome.send("LayerTree.releaseSnapshot", msg_dict)
        return wres.get()

    def replaySnapshot(self, snapshotId, fromStep=None, toStep=None, scale=None):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        :param fromStep: The first step to replay from (replay from the very start if not specified).
        :type fromStep: Optional[int]
        :param toStep: The last step to replay to (replay till the end if not specified).
        :type toStep: Optional[int]
        :param scale: The scale to apply while replaying (defaults to 1).
        :type scale: Optional[float]
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        if fromStep is not None:
            msg_dict["fromStep"] = fromStep
        if toStep is not None:
            msg_dict["toStep"] = toStep
        if scale is not None:
            msg_dict["scale"] = scale
        wres = self.chrome.send("LayerTree.replaySnapshot", msg_dict)
        res = wres.get()
        return res

    def snapshotCommandLog(self, snapshotId):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        wres = self.chrome.send("LayerTree.snapshotCommandLog", msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
