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

    def close(self):
        """
        Close browser gracefully.
        """
        wres = self.chrome.send('Browser.close')
        return wres.get()

    def getVersion(self):
        """
        Returns version information.
        """
        wres = self.chrome.send('Browser.getVersion')
        return wres.get()

    def getBrowserCommandLine(self):
        """
        Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
        """
        wres = self.chrome.send('Browser.getBrowserCommandLine')
        return wres.get()

    def getHistograms(self, query=None):
        """
        Get Chrome histograms.

        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        wres = self.chrome.send('Browser.getHistograms', msg_dict)
        return wres.get()

    def getHistogram(self, name):
        """
        Get a Chrome histogram by name.

        :param name: Requested histogram name.
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        wres = self.chrome.send('Browser.getHistogram', msg_dict)
        return wres.get()

    def getWindowBounds(self, windowId):
        """
        Get position and size of the browser window.

        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        wres = self.chrome.send('Browser.getWindowBounds', msg_dict)
        return wres.get()

    def getWindowForTarget(self, targetId):
        """
        Get the browser window that contains the devtools target.

        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Browser.getWindowForTarget', msg_dict)
        return wres.get()

    def setWindowBounds(self, windowId, bounds):
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
        wres = self.chrome.send('Browser.setWindowBounds', msg_dict)
        return wres.get()


