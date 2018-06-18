from cripy.gevent.protocol.performance import events as Events
from cripy.gevent.protocol.performance import types as Types

__all__ = ["Performance"] + Events.__all__ + Types.__all__


class Performance(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Performance.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Performance.enable")
        return wres.get()

    def getMetrics(self):
        wres = self.chrome.send("Performance.getMetrics")
        res = wres.get()
        res["metrics"] = Types.Metric.safe_create_from_list(res["metrics"])
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
