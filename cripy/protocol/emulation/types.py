from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches.
VirtualTimePolicy = str


class ScreenOrientation(ChromeTypeBase):
    """Screen orientation."""

    def __init__(self, type: str, angle: int) -> None:
        """
        :param type: Orientation type.
        :type str:
        :param angle: Orientation angle.
        :type int:
        """
        super().__init__()
        self.type: str = type
        self.angle: int = angle


