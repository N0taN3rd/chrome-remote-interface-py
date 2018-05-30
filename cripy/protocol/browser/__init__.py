from typing import Any, List, Optional, Union
from cripy.protocol.target import types as Target
from cripy.protocol.browser import types as Types


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    async def close(self) -> Optional[dict]:
        res = await self.chrome.send('Browser.close')
        return res

    async def getVersion(self) -> Optional[dict]:
        res = await self.chrome.send('Browser.getVersion')
        return res

    async def getBrowserCommandLine(self) -> Optional[dict]:
        res = await self.chrome.send('Browser.getBrowserCommandLine')
        return res

    async def getHistograms(self, query: Optional[str] = None) -> Optional[dict]:
        """
        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        res = await self.chrome.send('Browser.getHistograms', msg_dict)
        res['histograms'] = Types.Histogram.safe_create_from_list(res['histograms'])
        return res

    async def getHistogram(self, name: str) -> Optional[dict]:
        """
        :param name: Requested histogram name.
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        res = await self.chrome.send('Browser.getHistogram', msg_dict)
        res['histogram'] = Types.Histogram.safe_create(res['histogram'])
        return res

    async def getWindowBounds(self, windowId: int) -> Optional[dict]:
        """
        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        res = await self.chrome.send('Browser.getWindowBounds', msg_dict)
        res['bounds'] = Types.Bounds.safe_create(res['bounds'])
        return res

    async def getWindowForTarget(self, targetId: str) -> Optional[dict]:
        """
        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        res = await self.chrome.send('Browser.getWindowForTarget', msg_dict)
        res['bounds'] = Types.Bounds.safe_create(res['bounds'])
        return res

    async def setWindowBounds(self, windowId: int, bounds: dict) -> Optional[dict]:
        """
        :param windowId: Browser window id.
        :type windowId: int
        :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        :type bounds: dict
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        if bounds is not None:
            msg_dict['bounds'] = bounds
        res = await self.chrome.send('Browser.setWindowBounds', msg_dict)
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None

