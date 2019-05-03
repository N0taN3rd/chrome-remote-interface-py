"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Browser"]


class Browser:
    """
    The Browser domain defines methods and events for browser managing.
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Browser`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Browser

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def grantPermissions(
        self,
        origin: str,
        permissions: List[str],
        browserContextId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Grant specific permissions to the given origin and reject all others.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-grantPermissions`

        :param origin: The origin
        :param permissions: The permissions
        :param browserContextId: BrowserContext to override permissions. When omitted, default browser context is used.
        :return: The results of the command
        """
        msg = {"origin": origin, "permissions": permissions}
        if browserContextId is not None:
            msg["browserContextId"] = browserContextId
        return self.client.send("Browser.grantPermissions", msg)

    def resetPermissions(
        self, browserContextId: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Reset all permission management for all origins.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-resetPermissions`

        :param browserContextId: BrowserContext to reset permissions. When omitted, default browser context is used.
        :return: The results of the command
        """
        msg = {}
        if browserContextId is not None:
            msg["browserContextId"] = browserContextId
        return self.client.send("Browser.resetPermissions", msg)

    def close(self) -> Awaitable[Dict]:
        """
        Close browser gracefully.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-close`

        :return: The results of the command
        """
        return self.client.send("Browser.close", {})

    def crash(self) -> Awaitable[Dict]:
        """
        Crashes browser on the main thread.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-crash`

        :return: The results of the command
        """
        return self.client.send("Browser.crash", {})

    def crashGpuProcess(self) -> Awaitable[Dict]:
        """
        Crashes GPU process.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-crashGpuProcess`

        :return: The results of the command
        """
        return self.client.send("Browser.crashGpuProcess", {})

    def getVersion(self) -> Awaitable[Dict]:
        """
        Returns version information.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getVersion`

        :return: The results of the command
        """
        return self.client.send("Browser.getVersion", {})

    def getBrowserCommandLine(self) -> Awaitable[Dict]:
        """
        Returns the command line switches for the browser process if, and only if
        --enable-automation is on the commandline.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getBrowserCommandLine`

        :return: The results of the command
        """
        return self.client.send("Browser.getBrowserCommandLine", {})

    def getHistograms(
        self, query: Optional[str] = None, delta: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Get Chrome histograms.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getHistograms`

        :param query: Requested substring in name. Only histograms which have query as a
         substring in their name are extracted. An empty or absent query returns
         all histograms.
        :param delta: If true, retrieve delta since last call.
        :return: The results of the command
        """
        msg = {}
        if query is not None:
            msg["query"] = query
        if delta is not None:
            msg["delta"] = delta
        return self.client.send("Browser.getHistograms", msg)

    def getHistogram(self, name: str, delta: Optional[bool] = None) -> Awaitable[Dict]:
        """
        Get a Chrome histogram by name.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getHistogram`

        :param name: Requested histogram name.
        :param delta: If true, retrieve delta since last call.
        :return: The results of the command
        """
        msg = {"name": name}
        if delta is not None:
            msg["delta"] = delta
        return self.client.send("Browser.getHistogram", msg)

    def getWindowBounds(self, windowId: int) -> Awaitable[Dict]:
        """
        Get position and size of the browser window.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getWindowBounds`

        :param windowId: Browser window id.
        :return: The results of the command
        """
        return self.client.send("Browser.getWindowBounds", {"windowId": windowId})

    def getWindowForTarget(self, targetId: Optional[str] = None) -> Awaitable[Dict]:
        """
        Get the browser window that contains the devtools target.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-getWindowForTarget`

        :param targetId: Devtools agent host id. If called as a part of the session, associated targetId is used.
        :return: The results of the command
        """
        msg = {}
        if targetId is not None:
            msg["targetId"] = targetId
        return self.client.send("Browser.getWindowForTarget", msg)

    def setWindowBounds(self, windowId: int, bounds: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Set position and/or size of the browser window.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-setWindowBounds`

        :param windowId: Browser window id.
        :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
         with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        :return: The results of the command
        """
        return self.client.send(
            "Browser.setWindowBounds", {"windowId": windowId, "bounds": bounds}
        )

    def setDockTile(
        self, badgeLabel: Optional[str] = None, image: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Set dock tile details, platform-specific.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Browser#method-setDockTile`

        :param badgeLabel: The badgeLabel
        :param image: Png encoded image.
        :return: The results of the command
        """
        msg = {}
        if badgeLabel is not None:
            msg["badgeLabel"] = badgeLabel
        if image is not None:
            msg["image"] = image
        return self.client.send("Browser.setDockTile", msg)
