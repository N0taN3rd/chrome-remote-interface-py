__all__ = ["Log"]


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ['Runtime', 'Network']

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

    def entryAdded(self, fn, once=False):
        """
        Issued when new message was logged.
        """
        self.chrome.on("Log.entryAdded", fn, once=once)


