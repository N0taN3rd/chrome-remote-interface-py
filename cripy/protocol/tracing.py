"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Tracing"]


@attr.dataclass(slots=True, cmp=False)
class Tracing(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def end(self) -> Awaitable[Dict]:
        """
        Stop trace events collection.
        """
        return self.client.send("Tracing.end")

    def getCategories(self) -> Awaitable[Dict]:
        """
        Gets supported tracing categories.
        """
        return self.client.send("Tracing.getCategories")

    def recordClockSyncMarker(self, syncId: str) -> Awaitable[Dict]:
        """
        Record a clock sync marker in the trace.

        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict["syncId"] = syncId
        return self.client.send("Tracing.recordClockSyncMarker", msg_dict)

    def requestMemoryDump(self) -> Awaitable[Dict]:
        """
        Request a global memory dump.
        """
        return self.client.send("Tracing.requestMemoryDump")

    def start(
        self,
        categories: Optional[str] = None,
        options: Optional[str] = None,
        bufferUsageReportingInterval: Optional[float] = None,
        transferMode: Optional[str] = None,
        streamCompression: Optional[str] = None,
        traceConfig: Optional[dict] = None,
    ) -> Awaitable[Dict]:
        """
        Start trace events collection.

        :param categories: Category/tag filter
        :type categories: Optional[str]
        :param options: Tracing options
        :type options: Optional[str]
        :param bufferUsageReportingInterval: If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        :type bufferUsageReportingInterval: Optional[float]
        :param transferMode: Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to `ReportEvents`).
        :type transferMode: Optional[str]
        :param streamCompression: Compression format to use. This only applies when using `ReturnAsStream` transfer mode (defaults to `none`)
        :type streamCompression: Optional[str]
        :param traceConfig: The traceConfig
        :type traceConfig: Optional[dict]
        """
        msg_dict = dict()
        if categories is not None:
            msg_dict["categories"] = categories
        if options is not None:
            msg_dict["options"] = options
        if bufferUsageReportingInterval is not None:
            msg_dict["bufferUsageReportingInterval"] = bufferUsageReportingInterval
        if transferMode is not None:
            msg_dict["transferMode"] = transferMode
        if streamCompression is not None:
            msg_dict["streamCompression"] = streamCompression
        if traceConfig is not None:
            msg_dict["traceConfig"] = traceConfig
        return self.client.send("Tracing.start", msg_dict)

    def bufferUsage(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Tracing.bufferUsage", _cb)

            return future

        self.client.on("Tracing.bufferUsage", cb)
        return lambda: self.client.remove_listener("Tracing.bufferUsage", cb)

    def dataCollected(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Contains an bucket of collected trace events. When tracing is stopped collected events will be
        send as a sequence of dataCollected events followed by tracingComplete event.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Tracing.dataCollected", _cb)

            return future

        self.client.on("Tracing.dataCollected", cb)
        return lambda: self.client.remove_listener("Tracing.dataCollected", cb)

    def tracingComplete(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Signals that tracing is stopped and there is no trace buffers pending flush, all data were
        delivered via dataCollected events.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Tracing.tracingComplete", _cb)

            return future

        self.client.on("Tracing.tracingComplete", cb)
        return lambda: self.client.remove_listener("Tracing.tracingComplete", cb)
