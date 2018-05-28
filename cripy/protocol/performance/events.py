from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class MetricsEvent(BaseEvent):
    """Current values of the metrics."""

    event: str = "Performance.metrics"

    def __init__(self) -> None:
        """
        :param metrics: Current values of the metrics.
        :type array:
        :param title: Timestamp title.
        :type str:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Performance.metrics": MetricsEvent,
}

