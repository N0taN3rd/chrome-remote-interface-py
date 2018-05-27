from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

VirtualTimePolicy = str


class ScreenOrientation(ChromeTypeBase):

    def __init__(self, type: str, angle: int) -> None:
        super().__init__()
        self.type: str = type
        self.angle: int = angle
