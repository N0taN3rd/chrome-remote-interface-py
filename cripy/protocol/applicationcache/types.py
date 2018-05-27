from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page


class ApplicationCacheResource(ChromeTypeBase):
    """Detailed application cache resource information."""

    def __init__(self, url: str, size: int, type: str) -> None:
        """
        :param url: Resource url.
        :param size: Resource size.
        :param type: Resource type.
        """
        super().__init__()
        self.url: str = url
        self.size: int = size
        self.type: str = type


class ApplicationCache(ChromeTypeBase):
    """Detailed application cache information."""

    def __init__(
        self,
        manifestURL: str,
        size: float,
        creationTime: float,
        updateTime: float,
        resources: List["ApplicationCacheResource"],
    ) -> None:
        """
        :param manifestURL: Manifest URL.
        :param size: Application cache size.
        :param creationTime: Application cache creation time.
        :param updateTime: Application cache update time.
        :param resources: Application cache resources.
        """
        super().__init__()
        self.manifestURL: str = manifestURL
        self.size: float = size
        self.creationTime: float = creationTime
        self.updateTime: float = updateTime
        self.resources: List[ApplicationCacheResource] = resources


class FrameWithManifest(ChromeTypeBase):
    """Frame identifier - manifest URL pair."""

    def __init__(self, frameId: "Page.FrameId", manifestURL: str, status: int) -> None:
        """
        :param frameId: Frame identifier.
        :param manifestURL: Manifest URL.
        :param status: Application cache status.
        """
        super().__init__()
        self.frameId: Page.FrameId = frameId
        self.manifestURL: str = manifestURL
        self.status: int = status
