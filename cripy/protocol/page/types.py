from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.network import types as Network

# Resource type as it was perceived by the rendering engine.
ResourceType = str

# Unique frame identifier.
FrameId = str

# Unique script identifier.
ScriptIdentifier = str

# Transition type.
TransitionType = str

# Javascript dialog type.
DialogType = str


class Frame(ChromeTypeBase):
    """Information about the Frame on the page."""
    def __init__(self, id: str, loaderId: 'Network.LoaderId', url: str, securityOrigin: str, mimeType: str, parentId: Optional[str] = None, name: Optional[str] = None, unreachableUrl: Optional[str] = None) -> None:
        """
        :param str id: Frame unique identifier.
        :param str parentId: Parent frame identifier.
        :param Network.LoaderId loaderId: Identifier of the loader associated with this frame.
        :param str name: Frame's name as specified in the tag.
        :param str url: Frame document's URL.
        :param str securityOrigin: Frame document's security origin.
        :param str mimeType: Frame document's mimeType as determined by the browser.
        :param str unreachableUrl: If the frame failed to load, this contains the URL that could not be loaded.
        """
        super().__init__()
        self.id: str = id
        self.parentId: Optional[str] = parentId
        self.loaderId: Network.LoaderId = loaderId
        self.name: Optional[str] = name
        self.url: str = url
        self.securityOrigin: str = securityOrigin
        self.mimeType: str = mimeType
        self.unreachableUrl: Optional[str] = unreachableUrl


class FrameResource(ChromeTypeBase):
    """Information about the Resource on the page."""
    def __init__(self, url: str, type: 'ResourceType', mimeType: str, lastModified: Optional['Network.TimeSinceEpoch'] = None, contentSize: Optional[float] = None, failed: Optional[bool] = None, canceled: Optional[bool] = None) -> None:
        """
        :param str url: Resource URL.
        :param ResourceType type: Type of this resource.
        :param str mimeType: Resource mimeType as determined by the browser.
        :param Network.TimeSinceEpoch lastModified: last-modified timestamp as reported by server.
        :param float contentSize: Resource content size.
        :param bool failed: True if the resource failed to load.
        :param bool canceled: True if the resource was canceled during loading.
        """
        super().__init__()
        self.url: str = url
        self.type: ResourceType = type
        self.mimeType: str = mimeType
        self.lastModified: Optional[Network.TimeSinceEpoch] = lastModified
        self.contentSize: Optional[float] = contentSize
        self.failed: Optional[bool] = failed
        self.canceled: Optional[bool] = canceled


class FrameResourceTree(ChromeTypeBase):
    """Information about the Frame hierarchy along with their cached resources."""
    def __init__(self, frame: 'Frame', resources: List['FrameResource'], childFrames: Optional[List['FrameResourceTree']] = None) -> None:
        """
        :param Frame frame: Frame information for this tree item.
        :param array childFrames: Child frames.
        :param array resources: Information about frame resources.
        """
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameResourceTree]] = childFrames
        self.resources: List[FrameResource] = resources


class FrameTree(ChromeTypeBase):
    """Information about the Frame hierarchy."""
    def __init__(self, frame: 'Frame', childFrames: Optional[List['FrameTree']] = None) -> None:
        """
        :param Frame frame: Frame information for this tree item.
        :param array childFrames: Child frames.
        """
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameTree]] = childFrames


class NavigationEntry(ChromeTypeBase):
    """Navigation history entry."""
    def __init__(self, id: int, url: str, userTypedURL: str, title: str, transitionType: 'TransitionType') -> None:
        """
        :param int id: Unique id of the navigation history entry.
        :param str url: URL of the navigation history entry.
        :param str userTypedURL: URL that the user typed in the url bar.
        :param str title: Title of the navigation history entry.
        :param TransitionType transitionType: Transition type.
        """
        super().__init__()
        self.id: int = id
        self.url: str = url
        self.userTypedURL: str = userTypedURL
        self.title: str = title
        self.transitionType: TransitionType = transitionType


class ScreencastFrameMetadata(ChromeTypeBase):
    """Screencast frame metadata."""
    def __init__(self, offsetTop: float, pageScaleFactor: float, deviceWidth: float, deviceHeight: float, scrollOffsetX: float, scrollOffsetY: float, timestamp: Optional['Network.TimeSinceEpoch'] = None) -> None:
        """
        :param float offsetTop: Top offset in DIP.
        :param float pageScaleFactor: Page scale factor.
        :param float deviceWidth: Device screen width in DIP.
        :param float deviceHeight: Device screen height in DIP.
        :param float scrollOffsetX: Position of horizontal scroll in CSS pixels.
        :param float scrollOffsetY: Position of vertical scroll in CSS pixels.
        :param Network.TimeSinceEpoch timestamp: Frame swap timestamp.
        """
        super().__init__()
        self.offsetTop: float = offsetTop
        self.pageScaleFactor: float = pageScaleFactor
        self.deviceWidth: float = deviceWidth
        self.deviceHeight: float = deviceHeight
        self.scrollOffsetX: float = scrollOffsetX
        self.scrollOffsetY: float = scrollOffsetY
        self.timestamp: Optional[Network.TimeSinceEpoch] = timestamp


class AppManifestError(ChromeTypeBase):
    """Error while paring app manifest."""
    def __init__(self, message: str, critical: int, line: int, column: int) -> None:
        """
        :param str message: Error message.
        :param int critical: If criticial, this is a non-recoverable parse error.
        :param int line: Error line.
        :param int column: Error column.
        """
        super().__init__()
        self.message: str = message
        self.critical: int = critical
        self.line: int = line
        self.column: int = column


class LayoutViewport(ChromeTypeBase):
    """Layout viewport position and dimensions."""
    def __init__(self, pageX: int, pageY: int, clientWidth: int, clientHeight: int) -> None:
        """
        :param int pageX: Horizontal offset relative to the document (CSS pixels).
        :param int pageY: Vertical offset relative to the document (CSS pixels).
        :param int clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :param int clientHeight: Height (CSS pixels), excludes scrollbar if present.
        """
        super().__init__()
        self.pageX: int = pageX
        self.pageY: int = pageY
        self.clientWidth: int = clientWidth
        self.clientHeight: int = clientHeight


class VisualViewport(ChromeTypeBase):
    """Visual viewport position, dimensions, and scale."""
    def __init__(self, offsetX: float, offsetY: float, pageX: float, pageY: float, clientWidth: float, clientHeight: float, scale: float) -> None:
        """
        :param float offsetX: Horizontal offset relative to the layout viewport (CSS pixels).
        :param float offsetY: Vertical offset relative to the layout viewport (CSS pixels).
        :param float pageX: Horizontal offset relative to the document (CSS pixels).
        :param float pageY: Vertical offset relative to the document (CSS pixels).
        :param float clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :param float clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :param float scale: Scale relative to the ideal viewport (size at width=device-width).
        """
        super().__init__()
        self.offsetX: float = offsetX
        self.offsetY: float = offsetY
        self.pageX: float = pageX
        self.pageY: float = pageY
        self.clientWidth: float = clientWidth
        self.clientHeight: float = clientHeight
        self.scale: float = scale


class Viewport(ChromeTypeBase):
    """Viewport for capturing screenshot."""
    def __init__(self, x: float, y: float, width: float, height: float, scale: float) -> None:
        """
        :param float x: X offset in CSS pixels.
        :param float y: Y offset in CSS pixels
        :param float width: Rectangle width in CSS pixels
        :param float height: Rectangle height in CSS pixels
        :param float scale: Page scale factor.
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
        self.scale: float = scale


