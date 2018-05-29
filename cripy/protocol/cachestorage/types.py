from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType

CacheId = TypeVar("CacheId", str, str)
"""Unique identifier of the Cache object."""


class Header(ProtocolType):

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: The name
        :type name: str
        :param value: The value
        :type value: str
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


class DataEntry(ProtocolType):
    """Data entry."""

    def __init__(
        self,
        requestURL: str,
        requestMethod: str,
        requestHeaders: List[Union["Header", dict]],
        responseTime: float,
        responseStatus: int,
        responseStatusText: str,
        responseHeaders: List[Union["Header", dict]],
    ) -> None:
        """
        :param requestURL: Request URL.
        :type requestURL: str
        :param requestMethod: Request method.
        :type requestMethod: str
        :param requestHeaders: Request headers
        :type requestHeaders: array
        :param responseTime: Number of seconds since epoch.
        :type responseTime: float
        :param responseStatus: HTTP response status code.
        :type responseStatus: int
        :param responseStatusText: HTTP response status text.
        :type responseStatusText: str
        :param responseHeaders: Response headers
        :type responseHeaders: array
        """
        super().__init__()
        self.requestURL: str = requestURL
        self.requestMethod: str = requestMethod
        self.requestHeaders: List[Header] = requestHeaders
        self.responseTime: float = responseTime
        self.responseStatus: int = responseStatus
        self.responseStatusText: str = responseStatusText
        self.responseHeaders: List[Header] = responseHeaders


class CachedResponse(ProtocolType):
    """Cached response"""

    def __init__(self, body: str) -> None:
        """
        :param body: Entry content, base64-encoded.
        :type body: str
        """
        super().__init__()
        self.body: str = body


class Cache(ProtocolType):
    """Cache identifier."""

    def __init__(self, cacheId: "CacheId", securityOrigin: str, cacheName: str) -> None:
        """
        :param cacheId: An opaque unique id of the cache.
        :type cacheId: CacheId
        :param securityOrigin: Security origin of the cache.
        :type securityOrigin: str
        :param cacheName: The name of the cache.
        :type cacheName: str
        """
        super().__init__()
        self.cacheId: CacheId = cacheId
        self.securityOrigin: str = securityOrigin
        self.cacheName: str = cacheName


OBJECT_LIST = {
    "Header": Header,
    "DataEntry": DataEntry,
    "CachedResponse": CachedResponse,
    "Cache": Cache,
}
