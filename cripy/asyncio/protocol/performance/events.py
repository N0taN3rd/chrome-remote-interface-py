from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.performance.types import *

__all__ = [
    "MetricsEvent",
    "PERFORMANCE_EVENTS_TO_CLASS",
    "PERFORMANCE_EVENTS_NS"
]


class MetricsEvent(object):
    """
    Current values of the metrics.
    """


    __slots__ = ["metrics", "title"]

    def __init__(self, metrics: List[Union[Metric, dict]], title: str) -> None:
        """
        Create a new instance of MetricsEvent

        :param metrics: Current values of the metrics.
        :type metrics: List[dict]
        :param title: Timestamp title.
        :type title: str
        """
        super().__init__()
        self.metrics = Metric.safe_create_from_list(metrics)
        self.title = title

    def __repr__(self) -> str:
        repr_args = []
        if self.metrics is not None:
            repr_args.append("metrics={!r}".format(self.metrics))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        return "MetricsEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['MetricsEvent', dict]]:
        """
        Safely create MetricsEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of MetricsEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of MetricsEvent if creation did not fail
        :rtype: Optional[Union[dict, MetricsEvent]]
        """
        if init is not None:
            try:
                ourselves = MetricsEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['MetricsEvent', dict]]]:
        """
        Safely create a new list MetricsEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list MetricsEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of MetricsEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, MetricsEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MetricsEvent.safe_create(it))
            return list_of_self
        else:
            return init


PERFORMANCE_EVENTS_TO_CLASS = {
   "Performance.metrics": MetricsEvent,
}

PerformanceNS = namedtuple("PerformanceNS", ["Metrics"])

PERFORMANCE_EVENTS_NS = PerformanceNS(
  Metrics="Performance.metrics",
)
