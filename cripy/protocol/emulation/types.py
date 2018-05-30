from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


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
    def safe_create(init: Optional[dict]) -> Optional[Union['ScreenOrientation', dict]]:
        if init is not None:
             try:
                ourselves = ScreenOrientation(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScreenOrientation', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenOrientation.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ScreenOrientation": ScreenOrientation,
}
