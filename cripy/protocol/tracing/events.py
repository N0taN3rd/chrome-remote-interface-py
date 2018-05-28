from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class BufferUsageEvent(BaseEvent):

    event: str = "Tracing.bufferUsage"

    def __init__(self) -> None:
        """
        :param float percentFull: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type percentFull: float
        :param float eventCount: An approximate number of events in the trace log.
        :type eventCount: float
        :param float value: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type value: float
        """
        super().__init__()


class DataCollectedEvent(BaseEvent):
    """Contains an bucket of collected trace events.
	When tracing is stopped collected events will be send as a sequence of dataCollected events followed by tracingComplete event."""

    event: str = "Tracing.dataCollected"

    def __init__(self) -> None:
        """
        :param array value: The value
        :type value: array
        """
        super().__init__()


class TracingCompleteEvent(BaseEvent):
    """Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events."""

    event: str = "Tracing.tracingComplete"

    def __init__(self) -> None:
        """
        :param IO.StreamHandle stream: A handle of the stream that holds resulting trace data.
        :type stream: IO.StreamHandle
        :param StreamCompression streamCompression: Compression format of returned stream.
        :type streamCompression: StreamCompression
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Tracing.bufferUsage": BufferUsageEvent,
   "Tracing.dataCollected": DataCollectedEvent,
   "Tracing.tracingComplete": TracingCompleteEvent,
}

