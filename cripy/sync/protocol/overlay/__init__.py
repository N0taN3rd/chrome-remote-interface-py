from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.page import types as Page
from cripy.sync.protocol.overlay import events as Events
from cripy.sync.protocol.overlay import types as Types

__all__ = ["Overlay"] + Events.__all__ + Types.__all__ 


class Overlay(object):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """

    dependencies = ['DOM', 'Page', 'Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('Overlay.disable')


    def enable(self):
        self.chrome.send('Overlay.enable')


    def getHighlightObjectForTest(self, nodeId):
        """
        :param nodeId: Id of the node to get highlight object for.
        :type nodeId: int
        """
        def cb(res):
            self.chrome.emit('Overlay.getHighlightObjectForTest', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('Overlay.getHighlightObjectForTest', params=msg_dict, cb=cb)


    def hideHighlight(self):
        self.chrome.send('Overlay.hideHighlight')


    def highlightFrame(self, frameId, contentColor, contentOutlineColor):
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
            msg_dict['frameId'] = frameId
        if contentColor is not None:
            msg_dict['contentColor'] = contentColor
        if contentOutlineColor is not None:
            msg_dict['contentOutlineColor'] = contentOutlineColor
        self.chrome.send('Overlay.highlightFrame', params=msg_dict)


    def highlightNode(self, highlightConfig, nodeId, backendNodeId, objectId):
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
            msg_dict['highlightConfig'] = highlightConfig
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('Overlay.highlightNode', params=msg_dict)


    def highlightQuad(self, quad, color, outlineColor):
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
            msg_dict['quad'] = quad
        if color is not None:
            msg_dict['color'] = color
        if outlineColor is not None:
            msg_dict['outlineColor'] = outlineColor
        self.chrome.send('Overlay.highlightQuad', params=msg_dict)


    def highlightRect(self, x, y, width, height, color, outlineColor):
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
        self.chrome.send('Overlay.highlightRect', params=msg_dict)


    def setInspectMode(self, mode, highlightConfig):
        """
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
        self.chrome.send('Overlay.setInspectMode', params=msg_dict)


    def setPausedInDebuggerMessage(self, message):
        """
        :param message: The message to display, also triggers resume and step over controls.
        :type message: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict['message'] = message
        self.chrome.send('Overlay.setPausedInDebuggerMessage', params=msg_dict)


    def setShowDebugBorders(self, show):
        """
        :param show: True for showing debug borders
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        self.chrome.send('Overlay.setShowDebugBorders', params=msg_dict)


    def setShowFPSCounter(self, show):
        """
        :param show: True for showing the FPS counter
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        self.chrome.send('Overlay.setShowFPSCounter', params=msg_dict)


    def setShowPaintRects(self, result):
        """
        :param result: True for showing paint rectangles
        :type result: bool
        """
        msg_dict = dict()
        if result is not None:
            msg_dict['result'] = result
        self.chrome.send('Overlay.setShowPaintRects', params=msg_dict)


    def setShowScrollBottleneckRects(self, show):
        """
        :param show: True for showing scroll bottleneck rects
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        self.chrome.send('Overlay.setShowScrollBottleneckRects', params=msg_dict)


    def setShowViewportSizeOnResize(self, show):
        """
        :param show: Whether to paint size or not.
        :type show: bool
        """
        msg_dict = dict()
        if show is not None:
            msg_dict['show'] = show
        self.chrome.send('Overlay.setShowViewportSizeOnResize', params=msg_dict)


    def setSuspended(self, suspended):
        """
        :param suspended: Whether overlay should be suspended and not consume any resources until resumed.
        :type suspended: bool
        """
        msg_dict = dict()
        if suspended is not None:
            msg_dict['suspended'] = suspended
        self.chrome.send('Overlay.setSuspended', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

