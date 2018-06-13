from cripy.sync.protocol.cachestorage import types as Types

__all__ = ["CacheStorage"]+ Types.__all__ 


class CacheStorage(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def deleteCache(self, cacheId):
        """
        :param cacheId: Id of cache for deletion.
        :type cacheId: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict['cacheId'] = cacheId
        self.chrome.send('CacheStorage.deleteCache', params=msg_dict)


    def deleteEntry(self, cacheId, request):
        """
        :param cacheId: Id of cache where the entry will be deleted.
        :type cacheId: str
        :param request: URL spec of the request.
        :type request: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict['cacheId'] = cacheId
        if request is not None:
            msg_dict['request'] = request
        self.chrome.send('CacheStorage.deleteEntry', params=msg_dict)


    def requestCacheNames(self, securityOrigin):
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        def cb(res):
            res['caches'] = Types.Cache.safe_create_from_list(res['caches'])
            self.chrome.emit('CacheStorage.requestCacheNames', res)
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        self.chrome.send('CacheStorage.requestCacheNames', params=msg_dict, cb=cb)


    def requestCachedResponse(self, cacheId, requestURL):
        """
        :param cacheId: Id of cache that contains the enty.
        :type cacheId: str
        :param requestURL: URL spec of the request.
        :type requestURL: str
        """
        def cb(res):
            res['response'] = Types.CachedResponse.safe_create(res['response'])
            self.chrome.emit('CacheStorage.requestCachedResponse', res)
        msg_dict = dict()
        if cacheId is not None:
            msg_dict['cacheId'] = cacheId
        if requestURL is not None:
            msg_dict['requestURL'] = requestURL
        self.chrome.send('CacheStorage.requestCachedResponse', params=msg_dict, cb=cb)


    def requestEntries(self, cacheId, skipCount, pageSize):
        """
        :param cacheId: ID of cache to get entries from.
        :type cacheId: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        """
        def cb(res):
            res['cacheDataEntries'] = Types.DataEntry.safe_create_from_list(res['cacheDataEntries'])
            self.chrome.emit('CacheStorage.requestEntries', res)
        msg_dict = dict()
        if cacheId is not None:
            msg_dict['cacheId'] = cacheId
        if skipCount is not None:
            msg_dict['skipCount'] = skipCount
        if pageSize is not None:
            msg_dict['pageSize'] = pageSize
        self.chrome.send('CacheStorage.requestEntries', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return None

