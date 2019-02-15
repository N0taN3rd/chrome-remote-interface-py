"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Overlay"]


@attr.dataclass(slots=True, cmp=False)
class Overlay(object):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Dict]:
        """
        Disables domain notifications.
        """
        return self.client.send("Overlay.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables domain notifications.
        """
        return self.client.send("Overlay.enable")

    def getHighlightObjectForTest(self, nodeId: int) -> Awaitable[Dict]:
        """
        For testing.

        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("Overlay.getHighlightObjectForTest", msg_dict)

    def hideHighlight(self) -> Awaitable[Dict]:
        """
        Hides any highlight.
        """
        return self.client.send("Overlay.hideHighlight")

    def highlightFrame(
        self,
        frameId: str,
        contentColor: Optional[dict] = None,
        contentOutlineColor: Optional[dict] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights owner element of the frame with given id.

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
        return self.client.send("Overlay.highlightFrame", msg_dict)

    def highlightNode(
        self,
        highlightConfig: dict,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        selector: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
objectId must be specified.

        :param highlightConfig: A descriptor for the highlight appearance.
        :type highlightConfig: dict
        :param nodeId: Identifier of the node to highlight.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node to highlight.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node to be highlighted.
        :type objectId: Optional[str]
        :param selector: Selectors to highlight relevant nodes.
        :type selector: Optional[str]
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
        if selector is not None:
            msg_dict["selector"] = selector
        return self.client.send("Overlay.highlightNode", msg_dict)

    def highlightQuad(
        self,
        quad: list,
        color: Optional[dict] = None,
        outlineColor: Optional[dict] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

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
        return self.client.send("Overlay.highlightQuad", msg_dict)

    def highlightRect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Optional[dict] = None,
        outlineColor: Optional[dict] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

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
        return self.client.send("Overlay.highlightRect", msg_dict)

    def setInspectMode(
        self, mode: str, highlightConfig: Optional[dict] = None
    ) -> Awaitable[Dict]:
        """
        Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
Backend then generates 'inspectNodeRequested' event upon element selection.

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
        return self.client.send("Overlay.setInspectMode", msg_dict)

    def setShowAdHighlights(self, show: bool) -> Awaitable[Dict]:
        """
        Highlights owner element of all frames detected to be ads.

        :param show: True for showing ad highlights
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowAdHighlights", msg_dict)

    def setPausedInDebuggerMessage(
        self, message: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict["message"] = message
        return self.client.send("Overlay.setPausedInDebuggerMessage", msg_dict)

    def setShowDebugBorders(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows debug borders on layers

        :param show: True for showing debug borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowDebugBorders", msg_dict)

    def setShowFPSCounter(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows the FPS counter

        :param show: True for showing the FPS counter
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowFPSCounter", msg_dict)

    def setShowPaintRects(self, result: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows paint rectangles

        :param result: True for showing paint rectangles
        :type result: bool
        """
        msg_dict = dict()
        if result is not None:
            msg_dict["result"] = result
        return self.client.send("Overlay.setShowPaintRects", msg_dict)

    def setShowScrollBottleneckRects(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows scroll bottleneck rects

        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowScrollBottleneckRects", msg_dict)

    def setShowHitTestBorders(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows hit-test borders on layers

        :param show: True for showing hit-test borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowHitTestBorders", msg_dict)

    def setShowViewportSizeOnResize(self, show: bool) -> Awaitable[Dict]:
        """
        Paints viewport size upon main frame resize.

        :param show: Whether to paint size or not.
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict["show"] = show
        return self.client.send("Overlay.setShowViewportSizeOnResize", msg_dict)

    def setSuspended(self, suspended: bool) -> Awaitable[Dict]:
        """
        :param suspended: Whether overlay should be suspended and not consume any resources until resumed.
        :type suspended: bool
        """
        msg_dict = dict()
        if suspended is not None:
            msg_dict["suspended"] = suspended
        return self.client.send("Overlay.setSuspended", msg_dict)

    def inspectNodeRequested(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when the node should be inspected. This happens after call to `setInspectMode` or when
        user manually inspects an element.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Overlay.inspectNodeRequested", _cb)

            return future

        self.client.on("Overlay.inspectNodeRequested", cb)
        return lambda: self.client.remove_listener("Overlay.inspectNodeRequested", cb)

    def nodeHighlightRequested(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when the node should be highlighted. This happens after call to `setInspectMode`.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Overlay.nodeHighlightRequested", _cb)

            return future

        self.client.on("Overlay.nodeHighlightRequested", cb)
        return lambda: self.client.remove_listener("Overlay.nodeHighlightRequested", cb)

    def screenshotRequested(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when user asks to capture screenshot of some area on the page.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Overlay.screenshotRequested", _cb)

            return future

        self.client.on("Overlay.screenshotRequested", cb)
        return lambda: self.client.remove_listener("Overlay.screenshotRequested", cb)

    def inspectModeCanceled(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when user cancels the inspect mode.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Overlay.inspectModeCanceled", _cb)

            return future

        self.client.on("Overlay.inspectModeCanceled", cb)
        return lambda: self.client.remove_listener("Overlay.inspectModeCanceled", cb)
