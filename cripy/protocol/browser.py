# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Browser"]


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def close(self) -> Optional[dict]:
        """
        Close browser gracefully.
        """
        res = await self.client.send("Browser.close")
        return res

    async def getVersion(self) -> Optional[dict]:
        """
        Returns version information.
        """
        res = await self.client.send("Browser.getVersion")
        return res

    async def getBrowserCommandLine(self) -> Optional[dict]:
        """
        Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
        """
        res = await self.client.send("Browser.getBrowserCommandLine")
        return res

    async def getHistograms(
        self, query: Optional[str] = None, delta: Optional[bool] = None
    ) -> Optional[dict]:
        """
        Get Chrome histograms.

        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        :param delta: If true, retrieve delta since last call.
        :type delta: Optional[bool]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict["query"] = query
        if delta is not None:
            msg_dict["delta"] = delta
        res = await self.client.send("Browser.getHistograms", msg_dict)
        return res

    async def getHistogram(
        self, name: str, delta: Optional[bool] = None
    ) -> Optional[dict]:
        """
        Get a Chrome histogram by name.

        :param name: Requested histogram name.
        :type name: str
        :param delta: If true, retrieve delta since last call.
        :type delta: Optional[bool]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        if delta is not None:
            msg_dict["delta"] = delta
        res = await self.client.send("Browser.getHistogram", msg_dict)
        return res

    async def getWindowBounds(self, windowId: int) -> Optional[dict]:
        """
        Get position and size of the browser window.

        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict["windowId"] = windowId
        res = await self.client.send("Browser.getWindowBounds", msg_dict)
        return res

    async def getWindowForTarget(self, targetId: str) -> Optional[dict]:
        """
        Get the browser window that contains the devtools target.

        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        res = await self.client.send("Browser.getWindowForTarget", msg_dict)
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
            msg_dict["windowId"] = windowId
        if bounds is not None:
            msg_dict["bounds"] = bounds
        res = await self.client.send("Browser.setWindowBounds", msg_dict)
        return res

    def __repr__(self):
        return f"Browser()"
