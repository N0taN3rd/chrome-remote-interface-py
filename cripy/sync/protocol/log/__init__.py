from cripy.sync.protocol.log import events as Events
from cripy.sync.protocol.log import types as Types

__all__ = ["Log"] + Events.__all__ + Types.__all__ 


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ['Runtime', 'Network']

    def __init__(self, chrome):
        self.chrome = chrome

    def clear(self, cb=None):
        self.chrome.send('Log.clear')


    def disable(self, cb=None):
        self.chrome.send('Log.disable')


    def enable(self, cb=None):
        self.chrome.send('Log.enable')


    def startViolationsReport(self, config, cb=None):
        """
        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict['config'] = config
        self.chrome.send('Log.startViolationsReport', params=msg_dict)


    def stopViolationsReport(self, cb=None):
        self.chrome.send('Log.stopViolationsReport')


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

