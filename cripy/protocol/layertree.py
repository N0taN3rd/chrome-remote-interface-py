# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["LayerTree"]


@attr.dataclass(slots=True, cmp=False)
class LayerTree(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def compositingReasons(self, layerId: str) -> Awaitable[Optional[dict]]:
        """
        Provides the reasons why the given layer was composited.

        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        return self.client.send("LayerTree.compositingReasons", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables compositing tree inspection.
        """
        return self.client.send("LayerTree.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables compositing tree inspection.
        """
        return self.client.send("LayerTree.enable")

    def loadSnapshot(self, tiles: List[dict]) -> Awaitable[Optional[dict]]:
        """
        Returns the snapshot identifier.

        :param tiles: An array of tiles composing the snapshot.
        :type tiles: List[dict]
        """
        msg_dict = dict()
        if tiles is not None:
            msg_dict["tiles"] = tiles
        return self.client.send("LayerTree.loadSnapshot", msg_dict)

    def makeSnapshot(self, layerId: str) -> Awaitable[Optional[dict]]:
        """
        Returns the layer snapshot identifier.

        :param layerId: The id of the layer.
        :type layerId: str
        """
        msg_dict = dict()
        if layerId is not None:
            msg_dict["layerId"] = layerId
        return self.client.send("LayerTree.makeSnapshot", msg_dict)

    def profileSnapshot(
        self,
        snapshotId: str,
        minRepeatCount: Optional[int] = None,
        minDuration: Optional[float] = None,
        clipRect: Optional[dict] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("LayerTree.profileSnapshot", msg_dict)

    def releaseSnapshot(self, snapshotId: str) -> Awaitable[Optional[dict]]:
        """
        Releases layer snapshot captured by the back-end.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        return self.client.send("LayerTree.releaseSnapshot", msg_dict)

    def replaySnapshot(
        self,
        snapshotId: str,
        fromStep: Optional[int] = None,
        toStep: Optional[int] = None,
        scale: Optional[float] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("LayerTree.replaySnapshot", msg_dict)

    def snapshotCommandLog(self, snapshotId: str) -> Awaitable[Optional[dict]]:
        """
        Replays the layer snapshot and returns canvas log.

        :param snapshotId: The id of the layer snapshot.
        :type snapshotId: str
        """
        msg_dict = dict()
        if snapshotId is not None:
            msg_dict["snapshotId"] = snapshotId
        return self.client.send("LayerTree.snapshotCommandLog", msg_dict)

    def layerPainted(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("LayerTree.layerPainted", _cb)

            return future

        self.client.on("LayerTree.layerPainted", cb)

    def layerTreeDidChange(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("LayerTree.layerTreeDidChange", _cb)

            return future

        self.client.on("LayerTree.layerTreeDidChange", cb)
