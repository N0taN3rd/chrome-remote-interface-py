from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page


class ApplicationCacheResource(ChromeTypeBase):
    """Detailed application cache resource information."""
    def __init__(self, url: str, size: int, type: str) -> None:
        """
        :param str url: Resource url.
        :param int size: Resource size.
        :param str type: Resource type.
        """
        super().__init__()
        self.url: str = url
        self.size: int = size
        self.type: str = type


class ApplicationCache(ChromeTypeBase):
    """Detailed application cache information."""
    def __init__(self, manifestURL: str, size: float, creationTime: float, updateTime: float, resources: List['ApplicationCacheResource']) -> None:
        """
        :param str manifestURL: Manifest URL.
        :param float size: Application cache size.
        :param float creationTime: Application cache creation time.
        :param float updateTime: Application cache update time.
        :param array resources: Application cache resources.
        """
        super().__init__()
        self.manifestURL: str = manifestURL
        self.size: float = size
        self.creationTime: float = creationTime
        self.updateTime: float = updateTime
        self.resources: List[ApplicationCacheResource] = resources


class FrameWithManifest(ChromeTypeBase):
    """Frame identifier - manifest URL pair."""
    def __init__(self, frameId: 'Page.FrameId', manifestURL: str, status: int) -> None:
        """
        :param Page.FrameId frameId: Frame identifier.
        :param str manifestURL: Manifest URL.
        :param int status: Application cache status.
        """
        super().__init__()
        self.frameId: Page.FrameId = frameId
        self.manifestURL: str = manifestURL
        self.status: int = status


