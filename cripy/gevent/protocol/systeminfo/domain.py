from cripy.gevent.protocol.systeminfo import types as Types

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
        res = wres.get()
        res['gpu'] = Types.GPUInfo.safe_create(res['gpu'])
        return res

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

