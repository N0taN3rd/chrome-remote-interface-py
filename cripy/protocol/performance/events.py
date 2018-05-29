from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class MetricsEvent(BaseEvent):
    """Current values of the metrics."""

    event: str = "Performance.metrics"

    def __init__(self, metrics: List[Union[Metric, dict]], title: str) -> None:
        """
        :param metrics: Current values of the metrics.
        :type metrics: array
        :param title: Timestamp title.
        :type title: str
        """
        super().__init__()
        self.metrics: List[Metric] = metrics
        self.title: str = title


EVENT_TO_CLASS = {"Performance.metrics": MetricsEvent}
