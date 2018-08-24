# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Storage"]


class Storage(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def clearDataForOrigin(
        self, origin: str, storageTypes: str
    ) -> Optional[dict]:
        """
        Clears storage for origin.

        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if storageTypes is not None:
            msg_dict["storageTypes"] = storageTypes
        res = await self.client.send("Storage.clearDataForOrigin", msg_dict)
        return res

    async def getUsageAndQuota(self, origin: str) -> Optional[dict]:
        """
        Returns usage and quota in bytes.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Storage.getUsageAndQuota", msg_dict)
        return res

    async def trackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        Registers origin to be notified when an update occurs to its cache storage list.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Storage.trackCacheStorageForOrigin", msg_dict)
        return res

    async def trackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Storage.trackIndexedDBForOrigin", msg_dict)
        return res

    async def untrackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for cache storage.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Storage.untrackCacheStorageForOrigin", msg_dict)
        return res

    async def untrackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Storage.untrackIndexedDBForOrigin", msg_dict)
        return res

    def cacheStorageContentUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        A cache's contents have been modified.
        """
        if once:
            self.client.once("Storage.cacheStorageContentUpdated", fn)
        else:
            self.client.on("Storage.cacheStorageContentUpdated", fn)

    def cacheStorageListUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        A cache has been added/deleted.
        """
        if once:
            self.client.once("Storage.cacheStorageListUpdated", fn)
        else:
            self.client.on("Storage.cacheStorageListUpdated", fn)

    def indexedDBContentUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        The origin's IndexedDB object store has been modified.
        """
        if once:
            self.client.once("Storage.indexedDBContentUpdated", fn)
        else:
            self.client.on("Storage.indexedDBContentUpdated", fn)

    def indexedDBListUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        The origin's IndexedDB database list has been modified.
        """
        if once:
            self.client.once("Storage.indexedDBListUpdated", fn)
        else:
            self.client.on("Storage.indexedDBListUpdated", fn)

    def __repr__(self):
        return f"Storage()"
