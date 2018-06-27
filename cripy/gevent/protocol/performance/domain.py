from cripy.gevent.protocol.performance import events as Events
from cripy.gevent.protocol.performance import types as Types

__all__ = ["Performance"]


class Performance(object):
    events = Events.PERFORMANCE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Performance object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disable collecting and reporting metrics.
        """
        wres = self.chrome.send('Performance.disable')
        return wres.get()

    def enable(self):
        """
        Enable collecting and reporting metrics.
        """
        wres = self.chrome.send('Performance.enable')
        return wres.get()

    def getMetrics(self):
        """
        Retrieve current values of run-time metrics.
        """
        wres = self.chrome.send('Performance.getMetrics')
        res = wres.get()
        res['metrics'] = Types.Metric.safe_create_from_list(res['metrics'])
        return res

    def metrics(self, fn, once=False):
        self.chrome.on("Performance.metrics", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.PERFORMANCE_EVENTS_TO_CLASS

