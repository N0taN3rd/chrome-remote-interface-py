from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

VirtualTimePolicy = str


class ScreenOrientation(ChromeTypeBase):
    """Screen orientation."""

    def __init__(self, type: str, angle: int) -> None:
        """
        :param type: Orientation type.
        :param angle: Orientation angle.
        """
        super().__init__()
        self.type: str = type
        self.angle: int = angle
