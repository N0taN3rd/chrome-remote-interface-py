__all__ = ["Schema"]


class Schema(object):
    """
    This domain is deprecated.
    """

    def __init__(self, chrome):
        """
        Construct a new Schema object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def getDomains(self):
        """
        Returns supported domains.
        """
        wres = self.chrome.send('Schema.getDomains')
        return wres.get()


