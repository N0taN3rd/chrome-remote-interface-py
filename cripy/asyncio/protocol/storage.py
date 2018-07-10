from typing import Any, List, Optional, Union


__all__ = ["Storage"]


class Storage(object):

    def __init__(self, chrome):
        """
        Construct a new Storage object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clearDataForOrigin(self, origin: str, storageTypes: str) -> Optional[dict]:
        """
        Clears storage for origin.

        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        if storageTypes is not None:
            msg_dict['storageTypes'] = storageTypes
        res = await self.chrome.send('Storage.clearDataForOrigin', msg_dict)
        return res

    async def getUsageAndQuota(self, origin: str) -> Optional[dict]:
        """
        Returns usage and quota in bytes.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        res = await self.chrome.send('Storage.getUsageAndQuota', msg_dict)
        return res

    async def trackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        Registers origin to be notified when an update occurs to its cache storage list.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        res = await self.chrome.send('Storage.trackCacheStorageForOrigin', msg_dict)
        return res

    async def trackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        res = await self.chrome.send('Storage.trackIndexedDBForOrigin', msg_dict)
        return res

    async def untrackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for cache storage.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        res = await self.chrome.send('Storage.untrackCacheStorageForOrigin', msg_dict)
        return res

    async def untrackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        res = await self.chrome.send('Storage.untrackIndexedDBForOrigin', msg_dict)
        return res

    def cacheStorageContentUpdated(self, fn, once=False) -> None:
        """
        A cache's contents have been modified.
        """
        if once:
            self.chrome.once("Storage.cacheStorageContentUpdated", fn)
        else:
            self.chrome.on("Storage.cacheStorageContentUpdated", fn)

    def cacheStorageListUpdated(self, fn, once=False) -> None:
        """
        A cache has been added/deleted.
        """
        if once:
            self.chrome.once("Storage.cacheStorageListUpdated", fn)
        else:
            self.chrome.on("Storage.cacheStorageListUpdated", fn)

    def indexedDBContentUpdated(self, fn, once=False) -> None:
        """
        The origin's IndexedDB object store has been modified.
        """
        if once:
            self.chrome.once("Storage.indexedDBContentUpdated", fn)
        else:
            self.chrome.on("Storage.indexedDBContentUpdated", fn)

    def indexedDBListUpdated(self, fn, once=False) -> None:
        """
        The origin's IndexedDB database list has been modified.
        """
        if once:
            self.chrome.once("Storage.indexedDBListUpdated", fn)
        else:
            self.chrome.on("Storage.indexedDBListUpdated", fn)



