from types import SimpleNamespace
from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.dom import types as DOM

try:
    from cripy.gevent.protocol.overlay.types import *
except ImportError:
    pass

__all__ = [
    "InspectNodeRequestedEvent",
    "NodeHighlightRequestedEvent",
    "ScreenshotRequestedEvent",
]


class InspectNodeRequestedEvent(object):
    """
    Fired when the node should be inspected.
	This happens after call to `setInspectMode` or when user manually inspects an element.
    """

    event = "Overlay.inspectNodeRequested"

    def __init__(self, backendNodeId):
        """
        :param backendNodeId: Id of the node to inspect.
        :type backendNodeId: int
        """
        super().__init__()
        self.backendNodeId = backendNodeId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        return "InspectNodeRequestedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = InspectNodeRequestedEvent(**init)
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
                list_of_self.append(InspectNodeRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class NodeHighlightRequestedEvent(object):
    """
    Fired when the node should be highlighted.
	This happens after call to `setInspectMode`.
    """

    event = "Overlay.nodeHighlightRequested"

    def __init__(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        super().__init__()
        self.nodeId = nodeId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        return "NodeHighlightRequestedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = NodeHighlightRequestedEvent(**init)
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
                list_of_self.append(NodeHighlightRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScreenshotRequestedEvent(object):
    """
    Fired when user asks to capture screenshot of some area on the page.
    """

    event = "Overlay.screenshotRequested"

    def __init__(self, viewport):
        """
        :param viewport: Viewport to capture, in CSS.
        :type viewport: dict
        """
        super().__init__()
        self.viewport = Page.Viewport.safe_create(viewport)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.viewport is not None:
            repr_args.append("viewport={!r}".format(self.viewport))
        return "ScreenshotRequestedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScreenshotRequestedEvent(**init)
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
                list_of_self.append(ScreenshotRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Overlay.inspectNodeRequested": InspectNodeRequestedEvent,
    "Overlay.nodeHighlightRequested": NodeHighlightRequestedEvent,
    "Overlay.screenshotRequested": ScreenshotRequestedEvent,
}

EVENT_NS = SimpleNamespace(
    InspectNodeRequested="Overlay.inspectNodeRequested",
    NodeHighlightRequested="Overlay.nodeHighlightRequested",
    ScreenshotRequested="Overlay.screenshotRequested",
)
