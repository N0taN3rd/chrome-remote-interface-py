from cripy.sync.protocol.domstorage import events as Events
from cripy.sync.protocol.domstorage import types as Types

__all__ = ["DOMStorage"] + Events.__all__ + Types.__all__ 


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def clear(self, storageId, cb=None):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        self.chrome.send('DOMStorage.clear', params=msg_dict)


    def disable(self, cb=None):
        self.chrome.send('DOMStorage.disable')


    def enable(self, cb=None):
        self.chrome.send('DOMStorage.enable')


    def getDOMStorageItems(self, storageId, cb=None):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        self.chrome.send('DOMStorage.getDOMStorageItems', params=msg_dict, cb=cb_wrapper)


    def removeDOMStorageItem(self, storageId, key, cb=None):
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
        self.chrome.send('DOMStorage.removeDOMStorageItem', params=msg_dict)


    def setDOMStorageItem(self, storageId, key, value, cb=None):
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
        self.chrome.send('DOMStorage.setDOMStorageItem', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

