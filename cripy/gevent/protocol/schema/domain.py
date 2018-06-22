from cripy.gevent.protocol.schema import types as Types

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
        res = wres.get()
        res['domains'] = Types.Domain.safe_create_from_list(res['domains'])
        return res

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

