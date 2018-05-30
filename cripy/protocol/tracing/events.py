from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.io import types as IO
from cripy.protocol.tracing.types import (
    StreamCompression,
)


class BufferUsageEvent(BaseEvent):

    event = "Tracing.bufferUsage"

    def __init__(self, percentFull: Optional[float] = None, eventCount: Optional[float] = None, value: Optional[float] = None) -> None:
        """
        :param percentFull: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type percentFull: Optional[float]
        :param eventCount: An approximate number of events in the trace log.
        :type eventCount: Optional[float]
        :param value: A number in range [0..1] that indicates the used size of event buffer as a fraction of its total size.
        :type value: Optional[float]
        """
        super().__init__()
        self.percentFull = percentFull
        self.eventCount = eventCount
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['BufferUsageEvent']:
        if init is not None:
            return BufferUsageEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['BufferUsageEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BufferUsageEvent(**it))
            return list_of_self
        else:
            return init


class DataCollectedEvent(BaseEvent):
    """
    Contains an bucket of collected trace events.
	When tracing is stopped collected events will be send as a sequence of dataCollected events followed by tracingComplete event.
    """

    event = "Tracing.dataCollected"

    def __init__(self, value: List[dict]) -> None:
        """
        :param value: The value
        :type value: List[dict]
        """
        super().__init__()
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DataCollectedEvent']:
        if init is not None:
            return DataCollectedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DataCollectedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataCollectedEvent(**it))
            return list_of_self
        else:
            return init


class TracingCompleteEvent(BaseEvent):
    """
    Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events.
    """

    event = "Tracing.tracingComplete"

    def __init__(self, stream: Optional[IO.StreamHandle] = None, streamCompression: Optional[StreamCompression] = None) -> None:
        """
        :param stream: A handle of the stream that holds resulting trace data.
        :type stream: Optional[str]
        :param streamCompression: Compression format of returned stream.
        :type streamCompression: Optional[str]
        """
        super().__init__()
        self.stream = stream
        self.streamCompression = streamCompression

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TracingCompleteEvent']:
        if init is not None:
            return TracingCompleteEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TracingCompleteEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TracingCompleteEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Tracing.bufferUsage": BufferUsageEvent,
   "Tracing.dataCollected": DataCollectedEvent,
   "Tracing.tracingComplete": TracingCompleteEvent,
}

