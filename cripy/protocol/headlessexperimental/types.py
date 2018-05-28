from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase


class ScreenshotParams(ChromeTypeBase):
    """Encoding options for a screenshot."""
    def __init__(self, format: Optional[str] = None, quality: Optional[int] = None) -> None:
        """
        :param format: Image compression format (defaults to png).
        :type format: str
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: int
        """
        super().__init__()
        self.format: Optional[str] = format
        self.quality: Optional[int] = quality


