from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.tracing import events as Events
from cripy.asyncio.protocol.tracing import types as Types

__all__ = ["Tracing"]


class Tracing(object):
    dependencies = ['IO']

    events = Events.TRACING_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Tracing object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def end(self) -> Optional[dict]:
        """
        Stop trace events collection.
        """
        mayberes = await self.chrome.send('Tracing.end')
        return mayberes

    async def getCategories(self) -> Optional[dict]:
        """
        Gets supported tracing categories.
        """
        mayberes = await self.chrome.send('Tracing.getCategories')
        res = await mayberes
        return res

    async def recordClockSyncMarker(self, syncId: str) -> Optional[dict]:
        """
        Record a clock sync marker in the trace.

        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict['syncId'] = syncId
        mayberes = await self.chrome.send('Tracing.recordClockSyncMarker', msg_dict)
        return mayberes

    async def requestMemoryDump(self) -> Optional[dict]:
        """
        Request a global memory dump.
        """
        mayberes = await self.chrome.send('Tracing.requestMemoryDump')
        res = await mayberes
        return res

    async def start(self, categories: Optional[str] = None, options: Optional[str] = None, bufferUsageReportingInterval: Optional[float] = None, transferMode: Optional[str] = None, streamCompression: Optional[str] = None, traceConfig: Optional[dict] = None) -> Optional[dict]:
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
            msg_dict['categories'] = categories
        if options is not None:
            msg_dict['options'] = options
        if bufferUsageReportingInterval is not None:
            msg_dict['bufferUsageReportingInterval'] = bufferUsageReportingInterval
        if transferMode is not None:
            msg_dict['transferMode'] = transferMode
        if streamCompression is not None:
            msg_dict['streamCompression'] = streamCompression
        if traceConfig is not None:
            msg_dict['traceConfig'] = traceConfig
        mayberes = await self.chrome.send('Tracing.start', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.TRACING_EVENTS_TO_CLASS

