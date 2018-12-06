"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Browser"]


@attr.dataclass(slots=True, cmp=False)
class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def grantPermissions(
        self,
        origin: str,
        permissions: List[str],
        browserContextId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Grant specific permissions to the given origin and reject all others.

        :param origin: The origin
        :type origin: str
        :param permissions: The permissions
        :type permissions: List[str]
        :param browserContextId: BrowserContext to override permissions. When omitted, default browser context is used.
        :type browserContextId: Optional[str]
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if permissions is not None:
            msg_dict["permissions"] = permissions
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        return self.client.send("Browser.grantPermissions", msg_dict)

    def resetPermissions(
        self, browserContextId: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Reset all permission management for all origins.

        :param browserContextId: BrowserContext to reset permissions. When omitted, default browser context is used.
        :type browserContextId: Optional[str]
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        return self.client.send("Browser.resetPermissions", msg_dict)

    def close(self) -> Awaitable[Dict]:
        """
        Close browser gracefully.
        """
        return self.client.send("Browser.close")

    def crash(self) -> Awaitable[Dict]:
        """
        Crashes browser on the main thread.
        """
        return self.client.send("Browser.crash")

    def getVersion(self) -> Awaitable[Dict]:
        """
        Returns version information.
        """
        return self.client.send("Browser.getVersion")

    def getBrowserCommandLine(self) -> Awaitable[Dict]:
        """
        Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
        """
        return self.client.send("Browser.getBrowserCommandLine")

    def getHistograms(
        self, query: Optional[str] = None, delta: Optional[bool] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("Browser.getHistograms", msg_dict)

    def getHistogram(self, name: str, delta: Optional[bool] = None) -> Awaitable[Dict]:
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
        return self.client.send("Browser.getHistogram", msg_dict)

    def getWindowBounds(self, windowId: int) -> Awaitable[Dict]:
        """
        Get position and size of the browser window.

        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict["windowId"] = windowId
        return self.client.send("Browser.getWindowBounds", msg_dict)

    def getWindowForTarget(self, targetId: Optional[str] = None) -> Awaitable[Dict]:
        """
        Get the browser window that contains the devtools target.

        :param targetId: Devtools agent host id. If called as a part of the session, associated targetId is used.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        return self.client.send("Browser.getWindowForTarget", msg_dict)

    def setWindowBounds(self, windowId: int, bounds: dict) -> Awaitable[Dict]:
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
        return self.client.send("Browser.setWindowBounds", msg_dict)

    def setDockTile(
        self, badgeLabel: Optional[str] = None, image: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Set dock tile details, platform-specific.

        :param badgeLabel: The badgeLabel
        :type badgeLabel: Optional[str]
        :param image: Png encoded image.
        :type image: Optional[str]
        """
        msg_dict = dict()
        if badgeLabel is not None:
            msg_dict["badgeLabel"] = badgeLabel
        if image is not None:
            msg_dict["image"] = image
        return self.client.send("Browser.setDockTile", msg_dict)
