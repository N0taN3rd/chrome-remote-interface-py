from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.applicationcache import events as Events
from cripy.asyncio.protocol.applicationcache import types as Types

__all__ = ["ApplicationCache"]


class ApplicationCache(object):
    events = Events.APPLICATIONCACHE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new ApplicationCache object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def enable(self) -> Optional[dict]:
        """
        Enables application cache domain notifications.
        """
        res = await self.chrome.send('ApplicationCache.enable')
        return res

    async def getApplicationCacheForFrame(self, frameId: str) -> Optional[dict]:
        """
        Returns relevant application cache data for the document in given frame.

        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        res = await self.chrome.send('ApplicationCache.getApplicationCacheForFrame', msg_dict)
        res['applicationCache'] = Types.ApplicationCache.safe_create(res['applicationCache'])
        return res

    async def getFramesWithManifests(self) -> Optional[dict]:
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
        """
        res = await self.chrome.send('ApplicationCache.getFramesWithManifests')
        res['frameIds'] = Types.FrameWithManifest.safe_create_from_list(res['frameIds'])
        return res

    async def getManifestForFrame(self, frameId: str) -> Optional[dict]:
        """
        Returns manifest URL for document in the given frame.

        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        res = await self.chrome.send('ApplicationCache.getManifestForFrame', msg_dict)
        return res

    def applicationCacheStatusUpdated(self, fn, once=False):
        if once:
            self.chrome.once("ApplicationCache.applicationCacheStatusUpdated", fn)
        else:
            self.chrome.on("ApplicationCache.applicationCacheStatusUpdated", fn)

    def networkStateUpdated(self, fn, once=False):
        if once:
            self.chrome.once("ApplicationCache.networkStateUpdated", fn)
        else:
            self.chrome.on("ApplicationCache.networkStateUpdated", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.APPLICATIONCACHE_EVENTS_TO_CLASS

