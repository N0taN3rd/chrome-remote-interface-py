from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.page import types as Page
from cripy.protocol.dom import types as DOM


class InspectNodeRequestedEvent(BaseEvent):
    """Fired when the node should be inspected.
	This happens after call to `setInspectMode` or when user manually inspects an element."""

    event: str = "Overlay.inspectNodeRequested"

    def __init__(self, backendNodeId: DOM.BackendNodeId) -> None:
        """
        :param backendNodeId: Id of the node to inspect.
        :type backendNodeId: DOM.BackendNodeId
        """
        super().__init__()
        self.backendNodeId: DOM.BackendNodeId = backendNodeId


class NodeHighlightRequestedEvent(BaseEvent):
    """Fired when the node should be highlighted.
	This happens after call to `setInspectMode`."""

    event: str = "Overlay.nodeHighlightRequested"

    def __init__(self, nodeId: DOM.NodeId) -> None:
        """
        :param nodeId: The nodeId
        :type nodeId: DOM.NodeId
        """
        super().__init__()
        self.nodeId: DOM.NodeId = nodeId


class ScreenshotRequestedEvent(BaseEvent):
    """Fired when user asks to capture screenshot of some area on the page."""

    event: str = "Overlay.screenshotRequested"

    def __init__(self, viewport: Page.Viewport) -> None:
        """
        :param viewport: Viewport to capture, in CSS.
        :type viewport: Page.Viewport
        """
        super().__init__()
        self.viewport: Page.Viewport = viewport


EVENT_TO_CLASS = {
   "Overlay.inspectNodeRequested": InspectNodeRequestedEvent,
   "Overlay.nodeHighlightRequested": NodeHighlightRequestedEvent,
   "Overlay.screenshotRequested": ScreenshotRequestedEvent,
}

