"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["LayerTree"]


class LayerTree:
    """
    Domain Dependencies: 
      * DOM
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of LayerTree

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def compositingReasons(self, layerId: str) -> Awaitable[Dict]:
        """
        Provides the reasons why the given layer was composited.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-compositingReasons`

        :param layerId: The id of the layer for which we want to get the reasons it was composited.
        :return: The results of the command
        """
        return self.client.send("LayerTree.compositingReasons", {"layerId": layerId})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables compositing tree inspection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-disable`

        :return: The results of the command
        """
        return self.client.send("LayerTree.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables compositing tree inspection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-enable`

        :return: The results of the command
        """
        return self.client.send("LayerTree.enable", {})

    def loadSnapshot(self, tiles: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        Returns the snapshot identifier.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-loadSnapshot`

        :param tiles: An array of tiles composing the snapshot.
        :return: The results of the command
        """
        return self.client.send("LayerTree.loadSnapshot", {"tiles": tiles})

    def makeSnapshot(self, layerId: str) -> Awaitable[Dict]:
        """
        Returns the layer snapshot identifier.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-makeSnapshot`

        :param layerId: The id of the layer.
        :return: The results of the command
        """
        return self.client.send("LayerTree.makeSnapshot", {"layerId": layerId})

    def profileSnapshot(
        self,
        snapshotId: str,
        minRepeatCount: Optional[int] = None,
        minDuration: Optional[Union[int, float]] = None,
        clipRect: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-profileSnapshot`

        :param snapshotId: The id of the layer snapshot.
        :param minRepeatCount: The maximum number of times to replay the snapshot (1, if not specified).
        :param minDuration: The minimum duration (in seconds) to replay the snapshot.
        :param clipRect: The clip rectangle to apply when replaying the snapshot.
        :return: The results of the command
        """
        msg = {"snapshotId": snapshotId}
        if minRepeatCount is not None:
            msg["minRepeatCount"] = minRepeatCount
        if minDuration is not None:
            msg["minDuration"] = minDuration
        if clipRect is not None:
            msg["clipRect"] = clipRect
        return self.client.send("LayerTree.profileSnapshot", msg)

    def releaseSnapshot(self, snapshotId: str) -> Awaitable[Dict]:
        """
        Releases layer snapshot captured by the back-end.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-releaseSnapshot`

        :param snapshotId: The id of the layer snapshot.
        :return: The results of the command
        """
        return self.client.send("LayerTree.releaseSnapshot", {"snapshotId": snapshotId})

    def replaySnapshot(
        self,
        snapshotId: str,
        fromStep: Optional[int] = None,
        toStep: Optional[int] = None,
        scale: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Replays the layer snapshot and returns the resulting bitmap.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-replaySnapshot`

        :param snapshotId: The id of the layer snapshot.
        :param fromStep: The first step to replay from (replay from the very start if not specified).
        :param toStep: The last step to replay to (replay till the end if not specified).
        :param scale: The scale to apply while replaying (defaults to 1).
        :return: The results of the command
        """
        msg = {"snapshotId": snapshotId}
        if fromStep is not None:
            msg["fromStep"] = fromStep
        if toStep is not None:
            msg["toStep"] = toStep
        if scale is not None:
            msg["scale"] = scale
        return self.client.send("LayerTree.replaySnapshot", msg)

    def snapshotCommandLog(self, snapshotId: str) -> Awaitable[Dict]:
        """
        Replays the layer snapshot and returns canvas log.

        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#method-snapshotCommandLog`

        :param snapshotId: The id of the layer snapshot.
        :return: The results of the command
        """
        return self.client.send(
            "LayerTree.snapshotCommandLog", {"snapshotId": snapshotId}
        )

    def layerPainted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#event-layerPainted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "LayerTree.layerPainted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def layerTreeDidChange(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/LayerTree#event-layerTreeDidChange`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "LayerTree.layerTreeDidChange"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
