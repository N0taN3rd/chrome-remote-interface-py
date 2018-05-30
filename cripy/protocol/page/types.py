from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.network import types as Network

TransitionType = TypeVar("TransitionType", str, str) # Transition type.

ScriptIdentifier = TypeVar("ScriptIdentifier", str, str) # Unique script identifier.

ResourceType = TypeVar("ResourceType", str, str) # Resource type as it was perceived by the rendering engine.

FrameId = TypeVar("FrameId", str, str) # Unique frame identifier.

DialogType = TypeVar("DialogType", str, str) # Javascript dialog type.


class VisualViewport(ProtocolType):
    """
    Visual viewport position, dimensions, and scale.
    """

    def __init__(self, offsetX: float, offsetY: float, pageX: float, pageY: float, clientWidth: float, clientHeight: float, scale: float) -> None:
        """
        :param offsetX: Horizontal offset relative to the layout viewport (CSS pixels).
        :type offsetX: float
        :param offsetY: Vertical offset relative to the layout viewport (CSS pixels).
        :type offsetY: float
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type pageX: float
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type pageY: float
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type clientWidth: float
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type clientHeight: float
        :param scale: Scale relative to the ideal viewport (size at width=device-width).
        :type scale: float
        """
        super().__init__()
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight
        self.scale = scale

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['VisualViewport']:
        if init is not None:
            return VisualViewport(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['VisualViewport']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VisualViewport(**it))
            return list_of_self
        else:
            return init


