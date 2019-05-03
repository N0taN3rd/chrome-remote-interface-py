"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Overlay"]


class Overlay:
    """
    This domain provides various functionality related to drawing atop the inspected page.
     
    Domain Dependencies: 
      * DOM
      * Page
      * Runtime
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Overlay

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-disable`

        :return: The results of the command
        """
        return self.client.send("Overlay.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-enable`

        :return: The results of the command
        """
        return self.client.send("Overlay.enable", {})

    def getHighlightObjectForTest(self, nodeId: int) -> Awaitable[Dict]:
        """
        For testing.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-getHighlightObjectForTest`

        :param nodeId: Id of the node to get highlight object for.
        :return: The results of the command
        """
        return self.client.send("Overlay.getHighlightObjectForTest", {"nodeId": nodeId})

    def hideHighlight(self) -> Awaitable[Dict]:
        """
        Hides any highlight.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-hideHighlight`

        :return: The results of the command
        """
        return self.client.send("Overlay.hideHighlight", {})

    def highlightFrame(
        self,
        frameId: str,
        contentColor: Optional[Dict[str, Any]] = None,
        contentOutlineColor: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights owner element of the frame with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-highlightFrame`

        :param frameId: Identifier of the frame to highlight.
        :param contentColor: The content box highlight fill color (default: transparent).
        :param contentOutlineColor: The content box highlight outline color (default: transparent).
        :return: The results of the command
        """
        msg = {"frameId": frameId}
        if contentColor is not None:
            msg["contentColor"] = contentColor
        if contentOutlineColor is not None:
            msg["contentOutlineColor"] = contentOutlineColor
        return self.client.send("Overlay.highlightFrame", msg)

    def highlightNode(
        self,
        highlightConfig: Dict[str, Any],
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        selector: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
        objectId must be specified.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-highlightNode`

        :param highlightConfig: A descriptor for the highlight appearance.
        :param nodeId: Identifier of the node to highlight.
        :param backendNodeId: Identifier of the backend node to highlight.
        :param objectId: JavaScript object id of the node to be highlighted.
        :param selector: Selectors to highlight relevant nodes.
        :return: The results of the command
        """
        msg = {"highlightConfig": highlightConfig}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        if selector is not None:
            msg["selector"] = selector
        return self.client.send("Overlay.highlightNode", msg)

    def highlightQuad(
        self,
        quad: List[Union[int, float]],
        color: Optional[Dict[str, Any]] = None,
        outlineColor: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-highlightQuad`

        :param quad: Quad to highlight
        :param color: The highlight fill color (default: transparent).
        :param outlineColor: The highlight outline color (default: transparent).
        :return: The results of the command
        """
        msg = {"quad": quad}
        if color is not None:
            msg["color"] = color
        if outlineColor is not None:
            msg["outlineColor"] = outlineColor
        return self.client.send("Overlay.highlightQuad", msg)

    def highlightRect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Optional[Dict[str, Any]] = None,
        outlineColor: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-highlightRect`

        :param x: X coordinate
        :param y: Y coordinate
        :param width: Rectangle width
        :param height: Rectangle height
        :param color: The highlight fill color (default: transparent).
        :param outlineColor: The highlight outline color (default: transparent).
        :return: The results of the command
        """
        msg = {"x": x, "y": y, "width": width, "height": height}
        if color is not None:
            msg["color"] = color
        if outlineColor is not None:
            msg["outlineColor"] = outlineColor
        return self.client.send("Overlay.highlightRect", msg)

    def setInspectMode(
        self, mode: str, highlightConfig: Optional[Dict[str, Any]] = None
    ) -> Awaitable[Dict]:
        """
        Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
        Backend then generates 'inspectNodeRequested' event upon element selection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setInspectMode`

        :param mode: Set an inspection mode.
        :param highlightConfig: A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled
         == false`.
        :return: The results of the command
        """
        msg = {"mode": mode}
        if highlightConfig is not None:
            msg["highlightConfig"] = highlightConfig
        return self.client.send("Overlay.setInspectMode", msg)

    def setShowAdHighlights(self, show: bool) -> Awaitable[Dict]:
        """
        Highlights owner element of all frames detected to be ads.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowAdHighlights`

        :param show: True for showing ad highlights
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowAdHighlights", {"show": show})

    def setPausedInDebuggerMessage(
        self, message: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setPausedInDebuggerMessage`

        :param message: The message to display, also triggers resume and step over controls.
        :return: The results of the command
        """
        msg = {}
        if message is not None:
            msg["message"] = message
        return self.client.send("Overlay.setPausedInDebuggerMessage", msg)

    def setShowDebugBorders(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows debug borders on layers

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowDebugBorders`

        :param show: True for showing debug borders
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowDebugBorders", {"show": show})

    def setShowFPSCounter(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows the FPS counter

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowFPSCounter`

        :param show: True for showing the FPS counter
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowFPSCounter", {"show": show})

    def setShowPaintRects(self, result: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows paint rectangles

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowPaintRects`

        :param result: True for showing paint rectangles
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowPaintRects", {"result": result})

    def setShowScrollBottleneckRects(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows scroll bottleneck rects

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowScrollBottleneckRects`

        :param show: True for showing scroll bottleneck rects
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowScrollBottleneckRects", {"show": show})

    def setShowHitTestBorders(self, show: bool) -> Awaitable[Dict]:
        """
        Requests that backend shows hit-test borders on layers

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowHitTestBorders`

        :param show: True for showing hit-test borders
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowHitTestBorders", {"show": show})

    def setShowViewportSizeOnResize(self, show: bool) -> Awaitable[Dict]:
        """
        Paints viewport size upon main frame resize.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#method-setShowViewportSizeOnResize`

        :param show: Whether to paint size or not.
        :return: The results of the command
        """
        return self.client.send("Overlay.setShowViewportSizeOnResize", {"show": show})

    def inspectNodeRequested(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when the node should be inspected. This happens after call to `setInspectMode` or when
        user manually inspects an element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#event-inspectNodeRequested`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Overlay.inspectNodeRequested"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def nodeHighlightRequested(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when the node should be highlighted. This happens after call to `setInspectMode`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#event-nodeHighlightRequested`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Overlay.nodeHighlightRequested"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def screenshotRequested(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when user asks to capture screenshot of some area on the page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#event-screenshotRequested`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Overlay.screenshotRequested"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def inspectModeCanceled(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Fired when user cancels the inspect mode.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Overlay#event-inspectModeCanceled`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Overlay.inspectModeCanceled"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
