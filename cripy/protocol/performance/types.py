from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class Metric(ChromeTypeBase):
    """Run-time execution metric."""

    def __init__(self, name: str, value: float) -> None:
        """
        :param name: Metric name.
        :param value: Metric value.
        """
        super().__init__()
        self.name: str = name
        self.value: float = value
