from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

WindowID = int

WindowState = str


class Bounds(ChromeTypeBase):

    def __init__(
        self,
        left: Optional[int] = None,
        top: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        windowState: Optional["WindowState"] = None,
    ) -> None:
        super().__init__()
        self.left: Optional[int] = left
        self.top: Optional[int] = top
        self.width: Optional[int] = width
        self.height: Optional[int] = height
        self.windowState: Optional[WindowState] = windowState


class Bucket(ChromeTypeBase):

    def __init__(self, low: int, high: int, count: int) -> None:
        super().__init__()
        self.low: int = low
        self.high: int = high
        self.count: int = count


class Histogram(ChromeTypeBase):

    def __init__(
        self, name: str, sum: int, count: int, buckets: List["Bucket"]
    ) -> None:
        super().__init__()
        self.name: str = name
        self.sum: int = sum
        self.count: int = count
        self.buckets: List[Bucket] = buckets
