from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

CacheId = str


class DataEntry(ChromeTypeBase):
    """Data entry."""

    def __init__(
        self,
        requestURL: str,
        requestMethod: str,
        requestHeaders: List["Header"],
        responseTime: float,
        responseStatus: int,
        responseStatusText: str,
        responseHeaders: List["Header"],
    ) -> None:
        """
        :param requestURL: Request URL.
        :param requestMethod: Request method.
        :param requestHeaders: Request headers
        :param responseTime: Number of seconds since epoch.
        :param responseStatus: HTTP response status code.
        :param responseStatusText: HTTP response status text.
        :param responseHeaders: Response headers
        """
        super().__init__()
        self.requestURL: str = requestURL
        self.requestMethod: str = requestMethod
        self.requestHeaders: List[Header] = requestHeaders
        self.responseTime: float = responseTime
        self.responseStatus: int = responseStatus
        self.responseStatusText: str = responseStatusText
        self.responseHeaders: List[Header] = responseHeaders


class Cache(ChromeTypeBase):
    """Cache identifier."""

    def __init__(self, cacheId: "CacheId", securityOrigin: str, cacheName: str) -> None:
        """
        :param cacheId: An opaque unique id of the cache.
        :param securityOrigin: Security origin of the cache.
        :param cacheName: The name of the cache.
        """
        super().__init__()
        self.cacheId: CacheId = cacheId
        self.securityOrigin: str = securityOrigin
        self.cacheName: str = cacheName


class Header(ChromeTypeBase):

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: The name
        :param value: The value
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


class CachedResponse(ChromeTypeBase):
    """Cached response"""

    def __init__(self, body: str) -> None:
        """
        :param body: Entry content, base64-encoded.
        """
        super().__init__()
        self.body: str = body
