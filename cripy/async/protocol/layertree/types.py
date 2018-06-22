from typing import Any, List, Optional, Union
from cripy.async.protocol.dom import types as DOM

__all__ = [
    "StickyPositionConstraint",
    "ScrollRect",
    "PictureTile",
    "Layer",
    "LAYERTREE_TYPES_TO_OBJECT"
]


class StickyPositionConstraint(object):
    """
    Sticky position constraints.
    """

    __slots__ = ["stickyBoxRect", "containingBlockRect", "nearestLayerShiftingStickyBox", "nearestLayerShiftingContainingBlock"]

    def __init__(self, stickyBoxRect: Union['DOM.Rect', dict], containingBlockRect: Union['DOM.Rect', dict], nearestLayerShiftingStickyBox: Optional[str] = None, nearestLayerShiftingContainingBlock: Optional[str] = None) -> None:
        """
        :param stickyBoxRect: Layout rectangle of the sticky element before being shifted
        :type stickyBoxRect: dict
        :param containingBlockRect: Layout rectangle of the containing block of the sticky element
        :type containingBlockRect: dict
        :param nearestLayerShiftingStickyBox: The nearest sticky layer that shifts the sticky box
        :type nearestLayerShiftingStickyBox: Optional[str]
        :param nearestLayerShiftingContainingBlock: The nearest sticky layer that shifts the containing block
        :type nearestLayerShiftingContainingBlock: Optional[str]
        """
        super().__init__()
        self.stickyBoxRect = DOM.Rect.safe_create(stickyBoxRect)
        self.containingBlockRect = DOM.Rect.safe_create(containingBlockRect)
        self.nearestLayerShiftingStickyBox = nearestLayerShiftingStickyBox
        self.nearestLayerShiftingContainingBlock = nearestLayerShiftingContainingBlock

    def __repr__(self) -> str:
        repr_args = []
        if self.stickyBoxRect is not None:
            repr_args.append("stickyBoxRect={!r}".format(self.stickyBoxRect))
        if self.containingBlockRect is not None:
            repr_args.append("containingBlockRect={!r}".format(self.containingBlockRect))
        if self.nearestLayerShiftingStickyBox is not None:
            repr_args.append("nearestLayerShiftingStickyBox={!r}".format(self.nearestLayerShiftingStickyBox))
        if self.nearestLayerShiftingContainingBlock is not None:
            repr_args.append("nearestLayerShiftingContainingBlock={!r}".format(self.nearestLayerShiftingContainingBlock))
        return "StickyPositionConstraint(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StickyPositionConstraint', dict]]:
        """
        Safely create StickyPositionConstraint from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of StickyPositionConstraint
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of StickyPositionConstraint if creation did not fail
        :rtype: Optional[Union[dict, StickyPositionConstraint]]
        """
        if init is not None:
            try:
                ourselves = StickyPositionConstraint(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['StickyPositionConstraint', dict]]]:
        """
        Safely create a new list StickyPositionConstraints from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list StickyPositionConstraint instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of StickyPositionConstraint instances if creation did not fail
        :rtype: Optional[List[Union[dict, StickyPositionConstraint]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StickyPositionConstraint.safe_create(it))
            return list_of_self
        else:
            return init


class ScrollRect(object):
    """
    Rectangle where scrolling happens on the main thread.
    """

    __slots__ = ["rect", "type"]

    def __init__(self, rect: Union['DOM.Rect', dict], type: str) -> None:
        """
        :param rect: Rectangle itself.
        :type rect: dict
        :param type: Reason for rectangle to force scrolling on the main thread
        :type type: str
        """
        super().__init__()
        self.rect = DOM.Rect.safe_create(rect)
        self.type = type

    def __repr__(self) -> str:
        repr_args = []
        if self.rect is not None:
            repr_args.append("rect={!r}".format(self.rect))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        return "ScrollRect(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScrollRect', dict]]:
        """
        Safely create ScrollRect from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScrollRect
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScrollRect if creation did not fail
        :rtype: Optional[Union[dict, ScrollRect]]
        """
        if init is not None:
            try:
                ourselves = ScrollRect(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScrollRect', dict]]]:
        """
        Safely create a new list ScrollRects from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScrollRect instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScrollRect instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScrollRect]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScrollRect.safe_create(it))
            return list_of_self
        else:
            return init


