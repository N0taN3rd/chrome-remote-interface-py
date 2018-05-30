from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

CacheId = TypeVar("CacheId", str, str) # Unique identifier of the Cache object.


class Header(ProtocolType):
    def __init__(self, name: str, value: str) -> None:
        """
        :param name: The name
        :type name: str
        :param value: The value
        :type value: str
        """
        super().__init__()
        self.name = name
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Header']:
        if init is not None:
            return Header(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Header']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Header(**it))
            return list_of_self
        else:
            return init


class DataEntry(ProtocolType):
    """
    Data entry.
    """

    def __init__(self, requestURL: str, requestMethod: str, requestHeaders: List[Union['Header', dict]], responseTime: float, responseStatus: int, responseStatusText: str, responseHeaders: List[Union['Header', dict]]) -> None:
        """
        :param requestURL: Request URL.
        :type requestURL: str
        :param requestMethod: Request method.
        :type requestMethod: str
        :param requestHeaders: Request headers
        :type requestHeaders: List[dict]
        :param responseTime: Number of seconds since epoch.
        :type responseTime: float
        :param responseStatus: HTTP response status code.
        :type responseStatus: int
        :param responseStatusText: HTTP response status text.
        :type responseStatusText: str
        :param responseHeaders: Response headers
        :type responseHeaders: List[dict]
        """
        super().__init__()
        self.requestURL = requestURL
        self.requestMethod = requestMethod
        self.requestHeaders = Header.safe_create_from_list(requestHeaders)
        self.responseTime = responseTime
        self.responseStatus = responseStatus
        self.responseStatusText = responseStatusText
        self.responseHeaders = Header.safe_create_from_list(responseHeaders)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DataEntry']:
        if init is not None:
            return DataEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DataEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataEntry(**it))
            return list_of_self
        else:
            return init


class CachedResponse(ProtocolType):
    """
    Cached response
    """

    def __init__(self, body: str) -> None:
        """
        :param body: Entry content, base64-encoded.
        :type body: str
        """
        super().__init__()
        self.body = body

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CachedResponse']:
        if init is not None:
            return CachedResponse(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CachedResponse']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CachedResponse(**it))
            return list_of_self
        else:
            return init


class Cache(ProtocolType):
    """
    Cache identifier.
    """

    def __init__(self, cacheId: CacheId, securityOrigin: str, cacheName: str) -> None:
        """
        :param cacheId: An opaque unique id of the cache.
        :type cacheId: str
        :param securityOrigin: Security origin of the cache.
        :type securityOrigin: str
        :param cacheName: The name of the cache.
        :type cacheName: str
        """
        super().__init__()
        self.cacheId = cacheId
        self.securityOrigin = securityOrigin
        self.cacheName = cacheName

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Cache']:
        if init is not None:
            return Cache(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Cache']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Cache(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Header": Header,
    "DataEntry": DataEntry,
    "CachedResponse": CachedResponse,
    "Cache": Cache,
}
