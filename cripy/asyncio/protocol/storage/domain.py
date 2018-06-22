from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.storage import events as Events
from cripy.asyncio.protocol.storage import types as Types

__all__ = ["Storage"]


class Storage(object):
    events = Events.STORAGE_EVENTS_NS

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
        mayberes = await self.chrome.send('Storage.clearDataForOrigin', msg_dict)
        return mayberes

    async def getUsageAndQuota(self, origin: str) -> Optional[dict]:
        """
        Returns usage and quota in bytes.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        mayberes = await self.chrome.send('Storage.getUsageAndQuota', msg_dict)
        res = await mayberes
        res['usageBreakdown'] = Types.UsageForType.safe_create_from_list(res['usageBreakdown'])
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
        mayberes = await self.chrome.send('Storage.trackCacheStorageForOrigin', msg_dict)
        return mayberes

    async def trackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        mayberes = await self.chrome.send('Storage.trackIndexedDBForOrigin', msg_dict)
        return mayberes

    async def untrackCacheStorageForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for cache storage.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        mayberes = await self.chrome.send('Storage.untrackCacheStorageForOrigin', msg_dict)
        return mayberes

    async def untrackIndexedDBForOrigin(self, origin: str) -> Optional[dict]:
        """
        Unregisters origin from receiving notifications for IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        mayberes = await self.chrome.send('Storage.untrackIndexedDBForOrigin', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.STORAGE_EVENTS_TO_CLASS

