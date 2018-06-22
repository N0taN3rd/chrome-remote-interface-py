from cripy.gevent.protocol.inspector import events as Events

__all__ = ["Inspector"]


class Inspector(object):
    events = Events.INSPECTOR_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Inspector object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables inspector domain notifications.
        """
        wres = self.chrome.send('Inspector.disable')
        return wres.get()

    def enable(self):
        """
        Enables inspector domain notifications.
        """
        wres = self.chrome.send('Inspector.enable')
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
        return Events.INSPECTOR_EVENTS_TO_CLASS

