from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

PressureLevel = TypeVar("PressureLevel", str, str)
"""Memory pressure level."""


class SamplingProfileNode(ChromeTypeBase):
    """Heap profile sample."""
    def __init__(self, size: float, total: float, stack: List['str']) -> None:
        """
        :param size: Size of the sampled allocation.
        :type size: float
        :param total: Total bytes attributed to this sample.
        :type total: float
        :param stack: Execution stack at the point of allocation.
        :type stack: array
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
        :type samples: array
        """
        super().__init__()
        self.samples: List[SamplingProfileNode] = samples


