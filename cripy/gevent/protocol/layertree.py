__all__ = ["LayerTree"]


class LayerTree(object):
    dependencies = ['DOM']

    def __init__(self, chrome):
        """
        Construct a new LayerTree object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def compositingReasons(self, layerId):
        """
        Provides the reasons why the given layer was composited.

        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict['layerId'] = layerId
        wres = self.chrome.send('LayerTree.compositingReasons', msg_dict)
        return wres.get()

    def disable(self):
        """
        Disables compositing tree inspection.
        """
        wres = self.chrome.send('LayerTree.disable')
        return wres.get()

    def enable(self):
        """
        Enables compositing tree inspection.
        """
        wres = self.chrome.send('LayerTree.enable')
        return wres.get()

    def loadSnapshot(self, tiles):
        """
        Returns the snapshot identifier.

        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        msg_dict = dict()
        if tiles is not None:
            msg_dict['tiles'] = tiles
        wres = self.chrome.send('LayerTree.loadSnapshot', msg_dict)
        return wres.get()

    def makeSnapshot(self, layerId):
        """
        Returns the layer snapshot identifier.

        :param layerId: The id of the layer.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict['layerId'] = layerId
        wres = self.chrome.send('LayerTree.makeSnapshot', msg_dict)
        return wres.get()

    def profileSnapshot(self, snapshotId, minRepeatCount=None, minDuration=None, clipRect=None):
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
            msg_dict['snapshotId'] = snapshotId
        if minRepeatCount is not None:
            msg_dict['minRepeatCount'] = minRepeatCount
        if minDuration is not None:
            msg_dict['minDuration'] = minDuration
        if clipRect is not None:
            msg_dict['clipRect'] = clipRect
        wres = self.chrome.send('LayerTree.profileSnapshot', msg_dict)
        return wres.get()

    def releaseSnapshot(self, snapshotId):
        """
        Releases layer snapshot captured by the back-end.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        wres = self.chrome.send('LayerTree.releaseSnapshot', msg_dict)
        return wres.get()

    def replaySnapshot(self, snapshotId, fromStep=None, toStep=None, scale=None):
        """
        Replays the layer snapshot and returns the resulting bitmap.

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
            msg_dict['snapshotId'] = snapshotId
        if fromStep is not None:
            msg_dict['fromStep'] = fromStep
        if toStep is not None:
            msg_dict['toStep'] = toStep
        if scale is not None:
            msg_dict['scale'] = scale
        wres = self.chrome.send('LayerTree.replaySnapshot', msg_dict)
        return wres.get()

    def snapshotCommandLog(self, snapshotId):
        """
        Replays the layer snapshot and returns canvas log.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict['snapshotId'] = snapshotId
        wres = self.chrome.send('LayerTree.snapshotCommandLog', msg_dict)
        return wres.get()

    def layerPainted(self, fn, once=False):
        self.chrome.on("LayerTree.layerPainted", fn, once=once)

    def layerTreeDidChange(self, fn, once=False):
        self.chrome.on("LayerTree.layerTreeDidChange", fn, once=once)


