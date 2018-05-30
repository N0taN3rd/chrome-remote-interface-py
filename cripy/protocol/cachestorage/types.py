from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


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
    def safe_create(init: Optional[dict]) -> Optional[Union['Header', dict]]:
        if init is not None:
             try:
                ourselves = Header(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Header', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Header.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['DataEntry', dict]]:
        if init is not None:
             try:
                ourselves = DataEntry(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DataEntry', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataEntry.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['CachedResponse', dict]]:
        if init is not None:
             try:
                ourselves = CachedResponse(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CachedResponse', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CachedResponse.safe_create(it))
            return list_of_self
        else:
            return init


class Cache(ProtocolType):
    """
    Cache identifier.
    """

    def __init__(self, cacheId: str, securityOrigin: str, cacheName: str) -> None:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['Cache', dict]]:
        if init is not None:
             try:
                ourselves = Cache(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Cache', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Cache.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Header": Header,
    "DataEntry": DataEntry,
    "CachedResponse": CachedResponse,
    "Cache": Cache,
}
