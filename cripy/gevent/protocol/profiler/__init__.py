from cripy.gevent.protocol.profiler import events as Events
from cripy.gevent.protocol.profiler import types as Types

__all__ = ["Profiler"] + Events.__all__ + Types.__all__


class Profiler(object):
    dependencies = ["Runtime", "Debugger"]

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Profiler.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Profiler.enable")
        return wres.get()

    def getBestEffortCoverage(self):
        wres = self.chrome.send("Profiler.getBestEffortCoverage")
        res = wres.get()
        res["result"] = Types.ScriptCoverage.safe_create_from_list(res["result"])
        return res

    def setSamplingInterval(self, interval):
        """
        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict["interval"] = interval
        wres = self.chrome.send("Profiler.setSamplingInterval", msg_dict)
        return wres.get()

    def start(self):
        wres = self.chrome.send("Profiler.start")
        return wres.get()

    def startPreciseCoverage(self, callCount=None, detailed=None):
        """
        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: Optional[bool]
        :param detailed: Collect block-based coverage.
        :type detailed: Optional[bool]
        """
        msg_dict = dict()
        if callCount is not None:
            msg_dict["callCount"] = callCount
        if detailed is not None:
            msg_dict["detailed"] = detailed
        wres = self.chrome.send("Profiler.startPreciseCoverage", msg_dict)
        return wres.get()

    def startTypeProfile(self):
        wres = self.chrome.send("Profiler.startTypeProfile")
        return wres.get()

    def stop(self):
        wres = self.chrome.send("Profiler.stop")
        res = wres.get()
        res["profile"] = Types.Profile.safe_create(res["profile"])
        return res

    def stopPreciseCoverage(self):
        wres = self.chrome.send("Profiler.stopPreciseCoverage")
        return wres.get()

    def stopTypeProfile(self):
        wres = self.chrome.send("Profiler.stopTypeProfile")
        return wres.get()

    def takePreciseCoverage(self):
        wres = self.chrome.send("Profiler.takePreciseCoverage")
        res = wres.get()
        res["result"] = Types.ScriptCoverage.safe_create_from_list(res["result"])
        return res

    def takeTypeProfile(self):
        wres = self.chrome.send("Profiler.takeTypeProfile")
        res = wres.get()
        res["result"] = Types.ScriptTypeProfile.safe_create_from_list(res["result"])
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
