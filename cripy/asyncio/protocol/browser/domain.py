from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.target import types as Target
from cripy.asyncio.protocol.browser import types as Types

__all__ = ["Browser"]


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """

    def __init__(self, chrome):
        """
        Construct a new Browser object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def close(self) -> Optional[dict]:
        """
        Close browser gracefully.
        """
        mayberes = await self.chrome.send('Browser.close')
        return mayberes

    async def getVersion(self) -> Optional[dict]:
        """
        Returns version information.
        """
        mayberes = await self.chrome.send('Browser.getVersion')
        res = await mayberes
        return res

    async def getBrowserCommandLine(self) -> Optional[dict]:
        """
        Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
        """
        mayberes = await self.chrome.send('Browser.getBrowserCommandLine')
        res = await mayberes
        return res

    async def getHistograms(self, query: Optional[str] = None) -> Optional[dict]:
        """
        Get Chrome histograms.

        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        mayberes = await self.chrome.send('Browser.getHistograms', msg_dict)
        res = await mayberes
        res['histograms'] = Types.Histogram.safe_create_from_list(res['histograms'])
        return res

    async def getHistogram(self, name: str) -> Optional[dict]:
        """
        Get a Chrome histogram by name.

        :param name: Requested histogram name.
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        mayberes = await self.chrome.send('Browser.getHistogram', msg_dict)
        res = await mayberes
        res['histogram'] = Types.Histogram.safe_create(res['histogram'])
        return res

    async def getWindowBounds(self, windowId: int) -> Optional[dict]:
        """
        Get position and size of the browser window.

        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        mayberes = await self.chrome.send('Browser.getWindowBounds', msg_dict)
        res = await mayberes
        res['bounds'] = Types.Bounds.safe_create(res['bounds'])
        return res

    async def getWindowForTarget(self, targetId: str) -> Optional[dict]:
        """
        Get the browser window that contains the devtools target.

        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Browser.getWindowForTarget', msg_dict)
        res = await mayberes
        res['bounds'] = Types.Bounds.safe_create(res['bounds'])
        return res

    async def setWindowBounds(self, windowId: int, bounds: dict) -> Optional[dict]:
        """
        Set position and/or size of the browser window.

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
        mayberes = await self.chrome.send('Browser.setWindowBounds', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

