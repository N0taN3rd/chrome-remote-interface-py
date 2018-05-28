from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# 
GestureSourceType = str

# UTC time in seconds, counted from January 1, 1970.
TimeSinceEpoch = float


class TouchPoint(ChromeTypeBase):
    pass
    def __init__(self, x: float, y: float, radiusX: Optional[float] = None, radiusY: Optional[float] = None, rotationAngle: Optional[float] = None, force: Optional[float] = None, id: Optional[float] = None) -> None:
        """
        :param x: X coordinate of the event relative to the main frame's viewport in CSS pixels.
        :type x: float
        :param y: Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
        :type y: float
        :param radiusX: X radius of the touch area (default: 1.0).
        :type radiusX: float
        :param radiusY: Y radius of the touch area (default: 1.0).
        :type radiusY: float
        :param rotationAngle: Rotation angle (default: 0.0).
        :type rotationAngle: float
        :param force: Force (default: 1.0).
        :type force: float
        :param id: Identifier used to track touch sources between events, must be unique within an event.
        :type id: float
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.radiusX: Optional[float] = radiusX
        self.radiusY: Optional[float] = radiusY
        self.rotationAngle: Optional[float] = rotationAngle
        self.force: Optional[float] = force
        self.id: Optional[float] = id


