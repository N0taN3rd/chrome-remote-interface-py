from cripy.gevent.protocol.target import types as Target
from cripy.gevent.protocol.browser import types as Types

__all__ = ["Browser"] + Types.__all__


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def close(self):
        wres = self.chrome.send("Browser.close")
        return wres.get()

    def getVersion(self):
        wres = self.chrome.send("Browser.getVersion")
        res = wres.get()
        return res

    def getBrowserCommandLine(self):
        wres = self.chrome.send("Browser.getBrowserCommandLine")
        res = wres.get()
        return res

    def getHistograms(self, query=None):
        """
        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict["query"] = query
        wres = self.chrome.send("Browser.getHistograms", msg_dict)
        res = wres.get()
        res["histograms"] = Types.Histogram.safe_create_from_list(res["histograms"])
        return res

    def getHistogram(self, name):
        """
        :param name: Requested histogram name.
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        wres = self.chrome.send("Browser.getHistogram", msg_dict)
        res = wres.get()
        res["histogram"] = Types.Histogram.safe_create(res["histogram"])
        return res

    def getWindowBounds(self, windowId):
        """
        :param windowId: Browser window id.
        :type windowId: int
        """
        msg_dict = dict()
        if windowId is not None:
            msg_dict["windowId"] = windowId
        wres = self.chrome.send("Browser.getWindowBounds", msg_dict)
        res = wres.get()
        res["bounds"] = Types.Bounds.safe_create(res["bounds"])
        return res

    def getWindowForTarget(self, targetId):
        """
        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        wres = self.chrome.send("Browser.getWindowForTarget", msg_dict)
        res = wres.get()
        res["bounds"] = Types.Bounds.safe_create(res["bounds"])
        return res

    def setWindowBounds(self, windowId, bounds):
        """
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
        wres = self.chrome.send("Browser.setWindowBounds", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return None
