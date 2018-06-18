from typing import Any, List, Optional, Union
from cripy.async.protocol.tracing import events as Events
from cripy.async.protocol.tracing import types as Types


class Tracing(object):
    dependencies = ["IO"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def end(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Tracing.end")
        return mayberes

    async def getCategories(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Tracing.getCategories")
        res = await mayberes
        return res

    async def recordClockSyncMarker(self, syncId: str) -> Optional[dict]:
        """
        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict["syncId"] = syncId
        mayberes = await self.chrome.send("Tracing.recordClockSyncMarker", msg_dict)
        return mayberes

    async def requestMemoryDump(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Tracing.requestMemoryDump")
        res = await mayberes
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
        mayberes = await self.chrome.send("Tracing.start", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