class Viewport(ProtocolType):
    """
    Viewport for capturing screenshot.
    """

    def __init__(self, x: float, y: float, width: float, height: float, scale: float) -> None:
        """
        :param x: X offset in CSS pixels.
        :type x: float
        :param y: Y offset in CSS pixels
        :type y: float
        :param width: Rectangle width in CSS pixels
        :type width: float
        :param height: Rectangle height in CSS pixels
        :type height: float
        :param scale: Page scale factor.
        :type scale: float
        """
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Viewport']:
        if init is not None:
            return Viewport(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Viewport']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Viewport(**it))
            return list_of_self
        else:
            return init


class ScreencastFrameMetadata(ProtocolType):
    """
    Screencast frame metadata.
    """

    def __init__(self, offsetTop: float, pageScaleFactor: float, deviceWidth: float, deviceHeight: float, scrollOffsetX: float, scrollOffsetY: float, timestamp: Optional[Network.TimeSinceEpoch] = None) -> None:
        """
        :param offsetTop: Top offset in DIP.
        :type offsetTop: float
        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        :param deviceWidth: Device screen width in DIP.
        :type deviceWidth: float
        :param deviceHeight: Device screen height in DIP.
        :type deviceHeight: float
        :param scrollOffsetX: Position of horizontal scroll in CSS pixels.
        :type scrollOffsetX: float
        :param scrollOffsetY: Position of vertical scroll in CSS pixels.
        :type scrollOffsetY: float
        :param timestamp: Frame swap timestamp.
        :type timestamp: Optional[float]
        """
        super().__init__()
        self.offsetTop = offsetTop
        self.pageScaleFactor = pageScaleFactor
        self.deviceWidth = deviceWidth
        self.deviceHeight = deviceHeight
        self.scrollOffsetX = scrollOffsetX
        self.scrollOffsetY = scrollOffsetY
        self.timestamp = timestamp

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreencastFrameMetadata']:
        if init is not None:
            return ScreencastFrameMetadata(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreencastFrameMetadata']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastFrameMetadata(**it))
            return list_of_self
        else:
            return init


class NavigationEntry(ProtocolType):
    """
    Navigation history entry.
    """

    def __init__(self, id: int, url: str, userTypedURL: str, title: str, transitionType: TransitionType) -> None:
        """
        :param id: Unique id of the navigation history entry.
        :type id: int
        :param url: URL of the navigation history entry.
        :type url: str
        :param userTypedURL: URL that the user typed in the url bar.
        :type userTypedURL: str
        :param title: Title of the navigation history entry.
        :type title: str
        :param transitionType: Transition type.
        :type transitionType: str
        """
        super().__init__()
        self.id = id
        self.url = url
        self.userTypedURL = userTypedURL
        self.title = title
        self.transitionType = transitionType

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['NavigationEntry']:
        if init is not None:
            return NavigationEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['NavigationEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NavigationEntry(**it))
            return list_of_self
        else:
            return init


class LayoutViewport(ProtocolType):
    """
    Layout viewport position and dimensions.
    """

    def __init__(self, pageX: int, pageY: int, clientWidth: int, clientHeight: int) -> None:
        """
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type pageX: int
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type pageY: int
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type clientWidth: int
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type clientHeight: int
        """
        super().__init__()
        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LayoutViewport']:
        if init is not None:
            return LayoutViewport(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LayoutViewport']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayoutViewport(**it))
            return list_of_self
        else:
            return init


class FrameTree(ProtocolType):
    """
    Information about the Frame hierarchy.
    """

    def __init__(self, frame: Union['Frame', dict], childFrames: Optional[List[Union['FrameTree', dict]]] = None) -> None:
        """
        :param frame: Frame information for this tree item.
        :type frame: dict
        :param childFrames: Child frames.
        :type childFrames: Optional[List[dict]]
        """
        super().__init__()
        self.frame = Frame.safe_create(frame)
        self.childFrames = FrameTree.safe_create_from_list(childFrames)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameTree']:
        if init is not None:
            return FrameTree(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameTree']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameTree(**it))
            return list_of_self
        else:
            return init


class FrameResourceTree(ProtocolType):
    """
    Information about the Frame hierarchy along with their cached resources.
    """

    def __init__(self, frame: Union['Frame', dict], resources: List[Union['FrameResource', dict]], childFrames: Optional[List[Union['FrameResourceTree', dict]]] = None) -> None:
        """
        :param frame: Frame information for this tree item.
        :type frame: dict
        :param childFrames: Child frames.
        :type childFrames: Optional[List[dict]]
        :param resources: Information about frame resources.
        :type resources: List[dict]
        """
        super().__init__()
        self.frame = Frame.safe_create(frame)
        self.childFrames = FrameResourceTree.safe_create_from_list(childFrames)
        self.resources = FrameResource.safe_create_from_list(resources)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameResourceTree']:
        if init is not None:
            return FrameResourceTree(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameResourceTree']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResourceTree(**it))
            return list_of_self
        else:
            return init


class FrameResource(ProtocolType):
    """
    Information about the Resource on the page.
    """

    def __init__(self, url: str, type: ResourceType, mimeType: str, lastModified: Optional[Network.TimeSinceEpoch] = None, contentSize: Optional[float] = None, failed: Optional[bool] = None, canceled: Optional[bool] = None) -> None:
        """
        :param url: Resource URL.
        :type url: str
        :param type: Type of this resource.
        :type type: str
        :param mimeType: Resource mimeType as determined by the browser.
        :type mimeType: str
        :param lastModified: last-modified timestamp as reported by server.
        :type lastModified: Optional[float]
        :param contentSize: Resource content size.
        :type contentSize: Optional[float]
        :param failed: True if the resource failed to load.
        :type failed: Optional[bool]
        :param canceled: True if the resource was canceled during loading.
        :type canceled: Optional[bool]
        """
        super().__init__()
        self.url = url
        self.type = type
        self.mimeType = mimeType
        self.lastModified = lastModified
        self.contentSize = contentSize
        self.failed = failed
        self.canceled = canceled

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameResource']:
        if init is not None:
            return FrameResource(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameResource']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResource(**it))
            return list_of_self
        else:
            return init


class Frame(ProtocolType):
    """
    Information about the Frame on the page.
    """

    def __init__(self, id: str, loaderId: Network.LoaderId, url: str, securityOrigin: str, mimeType: str, parentId: Optional[str] = None, name: Optional[str] = None, unreachableUrl: Optional[str] = None) -> None:
        """
        :param id: Frame unique identifier.
        :type id: str
        :param parentId: Parent frame identifier.
        :type parentId: Optional[str]
        :param loaderId: Identifier of the loader associated with this frame.
        :type loaderId: str
        :param name: Frame's name as specified in the tag.
        :type name: Optional[str]
        :param url: Frame document's URL.
        :type url: str
        :param securityOrigin: Frame document's security origin.
        :type securityOrigin: str
        :param mimeType: Frame document's mimeType as determined by the browser.
        :type mimeType: str
        :param unreachableUrl: If the frame failed to load, this contains the URL that could not be loaded.
        :type unreachableUrl: Optional[str]
        """
        super().__init__()
        self.id = id
        self.parentId = parentId
        self.loaderId = loaderId
        self.name = name
        self.url = url
        self.securityOrigin = securityOrigin
        self.mimeType = mimeType
        self.unreachableUrl = unreachableUrl

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Frame']:
        if init is not None:
            return Frame(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Frame']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Frame(**it))
            return list_of_self
        else:
            return init


class AppManifestError(ProtocolType):
    """
    Error while paring app manifest.
    """

    def __init__(self, message: str, critical: int, line: int, column: int) -> None:
        """
        :param message: Error message.
        :type message: str
        :param critical: If criticial, this is a non-recoverable parse error.
        :type critical: int
        :param line: Error line.
        :type line: int
        :param column: Error column.
        :type column: int
        """
        super().__init__()
        self.message = message
        self.critical = critical
        self.line = line
        self.column = column

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AppManifestError']:
        if init is not None:
            return AppManifestError(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AppManifestError']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AppManifestError(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "VisualViewport": VisualViewport,
    "Viewport": Viewport,
    "ScreencastFrameMetadata": ScreencastFrameMetadata,
    "NavigationEntry": NavigationEntry,
    "LayoutViewport": LayoutViewport,
    "FrameTree": FrameTree,
    "FrameResourceTree": FrameResourceTree,
    "FrameResource": FrameResource,
    "Frame": Frame,
    "AppManifestError": AppManifestError,
}
