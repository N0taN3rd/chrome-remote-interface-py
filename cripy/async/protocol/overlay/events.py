from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.page import types as Page
from cripy.async.protocol.dom import types as DOM
from cripy.async.protocol.overlay.types import *

__all__ = [
    "InspectNodeRequestedEvent",
    "NodeHighlightRequestedEvent",
    "ScreenshotRequestedEvent",
    "OVERLAY_EVENTS_TO_CLASS",
    "OVERLAY_EVENTS_NS"
]

class InspectNodeRequestedEvent(object):
    """
    Fired when the node should be inspected.
	This happens after call to `setInspectMode` or when user manually inspects an element.
    """

    event = "Overlay.inspectNodeRequested"

    __slots__ = ["backendNodeId"]

    def __init__(self, backendNodeId: int) -> None:
        """
        Create a new instance of InspectNodeRequestedEvent

        :param backendNodeId: Id of the node to inspect.
        :type backendNodeId: int
        """
        super().__init__()
        self.backendNodeId = backendNodeId

    def __repr__(self) -> str:
        repr_args = []
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        return "InspectNodeRequestedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['InspectNodeRequestedEvent', dict]]:
        """
        Safely create InspectNodeRequestedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InspectNodeRequestedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InspectNodeRequestedEvent if creation did not fail
        :rtype: Optional[Union[dict, InspectNodeRequestedEvent]]
        """
        if init is not None:
            try:
                ourselves = InspectNodeRequestedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['InspectNodeRequestedEvent', dict]]]:
        """
        Safely create a new list InspectNodeRequestedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InspectNodeRequestedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InspectNodeRequestedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, InspectNodeRequestedEvent]]]
        """
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

    __slots__ = ["nodeId"]

    def __init__(self, nodeId: int) -> None:
        """
        Create a new instance of NodeHighlightRequestedEvent

        :param nodeId: The nodeId
        :type nodeId: int
        """
        super().__init__()
        self.nodeId = nodeId

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        return "NodeHighlightRequestedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['NodeHighlightRequestedEvent', dict]]:
        """
        Safely create NodeHighlightRequestedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NodeHighlightRequestedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NodeHighlightRequestedEvent if creation did not fail
        :rtype: Optional[Union[dict, NodeHighlightRequestedEvent]]
        """
        if init is not None:
            try:
                ourselves = NodeHighlightRequestedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['NodeHighlightRequestedEvent', dict]]]:
        """
        Safely create a new list NodeHighlightRequestedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NodeHighlightRequestedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NodeHighlightRequestedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, NodeHighlightRequestedEvent]]]
        """
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

    __slots__ = ["viewport"]

    def __init__(self, viewport: Union[Page.Viewport, dict]) -> None:
        """
        Create a new instance of ScreenshotRequestedEvent

        :param viewport: Viewport to capture, in CSS.
        :type viewport: dict
        """
        super().__init__()
        self.viewport = Page.Viewport.safe_create(viewport)

    def __repr__(self) -> str:
        repr_args = []
        if self.viewport is not None:
            repr_args.append("viewport={!r}".format(self.viewport))
        return "ScreenshotRequestedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScreenshotRequestedEvent', dict]]:
        """
        Safely create ScreenshotRequestedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreenshotRequestedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreenshotRequestedEvent if creation did not fail
        :rtype: Optional[Union[dict, ScreenshotRequestedEvent]]
        """
        if init is not None:
            try:
                ourselves = ScreenshotRequestedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScreenshotRequestedEvent', dict]]]:
        """
        Safely create a new list ScreenshotRequestedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreenshotRequestedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreenshotRequestedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreenshotRequestedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenshotRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


OVERLAY_EVENTS_TO_CLASS = {
   "Overlay.inspectNodeRequested": InspectNodeRequestedEvent,
   "Overlay.nodeHighlightRequested": NodeHighlightRequestedEvent,
   "Overlay.screenshotRequested": ScreenshotRequestedEvent,
}

OverlayNS = namedtuple("OverlayNS", ["InspectNodeRequested", "NodeHighlightRequested", "ScreenshotRequested"])

OVERLAY_EVENTS_NS = OverlayNS(
  InspectNodeRequested="Overlay.inspectNodeRequested",
  NodeHighlightRequested="Overlay.nodeHighlightRequested",
  ScreenshotRequested="Overlay.screenshotRequested",
)
