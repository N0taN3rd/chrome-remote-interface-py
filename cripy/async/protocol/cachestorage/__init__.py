from typing import Any, List, Optional, Union
from cripy.async.protocol.cachestorage import types as Types


class CacheStorage(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def deleteCache(self, cacheId: str) -> Optional[dict]:
        """
        :param cacheId: Id of cache for deletion.
        :type cacheId: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        mayberes = await self.chrome.send("CacheStorage.deleteCache", msg_dict)
        return mayberes

    async def deleteEntry(self, cacheId: str, request: str) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("CacheStorage.deleteEntry", msg_dict)
        return mayberes

    async def requestCacheNames(self, securityOrigin: str) -> Optional[dict]:
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        mayberes = await self.chrome.send("CacheStorage.requestCacheNames", msg_dict)
        res = await mayberes
        res["caches"] = Types.Cache.safe_create_from_list(res["caches"])
        return res

    async def requestCachedResponse(
        self, cacheId: str, requestURL: str
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send(
            "CacheStorage.requestCachedResponse", msg_dict
        )
        res = await mayberes
        res["response"] = Types.CachedResponse.safe_create(res["response"])
        return res

    async def requestEntries(
        self, cacheId: str, skipCount: int, pageSize: int
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("CacheStorage.requestEntries", msg_dict)
        res = await mayberes
        res["cacheDataEntries"] = Types.DataEntry.safe_create_from_list(
            res["cacheDataEntries"]
        )
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
