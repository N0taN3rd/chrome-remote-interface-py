from typing import Any, List, Optional, Union, TypeVar


class TouchPoint(object):

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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.x is not None:
            repr_args.append("x={!r}".format(self.x))
        if self.y is not None:
            repr_args.append("y={!r}".format(self.y))
        if self.radiusX is not None:
            repr_args.append("radiusX={!r}".format(self.radiusX))
        if self.radiusY is not None:
            repr_args.append("radiusY={!r}".format(self.radiusY))
        if self.rotationAngle is not None:
            repr_args.append("rotationAngle={!r}".format(self.rotationAngle))
        if self.force is not None:
            repr_args.append("force={!r}".format(self.force))
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        return "TouchPoint(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["TouchPoint", dict]]:
        if init is not None:
            try:
                ourselves = TouchPoint(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["TouchPoint", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TouchPoint.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"TouchPoint": TouchPoint}
