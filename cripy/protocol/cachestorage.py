# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["CacheStorage"]


@attr.dataclass(slots=True)
class CacheStorage(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def deleteCache(self, cacheId: str) -> Awaitable[Optional[dict]]:
        """
        Deletes a cache.

        :param cacheId: Id of cache for deletion.
        :type cacheId: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        return self.client.send("CacheStorage.deleteCache", msg_dict)

    def deleteEntry(self, cacheId: str, request: str) -> Awaitable[Optional[dict]]:
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

    def requestCacheNames(self, securityOrigin: str) -> Awaitable[Optional[dict]]:
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
        self, cacheId: str, requestURL: str
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("CacheStorage.requestCachedResponse", msg_dict)

    def requestEntries(
        self, cacheId: str, skipCount: int, pageSize: int
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("CacheStorage.requestEntries", msg_dict)
