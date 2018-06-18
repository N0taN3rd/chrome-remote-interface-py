from cripy.gevent.protocol.cachestorage import types as Types

__all__ = ["CacheStorage"] + Types.__all__


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
            msg_dict["cacheId"] = cacheId
        wres = self.chrome.send("CacheStorage.deleteCache", msg_dict)
        return wres.get()

    def deleteEntry(self, cacheId, request):
        """
        :param cacheId: Id of cache where the entry will be deleted.
        :type cacheId: str
        :param request: URL spec of the request.
        :type request: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if request is not None:
            msg_dict["request"] = request
        wres = self.chrome.send("CacheStorage.deleteEntry", msg_dict)
        return wres.get()

    def requestCacheNames(self, securityOrigin):
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        wres = self.chrome.send("CacheStorage.requestCacheNames", msg_dict)
        res = wres.get()
        res["caches"] = Types.Cache.safe_create_from_list(res["caches"])
        return res

    def requestCachedResponse(self, cacheId, requestURL):
        """
        :param cacheId: Id of cache that contains the enty.
        :type cacheId: str
        :param requestURL: URL spec of the request.
        :type requestURL: str
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if requestURL is not None:
            msg_dict["requestURL"] = requestURL
        wres = self.chrome.send("CacheStorage.requestCachedResponse", msg_dict)
        res = wres.get()
        res["response"] = Types.CachedResponse.safe_create(res["response"])
        return res

    def requestEntries(self, cacheId, skipCount, pageSize):
        """
        :param cacheId: ID of cache to get entries from.
        :type cacheId: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        """
        msg_dict = dict()
        if cacheId is not None:
            msg_dict["cacheId"] = cacheId
        if skipCount is not None:
            msg_dict["skipCount"] = skipCount
        if pageSize is not None:
            msg_dict["pageSize"] = pageSize
        wres = self.chrome.send("CacheStorage.requestEntries", msg_dict)
        res = wres.get()
        res["cacheDataEntries"] = Types.DataEntry.safe_create_from_list(
            res["cacheDataEntries"]
        )
        return res

    @staticmethod
    def get_event_classes():
        return None
