from cripy.sync.protocol.performance import events as Events
from cripy.sync.protocol.performance import types as Types

__all__ = ["Performance"] + Events.__all__ + Types.__all__ 


class Performance(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('Performance.disable')


    def enable(self):
        self.chrome.send('Performance.enable')


    def getMetrics(self):
        def cb(res):
            res['metrics'] = Types.Metric.safe_create_from_list(res['metrics'])
            self.chrome.emit('Performance.getMetrics', res)
        self.chrome.send('Performance.getMetrics', cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

