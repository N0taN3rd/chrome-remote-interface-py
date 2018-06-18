from cripy.gevent.protocol.systeminfo import types as Types

__all__ = ["SystemInfo"] + Types.__all__


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def getInfo(self):
        wres = self.chrome.send("SystemInfo.getInfo")
        res = wres.get()
        res["gpu"] = Types.GPUInfo.safe_create(res["gpu"])
        return res

    @staticmethod
    def get_event_classes():
        return None
