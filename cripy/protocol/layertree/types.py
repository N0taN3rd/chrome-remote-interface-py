from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

# Unique Layer identifier.
LayerId = str

# Unique snapshot identifier.
SnapshotId = str

# Array of timings, one per paint step.
PaintProfile = list


class ScrollRect(ChromeTypeBase):
    """Rectangle where scrolling happens on the main thread."""

    def __init__(self, rect: 'DOM.Rect', type: str) -> None:
        """
        :param rect: Rectangle itself.
        :type DOM.Rect:
        :param type: Reason for rectangle to force scrolling on the main thread
        :type str:
        """
        super().__init__()
        self.rect: DOM.Rect = rect
        self.type: str = type


class StickyPositionConstraint(ChromeTypeBase):
    """Sticky position constraints."""

    def __init__(self, stickyBoxRect: 'DOM.Rect', containingBlockRect: 'DOM.Rect', nearestLayerShiftingStickyBox: Optional['LayerId'] = None, nearestLayerShiftingContainingBlock: Optional['LayerId'] = None) -> None:
        """
        :param stickyBoxRect: Layout rectangle of the sticky element before being shifted
        :type DOM.Rect:
        :param containingBlockRect: Layout rectangle of the containing block of the sticky element
        :type DOM.Rect:
        :param nearestLayerShiftingStickyBox: The nearest sticky layer that shifts the sticky box
        :type LayerId:
        :param nearestLayerShiftingContainingBlock: The nearest sticky layer that shifts the containing block
        :type LayerId:
        """
        super().__init__()
        self.stickyBoxRect: DOM.Rect = stickyBoxRect
        self.containingBlockRect: DOM.Rect = containingBlockRect
        self.nearestLayerShiftingStickyBox: Optional[LayerId] = nearestLayerShiftingStickyBox
        self.nearestLayerShiftingContainingBlock: Optional[LayerId] = nearestLayerShiftingContainingBlock


class PictureTile(ChromeTypeBase):
    """Serialized fragment of layer picture along with its offset within the layer."""

    def __init__(self, x: float, y: float, picture: str) -> None:
        """
        :param x: Offset from owning layer left boundary
        :type float:
        :param y: Offset from owning layer top boundary
        :type float:
        :param picture: Base64-encoded snapshot data.
        :type str:
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.picture: str = picture


class Layer(ChromeTypeBase):
    """Information about a compositing layer."""

    def __init__(self, layerId: 'LayerId', offsetX: float, offsetY: float, width: float, height: float, paintCount: int, drawsContent: bool, parentLayerId: Optional['LayerId'] = None, backendNodeId: Optional['DOM.BackendNodeId'] = None, transform: Optional[List['float']] = None, anchorX: Optional[float] = None, anchorY: Optional[float] = None, anchorZ: Optional[float] = None, invisible: Optional[bool] = None, scrollRects: Optional[List['ScrollRect']] = None, stickyPositionConstraint: Optional['StickyPositionConstraint'] = None) -> None:
        """
        :param layerId: The unique id for this layer.
        :type LayerId:
        :param parentLayerId: The id of parent (not present for root).
        :type LayerId:
        :param backendNodeId: The backend id for the node associated with this layer.
        :type DOM.BackendNodeId:
        :param offsetX: Offset from parent layer, X coordinate.
        :type float:
        :param offsetY: Offset from parent layer, Y coordinate.
        :type float:
        :param width: Layer width.
        :type float:
        :param height: Layer height.
        :type float:
        :param transform: Transformation matrix for layer, default is identity matrix
        :type array:
        :param anchorX: Transform anchor point X, absent if no transform specified
        :type float:
        :param anchorY: Transform anchor point Y, absent if no transform specified
        :type float:
        :param anchorZ: Transform anchor point Z, absent if no transform specified
        :type float:
        :param paintCount: Indicates how many time this layer has painted.
        :type int:
        :param drawsContent: Indicates whether this layer hosts any content, rather than being used for
        transform/scrolling purposes only.
        :type bool:
        :param invisible: Set if layer is not visible.
        :type bool:
        :param scrollRects: Rectangles scrolling on main thread only.
        :type array:
        :param stickyPositionConstraint: Sticky position constraint information
        :type StickyPositionConstraint:
        """
        super().__init__()
        self.layerId: LayerId = layerId
        self.parentLayerId: Optional[LayerId] = parentLayerId
        self.backendNodeId: Optional[DOM.BackendNodeId] = backendNodeId
        self.offsetX: float = offsetX
        self.offsetY: float = offsetY
        self.width: float = width
        self.height: float = height
        self.transform: Optional[List[float]] = transform
        self.anchorX: Optional[float] = anchorX
        self.anchorY: Optional[float] = anchorY
        self.anchorZ: Optional[float] = anchorZ
        self.paintCount: int = paintCount
        self.drawsContent: bool = drawsContent
        self.invisible: Optional[bool] = invisible
        self.scrollRects: Optional[List[ScrollRect]] = scrollRects
        self.stickyPositionConstraint: Optional[StickyPositionConstraint] = stickyPositionConstraint


