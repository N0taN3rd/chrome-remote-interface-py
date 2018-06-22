from cripy.gevent.protocol.domstorage import events as Events
from cripy.gevent.protocol.domstorage import types as Types

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

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.DOMSTORAGE_EVENTS_TO_CLASS

