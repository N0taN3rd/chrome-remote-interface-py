from cripy.sync.protocol.performance import events as Events
from cripy.sync.protocol.performance import types as Types

__all__ = ["Performance"] + Events.__all__ + Types.__all__ 


class Performance(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self, cb=None):
        self.chrome.send('Performance.disable')


    def enable(self, cb=None):
        self.chrome.send('Performance.enable')


    def getMetrics(self, cb=None):
        def cb_wrapper(res):
            res['metrics'] = Types.Metric.safe_create_from_list(res['metrics'])
            cb(res)
        self.chrome.send('Performance.getMetrics', cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

