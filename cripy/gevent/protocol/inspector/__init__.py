from cripy.gevent.protocol.inspector import events as Events

__all__ = ["Inspector"] + Events.__all__


class Inspector(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Inspector.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Inspector.enable")
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
