from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class ScreenshotParams(ProtocolType):
    """
    Encoding options for a screenshot.
    """

    def __init__(self, format: Optional[str] = None, quality: Optional[int] = None) -> None:
        """
        :param format: Image compression format (defaults to png).
        :type format: Optional[str]
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: Optional[int]
        """
        super().__init__()
        self.format = format
        self.quality = quality

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreenshotParams']:
        if init is not None:
            return ScreenshotParams(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreenshotParams']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenshotParams(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ScreenshotParams": ScreenshotParams,
}
