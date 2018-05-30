from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM


class StickyPositionConstraint(ProtocolType):
    """
    Sticky position constraints.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StickyPositionConstraint', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StickyPositionConstraint.safe_create(it))
            return list_of_self
        else:
            return init


class ScrollRect(ProtocolType):
    """
    Rectangle where scrolling happens on the main thread.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScrollRect', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScrollRect.safe_create(it))
            return list_of_self
        else:
            return init


class PictureTile(ProtocolType):
    """
    Serialized fragment of layer picture along with its offset within the layer.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PictureTile', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PictureTile.safe_create(it))
            return list_of_self
        else:
            return init


class Layer(ProtocolType):
    """
    Information about a compositing layer.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Layer', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Layer.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "StickyPositionConstraint": StickyPositionConstraint,
    "ScrollRect": ScrollRect,
    "PictureTile": PictureTile,
    "Layer": Layer,
}
