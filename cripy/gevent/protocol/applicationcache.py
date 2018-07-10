__all__ = ["ApplicationCache"]


class ApplicationCache(object):
    def __init__(self, chrome):
        """
        Construct a new ApplicationCache object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def enable(self):
        """
        Enables application cache domain notifications.
        """
        wres = self.chrome.send('ApplicationCache.enable')
        return wres.get()

    def getApplicationCacheForFrame(self, frameId):
        """
        Returns relevant application cache data for the document in given frame.

        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        wres = self.chrome.send('ApplicationCache.getApplicationCacheForFrame', msg_dict)
        return wres.get()

    def getFramesWithManifests(self):
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
        """
        wres = self.chrome.send('ApplicationCache.getFramesWithManifests')
        return wres.get()

    def getManifestForFrame(self, frameId):
        """
        Returns manifest URL for document in the given frame.

        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        wres = self.chrome.send('ApplicationCache.getManifestForFrame', msg_dict)
        return wres.get()

    def applicationCacheStatusUpdated(self, fn, once=False):
        self.chrome.on("ApplicationCache.applicationCacheStatusUpdated", fn, once=once)

    def networkStateUpdated(self, fn, once=False):
        self.chrome.on("ApplicationCache.networkStateUpdated", fn, once=once)


