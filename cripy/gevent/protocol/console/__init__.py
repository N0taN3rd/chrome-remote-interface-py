from cripy.gevent.protocol.console import events as Events
from cripy.gevent.protocol.console import types as Types

__all__ = ["Console"] + Events.__all__ + Types.__all__


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ["Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    def clearMessages(self):
        wres = self.chrome.send("Console.clearMessages")
        return wres.get()

    def disable(self):
        wres = self.chrome.send("Console.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Console.enable")
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
