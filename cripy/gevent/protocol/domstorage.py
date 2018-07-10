__all__ = ["DOMStorage"]


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """

    def __init__(self, chrome):
        """
        Construct a new DOMStorage object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clear(self, storageId):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        wres = self.chrome.send('DOMStorage.clear', msg_dict)
        return wres.get()

    def disable(self):
        """
        Disables storage tracking, prevents storage events from being sent to the client.
        """
        wres = self.chrome.send('DOMStorage.disable')
        return wres.get()

    def enable(self):
        """
        Enables storage tracking, storage events will now be delivered to the client.
        """
        wres = self.chrome.send('DOMStorage.enable')
        return wres.get()

    def getDOMStorageItems(self, storageId):
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        wres = self.chrome.send('DOMStorage.getDOMStorageItems', msg_dict)
        return wres.get()

    def removeDOMStorageItem(self, storageId, key):
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
        wres = self.chrome.send('DOMStorage.removeDOMStorageItem', msg_dict)
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
            msg_dict['storageId'] = storageId
        if key is not None:
            msg_dict['key'] = key
        if value is not None:
            msg_dict['value'] = value
        wres = self.chrome.send('DOMStorage.setDOMStorageItem', msg_dict)
        return wres.get()

    def domStorageItemAdded(self, fn, once=False):
        self.chrome.on("DOMStorage.domStorageItemAdded", fn, once=once)

    def domStorageItemRemoved(self, fn, once=False):
        self.chrome.on("DOMStorage.domStorageItemRemoved", fn, once=once)

    def domStorageItemUpdated(self, fn, once=False):
        self.chrome.on("DOMStorage.domStorageItemUpdated", fn, once=once)

    def domStorageItemsCleared(self, fn, once=False):
        self.chrome.on("DOMStorage.domStorageItemsCleared", fn, once=once)


