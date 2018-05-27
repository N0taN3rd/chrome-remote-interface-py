from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.network import types as Network

ResourceType = str

FrameId = str

ScriptIdentifier = str

TransitionType = str

DialogType = str


class Frame(ChromeTypeBase):

    def __init__(
        self,
        id: str,
        loaderId: "Network.LoaderId",
        url: str,
        securityOrigin: str,
        mimeType: str,
        parentId: Optional[str] = None,
        name: Optional[str] = None,
        unreachableUrl: Optional[str] = None,
    ) -> None:
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

    def __init__(
        self,
        url: str,
        type: "ResourceType",
        mimeType: str,
        lastModified: Optional["Network.TimeSinceEpoch"] = None,
        contentSize: Optional[float] = None,
        failed: Optional[bool] = None,
        canceled: Optional[bool] = None,
    ) -> None:
        super().__init__()
        self.url: str = url
        self.type: ResourceType = type
        self.mimeType: str = mimeType
        self.lastModified: Optional[Network.TimeSinceEpoch] = lastModified
        self.contentSize: Optional[float] = contentSize
        self.failed: Optional[bool] = failed
        self.canceled: Optional[bool] = canceled


class FrameResourceTree(ChromeTypeBase):

    def __init__(
        self,
        frame: "Frame",
        resources: List["FrameResource"],
        childFrames: Optional[List["FrameResourceTree"]] = None,
    ) -> None:
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameResourceTree]] = childFrames
        self.resources: List[FrameResource] = resources


class FrameTree(ChromeTypeBase):

    def __init__(
        self, frame: "Frame", childFrames: Optional[List["FrameTree"]] = None
    ) -> None:
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameTree]] = childFrames


class NavigationEntry(ChromeTypeBase):

    def __init__(
        self,
        id: int,
        url: str,
        userTypedURL: str,
        title: str,
        transitionType: "TransitionType",
    ) -> None:
        super().__init__()
        self.id: int = id
        self.url: str = url
        self.userTypedURL: str = userTypedURL
        self.title: str = title
        self.transitionType: TransitionType = transitionType


class ScreencastFrameMetadata(ChromeTypeBase):

    def __init__(
        self,
        offsetTop: float,
        pageScaleFactor: float,
        deviceWidth: float,
        deviceHeight: float,
        scrollOffsetX: float,
        scrollOffsetY: float,
        timestamp: Optional["Network.TimeSinceEpoch"] = None,
    ) -> None:
        super().__init__()
        self.offsetTop: float = offsetTop
        self.pageScaleFactor: float = pageScaleFactor
        self.deviceWidth: float = deviceWidth
        self.deviceHeight: float = deviceHeight
        self.scrollOffsetX: float = scrollOffsetX
        self.scrollOffsetY: float = scrollOffsetY
        self.timestamp: Optional[Network.TimeSinceEpoch] = timestamp


class AppManifestError(ChromeTypeBase):

    def __init__(self, message: str, critical: int, line: int, column: int) -> None:
        super().__init__()
        self.message: str = message
        self.critical: int = critical
        self.line: int = line
        self.column: int = column


class LayoutViewport(ChromeTypeBase):

    def __init__(
        self, pageX: int, pageY: int, clientWidth: int, clientHeight: int
    ) -> None:
        super().__init__()
        self.pageX: int = pageX
        self.pageY: int = pageY
        self.clientWidth: int = clientWidth
        self.clientHeight: int = clientHeight


class VisualViewport(ChromeTypeBase):

    def __init__(
        self,
        offsetX: float,
        offsetY: float,
        pageX: float,
        pageY: float,
        clientWidth: float,
        clientHeight: float,
        scale: float,
    ) -> None:
        super().__init__()
        self.offsetX: float = offsetX
        self.offsetY: float = offsetY
        self.pageX: float = pageX
        self.pageY: float = pageY
        self.clientWidth: float = clientWidth
        self.clientHeight: float = clientHeight
        self.scale: float = scale


class Viewport(ChromeTypeBase):

    def __init__(
        self, x: float, y: float, width: float, height: float, scale: float
    ) -> None:
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
        self.scale: float = scale
