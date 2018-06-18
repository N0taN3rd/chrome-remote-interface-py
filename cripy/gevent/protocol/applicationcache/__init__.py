from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.applicationcache import events as Events
from cripy.gevent.protocol.applicationcache import types as Types

__all__ = ["ApplicationCache"] + Events.__all__ + Types.__all__


class ApplicationCache(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def enable(self):
        wres = self.chrome.send("ApplicationCache.enable")
        return wres.get()

    def getApplicationCacheForFrame(self, frameId):
        """
        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        wres = self.chrome.send(
            "ApplicationCache.getApplicationCacheForFrame", msg_dict
        )
        res = wres.get()
        res["applicationCache"] = Types.ApplicationCache.safe_create(
            res["applicationCache"]
        )
        return res

    def getFramesWithManifests(self):
        wres = self.chrome.send("ApplicationCache.getFramesWithManifests")
        res = wres.get()
        res["frameIds"] = Types.FrameWithManifest.safe_create_from_list(res["frameIds"])
        return res

    def getManifestForFrame(self, frameId):
        """
        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        wres = self.chrome.send("ApplicationCache.getManifestForFrame", msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
