__all__ = ["Tracing"]


class Tracing(object):
    dependencies = ['IO']

    def __init__(self, chrome):
        """
        Construct a new Tracing object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def end(self):
        """
        Stop trace events collection.
        """
        wres = self.chrome.send('Tracing.end')
        return wres.get()

    def getCategories(self):
        """
        Gets supported tracing categories.
        """
        wres = self.chrome.send('Tracing.getCategories')
        return wres.get()

    def recordClockSyncMarker(self, syncId):
        """
        Record a clock sync marker in the trace.

        :param syncId: The ID of this clock sync marker
        :type syncId: str
        """
        msg_dict = dict()
        if syncId is not None:
            msg_dict['syncId'] = syncId
        wres = self.chrome.send('Tracing.recordClockSyncMarker', msg_dict)
        return wres.get()

    def requestMemoryDump(self):
        """
        Request a global memory dump.
        """
        wres = self.chrome.send('Tracing.requestMemoryDump')
        return wres.get()

    def start(self, categories=None, options=None, bufferUsageReportingInterval=None, transferMode=None, streamCompression=None, traceConfig=None):
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
        wres = self.chrome.send('Tracing.start', msg_dict)
        return wres.get()

    def bufferUsage(self, fn, once=False):
        self.chrome.on("Tracing.bufferUsage", fn, once=once)

    def dataCollected(self, fn, once=False):
        """
        Contains an bucket of collected trace events. When tracing is stopped collected events will be
        send as a sequence of dataCollected events followed by tracingComplete event.
        """
        self.chrome.on("Tracing.dataCollected", fn, once=once)

    def tracingComplete(self, fn, once=False):
        """
        Signals that tracing is stopped and there is no trace buffers pending flush, all data were
        delivered via dataCollected events.
        """
        self.chrome.on("Tracing.tracingComplete", fn, once=once)


