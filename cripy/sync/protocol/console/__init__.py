from cripy.sync.protocol.console import events as Events
from cripy.sync.protocol.console import types as Types

__all__ = ["Console"] + Events.__all__ + Types.__all__ 


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ['Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def clearMessages(self, cb=None):
        self.chrome.send('Console.clearMessages')


    def disable(self, cb=None):
        self.chrome.send('Console.disable')


    def enable(self, cb=None):
        self.chrome.send('Console.enable')


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

