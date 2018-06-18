from types import SimpleNamespace

try:
    from cripy.gevent.protocol.performance.types import *
except ImportError:
    pass

__all__ = ["MetricsEvent"]


class MetricsEvent(object):
    """
    Current values of the metrics.
    """

    event = "Performance.metrics"

    def __init__(self, metrics, title):
        """
        :param metrics: Current values of the metrics.
        :type metrics: List[dict]
        :param title: Timestamp title.
        :type title: str
        """
        super().__init__()
        self.metrics = metrics
        self.title = title

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.metrics is not None:
            repr_args.append("metrics={!r}".format(self.metrics))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        return "MetricsEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = MetricsEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MetricsEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {"Performance.metrics": MetricsEvent}

EVENT_NS = SimpleNamespace(Metrics="Performance.metrics")
