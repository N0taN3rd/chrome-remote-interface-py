from cripy.sync.protocol.dom import types as DOM

__all__ = [
    "StickyPositionConstraint",
    "ScrollRect",
    "PictureTile",
    "Layer",
]


class StickyPositionConstraint(object):
    """
    Sticky position constraints.
    """

    def __init__(self, stickyBoxRect, containingBlockRect, nearestLayerShiftingStickyBox, nearestLayerShiftingContainingBlock):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
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
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StickyPositionConstraint(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, rect, type):
        """
        :param rect: Rectangle itself.
        :type rect: dict
        :param type: Reason for rectangle to force scrolling on the main thread
        :type type: str
        """
        super().__init__()
        self.rect = DOM.Rect.safe_create(rect)
        self.type = type

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.rect is not None:
            repr_args.append("rect={!r}".format(self.rect))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        return "ScrollRect(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScrollRect(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, x, y, picture):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.x is not None:
            repr_args.append("x={!r}".format(self.x))
        if self.y is not None:
            repr_args.append("y={!r}".format(self.y))
        if self.picture is not None:
            repr_args.append("picture={!r}".format(self.picture))
        return "PictureTile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PictureTile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, layerId, offsetX, offsetY, width, height, paintCount, drawsContent, parentLayerId, backendNodeId, transform, anchorX, anchorY, anchorZ, invisible, scrollRects, stickyPositionConstraint):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
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
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Layer(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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
