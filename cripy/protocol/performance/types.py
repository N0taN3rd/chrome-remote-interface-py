from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase


class Metric(ChromeTypeBase):
    """Run-time execution metric."""
    def __init__(self, name: str, value: float) -> None:
        """
        :param name: Metric name.
        :type name: str
        :param value: Metric value.
        :type value: float
        """
        super().__init__()
        self.name: str = name
        self.value: float = value

