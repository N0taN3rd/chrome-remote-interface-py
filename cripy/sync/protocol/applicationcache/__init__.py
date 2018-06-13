from cripy.sync.protocol.page import types as Page
from cripy.sync.protocol.applicationcache import events as Events
from cripy.sync.protocol.applicationcache import types as Types

__all__ = ["ApplicationCache"] + Events.__all__ + Types.__all__ 


class ApplicationCache(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def enable(self):
        self.chrome.send('ApplicationCache.enable')


    def getApplicationCacheForFrame(self, frameId):
        """
        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        def cb(res):
            res['applicationCache'] = Types.ApplicationCache.safe_create(res['applicationCache'])
            self.chrome.emit('ApplicationCache.getApplicationCacheForFrame', res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('ApplicationCache.getApplicationCacheForFrame', params=msg_dict, cb=cb)


    def getFramesWithManifests(self):
        def cb(res):
            res['frameIds'] = Types.FrameWithManifest.safe_create_from_list(res['frameIds'])
            self.chrome.emit('ApplicationCache.getFramesWithManifests', res)
        self.chrome.send('ApplicationCache.getFramesWithManifests', cb=cb)


    def getManifestForFrame(self, frameId):
        """
        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        def cb(res):
            self.chrome.emit('ApplicationCache.getManifestForFrame', res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('ApplicationCache.getManifestForFrame', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

