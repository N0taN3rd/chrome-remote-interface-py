from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class InspectNodeRequestedEvent(BaseEvent):
    """Fired when the node should be inspected.
	This happens after call to `setInspectMode` or when user manually inspects an element."""

    event: str = "Overlay.inspectNodeRequested"

    def __init__(self) -> None:
        """
        :param backendNodeId: Id of the node to inspect.
        :type DOM.BackendNodeId:
        """
        super().__init__()


class NodeHighlightRequestedEvent(BaseEvent):
    """Fired when the node should be highlighted.
	This happens after call to `setInspectMode`."""

    event: str = "Overlay.nodeHighlightRequested"

    def __init__(self) -> None:
        """
        :param nodeId: The nodeId
        :type DOM.NodeId:
        """
        super().__init__()


class ScreenshotRequestedEvent(BaseEvent):
    """Fired when user asks to capture screenshot of some area on the page."""

    event: str = "Overlay.screenshotRequested"

    def __init__(self) -> None:
        """
        :param viewport: Viewport to capture, in CSS.
        :type Page.Viewport:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Overlay.inspectNodeRequested": InspectNodeRequestedEvent,
   "Overlay.nodeHighlightRequested": NodeHighlightRequestedEvent,
   "Overlay.screenshotRequested": ScreenshotRequestedEvent,
}

