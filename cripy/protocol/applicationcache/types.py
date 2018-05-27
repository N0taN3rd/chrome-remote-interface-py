from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page


class ApplicationCacheResource(ChromeTypeBase):

    def __init__(self, url: str, size: int, type: str) -> None:
        super().__init__()
        self.url: str = url
        self.size: int = size
        self.type: str = type


class ApplicationCache(ChromeTypeBase):

    def __init__(
        self,
        manifestURL: str,
        size: float,
        creationTime: float,
        updateTime: float,
        resources: List["ApplicationCacheResource"],
    ) -> None:
        super().__init__()
        self.manifestURL: str = manifestURL
        self.size: float = size
        self.creationTime: float = creationTime
        self.updateTime: float = updateTime
        self.resources: List[ApplicationCacheResource] = resources


class FrameWithManifest(ChromeTypeBase):

    def __init__(self, frameId: "Page.FrameId", manifestURL: str, status: int) -> None:
        super().__init__()
        self.frameId: Page.FrameId = frameId
        self.manifestURL: str = manifestURL
        self.status: int = status
