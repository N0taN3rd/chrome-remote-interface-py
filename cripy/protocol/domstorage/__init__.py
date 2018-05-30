from typing import Any, List, Optional, Union
from cripy.protocol.domstorage import events as Events
from cripy.protocol.domstorage import types as Types


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    async def clear(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        res = await self.chrome.send('DOMStorage.clear', msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('DOMStorage.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('DOMStorage.enable')
        return res

    async def getDOMStorageItems(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        res = await self.chrome.send('DOMStorage.getDOMStorageItems', msg_dict)
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
        res = await self.chrome.send('DOMStorage.removeDOMStorageItem', msg_dict)
        return res

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
        res = await self.chrome.send('DOMStorage.setDOMStorageItem', msg_dict)
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

