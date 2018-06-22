
__all__ = [
    "TouchPoint",
    "INPUT_TYPE_TO_OBJECT"
]


class TouchPoint(object):
    __slots__ = ["x", "y", "radiusX", "radiusY", "rotationAngle", "force", "id"]

    def __init__(self, x, y, radiusX=None, radiusY=None, rotationAngle=None, force=None, id=None):
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
        super(TouchPoint, self).__init__()
        self.x = x
        self.y = y
        self.radiusX = radiusX
        self.radiusY = radiusY
        self.rotationAngle = rotationAngle
        self.force = force
        self.id = id

    def __repr__(self):
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
        return "TouchPoint(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TouchPoint from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TouchPoint
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TouchPoint if creation did not fail
        :rtype: Optional[Union[dict, TouchPoint]]
        """
        if init is not None:
            try:
                ourselves = TouchPoint(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list TouchPoints from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TouchPoint instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TouchPoint instances if creation did not fail
        :rtype: Optional[List[Union[dict, TouchPoint]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TouchPoint.safe_create(it))
            return list_of_self
        else:
            return init


INPUT_TYPE_TO_OBJECT = {
    "TouchPoint": TouchPoint,
}
