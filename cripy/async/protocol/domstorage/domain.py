from typing import Any, List, Optional, Union
from cripy.async.protocol.domstorage import events as Events
from cripy.async.protocol.domstorage import types as Types

__all__ = ["DOMStorage"]


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """

    events = Events.DOMSTORAGE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new DOMStorage object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clear(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        mayberes = await self.chrome.send('DOMStorage.clear', msg_dict)
        return mayberes

    async def disable(self) -> Optional[dict]:
        """
        Disables storage tracking, prevents storage events from being sent to the client.
        """
        mayberes = await self.chrome.send('DOMStorage.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables storage tracking, storage events will now be delivered to the client.
        """
        mayberes = await self.chrome.send('DOMStorage.enable')
        return mayberes

    async def getDOMStorageItems(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        mayberes = await self.chrome.send('DOMStorage.getDOMStorageItems', msg_dict)
        res = await mayberes
        return res

    async def removeDOMStorageItem(self, storageId: dict, key: str) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        if key is not None:
            msg_dict['key'] = key
        mayberes = await self.chrome.send('DOMStorage.removeDOMStorageItem', msg_dict)
        return mayberes

    async def setDOMStorageItem(self, storageId: dict, key: str, value: str) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param value: The value
        :type value: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        if key is not None:
            msg_dict['key'] = key
        if value is not None:
            msg_dict['value'] = value
        mayberes = await self.chrome.send('DOMStorage.setDOMStorageItem', msg_dict)
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
        return Events.DOMSTORAGE_EVENTS_TO_CLASS

