__all__ = ["SystemInfo"]


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    def __init__(self, chrome):
        """
        Construct a new SystemInfo object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def getInfo(self):
        """
        Returns information about the system.
        """
        wres = self.chrome.send('SystemInfo.getInfo')
        return wres.get()


