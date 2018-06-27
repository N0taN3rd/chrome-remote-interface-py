from cripy.gevent.protocol.storage import events as Events
from cripy.gevent.protocol.storage import types as Types

__all__ = ["Storage"]


class Storage(object):
    events = Events.STORAGE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Storage object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clearDataForOrigin(self, origin, storageTypes):
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
        wres = self.chrome.send('Storage.clearDataForOrigin', msg_dict)
        return wres.get()

    def getUsageAndQuota(self, origin):
        """
        Returns usage and quota in bytes.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        wres = self.chrome.send('Storage.getUsageAndQuota', msg_dict)
        res = wres.get()
        res['usageBreakdown'] = Types.UsageForType.safe_create_from_list(res['usageBreakdown'])
        return res

    def trackCacheStorageForOrigin(self, origin):
        """
        Registers origin to be notified when an update occurs to its cache storage list.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        wres = self.chrome.send('Storage.trackCacheStorageForOrigin', msg_dict)
        return wres.get()

    def trackIndexedDBForOrigin(self, origin):
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        wres = self.chrome.send('Storage.trackIndexedDBForOrigin', msg_dict)
        return wres.get()

    def untrackCacheStorageForOrigin(self, origin):
        """
        Unregisters origin from receiving notifications for cache storage.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        wres = self.chrome.send('Storage.untrackCacheStorageForOrigin', msg_dict)
        return wres.get()

    def untrackIndexedDBForOrigin(self, origin):
        """
        Unregisters origin from receiving notifications for IndexedDB.

        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        wres = self.chrome.send('Storage.untrackIndexedDBForOrigin', msg_dict)
        return wres.get()

    def cacheStorageContentUpdated(self, fn, once=False):
        self.chrome.on("Storage.cacheStorageContentUpdated", fn, once=once)

    def cacheStorageListUpdated(self, fn, once=False):
        self.chrome.on("Storage.cacheStorageListUpdated", fn, once=once)

    def indexedDBContentUpdated(self, fn, once=False):
        self.chrome.on("Storage.indexedDBContentUpdated", fn, once=once)

    def indexedDBListUpdated(self, fn, once=False):
        self.chrome.on("Storage.indexedDBListUpdated", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.STORAGE_EVENTS_TO_CLASS

