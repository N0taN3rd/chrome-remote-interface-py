from typing import Any, List, Optional, Union
from cripy.protocol.dom import types as DOM
from cripy.protocol.layertree import events as Events
from cripy.protocol.layertree import types as Types


class LayerTree(object):
    dependencies = ["DOM"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def compositingReasons(self, layerId: str) -> Optional[dict]:
        """
        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        mayberes = await self.chrome.send("LayerTree.compositingReasons", msg_dict)
        res = await mayberes
        return res

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("LayerTree.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("LayerTree.enable")
        return mayberes

    async def loadSnapshot(self, tiles: List[dict]) -> Optional[dict]:
        """
        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        msg_dict = dict()
        if tiles is not None:
            msg_dict["tiles"] = tiles
        mayberes = await self.chrome.send("LayerTree.loadSnapshot", msg_dict)
        res = await mayberes
        return res

    async def makeSnapshot(self, layerId: str) -> Optional[dict]:
        """
        :param layerId: The id of the layer.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        mayberes = await self.chrome.send("LayerTree.makeSnapshot", msg_dict)
        res = await mayberes
        return res

    async def profileSnapshot(
        self,
        snapshotId: str,
        minRepeatCount: Optional[int] = None,
        minDuration: Optional[float] = None,
        clipRect: Optional[dict] = None,
    ) -> Optional[dict]:
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
        mayberes = await self.chrome.send("LayerTree.profileSnapshot", msg_dict)
        res = await mayberes
        return res

    async def releaseSnapshot(self, snapshotId: str) -> Optional[dict]:
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        mayberes = await self.chrome.send("LayerTree.releaseSnapshot", msg_dict)
        return mayberes

    async def replaySnapshot(
        self,
        snapshotId: str,
        fromStep: Optional[int] = None,
        toStep: Optional[int] = None,
        scale: Optional[float] = None,
    ) -> Optional[dict]:
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
        mayberes = await self.chrome.send("LayerTree.replaySnapshot", msg_dict)
        res = await mayberes
        return res

    async def snapshotCommandLog(self, snapshotId: str) -> Optional[dict]:
        """
        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        mayberes = await self.chrome.send("LayerTree.snapshotCommandLog", msg_dict)
        res = await mayberes
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
