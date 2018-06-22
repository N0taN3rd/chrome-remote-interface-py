from cripy.gevent.protocol.log import events as Events
from cripy.gevent.protocol.log import types as Types

__all__ = ["Log"]


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ['Runtime', 'Network']

    events = Events.LOG_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Log object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clear(self):
        """
        Clears the log.
        """
        wres = self.chrome.send('Log.clear')
        return wres.get()

    def disable(self):
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        wres = self.chrome.send('Log.disable')
        return wres.get()

    def enable(self):
        """
        Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
        """
        wres = self.chrome.send('Log.enable')
        return wres.get()

    def startViolationsReport(self, config):
        """
        start violation reporting.

        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict['config'] = config
        wres = self.chrome.send('Log.startViolationsReport', msg_dict)
        return wres.get()

    def stopViolationsReport(self):
        """
        Stop violation reporting.
        """
        wres = self.chrome.send('Log.stopViolationsReport')
        return wres.get()

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.LOG_EVENTS_TO_CLASS

