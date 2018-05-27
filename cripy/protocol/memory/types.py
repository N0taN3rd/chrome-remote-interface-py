from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

PressureLevel = str


class SamplingProfileNode(ChromeTypeBase):

    def __init__(self, size: float, total: float, stack: List["str"]) -> None:
        super().__init__()
        self.size: float = size
        self.total: float = total
        self.stack: List[str] = stack


class SamplingProfile(ChromeTypeBase):

    def __init__(self, samples: List["SamplingProfileNode"]) -> None:
        super().__init__()
        self.samples: List[SamplingProfileNode] = samples
