from cripy.sync.protocol.target import types as Target
from cripy.sync.protocol.browser import types as Types

__all__ = ["Browser"]+ Types.__all__ 


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def close(self, cb=None):
        self.chrome.send('Browser.close')


    def getVersion(self, cb=None):
        def cb_wrapper(res):
            cb(res)
        self.chrome.send('Browser.getVersion', cb=cb_wrapper)


    def getBrowserCommandLine(self, cb=None):
        def cb_wrapper(res):
            cb(res)
        self.chrome.send('Browser.getBrowserCommandLine', cb=cb_wrapper)


    def getHistograms(self, query, cb=None):
        """
        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        def cb_wrapper(res):
            res['histograms'] = Types.Histogram.safe_create_from_list(res['histograms'])
            cb(res)
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        self.chrome.send('Browser.getHistograms', params=msg_dict, cb=cb_wrapper)


    def getHistogram(self, name, cb=None):
        """
        :param name: Requested histogram name.
        :type name: str
        """
        def cb_wrapper(res):
            res['histogram'] = Types.Histogram.safe_create(res['histogram'])
            cb(res)
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('Browser.getHistogram', params=msg_dict, cb=cb_wrapper)


    def getWindowBounds(self, windowId, cb=None):
        """
        :param windowId: Browser window id.
        :type windowId: int
        """
        def cb_wrapper(res):
            res['bounds'] = Types.Bounds.safe_create(res['bounds'])
            cb(res)
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        self.chrome.send('Browser.getWindowBounds', params=msg_dict, cb=cb_wrapper)


    def getWindowForTarget(self, targetId, cb=None):
        """
        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        def cb_wrapper(res):
            res['bounds'] = Types.Bounds.safe_create(res['bounds'])
            cb(res)
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        self.chrome.send('Browser.getWindowForTarget', params=msg_dict, cb=cb_wrapper)


    def setWindowBounds(self, windowId, bounds, cb=None):
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
        self.chrome.send('Browser.setWindowBounds', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return None

