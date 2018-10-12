# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["LayerTree"]


class LayerTree(object):
    dependencies: ClassVar[List[str]] = ["DOM"]

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def compositingReasons(self, layerId: str) -> Optional[dict]:
        """
        Provides the reasons why the given layer was composited.

        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        res = await self.client.send("LayerTree.compositingReasons", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables compositing tree inspection.
        """
        res = await self.client.send("LayerTree.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables compositing tree inspection.
        """
        res = await self.client.send("LayerTree.enable")
        return res

    async def loadSnapshot(self, tiles: List[dict]) -> Optional[dict]:
        """
        Returns the snapshot identifier.

        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        msg_dict = dict()
        if tiles is not None:
            msg_dict["tiles"] = tiles
        res = await self.client.send("LayerTree.loadSnapshot", msg_dict)
        return res

    async def makeSnapshot(self, layerId: str) -> Optional[dict]:
        """
        Returns the layer snapshot identifier.

        :param layerId: The id of the layer.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        res = await self.client.send("LayerTree.makeSnapshot", msg_dict)
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
        res = await self.client.send("LayerTree.profileSnapshot", msg_dict)
        return res

    async def releaseSnapshot(self, snapshotId: str) -> Optional[dict]:
        """
        Releases layer snapshot captured by the back-end.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        res = await self.client.send("LayerTree.releaseSnapshot", msg_dict)
        return res

    async def replaySnapshot(
        self,
        snapshotId: str,
        fromStep: Optional[int] = None,
        toStep: Optional[int] = None,
        scale: Optional[float] = None,
    ) -> Optional[dict]:
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
            msg_dict["snapshotId"] = snapshotId
        if fromStep is not None:
            msg_dict["fromStep"] = fromStep
        if toStep is not None:
            msg_dict["toStep"] = toStep
        if scale is not None:
            msg_dict["scale"] = scale
        res = await self.client.send("LayerTree.replaySnapshot", msg_dict)
        return res

    async def snapshotCommandLog(self, snapshotId: str) -> Optional[dict]:
        """
        Replays the layer snapshot and returns canvas log.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        res = await self.client.send("LayerTree.snapshotCommandLog", msg_dict)
        return res

    def layerPainted(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("LayerTree.layerPainted", fn)
        else:
            self.client.on("LayerTree.layerPainted", fn)

    def layerTreeDidChange(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("LayerTree.layerTreeDidChange", fn)
        else:
            self.client.on("LayerTree.layerTreeDidChange", fn)

    def __repr__(self):
        return f"LayerTree()"
