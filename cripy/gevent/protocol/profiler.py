__all__ = ["Profiler"]


class Profiler(object):
    dependencies = ['Runtime', 'Debugger']

    def __init__(self, chrome):
        """
        Construct a new Profiler object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send('Profiler.disable')
        return wres.get()

    def enable(self):
        wres = self.chrome.send('Profiler.enable')
        return wres.get()

    def getBestEffortCoverage(self):
        """
        Collect coverage data for the current isolate. The coverage data may be incomplete due to
garbage collection.
        """
        wres = self.chrome.send('Profiler.getBestEffortCoverage')
        return wres.get()

    def setSamplingInterval(self, interval):
        """
        Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict['interval'] = interval
        wres = self.chrome.send('Profiler.setSamplingInterval', msg_dict)
        return wres.get()

    def start(self):
        wres = self.chrome.send('Profiler.start')
        return wres.get()

    def startPreciseCoverage(self, callCount=None, detailed=None):
        """
        Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
coverage may be incomplete. Enabling prevents running optimized code and resets execution
counters.

        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: Optional[bool]
        :param detailed: Collect block-based coverage.
        :type detailed: Optional[bool]
        """
        msg_dict = dict()
        if callCount is not None:
            msg_dict['callCount'] = callCount
        if detailed is not None:
            msg_dict['detailed'] = detailed
        wres = self.chrome.send('Profiler.startPreciseCoverage', msg_dict)
        return wres.get()

    def startTypeProfile(self):
        """
        Enable type profile.
        """
        wres = self.chrome.send('Profiler.startTypeProfile')
        return wres.get()

    def stop(self):
        wres = self.chrome.send('Profiler.stop')
        return wres.get()

    def stopPreciseCoverage(self):
        """
        Disable precise code coverage. Disabling releases unnecessary execution count records and allows
executing optimized code.
        """
        wres = self.chrome.send('Profiler.stopPreciseCoverage')
        return wres.get()

    def stopTypeProfile(self):
        """
        Disable type profile. Disabling releases type profile data collected so far.
        """
        wres = self.chrome.send('Profiler.stopTypeProfile')
        return wres.get()

    def takePreciseCoverage(self):
        """
        Collect coverage data for the current isolate, and resets execution counters. Precise code
coverage needs to have started.
        """
        wres = self.chrome.send('Profiler.takePreciseCoverage')
        return wres.get()

    def takeTypeProfile(self):
        """
        Collect type profile.
        """
        wres = self.chrome.send('Profiler.takeTypeProfile')
        return wres.get()

    def consoleProfileFinished(self, fn, once=False):
        self.chrome.on("Profiler.consoleProfileFinished", fn, once=once)

    def consoleProfileStarted(self, fn, once=False):
        """
        Sent when new profile recording is started using console.profile() call.
        """
        self.chrome.on("Profiler.consoleProfileStarted", fn, once=once)


