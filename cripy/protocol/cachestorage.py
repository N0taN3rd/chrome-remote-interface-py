"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["CacheStorage"]


@attr.dataclass(slots=True, cmp=False)
class CacheStorage(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def deleteCache(self, cacheId: str) -> Awaitable[Dict]:
        """
        Deletes a cache.

        :param cacheId: Id of cache for deletion.
        :type cacheId: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        return self.client.send("CacheStorage.deleteCache", msg_dict)

    def deleteEntry(self, cacheId: str, request: str) -> Awaitable[Dict]:
        """
        Deletes a cache entry.

        :param cacheId: Id of cache where the entry will be deleted.
        :type cacheId: str
        :param request: URL spec of the request.
        :type request: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if request is not None:
            msg_dict["request"] = request
        return self.client.send("CacheStorage.deleteEntry", msg_dict)

    def requestCacheNames(self, securityOrigin: str) -> Awaitable[Dict]:
        """
        Requests cache names.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        return self.client.send("CacheStorage.requestCacheNames", msg_dict)

    def requestCachedResponse(
        self, cacheId: str, requestURL: str, requestHeaders: List[dict]
    ) -> Awaitable[Dict]:
        """
        Fetches cache entry.

        :param cacheId: Id of cache that contains the entry.
        :type cacheId: str
        :param requestURL: URL spec of the request.
        :type requestURL: str
        :param requestHeaders: headers of the request.
        :type requestHeaders: List[dict]
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if requestURL is not None:
            msg_dict["requestURL"] = requestURL
        if requestHeaders is not None:
            msg_dict["requestHeaders"] = requestHeaders
        return self.client.send("CacheStorage.requestCachedResponse", msg_dict)

    def requestEntries(
        self,
        cacheId: str,
        skipCount: int,
        pageSize: int,
        pathFilter: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Requests data from cache.

        :param cacheId: ID of cache to get entries from.
        :type cacheId: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        :param pathFilter: If present, only return the entries containing this substring in the path
        :type pathFilter: Optional[str]
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if skipCount is not None:
            msg_dict["skipCount"] = skipCount
        if pageSize is not None:
            msg_dict["pageSize"] = pageSize
        if pathFilter is not None:
            msg_dict["pathFilter"] = pathFilter
        return self.client.send("CacheStorage.requestEntries", msg_dict)
