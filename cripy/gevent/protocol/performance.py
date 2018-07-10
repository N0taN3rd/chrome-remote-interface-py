__all__ = ["Performance"]


class Performance(object):
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
        return wres.get()

    def metrics(self, fn, once=False):
        """
        Current values of the metrics.
        """
        self.chrome.on("Performance.metrics", fn, once=once)


