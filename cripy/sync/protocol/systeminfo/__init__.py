from cripy.sync.protocol.systeminfo import types as Types

__all__ = ["SystemInfo"]+ Types.__all__ 


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def getInfo(self):
        def cb(res):
            res['gpu'] = Types.GPUInfo.safe_create(res['gpu'])
            self.chrome.emit('SystemInfo.getInfo', res)
        self.chrome.send('SystemInfo.getInfo', cb=cb)


    @staticmethod
    def get_event_classes():
        return None

