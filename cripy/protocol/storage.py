# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Storage"]


@attr.dataclass(slots=True, cmp=False)
class Storage(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def clearDataForOrigin(
        self, origin: str, storageTypes: str
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Storage.clearDataForOrigin", msg_dict)

    def getUsageAndQuota(self, origin: str) -> Awaitable[Optional[dict]]:
        """
        Returns usage and quota in bytes.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        return self.client.send("Storage.getUsageAndQuota", msg_dict)

    def trackCacheStorageForOrigin(self, origin: str) -> Awaitable[Optional[dict]]:
        """
        Registers origin to be notified when an update occurs to its cache storage list.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        return self.client.send("Storage.trackCacheStorageForOrigin", msg_dict)

    def trackIndexedDBForOrigin(self, origin: str) -> Awaitable[Optional[dict]]:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        return self.client.send("Storage.trackIndexedDBForOrigin", msg_dict)

    def untrackCacheStorageForOrigin(self, origin: str) -> Awaitable[Optional[dict]]:
        """
        Unregisters origin from receiving notifications for cache storage.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        return self.client.send("Storage.untrackCacheStorageForOrigin", msg_dict)

    def untrackIndexedDBForOrigin(self, origin: str) -> Awaitable[Optional[dict]]:
        """
        Unregisters origin from receiving notifications for IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        return self.client.send("Storage.untrackIndexedDBForOrigin", msg_dict)

    def cacheStorageContentUpdated(
        self, cb: Optional[Callable[..., Any]] = None
    ) -> Any:
        """
        A cache's contents have been modified.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Storage.cacheStorageContentUpdated", _cb)

            return future

        self.client.on("Storage.cacheStorageContentUpdated", cb)

    def cacheStorageListUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        A cache has been added/deleted.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Storage.cacheStorageListUpdated", _cb)

            return future

        self.client.on("Storage.cacheStorageListUpdated", cb)

    def indexedDBContentUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        The origin's IndexedDB object store has been modified.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Storage.indexedDBContentUpdated", _cb)

            return future

        self.client.on("Storage.indexedDBContentUpdated", cb)

    def indexedDBListUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        The origin's IndexedDB database list has been modified.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Storage.indexedDBListUpdated", _cb)

            return future

        self.client.on("Storage.indexedDBListUpdated", cb)
