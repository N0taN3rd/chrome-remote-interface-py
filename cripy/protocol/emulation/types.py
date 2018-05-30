from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

VirtualTimePolicy = TypeVar("VirtualTimePolicy", str, str) # advance: If the scheduler runs out of immediate work, the virtual time base may fast forward to allow the next delayed task (if any) to run; pause: The virtual time base may not advance; pauseIfNetworkFetchesPending: The virtual time base may not advance if there are any pending resource fetches.


class ScreenOrientation(ProtocolType):
    """
    Screen orientation.
    """

    def __init__(self, type: str, angle: int) -> None:
        """
        :param type: Orientation type.
        :type type: str
        :param angle: Orientation angle.
        :type angle: int
        """
        super().__init__()
        self.type = type
        self.angle = angle

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreenOrientation']:
        if init is not None:
            return ScreenOrientation(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreenOrientation']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenOrientation(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ScreenOrientation": ScreenOrientation,
}
