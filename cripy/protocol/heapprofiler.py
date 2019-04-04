"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["HeapProfiler"]


class HeapProfiler:
    """
    Domain Dependencies: 
      * Runtime
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of HeapProfiler

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def addInspectedHeapObject(self, heapObjectId: str) -> Awaitable[Dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions).

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-addInspectedHeapObject`

        :param heapObjectId: Heap snapshot object id to be accessible by means of $x command line API.
        :return: The results of the command
        """
        return self.client.send(
            "HeapProfiler.addInspectedHeapObject", {"heapObjectId": heapObjectId}
        )

    def collectGarbage(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-collectGarbage`

        :return: The results of the command
        """
        return self.client.send("HeapProfiler.collectGarbage", {})

    def disable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-disable`

        :return: The results of the command
        """
        return self.client.send("HeapProfiler.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-enable`

        :return: The results of the command
        """
        return self.client.send("HeapProfiler.enable", {})

    def getHeapObjectId(self, objectId: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-getHeapObjectId`

        :param objectId: Identifier of the object to get heap object id for.
        :return: The results of the command
        """
        return self.client.send("HeapProfiler.getHeapObjectId", {"objectId": objectId})

    def getObjectByHeapObjectId(
        self, objectId: str, objectGroup: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-getObjectByHeapObjectId`

        :param objectId: The objectId
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :return: The results of the command
        """
        msg = {"objectId": objectId}
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        return self.client.send("HeapProfiler.getObjectByHeapObjectId", msg)

    def getSamplingProfile(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-getSamplingProfile`

        :return: The results of the command
        """
        return self.client.send("HeapProfiler.getSamplingProfile", {})

    def startSampling(
        self, samplingInterval: Optional[Union[int, float]] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-startSampling`

        :param samplingInterval: Average sample interval in bytes. Poisson distribution is used for the intervals. The
         default value is 32768 bytes.
        :return: The results of the command
        """
        msg = {}
        if samplingInterval is not None:
            msg["samplingInterval"] = samplingInterval
        return self.client.send("HeapProfiler.startSampling", msg)

    def startTrackingHeapObjects(
        self, trackAllocations: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-startTrackingHeapObjects`

        :param trackAllocations: The trackAllocations
        :return: The results of the command
        """
        msg = {}
        if trackAllocations is not None:
            msg["trackAllocations"] = trackAllocations
        return self.client.send("HeapProfiler.startTrackingHeapObjects", msg)

    def stopSampling(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-stopSampling`

        :return: The results of the command
        """
        return self.client.send("HeapProfiler.stopSampling", {})

    def stopTrackingHeapObjects(
        self, reportProgress: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-stopTrackingHeapObjects`

        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken
         when the tracking is stopped.
        :return: The results of the command
        """
        msg = {}
        if reportProgress is not None:
            msg["reportProgress"] = reportProgress
        return self.client.send("HeapProfiler.stopTrackingHeapObjects", msg)

    def takeHeapSnapshot(
        self, reportProgress: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#method-takeHeapSnapshot`

        :param reportProgress: If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
        :return: The results of the command
        """
        msg = {}
        if reportProgress is not None:
            msg["reportProgress"] = reportProgress
        return self.client.send("HeapProfiler.takeHeapSnapshot", msg)

    def addHeapSnapshotChunk(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#event-addHeapSnapshotChunk`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeapProfiler.addHeapSnapshotChunk"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def heapStatsUpdate(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        If heap objects tracking has been started then backend may send update for one or more fragments

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#event-heapStatsUpdate`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeapProfiler.heapStatsUpdate"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def lastSeenObjectId(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        If heap objects tracking has been started then backend regularly sends a current value for last
        seen object id and corresponding timestamp. If the were changes in the heap since last event
        then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#event-lastSeenObjectId`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeapProfiler.lastSeenObjectId"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def reportHeapSnapshotProgress(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#event-reportHeapSnapshotProgress`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeapProfiler.reportHeapSnapshotProgress"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def resetProfiles(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler#event-resetProfiles`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeapProfiler.resetProfiles"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
