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
    def safe_create(init: Optional[dict]) -> Optional[Union['MetricsEvent', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MetricsEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Performance.metrics": MetricsEvent,
}

