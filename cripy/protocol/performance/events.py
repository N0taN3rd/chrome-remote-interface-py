from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.performance.types import *
except ImportError:
    pass


class MetricsEvent(BaseEvent):
    """
    Current values of the metrics.
    """

    event = "Performance.metrics"

    def __init__(self, metrics: List[Union[Metric, dict]], title: str) -> None:
        """
        :param metrics: Current values of the metrics.
        :type metrics: List[dict]
        :param title: Timestamp title.
        :type title: str
        """
        super().__init__()
        self.metrics = Metric.safe_create_from_list(metrics)
        self.title = title

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['MetricsEvent']:
        if init is not None:
            return MetricsEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['MetricsEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MetricsEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Performance.metrics": MetricsEvent,
}

