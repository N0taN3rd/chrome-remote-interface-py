from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.applicationcache import events as Events
from cripy.gevent.protocol.applicationcache import types as Types

__all__ = ["ApplicationCache"]


class ApplicationCache(object):
    events = Events.APPLICATIONCACHE_EVENTS_NS

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
        res = wres.get()
        res['applicationCache'] = Types.ApplicationCache.safe_create(res['applicationCache'])
        return res

    def getFramesWithManifests(self):
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
        """
        wres = self.chrome.send('ApplicationCache.getFramesWithManifests')
        res = wres.get()
        res['frameIds'] = Types.FrameWithManifest.safe_create_from_list(res['frameIds'])
        return res

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
        res = wres.get()
        return res

    def applicationCacheStatusUpdated(self, fn, once=False):
        self.chrome.on("ApplicationCache.applicationCacheStatusUpdated", fn, once=once)

    def networkStateUpdated(self, fn, once=False):
        self.chrome.on("ApplicationCache.networkStateUpdated", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.APPLICATIONCACHE_EVENTS_TO_CLASS

