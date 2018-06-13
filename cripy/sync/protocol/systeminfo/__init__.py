from cripy.sync.protocol.systeminfo import types as Types

__all__ = ["SystemInfo"]+ Types.__all__ 


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def getInfo(self, cb=None):
        def cb_wrapper(res):
            res['gpu'] = Types.GPUInfo.safe_create(res['gpu'])
            cb(res)
        self.chrome.send('SystemInfo.getInfo', cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return None

