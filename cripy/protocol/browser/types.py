from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class Histogram(ProtocolType):
    """
    Chrome histogram.
    """

    def __init__(self, name: str, sum: int, count: int, buckets: List[Union['Bucket', dict]]) -> None:
        """
        :param name: Name.
        :type name: str
        :param sum: Sum of sample values.
        :type sum: int
        :param count: Total number of samples.
        :type count: int
        :param buckets: Buckets.
        :type buckets: List[dict]
        """
        super().__init__()
        self.name = name
        self.sum = sum
        self.count = count
        self.buckets = Bucket.safe_create_from_list(buckets)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Histogram', dict]]:
        if init is not None:
            try:
                ourselves = Histogram(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Histogram', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Histogram.safe_create(it))
            return list_of_self
        else:
            return init


class Bucket(ProtocolType):
    """
    Chrome histogram bucket.
    """

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
        self.low = low
        self.high = high
        self.count = count

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Bucket', dict]]:
        if init is not None:
            try:
                ourselves = Bucket(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Bucket', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Bucket.safe_create(it))
            return list_of_self
        else:
            return init


class Bounds(ProtocolType):
    """
    Browser window bounds information
    """

    def __init__(self, left: Optional[int] = None, top: Optional[int] = None, width: Optional[int] = None, height: Optional[int] = None, windowState: Optional[str] = None) -> None:
        """
        :param left: The offset from the left edge of the screen to the window in pixels.
        :type left: Optional[int]
        :param top: The offset from the top edge of the screen to the window in pixels.
        :type top: Optional[int]
        :param width: The window width in pixels.
        :type width: Optional[int]
        :param height: The window height in pixels.
        :type height: Optional[int]
        :param windowState: The window state. Default to normal.
        :type windowState: Optional[str]
        """
        super().__init__()
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.windowState = windowState

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Bounds', dict]]:
        if init is not None:
            try:
                ourselves = Bounds(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Bounds', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Bounds.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Histogram": Histogram,
    "Bucket": Bucket,
    "Bounds": Bounds,
}
