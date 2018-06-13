from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.layertree import events as Events
from cripy.sync.protocol.layertree import types as Types

__all__ = ["LayerTree"] + Events.__all__ + Types.__all__ 


class LayerTree(object):
    dependencies = ['DOM']

    def __init__(self, chrome):
        self.chrome = chrome

    def compositingReasons(self, layerId, cb=None):
        """
        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if layerId is not None:
            msg_dict['layerId'] = layerId
        self.chrome.send('LayerTree.compositingReasons', params=msg_dict, cb=cb_wrapper)


    def disable(self, cb=None):
        self.chrome.send('LayerTree.disable')


    def enable(self, cb=None):
        self.chrome.send('LayerTree.enable')


    def loadSnapshot(self, tiles, cb=None):
        """
        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if tiles is not None:
            msg_dict['tiles'] = tiles
        self.chrome.send('LayerTree.loadSnapshot', params=msg_dict, cb=cb_wrapper)


    def makeSnapshot(self, layerId, cb=None):
        """
        :param layerId: The id of the layer.
        :type layerId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if layerId is not None:
            msg_dict['layerId'] = layerId
        self.chrome.send('LayerTree.makeSnapshot', params=msg_dict, cb=cb_wrapper)


    def profileSnapshot(self, snapshotId, minRepeatCount, minDuration, clipRect, cb=None):
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
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        if minRepeatCount is not None:
            msg_dict['minRepeatCount'] = minRepeatCount
        if minDuration is not None:
            msg_dict['minDuration'] = minDuration
        if clipRect is not None:
            msg_dict['clipRect'] = clipRect
        self.chrome.send('LayerTree.profileSnapshot', params=msg_dict, cb=cb_wrapper)


    def releaseSnapshot(self, snapshotId, cb=None):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        self.chrome.send('LayerTree.releaseSnapshot', params=msg_dict)


    def replaySnapshot(self, snapshotId, fromStep, toStep, scale, cb=None):
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
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        if fromStep is not None:
            msg_dict['fromStep'] = fromStep
        if toStep is not None:
            msg_dict['toStep'] = toStep
        if scale is not None:
            msg_dict['scale'] = scale
        self.chrome.send('LayerTree.replaySnapshot', params=msg_dict, cb=cb_wrapper)


    def snapshotCommandLog(self, snapshotId, cb=None):
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        self.chrome.send('LayerTree.snapshotCommandLog', params=msg_dict, cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

