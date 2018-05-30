from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page


class InspectNodeRequestedEvent(BaseEvent):
    """
    Fired when the node should be inspected.
	This happens after call to `setInspectMode` or when user manually inspects an element.
    """

    event = "Overlay.inspectNodeRequested"

    def __init__(self, backendNodeId: DOM.BackendNodeId) -> None:
        """
        :param backendNodeId: Id of the node to inspect.
        :type backendNodeId: int
        """
        super().__init__()
        self.backendNodeId = backendNodeId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InspectNodeRequestedEvent']:
        if init is not None:
            return InspectNodeRequestedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InspectNodeRequestedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InspectNodeRequestedEvent(**it))
            return list_of_self
        else:
            return init


class NodeHighlightRequestedEvent(BaseEvent):
    """
    Fired when the node should be highlighted.
	This happens after call to `setInspectMode`.
    """

    event = "Overlay.nodeHighlightRequested"

    def __init__(self, nodeId: DOM.NodeId) -> None:
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        super().__init__()
        self.nodeId = nodeId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['NodeHighlightRequestedEvent']:
        if init is not None:
            return NodeHighlightRequestedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['NodeHighlightRequestedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NodeHighlightRequestedEvent(**it))
            return list_of_self
        else:
            return init


class ScreenshotRequestedEvent(BaseEvent):
    """
    Fired when user asks to capture screenshot of some area on the page.
    """

    event = "Overlay.screenshotRequested"

    def __init__(self, viewport: Union[Page.Viewport, dict]) -> None:
        """
        :param viewport: Viewport to capture, in CSS.
        :type viewport: dict
        """
        super().__init__()
        self.viewport = Page.Viewport.safe_create(viewport)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreenshotRequestedEvent']:
        if init is not None:
            return ScreenshotRequestedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreenshotRequestedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenshotRequestedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Overlay.inspectNodeRequested": InspectNodeRequestedEvent,
   "Overlay.nodeHighlightRequested": NodeHighlightRequestedEvent,
   "Overlay.screenshotRequested": ScreenshotRequestedEvent,
}

