from cripy.sync.protocol.storage import events as Events
from cripy.sync.protocol.storage import types as Types

__all__ = ["Storage"] + Events.__all__ + Types.__all__ 


class Storage(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def clearDataForOrigin(self, origin, storageTypes, cb=None):
        """
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
        self.chrome.send('Storage.clearDataForOrigin', params=msg_dict)


    def getUsageAndQuota(self, origin, cb=None):
        """
        :param origin: Security origin.
        :type origin: str
        """
        def cb_wrapper(res):
            res['usageBreakdown'] = Types.UsageForType.safe_create_from_list(res['usageBreakdown'])
            cb(res)
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Storage.getUsageAndQuota', params=msg_dict, cb=cb_wrapper)


    def trackCacheStorageForOrigin(self, origin, cb=None):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Storage.trackCacheStorageForOrigin', params=msg_dict)


    def trackIndexedDBForOrigin(self, origin, cb=None):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Storage.trackIndexedDBForOrigin', params=msg_dict)


    def untrackCacheStorageForOrigin(self, origin, cb=None):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Storage.untrackCacheStorageForOrigin', params=msg_dict)


    def untrackIndexedDBForOrigin(self, origin, cb=None):
        """
        :param origin: Security origin.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Storage.untrackIndexedDBForOrigin', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

