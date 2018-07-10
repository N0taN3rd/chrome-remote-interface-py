__all__ = ["Overlay"]


class Overlay(object):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """

    dependencies = ['DOM', 'Page', 'Runtime']

    def __init__(self, chrome):
        """
        Construct a new Overlay object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables domain notifications.
        """
        wres = self.chrome.send('Overlay.disable')
        return wres.get()

    def enable(self):
        """
        Enables domain notifications.
        """
        wres = self.chrome.send('Overlay.enable')
        return wres.get()

    def getHighlightObjectForTest(self, nodeId):
        """
        For testing.

        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('Overlay.getHighlightObjectForTest', msg_dict)
        return wres.get()

    def hideHighlight(self):
        """
        Hides any highlight.
        """
        wres = self.chrome.send('Overlay.hideHighlight')
        return wres.get()

    def highlightFrame(self, frameId, contentColor=None, contentOutlineColor=None):
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
            msg_dict['frameId'] = frameId
        if contentColor is not None:
            msg_dict['contentColor'] = contentColor
        if contentOutlineColor is not None:
            msg_dict['contentOutlineColor'] = contentOutlineColor
        wres = self.chrome.send('Overlay.highlightFrame', msg_dict)
        return wres.get()

    def highlightNode(self, highlightConfig, nodeId=None, backendNodeId=None, objectId=None):
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
        """
        msg_dict = dict()
        if highlightConfig is not None:
            msg_dict['highlightConfig'] = highlightConfig
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        wres = self.chrome.send('Overlay.highlightNode', msg_dict)
        return wres.get()

    def highlightQuad(self, quad, color=None, outlineColor=None):
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
            msg_dict['quad'] = quad
        if color is not None:
            msg_dict['color'] = color
        if outlineColor is not None:
            msg_dict['outlineColor'] = outlineColor
        wres = self.chrome.send('Overlay.highlightQuad', msg_dict)
        return wres.get()

    def highlightRect(self, x, y, width, height, color=None, outlineColor=None):
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
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if color is not None:
            msg_dict['color'] = color
        if outlineColor is not None:
            msg_dict['outlineColor'] = outlineColor
        wres = self.chrome.send('Overlay.highlightRect', msg_dict)
        return wres.get()

    def setInspectMode(self, mode, highlightConfig=None):
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
            msg_dict['mode'] = mode
        if highlightConfig is not None:
            msg_dict['highlightConfig'] = highlightConfig
        wres = self.chrome.send('Overlay.setInspectMode', msg_dict)
        return wres.get()

    def setPausedInDebuggerMessage(self, message=None):
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict['message'] = message
        wres = self.chrome.send('Overlay.setPausedInDebuggerMessage', msg_dict)
        return wres.get()

    def setShowDebugBorders(self, show):
        """
        Requests that backend shows debug borders on layers

        :param show: True for showing debug borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        wres = self.chrome.send('Overlay.setShowDebugBorders', msg_dict)
        return wres.get()

    def setShowFPSCounter(self, show):
        """
        Requests that backend shows the FPS counter

        :param show: True for showing the FPS counter
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        wres = self.chrome.send('Overlay.setShowFPSCounter', msg_dict)
        return wres.get()

    def setShowPaintRects(self, result):
        """
        Requests that backend shows paint rectangles

        :param result: True for showing paint rectangles
        :type result: bool
        """
        msg_dict = dict()
        if result is not None:
            msg_dict['result'] = result
        wres = self.chrome.send('Overlay.setShowPaintRects', msg_dict)
        return wres.get()

    def setShowScrollBottleneckRects(self, show):
        """
        Requests that backend shows scroll bottleneck rects

        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        wres = self.chrome.send('Overlay.setShowScrollBottleneckRects', msg_dict)
        return wres.get()

    def setShowViewportSizeOnResize(self, show):
        """
        Paints viewport size upon main frame resize.

        :param show: Whether to paint size or not.
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        wres = self.chrome.send('Overlay.setShowViewportSizeOnResize', msg_dict)
        return wres.get()

    def setSuspended(self, suspended):
        """
        :param suspended: Whether overlay should be suspended and not consume any resources until resumed.
        :type suspended: bool
        """
        msg_dict = dict()
        if suspended is not None:
            msg_dict['suspended'] = suspended
        wres = self.chrome.send('Overlay.setSuspended', msg_dict)
        return wres.get()

    def inspectNodeRequested(self, fn, once=False):
        """
        Fired when the node should be inspected. This happens after call to `setInspectMode` or when
        user manually inspects an element.
        """
        self.chrome.on("Overlay.inspectNodeRequested", fn, once=once)

    def nodeHighlightRequested(self, fn, once=False):
        """
        Fired when the node should be highlighted. This happens after call to `setInspectMode`.
        """
        self.chrome.on("Overlay.nodeHighlightRequested", fn, once=once)

    def screenshotRequested(self, fn, once=False):
        """
        Fired when user asks to capture screenshot of some area on the page.
        """
        self.chrome.on("Overlay.screenshotRequested", fn, once=once)


