from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

GestureSourceType = str

TimeSinceEpoch = float


class TouchPoint(ChromeTypeBase):

    def __init__(
        self,
        x: float,
        y: float,
        radiusX: Optional[float] = None,
        radiusY: Optional[float] = None,
        rotationAngle: Optional[float] = None,
        force: Optional[float] = None,
        id: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.radiusX: Optional[float] = radiusX
        self.radiusY: Optional[float] = radiusY
        self.rotationAngle: Optional[float] = rotationAngle
        self.force: Optional[float] = force
        self.id: Optional[float] = id
