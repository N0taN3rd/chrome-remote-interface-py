from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# Memory pressure level.
PressureLevel = str


class SamplingProfileNode(ChromeTypeBase):
    """Heap profile sample."""

    def __init__(self, size: float, total: float, stack: List['str']) -> None:
        """
        :param size: Size of the sampled allocation.
        :type float:
        :param total: Total bytes attributed to this sample.
        :type float:
        :param stack: Execution stack at the point of allocation.
        :type array:
        """
        super().__init__()
        self.size: float = size
        self.total: float = total
        self.stack: List[str] = stack


class SamplingProfile(ChromeTypeBase):
    """Array of heap profile samples."""

    def __init__(self, samples: List['SamplingProfileNode']) -> None:
        """
        :param samples: The samples
        :type array:
        """
        super().__init__()
        self.samples: List[SamplingProfileNode] = samples


