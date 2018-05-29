from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.io import types as IO
from cripy.protocol.tracing.types import StreamCompression


class BufferUsageEvent(BaseEvent):

    event: str = "Tracing.bufferUsage"

    def __init__(
        self,
        percentFull: Optional[float] = None,
        eventCount: Optional[float] = None,
        value: Optional[float] = None,
    ) -> None:
        """
        :param percentFull: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type percentFull: float
        :param eventCount: An approximate number of events in the trace log.
        :type eventCount: float
        :param value: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type value: float
        """
        super().__init__()
        self.percentFull: Optional[float] = percentFull
        self.eventCount: Optional[float] = eventCount
        self.value: Optional[float] = value


class DataCollectedEvent(BaseEvent):
    """Contains an bucket of collected trace events.
	When tracing is stopped collected events will be send as a sequence of dataCollected events followed by tracingComplete event."""

    event: str = "Tracing.dataCollected"

    def __init__(self, value: List[dict]) -> None:
        """
        :param value: The value
        :type value: array
        """
        super().__init__()
        self.value: List[dict] = value


class TracingCompleteEvent(BaseEvent):
    """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""

    event: str = "Tracing.tracingComplete"

    def __init__(
        self,
        stream: Optional[IO.StreamHandle] = None,
        streamCompression: Optional[StreamCompression] = None,
    ) -> None:
        """
        :param stream: A handle of the stream that holds resulting trace data.
        :type stream: IO.StreamHandle
        :param streamCompression: Compression format of returned stream.
        :type streamCompression: StreamCompression
        """
        super().__init__()
        self.stream: Optional[IO.StreamHandle] = stream
        self.streamCompression: Optional[StreamCompression] = streamCompression


EVENT_TO_CLASS = {
    "Tracing.bufferUsage": BufferUsageEvent,
    "Tracing.dataCollected": DataCollectedEvent,
    "Tracing.tracingComplete": TracingCompleteEvent,
}
