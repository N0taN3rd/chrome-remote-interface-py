__all__ = ["Console"]


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ['Runtime']

    def __init__(self, chrome):
        """
        Construct a new Console object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clearMessages(self):
        """
        Does nothing.
        """
        wres = self.chrome.send('Console.clearMessages')
        return wres.get()

    def disable(self):
        """
        Disables console domain, prevents further console messages from being reported to the client.
        """
        wres = self.chrome.send('Console.disable')
        return wres.get()

    def enable(self):
        """
        Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        wres = self.chrome.send('Console.enable')
        return wres.get()

    def messageAdded(self, fn, once=False):
        """
        Issued when new console message is added.
        """
        self.chrome.on("Console.messageAdded", fn, once=once)


