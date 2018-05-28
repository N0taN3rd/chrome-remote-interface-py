from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# Unique identifier of the Cache object.
CacheId = str


class DataEntry(ChromeTypeBase):
    """Data entry."""
    def __init__(self, requestURL: str, requestMethod: str, requestHeaders: List['Header'], responseTime: float, responseStatus: int, responseStatusText: str, responseHeaders: List['Header']) -> None:
        """
        :param str requestURL: Request URL.
        :param str requestMethod: Request method.
        :param array requestHeaders: Request headers
        :param float responseTime: Number of seconds since epoch.
        :param int responseStatus: HTTP response status code.
        :param str responseStatusText: HTTP response status text.
        :param array responseHeaders: Response headers
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
    def __init__(self, cacheId: 'CacheId', securityOrigin: str, cacheName: str) -> None:
        """
        :param CacheId cacheId: An opaque unique id of the cache.
        :param str securityOrigin: Security origin of the cache.
        :param str cacheName: The name of the cache.
        """
        super().__init__()
        self.cacheId: CacheId = cacheId
        self.securityOrigin: str = securityOrigin
        self.cacheName: str = cacheName


class Header(ChromeTypeBase):
    pass
    def __init__(self, name: str, value: str) -> None:
        """
        :param str name: The name
        :param str value: The value
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


class CachedResponse(ChromeTypeBase):
    """Cached response"""
    def __init__(self, body: str) -> None:
        """
        :param str body: Entry content, base64-encoded.
        """
        super().__init__()
        self.body: str = body


