from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class ScreenshotParams(ChromeTypeBase):

    def __init__(
        self, format: Optional[str] = None, quality: Optional[int] = None
    ) -> None:
        super().__init__()
        self.format: Optional[str] = format
        self.quality: Optional[int] = quality
