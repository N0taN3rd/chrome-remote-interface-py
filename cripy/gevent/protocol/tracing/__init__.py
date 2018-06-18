from cripy.gevent.protocol.tracing import events as Events
from cripy.gevent.protocol.tracing import types as Types

__all__ = ["Tracing"] + Events.__all__ + Types.__all__


class Tracing(object):
    dependencies = ["IO"]

    def __init__(self, chrome):
        self.chrome = chrome

    def end(self):
        wres = self.chrome.send("Tracing.end")
        return wres.get()

    def getCategories(self):
        wres = self.chrome.send("Tracing.getCategories")
        res = wres.get()
        return res

    def recordClockSyncMarker(self, syncId):
        """
        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict["syncId"] = syncId
        wres = self.chrome.send("Tracing.recordClockSyncMarker", msg_dict)
        return wres.get()

    def requestMemoryDump(self):
        wres = self.chrome.send("Tracing.requestMemoryDump")
        res = wres.get()
        return res

    def start(
        self,
        categories=None,
        options=None,
        bufferUsageReportingInterval=None,
        transferMode=None,
        streamCompression=None,
        traceConfig=None,
    ):
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
        wres = self.chrome.send("Tracing.start", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
