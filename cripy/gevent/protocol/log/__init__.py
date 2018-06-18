from cripy.gevent.protocol.log import events as Events
from cripy.gevent.protocol.log import types as Types

__all__ = ["Log"] + Events.__all__ + Types.__all__


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ["Runtime", "Network"]

    def __init__(self, chrome):
        self.chrome = chrome

    def clear(self):
        wres = self.chrome.send("Log.clear")
        return wres.get()

    def disable(self):
        wres = self.chrome.send("Log.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Log.enable")
        return wres.get()

    def startViolationsReport(self, config):
        """
        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict["config"] = config
        wres = self.chrome.send("Log.startViolationsReport", msg_dict)
        return wres.get()

    def stopViolationsReport(self):
        wres = self.chrome.send("Log.stopViolationsReport")
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
