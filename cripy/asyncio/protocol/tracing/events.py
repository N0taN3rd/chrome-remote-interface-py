from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.tracing.types import *

__all__ = [
    "BufferUsageEvent",
    "DataCollectedEvent",
    "TracingCompleteEvent",
    "TRACING_EVENTS_TO_CLASS",
    "TRACING_EVENTS_NS"
]

class BufferUsageEvent(object):

    event = "Tracing.bufferUsage"

    __slots__ = ["percentFull", "eventCount", "value"]

    def __init__(self, percentFull: Optional[float] = None, eventCount: Optional[float] = None, value: Optional[float] = None) -> None:
        """
        Create a new instance of BufferUsageEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.percentFull is not None:
            repr_args.append("percentFull={!r}".format(self.percentFull))
        if self.eventCount is not None:
            repr_args.append("eventCount={!r}".format(self.eventCount))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "BufferUsageEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['BufferUsageEvent', dict]]:
        """
        Safely create BufferUsageEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of BufferUsageEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of BufferUsageEvent if creation did not fail
        :rtype: Optional[Union[dict, BufferUsageEvent]]
        """
        if init is not None:
            try:
                ourselves = BufferUsageEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['BufferUsageEvent', dict]]]:
        """
        Safely create a new list BufferUsageEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list BufferUsageEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of BufferUsageEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, BufferUsageEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BufferUsageEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DataCollectedEvent(object):
    """
    Contains an bucket of collected trace events.
	When tracing is stopped collected events will be send as a sequence of dataCollected events followed by tracingComplete event.
    """

    event = "Tracing.dataCollected"

    __slots__ = ["value"]

    def __init__(self, value: List[dict]) -> None:
        """
        Create a new instance of DataCollectedEvent

        :param value: The value
        :type value: List[dict]
        """
        super().__init__()
        self.value = value

    def __repr__(self) -> str:
        repr_args = []
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "DataCollectedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DataCollectedEvent', dict]]:
        """
        Safely create DataCollectedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DataCollectedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DataCollectedEvent if creation did not fail
        :rtype: Optional[Union[dict, DataCollectedEvent]]
        """
        if init is not None:
            try:
                ourselves = DataCollectedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DataCollectedEvent', dict]]]:
        """
        Safely create a new list DataCollectedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DataCollectedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DataCollectedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DataCollectedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataCollectedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class TracingCompleteEvent(object):
    """
    Signals that tracing is stopped and there is no trace buffers pending flush, all data were delivered via dataCollected events.
    """

    event = "Tracing.tracingComplete"

    __slots__ = ["stream", "streamCompression"]

    def __init__(self, stream: Optional[str] = None, streamCompression: Optional[str] = None) -> None:
        """
        Create a new instance of TracingCompleteEvent

        :param stream: A handle of the stream that holds resulting trace data.
        :type stream: Optional[str]
        :param streamCompression: Compression format of returned stream.
        :type streamCompression: Optional[str]
        """
        super().__init__()
        self.stream = stream
        self.streamCompression = streamCompression

    def __repr__(self) -> str:
        repr_args = []
        if self.stream is not None:
            repr_args.append("stream={!r}".format(self.stream))
        if self.streamCompression is not None:
            repr_args.append("streamCompression={!r}".format(self.streamCompression))
        return "TracingCompleteEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TracingCompleteEvent', dict]]:
        """
        Safely create TracingCompleteEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TracingCompleteEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TracingCompleteEvent if creation did not fail
        :rtype: Optional[Union[dict, TracingCompleteEvent]]
        """
        if init is not None:
            try:
                ourselves = TracingCompleteEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TracingCompleteEvent', dict]]]:
        """
        Safely create a new list TracingCompleteEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TracingCompleteEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TracingCompleteEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, TracingCompleteEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TracingCompleteEvent.safe_create(it))
            return list_of_self
        else:
            return init


TRACING_EVENTS_TO_CLASS = {
   "Tracing.bufferUsage": BufferUsageEvent,
   "Tracing.dataCollected": DataCollectedEvent,
   "Tracing.tracingComplete": TracingCompleteEvent,
}

TracingNS = namedtuple("TracingNS", ["BufferUsage", "DataCollected", "TracingComplete"])

TRACING_EVENTS_NS = TracingNS(
  BufferUsage="Tracing.bufferUsage",
  DataCollected="Tracing.dataCollected",
  TracingComplete="Tracing.tracingComplete",
)
