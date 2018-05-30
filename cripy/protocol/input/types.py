from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

TimeSinceEpoch = TypeVar("TimeSinceEpoch", float, float) # UTC time in seconds, counted from January 1, 1970.

GestureSourceType = TypeVar("GestureSourceType", str, str) # 


class TouchPoint(ProtocolType):
    def __init__(self, x: float, y: float, radiusX: Optional[float] = None, radiusY: Optional[float] = None, rotationAngle: Optional[float] = None, force: Optional[float] = None, id: Optional[float] = None) -> None:
        """
        :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
        :type x: float
        :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
        :type y: float
        :param radiusX: X radius of the touch area (default: 1.0).
        :type radiusX: Optional[float]
        :param radiusY: Y radius of the touch area (default: 1.0).
        :type radiusY: Optional[float]
        :param rotationAngle: Rotation angle (default: 0.0).
        :type rotationAngle: Optional[float]
        :param force: Force (default: 1.0).
        :type force: Optional[float]
        :param id: Identifier used to track touch sources between events, must be unique within an event.
        :type id: Optional[float]
        """
        super().__init__()
        self.x = x
        self.y = y
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.rotationAngle = rotationAngle
        self.force = force
        self.id = id

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['TouchPoint']:
        if init is not None:
            return TouchPoint(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TouchPoint']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TouchPoint(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "TouchPoint": TouchPoint,
}
