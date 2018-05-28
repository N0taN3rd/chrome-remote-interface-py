from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

WindowState = TypeVar("WindowState", str, str)
"""The state of the browser window."""

WindowID = TypeVar("WindowID", int, int)
""""""


class Histogram(ChromeTypeBase):
    """Chrome histogram."""
    def __init__(self, name: str, sum: int, count: int, buckets: List['Bucket']) -> None:
        """
        :param name: Name.
        :type name: str
        :param sum: Sum of sample values.
        :type sum: int
        :param count: Total number of samples.
        :type count: int
        :param buckets: Buckets.
        :type buckets: array
        """
        super().__init__()
        self.name: str = name
        self.sum: int = sum
        self.count: int = count
        self.buckets: List[Bucket] = buckets


class Bucket(ChromeTypeBase):
    """Chrome histogram bucket."""
    def __init__(self, low: int, high: int, count: int) -> None:
        """
        :param low: Minimum value (inclusive).
        :type low: int
        :param high: Maximum value (exclusive).
        :type high: int
        :param count: Number of samples.
        :type count: int
        """
        super().__init__()
        self.low: int = low
        self.high: int = high
        self.count: int = count


class Bounds(ChromeTypeBase):
    """Browser window bounds information"""
    def __init__(self, left: Optional[int] = None, top: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, windowState: Optional['WindowState'] = None) -> None:
        """
        :param left: The offset from the left edge of the screen to the window in pixels.
        :type left: int
        :param top: The offset from the top edge of the screen to the window in pixels.
        :type top: int
        :param width: The window width in pixels.
        :type width: int
        :param height: The window height in pixels.
        :type height: int
        :param windowState: The window state. Default to normal.
        :type windowState: WindowState
        """
        super().__init__()
        self.left: Optional[int] = left
        self.top: Optional[int] = top
        self.width: Optional[int] = width
        self.height: Optional[int] = height
        self.windowState: Optional[WindowState] = windowState


