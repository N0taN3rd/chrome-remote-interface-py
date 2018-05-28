from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class MetricsEvent(BaseEvent):
    """Current values of the metrics."""

    event: str = "Performance.metrics"

    def __init__(self) -> None:
        """
        :param array metrics: Current values of the metrics.
        :type metrics: array
        :param str title: Timestamp title.
        :type title: str
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Performance.metrics": MetricsEvent,
}

