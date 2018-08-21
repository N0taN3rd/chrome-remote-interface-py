from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Tracing"]


@attr.dataclass(slots=True)
class Tracing(object):
    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["IO"]

    async def end(self) -> Optional[dict]:
        """
        Stop trace events collection.
        """
        res = await self.client.send("Tracing.end")
        return res

    async def getCategories(self) -> Optional[dict]:
        """
        Gets supported tracing categories.
        """
        res = await self.client.send("Tracing.getCategories")
        return res

    async def recordClockSyncMarker(self, syncId: str) -> Optional[dict]:
        """
        Record a clock sync marker in the trace.

        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict["syncId"] = syncId
        res = await self.client.send("Tracing.recordClockSyncMarker", msg_dict)
        return res

    async def requestMemoryDump(self) -> Optional[dict]:
        """
        Request a global memory dump.
        """
        res = await self.client.send("Tracing.requestMemoryDump")
        return res

    async def start(
        self,
        categories: Optional[str] = None,
        options: Optional[str] = None,
        bufferUsageReportingInterval: Optional[float] = None,
        transferMode: Optional[str] = None,
        streamCompression: Optional[str] = None,
        traceConfig: Optional[dict] = None,
    ) -> Optional[dict]:
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
        res = await self.client.send("Tracing.start", msg_dict)
        return res

    def bufferUsage(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("Tracing.bufferUsage", fn)
        else:
            self.client.on("Tracing.bufferUsage", fn)

    def dataCollected(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Contains an bucket of collected trace events. When tracing is stopped collected events will be
        send as a sequence of dataCollected events followed by tracingComplete event.
        """
        if once:
            self.client.once("Tracing.dataCollected", fn)
        else:
            self.client.on("Tracing.dataCollected", fn)

    def tracingComplete(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Signals that tracing is stopped and there is no trace buffers pending flush, all data were
        delivered via dataCollected events.
        """
        if once:
            self.client.once("Tracing.tracingComplete", fn)
        else:
            self.client.on("Tracing.tracingComplete", fn)
