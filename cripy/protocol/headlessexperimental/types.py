from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class ScreenshotParams(object):
    """
    Encoding options for a screenshot.
    """

    def __init__(
        self, format: Optional[str] = None, quality: Optional[int] = None
    ) -> None:
        """
        :param format: Image compression format (defaults to png).
        :type format: Optional[str]
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: Optional[int]
        """
        super().__init__()
        self.format = format
        self.quality = quality

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.format is not None:
            repr_args.append("format={!r}".format(self.format))
        if self.quality is not None:
            repr_args.append("quality={!r}".format(self.quality))
        return "ScreenshotParams(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["ScreenshotParams", dict]]:
        if init is not None:
            try:
                ourselves = ScreenshotParams(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ScreenshotParams", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenshotParams.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"ScreenshotParams": ScreenshotParams}
