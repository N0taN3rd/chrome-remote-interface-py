from cripy.gevent.protocol.storage import events as Events
from cripy.gevent.protocol.storage import types as Types

__all__ = ["Storage"] + Events.__all__ + Types.__all__


class Storage(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def clearDataForOrigin(self, origin, storageTypes):
        """
        :param origin: Security origin.
        :type origin: str
        :param storageTypes: Comma separated origin names.
        :type storageTypes: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if storageTypes is not None:
            msg_dict["storageTypes"] = storageTypes
        wres = self.chrome.send("Storage.clearDataForOrigin", msg_dict)
        return wres.get()

    def getUsageAndQuota(self, origin):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        wres = self.chrome.send("Storage.getUsageAndQuota", msg_dict)
        res = wres.get()
        res["usageBreakdown"] = Types.UsageForType.safe_create_from_list(
            res["usageBreakdown"]
        )
        return res

    def trackCacheStorageForOrigin(self, origin):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        wres = self.chrome.send("Storage.trackCacheStorageForOrigin", msg_dict)
        return wres.get()

    def trackIndexedDBForOrigin(self, origin):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        wres = self.chrome.send("Storage.trackIndexedDBForOrigin", msg_dict)
        return wres.get()

    def untrackCacheStorageForOrigin(self, origin):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        wres = self.chrome.send("Storage.untrackCacheStorageForOrigin", msg_dict)
        return wres.get()

    def untrackIndexedDBForOrigin(self, origin):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        wres = self.chrome.send("Storage.untrackIndexedDBForOrigin", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
