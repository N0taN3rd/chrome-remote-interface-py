from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType

VirtualTimePolicy = TypeVar("VirtualTimePolicy", str, str)
"""advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches."""


class ScreenOrientation(ProtocolType):
    """Screen orientation."""

    def __init__(self, type: str, angle: int) -> None:
        """
        :param type: Orientation type.
        :type type: str
        :param angle: Orientation angle.
        :type angle: int
        """
        super().__init__()
        self.type: str = type
        self.angle: int = angle


OBJECT_LIST = {"ScreenOrientation": ScreenOrientation}
