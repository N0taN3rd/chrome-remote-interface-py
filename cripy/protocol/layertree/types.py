from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

LayerId = str

SnapshotId = str

PaintProfile = list


class ScrollRect(ChromeTypeBase):

    def __init__(self, rect: "DOM.Rect", type: str) -> None:
        super().__init__()
        self.rect: DOM.Rect = rect
        self.type: str = type


class StickyPositionConstraint(ChromeTypeBase):

    def __init__(
        self,
        stickyBoxRect: "DOM.Rect",
        containingBlockRect: "DOM.Rect",
        nearestLayerShiftingStickyBox: Optional["LayerId"] = None,
        nearestLayerShiftingContainingBlock: Optional["LayerId"] = None,
    ) -> None:
        super().__init__()
        self.stickyBoxRect: DOM.Rect = stickyBoxRect
        self.containingBlockRect: DOM.Rect = containingBlockRect
        self.nearestLayerShiftingStickyBox: Optional[
            LayerId
        ] = nearestLayerShiftingStickyBox
        self.nearestLayerShiftingContainingBlock: Optional[
            LayerId
        ] = nearestLayerShiftingContainingBlock


class PictureTile(ChromeTypeBase):

    def __init__(self, x: float, y: float, picture: str) -> None:
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.picture: str = picture


class Layer(ChromeTypeBase):

    def __init__(
        self,
        layerId: "LayerId",
        offsetX: float,
        offsetY: float,
        width: float,
        height: float,
        paintCount: int,
        drawsContent: bool,
        parentLayerId: Optional["LayerId"] = None,
        backendNodeId: Optional["DOM.BackendNodeId"] = None,
        transform: Optional[List["float"]] = None,
        anchorX: Optional[float] = None,
        anchorY: Optional[float] = None,
        anchorZ: Optional[float] = None,
        invisible: Optional[bool] = None,
        scrollRects: Optional[List["ScrollRect"]] = None,
        stickyPositionConstraint: Optional["StickyPositionConstraint"] = None,
    ) -> None:
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
        self.stickyPositionConstraint: Optional[
            StickyPositionConstraint
        ] = stickyPositionConstraint
