__all__ = ["Storage"]


class Storage(object):
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
        return wres.get()

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
        """
        A cache's contents have been modified.
        """
        self.chrome.on("Storage.cacheStorageContentUpdated", fn, once=once)

    def cacheStorageListUpdated(self, fn, once=False):
        """
        A cache has been added/deleted.
        """
        self.chrome.on("Storage.cacheStorageListUpdated", fn, once=once)

    def indexedDBContentUpdated(self, fn, once=False):
        """
        The origin's IndexedDB object store has been modified.
        """
        self.chrome.on("Storage.indexedDBContentUpdated", fn, once=once)

    def indexedDBListUpdated(self, fn, once=False):
        """
        The origin's IndexedDB database list has been modified.
        """
        self.chrome.on("Storage.indexedDBListUpdated", fn, once=once)

