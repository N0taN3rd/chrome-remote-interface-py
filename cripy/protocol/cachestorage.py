"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["CacheStorage"]


class CacheStorage:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of CacheStorage

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def deleteCache(self, cacheId: str) -> Awaitable[Dict]:
        """
        Deletes a cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage#method-deleteCache`

        :param cacheId: Id of cache for deletion.
        :return: The results of the command
        """
        return self.client.send("CacheStorage.deleteCache", {"cacheId": cacheId})

    def deleteEntry(self, cacheId: str, request: str) -> Awaitable[Dict]:
        """
        Deletes a cache entry.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage#method-deleteEntry`

        :param cacheId: Id of cache where the entry will be deleted.
        :param request: URL spec of the request.
        :return: The results of the command
        """
        return self.client.send(
            "CacheStorage.deleteEntry", {"cacheId": cacheId, "request": request}
        )

    def requestCacheNames(self, securityOrigin: str) -> Awaitable[Dict]:
        """
        Requests cache names.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage#method-requestCacheNames`

        :param securityOrigin: Security origin.
        :return: The results of the command
        """
        return self.client.send(
            "CacheStorage.requestCacheNames", {"securityOrigin": securityOrigin}
        )

    def requestCachedResponse(
        self, cacheId: str, requestURL: str, requestHeaders: List[Dict[str, Any]]
    ) -> Awaitable[Dict]:
        """
        Fetches cache entry.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage#method-requestCachedResponse`

        :param cacheId: Id of cache that contains the entry.
        :param requestURL: URL spec of the request.
        :param requestHeaders: headers of the request.
        :return: The results of the command
        """
        return self.client.send(
            "CacheStorage.requestCachedResponse",
            {
                "cacheId": cacheId,
                "requestURL": requestURL,
                "requestHeaders": requestHeaders,
            },
        )

    def requestEntries(
        self,
        cacheId: str,
        skipCount: int,
        pageSize: int,
        pathFilter: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Requests data from cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CacheStorage#method-requestEntries`

        :param cacheId: ID of cache to get entries from.
        :param skipCount: Number of records to skip.
        :param pageSize: Number of records to fetch.
        :param pathFilter: If present, only return the entries containing this substring in the path
        :return: The results of the command
        """
        msg = {"cacheId": cacheId, "skipCount": skipCount, "pageSize": pageSize}
        if pathFilter is not None:
            msg["pathFilter"] = pathFilter
        return self.client.send("CacheStorage.requestEntries", msg)
