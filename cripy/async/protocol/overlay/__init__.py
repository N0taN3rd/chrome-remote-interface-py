from typing import Any, List, Optional, Union
from cripy.async.protocol.page import types as Page
from cripy.async.protocol.dom import types as DOM
from cripy.async.protocol.runtime import types as Runtime
from cripy.async.protocol.overlay import events as Events
from cripy.async.protocol.overlay import types as Types


class Overlay(object):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """

    dependencies = ["DOM", "Page", "Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Overlay.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Overlay.enable")
        return mayberes

    async def getHighlightObjectForTest(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        mayberes = await self.chrome.send("Overlay.getHighlightObjectForTest", msg_dict)
        res = await mayberes
        return res

    async def hideHighlight(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Overlay.hideHighlight")
        return mayberes

    async def highlightFrame(
        self,
        frameId: str,
        contentColor: Optional[dict] = None,
        contentOutlineColor: Optional[dict] = None,
    ) -> Optional[dict]:
        """
        :param frameId: Identifier of the frame to highlight.
        :type frameId: str
        :param contentColor: The content box highlight fill color (default: transparent).
        :type contentColor: Optional[dict]
        :param contentOutlineColor: The content box highlight outline color (default: transparent).
        :type contentOutlineColor: Optional[dict]
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        if contentColor is not None:
            msg_dict["contentColor"] = contentColor
        if contentOutlineColor is not None:
            msg_dict["contentOutlineColor"] = contentOutlineColor
        mayberes = await self.chrome.send("Overlay.highlightFrame", msg_dict)
        return mayberes

    async def highlightNode(
        self,
        highlightConfig: dict,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
        """
        :param highlightConfig: A descriptor for the highlight appearance.
        :type highlightConfig: dict
        :param nodeId: Identifier of the node to highlight.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node to highlight.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node to be highlighted.
        :type objectId: Optional[str]
        """
        msg_dict = dict()
        if highlightConfig is not None:
            msg_dict["highlightConfig"] = highlightConfig
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        mayberes = await self.chrome.send("Overlay.highlightNode", msg_dict)
        return mayberes

    async def highlightQuad(
        self,
        quad: list,
        color: Optional[dict] = None,
        outlineColor: Optional[dict] = None,
    ) -> Optional[dict]:
        """
        :param quad: Quad to highlight
        :type quad: Any
        :param color: The highlight fill color (default: transparent).
        :type color: Optional[dict]
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: Optional[dict]
        """
        msg_dict = dict()
        if quad is not None:
            msg_dict["quad"] = quad
        if color is not None:
            msg_dict["color"] = color
        if outlineColor is not None:
            msg_dict["outlineColor"] = outlineColor
        mayberes = await self.chrome.send("Overlay.highlightQuad", msg_dict)
        return mayberes

    async def highlightRect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Optional[dict] = None,
        outlineColor: Optional[dict] = None,
    ) -> Optional[dict]:
        """
        :param x: X coordinate
        :type x: int
        :param y: Y coordinate
        :type y: int
        :param width: Rectangle width
        :type width: int
        :param height: Rectangle height
        :type height: int
        :param color: The highlight fill color (default: transparent).
        :type color: Optional[dict]
        :param outlineColor: The highlight outline color (default: transparent).
        :type outlineColor: Optional[dict]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict["x"] = x
        if y is not None:
            msg_dict["y"] = y
        if width is not None:
            msg_dict["width"] = width
        if height is not None:
            msg_dict["height"] = height
        if color is not None:
            msg_dict["color"] = color
        if outlineColor is not None:
            msg_dict["outlineColor"] = outlineColor
        mayberes = await self.chrome.send("Overlay.highlightRect", msg_dict)
        return mayberes

    async def setInspectMode(
        self, mode: str, highlightConfig: Optional[dict] = None
    ) -> Optional[dict]:
        """
        :param mode: Set an inspection mode.
        :type mode: str
        :param highlightConfig: A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled == false`.
        :type highlightConfig: Optional[dict]
        """
        msg_dict = dict()
        if mode is not None:
            msg_dict["mode"] = mode
        if highlightConfig is not None:
            msg_dict["highlightConfig"] = highlightConfig
        mayberes = await self.chrome.send("Overlay.setInspectMode", msg_dict)
        return mayberes

    async def setPausedInDebuggerMessage(
        self, message: Optional[str] = None
    ) -> Optional[dict]:
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict["message"] = message
        mayberes = await self.chrome.send(
            "Overlay.setPausedInDebuggerMessage", msg_dict
        )
        return mayberes

    async def setShowDebugBorders(self, show: bool) -> Optional[dict]:
        """
        :param show: True for showing debug borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        mayberes = await self.chrome.send("Overlay.setShowDebugBorders", msg_dict)
        return mayberes

    async def setShowFPSCounter(self, show: bool) -> Optional[dict]:
        """
        :param show: True for showing the FPS counter
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        mayberes = await self.chrome.send("Overlay.setShowFPSCounter", msg_dict)
        return mayberes

    async def setShowPaintRects(self, result: bool) -> Optional[dict]:
        """
        :param result: True for showing paint rectangles
        :type result: bool
        """
        msg_dict = dict()
        if result is not None:
            msg_dict["result"] = result
        mayberes = await self.chrome.send("Overlay.setShowPaintRects", msg_dict)
        return mayberes

    async def setShowScrollBottleneckRects(self, show: bool) -> Optional[dict]:
        """
        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        mayberes = await self.chrome.send(
            "Overlay.setShowScrollBottleneckRects", msg_dict
        )
        return mayberes

    async def setShowViewportSizeOnResize(self, show: bool) -> Optional[dict]:
        """
        :param show: Whether to paint size or not.
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        mayberes = await self.chrome.send(
            "Overlay.setShowViewportSizeOnResize", msg_dict
        )
        return mayberes

    async def setSuspended(self, suspended: bool) -> Optional[dict]:
        """
        :param suspended: Whether overlay should be suspended and not consume any resources until resumed.
        :type suspended: bool
        """
        msg_dict = dict()
        if suspended is not None:
            msg_dict["suspended"] = suspended
        mayberes = await self.chrome.send("Overlay.setSuspended", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
