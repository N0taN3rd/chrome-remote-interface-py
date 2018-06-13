from cripy.sync.protocol.target import types as Target
from cripy.sync.protocol.browser import types as Types

__all__ = ["Browser"]+ Types.__all__ 


class Browser(object):
    """
    The Browser domain defines methods and events for browser managing.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def close(self):
        self.chrome.send('Browser.close')


    def getVersion(self):
        def cb(res):
            self.chrome.emit('Browser.getVersion', res)
        self.chrome.send('Browser.getVersion', cb=cb)


    def getBrowserCommandLine(self):
        def cb(res):
            self.chrome.emit('Browser.getBrowserCommandLine', res)
        self.chrome.send('Browser.getBrowserCommandLine', cb=cb)


    def getHistograms(self, query):
        """
        :param query: Requested substring in name. Only histograms which have query as a substring in their name are extracted. An empty or absent query returns all histograms.
        :type query: Optional[str]
        """
        def cb(res):
            res['histograms'] = Types.Histogram.safe_create_from_list(res['histograms'])
            self.chrome.emit('Browser.getHistograms', res)
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        self.chrome.send('Browser.getHistograms', params=msg_dict, cb=cb)


    def getHistogram(self, name):
        """
        :param name: Requested histogram name.
        :type name: str
        """
        def cb(res):
            res['histogram'] = Types.Histogram.safe_create(res['histogram'])
            self.chrome.emit('Browser.getHistogram', res)
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('Browser.getHistogram', params=msg_dict, cb=cb)


    def getWindowBounds(self, windowId):
        """
        :param windowId: Browser window id.
        :type windowId: int
        """
        def cb(res):
            res['bounds'] = Types.Bounds.safe_create(res['bounds'])
            self.chrome.emit('Browser.getWindowBounds', res)
        msg_dict = dict()
        if windowId is not None:
            msg_dict['windowId'] = windowId
        self.chrome.send('Browser.getWindowBounds', params=msg_dict, cb=cb)


    def getWindowForTarget(self, targetId):
        """
        :param targetId: Devtools agent host id.
        :type targetId: str
        """
        def cb(res):
            res['bounds'] = Types.Bounds.safe_create(res['bounds'])
            self.chrome.emit('Browser.getWindowForTarget', res)
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        self.chrome.send('Browser.getWindowForTarget', params=msg_dict, cb=cb)


    def setWindowBounds(self, windowId, bounds):
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

