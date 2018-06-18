from cripy.gevent.protocol.domstorage import events as Events
from cripy.gevent.protocol.domstorage import types as Types

__all__ = ["DOMStorage"] + Events.__all__ + Types.__all__


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def clear(self, storageId):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        wres = self.chrome.send("DOMStorage.clear", msg_dict)
        return wres.get()

    def disable(self):
        wres = self.chrome.send("DOMStorage.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("DOMStorage.enable")
        return wres.get()

    def getDOMStorageItems(self, storageId):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        wres = self.chrome.send("DOMStorage.getDOMStorageItems", msg_dict)
        res = wres.get()
        return res

    def removeDOMStorageItem(self, storageId, key):
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        if key is not None:
            msg_dict["key"] = key
        wres = self.chrome.send("DOMStorage.removeDOMStorageItem", msg_dict)
        return wres.get()

    def setDOMStorageItem(self, storageId, key, value):
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
            msg_dict["storageId"] = storageId
        if key is not None:
            msg_dict["key"] = key
        if value is not None:
            msg_dict["value"] = value
        wres = self.chrome.send("DOMStorage.setDOMStorageItem", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
