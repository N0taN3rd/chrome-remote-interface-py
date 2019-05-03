"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Tracing"]


class Tracing:
    """
    Domain Dependencies: 
      * IO
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Tracing

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def end(self) -> Awaitable[Dict]:
        """
        Stop trace events collection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#method-end`

        :return: The results of the command
        """
        return self.client.send("Tracing.end", {})

    def getCategories(self) -> Awaitable[Dict]:
        """
        Gets supported tracing categories.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#method-getCategories`

        :return: The results of the command
        """
        return self.client.send("Tracing.getCategories", {})

    def recordClockSyncMarker(self, syncId: str) -> Awaitable[Dict]:
        """
        Record a clock sync marker in the trace.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#method-recordClockSyncMarker`

        :param syncId: The ID of this clock sync marker
        :return: The results of the command
        """
        return self.client.send("Tracing.recordClockSyncMarker", {"syncId": syncId})

    def requestMemoryDump(self) -> Awaitable[Dict]:
        """
        Request a global memory dump.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#method-requestMemoryDump`

        :return: The results of the command
        """
        return self.client.send("Tracing.requestMemoryDump", {})

    def start(
        self,
        categories: Optional[str] = None,
        options: Optional[str] = None,
        bufferUsageReportingInterval: Optional[Union[int, float]] = None,
        transferMode: Optional[str] = None,
        streamFormat: Optional[str] = None,
        streamCompression: Optional[str] = None,
        traceConfig: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Start trace events collection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#method-start`

        :param categories: Category/tag filter
        :param options: Tracing options
        :param bufferUsageReportingInterval: If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        :param transferMode: Whether to report trace events as series of dataCollected events or to save trace to a
         stream (defaults to `ReportEvents`).
        :param streamFormat: Trace data format to use. This only applies when using `ReturnAsStream`
         transfer mode (defaults to `json`).
        :param streamCompression: Compression format to use. This only applies when using `ReturnAsStream`
         transfer mode (defaults to `none`)
        :param traceConfig: The traceConfig
        :return: The results of the command
        """
        msg = {}
        if categories is not None:
            msg["categories"] = categories
        if options is not None:
            msg["options"] = options
        if bufferUsageReportingInterval is not None:
            msg["bufferUsageReportingInterval"] = bufferUsageReportingInterval
        if transferMode is not None:
            msg["transferMode"] = transferMode
        if streamFormat is not None:
            msg["streamFormat"] = streamFormat
        if streamCompression is not None:
            msg["streamCompression"] = streamCompression
        if traceConfig is not None:
            msg["traceConfig"] = traceConfig
        return self.client.send("Tracing.start", msg)

    def bufferUsage(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#event-bufferUsage`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Tracing.bufferUsage"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def dataCollected(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Contains an bucket of collected trace events. When tracing is stopped collected events will be
        send as a sequence of dataCollected events followed by tracingComplete event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#event-dataCollected`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Tracing.dataCollected"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def tracingComplete(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Signals that tracing is stopped and there is no trace buffers pending flush, all data were
        delivered via dataCollected events.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tracing#event-tracingComplete`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Tracing.tracingComplete"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
