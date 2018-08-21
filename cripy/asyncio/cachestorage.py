from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["CacheStorage"]


@attr.dataclass(slots=True)
class CacheStorage(object):
    client: "Client" = attr.ib(repr=False)

    async def deleteCache(self, cacheId: str) -> Optional[dict]:
        """
        Deletes a cache.

        :param cacheId: Id of cache for deletion.
        :type cacheId: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        res = await self.client.send("CacheStorage.deleteCache", msg_dict)
        return res

    async def deleteEntry(self, cacheId: str, request: str) -> Optional[dict]:
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
        res = await self.client.send("CacheStorage.deleteEntry", msg_dict)
        return res

    async def requestCacheNames(self, securityOrigin: str) -> Optional[dict]:
        """
        Requests cache names.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        res = await self.client.send("CacheStorage.requestCacheNames", msg_dict)
        return res

    async def requestCachedResponse(
        self, cacheId: str, requestURL: str
    ) -> Optional[dict]:
        """
        Fetches cache entry.

        :param cacheId: Id of cache that contains the enty.
        :type cacheId: str
        :param requestURL: URL spec of the request.
        :type requestURL: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if requestURL is not None:
            msg_dict["requestURL"] = requestURL
        res = await self.client.send("CacheStorage.requestCachedResponse", msg_dict)
        return res

    async def requestEntries(
        self, cacheId: str, skipCount: int, pageSize: int
    ) -> Optional[dict]:
        """
        Requests data from cache.

        :param cacheId: ID of cache to get entries from.
        :type cacheId: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if skipCount is not None:
            msg_dict["skipCount"] = skipCount
        if pageSize is not None:
            msg_dict["pageSize"] = pageSize
        res = await self.client.send("CacheStorage.requestEntries", msg_dict)
        return res
