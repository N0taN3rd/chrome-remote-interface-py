from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

WindowID = int

WindowState = str


class Bounds(ChromeTypeBase):
    """Browser window bounds information"""

    def __init__(
        self,
        left: Optional[int] = None,
        top: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        windowState: Optional["WindowState"] = None,
    ) -> None:
        """
        :param left: The offset from the left edge of the screen to the window in pixels.
        :param top: The offset from the top edge of the screen to the window in pixels.
        :param width: The window width in pixels.
        :param height: The window height in pixels.
        :param windowState: The window state. Default to normal.
        """
        super().__init__()
        self.left: Optional[int] = left
        self.top: Optional[int] = top
        self.width: Optional[int] = width
        self.height: Optional[int] = height
        self.windowState: Optional[WindowState] = windowState


class Bucket(ChromeTypeBase):
    """Chrome histogram bucket."""

    def __init__(self, low: int, high: int, count: int) -> None:
        """
        :param low: Minimum value (inclusive).
        :param high: Maximum value (exclusive).
        :param count: Number of samples.
        """
        super().__init__()
        self.low: int = low
        self.high: int = high
        self.count: int = count


class Histogram(ChromeTypeBase):
    """Chrome histogram."""

    def __init__(
        self, name: str, sum: int, count: int, buckets: List["Bucket"]
    ) -> None:
        """
        :param name: Name.
        :param sum: Sum of sample values.
        :param count: Total number of samples.
        :param buckets: Buckets.
        """
        super().__init__()
        self.name: str = name
        self.sum: int = sum
        self.count: int = count
        self.buckets: List[Bucket] = buckets
