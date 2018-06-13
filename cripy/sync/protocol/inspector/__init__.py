from cripy.sync.protocol.inspector import events as Events

__all__ = ["Inspector"] + Events.__all__ 


class Inspector(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('Inspector.disable')


    def enable(self):
        self.chrome.send('Inspector.enable')


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