class PictureTile(object):
    """
    Serialized fragment of layer picture along with its offset within the layer.
    """

    __slots__ = ["x", "y", "picture"]

    def __init__(self, x: float, y: float, picture: str) -> None:
        """
        :param x: Offset from owning layer left boundary
        :type x: float
        :param y: Offset from owning layer top boundary
        :type y: float
        :param picture: Base64-encoded snapshot data.
        :type picture: str
        """
        super().__init__()
        self.x = x
        self.y = y
        self.picture = picture

    def __repr__(self) -> str:
        repr_args = []
        if self.x is not None:
            repr_args.append("x={!r}".format(self.x))
        if self.y is not None:
            repr_args.append("y={!r}".format(self.y))
        if self.picture is not None:
            repr_args.append("picture={!r}".format(self.picture))
        return "PictureTile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PictureTile', dict]]:
        """
        Safely create PictureTile from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of PictureTile
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of PictureTile if creation did not fail
        :rtype: Optional[Union[dict, PictureTile]]
        """
        if init is not None:
            try:
                ourselves = PictureTile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['PictureTile', dict]]]:
        """
        Safely create a new list PictureTiles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list PictureTile instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of PictureTile instances if creation did not fail
        :rtype: Optional[List[Union[dict, PictureTile]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PictureTile.safe_create(it))
            return list_of_self
        else:
            return init


class Layer(object):
    """
    Information about a compositing layer.
    """

    __slots__ = ["layerId", "parentLayerId", "backendNodeId", "offsetX", "offsetY", "width", "height", "transform", "anchorX", "anchorY", "anchorZ", "paintCount", "drawsContent", "invisible", "scrollRects", "stickyPositionConstraint"]

    def __init__(self, layerId: str, offsetX: float, offsetY: float, width: float, height: float, paintCount: int, drawsContent: bool, parentLayerId: Optional[str] = None, backendNodeId: Optional[int] = None, transform: Optional[List[float]] = None, anchorX: Optional[float] = None, anchorY: Optional[float] = None, anchorZ: Optional[float] = None, invisible: Optional[bool] = None, scrollRects: Optional[List[Union['ScrollRect', dict]]] = None, stickyPositionConstraint: Optional[Union['StickyPositionConstraint', dict]] = None) -> None:
        """
        :param layerId: The unique id for this layer.
        :type layerId: str
        :param parentLayerId: The id of parent (not present for root).
        :type parentLayerId: Optional[str]
        :param backendNodeId: The backend id for the node associated with this layer.
        :type backendNodeId: Optional[int]
        :param offsetX: Offset from parent layer, X coordinate.
        :type offsetX: float
        :param offsetY: Offset from parent layer, Y coordinate.
        :type offsetY: float
        :param width: Layer width.
        :type width: float
        :param height: Layer height.
        :type height: float
        :param transform: Transformation matrix for layer, default is identity matrix
        :type transform: Optional[List[float]]
        :param anchorX: Transform anchor point X, absent if no transform specified
        :type anchorX: Optional[float]
        :param anchorY: Transform anchor point Y, absent if no transform specified
        :type anchorY: Optional[float]
        :param anchorZ: Transform anchor point Z, absent if no transform specified
        :type anchorZ: Optional[float]
        :param paintCount: Indicates how many time this layer has painted.
        :type paintCount: int
        :param drawsContent: Indicates whether this layer hosts any content, rather than being used for transform/scrolling purposes only.
        :type drawsContent: bool
        :param invisible: Set if layer is not visible.
        :type invisible: Optional[bool]
        :param scrollRects: Rectangles scrolling on main thread only.
        :type scrollRects: Optional[List[dict]]
        :param stickyPositionConstraint: Sticky position constraint information
        :type stickyPositionConstraint: Optional[dict]
        """
        super().__init__()
        self.layerId = layerId
        self.parentLayerId = parentLayerId
        self.backendNodeId = backendNodeId
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.width = width
        self.height = height
        self.transform = transform
        self.anchorX = anchorX
        self.anchorY = anchorY
        self.anchorZ = anchorZ
        self.paintCount = paintCount
        self.drawsContent = drawsContent
        self.invisible = invisible
        self.scrollRects = ScrollRect.safe_create_from_list(scrollRects)
        self.stickyPositionConstraint = StickyPositionConstraint.safe_create(stickyPositionConstraint)

    def __repr__(self) -> str:
        repr_args = []
        if self.layerId is not None:
            repr_args.append("layerId={!r}".format(self.layerId))
        if self.parentLayerId is not None:
            repr_args.append("parentLayerId={!r}".format(self.parentLayerId))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        if self.offsetX is not None:
            repr_args.append("offsetX={!r}".format(self.offsetX))
        if self.offsetY is not None:
            repr_args.append("offsetY={!r}".format(self.offsetY))
        if self.width is not None:
            repr_args.append("width={!r}".format(self.width))
        if self.height is not None:
            repr_args.append("height={!r}".format(self.height))
        if self.transform is not None:
            repr_args.append("transform={!r}".format(self.transform))
        if self.anchorX is not None:
            repr_args.append("anchorX={!r}".format(self.anchorX))
        if self.anchorY is not None:
            repr_args.append("anchorY={!r}".format(self.anchorY))
        if self.anchorZ is not None:
            repr_args.append("anchorZ={!r}".format(self.anchorZ))
        if self.paintCount is not None:
            repr_args.append("paintCount={!r}".format(self.paintCount))
        if self.drawsContent is not None:
            repr_args.append("drawsContent={!r}".format(self.drawsContent))
        if self.invisible is not None:
            repr_args.append("invisible={!r}".format(self.invisible))
        if self.scrollRects is not None:
            repr_args.append("scrollRects={!r}".format(self.scrollRects))
        if self.stickyPositionConstraint is not None:
            repr_args.append("stickyPositionConstraint={!r}".format(self.stickyPositionConstraint))
        return "Layer(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Layer', dict]]:
        """
        Safely create Layer from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Layer
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Layer if creation did not fail
        :rtype: Optional[Union[dict, Layer]]
        """
        if init is not None:
            try:
                ourselves = Layer(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Layer', dict]]]:
        """
        Safely create a new list Layers from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Layer instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Layer instances if creation did not fail
        :rtype: Optional[List[Union[dict, Layer]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Layer.safe_create(it))
            return list_of_self
        else:
            return init


LAYERTREE_TYPES_TO_OBJECT = {
    "StickyPositionConstraint": StickyPositionConstraint,
    "ScrollRect": ScrollRect,
    "PictureTile": PictureTile,
    "Layer": Layer,
}
