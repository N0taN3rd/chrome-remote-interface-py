from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# 
WindowID = int

# The state of the browser window.
WindowState = str


class Bounds(ChromeTypeBase):
    """Browser window bounds information"""

    def __init__(self, left: Optional[int] = None, top: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, windowState: Optional['WindowState'] = None) -> None:
        """
        :param left: The offset from the left edge of the screen to the window in pixels.
        :type int:
        :param top: The offset from the top edge of the screen to the window in pixels.
        :type int:
        :param width: The window width in pixels.
        :type int:
        :param height: The window height in pixels.
        :type int:
        :param windowState: The window state. Default to normal.
        :type WindowState:
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
        :type int:
        :param high: Maximum value (exclusive).
        :type int:
        :param count: Number of samples.
        :type int:
        """
        super().__init__()
        self.low: int = low
        self.high: int = high
        self.count: int = count


class Histogram(ChromeTypeBase):
    """Chrome histogram."""

    def __init__(self, name: str, sum: int, count: int, buckets: List['Bucket']) -> None:
        """
        :param name: Name.
        :type str:
        :param sum: Sum of sample values.
        :type int:
        :param count: Total number of samples.
        :type int:
        :param buckets: Buckets.
        :type array:
        """
        super().__init__()
        self.name: str = name
        self.sum: int = sum
        self.count: int = count
        self.buckets: List[Bucket] = buckets


