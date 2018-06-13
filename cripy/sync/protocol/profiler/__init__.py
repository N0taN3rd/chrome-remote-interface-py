from cripy.sync.protocol.profiler import events as Events
from cripy.sync.protocol.profiler import types as Types

__all__ = ["Profiler"] + Events.__all__ + Types.__all__ 


class Profiler(object):
    dependencies = ['Runtime', 'Debugger']

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self, cb=None):
        self.chrome.send('Profiler.disable')


    def enable(self, cb=None):
        self.chrome.send('Profiler.enable')


    def getBestEffortCoverage(self, cb=None):
        def cb_wrapper(res):
            res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
            cb(res)
        self.chrome.send('Profiler.getBestEffortCoverage', cb=cb_wrapper)


    def setSamplingInterval(self, interval, cb=None):
        """
        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict['interval'] = interval
        self.chrome.send('Profiler.setSamplingInterval', params=msg_dict)


    def start(self, cb=None):
        self.chrome.send('Profiler.start')


    def startPreciseCoverage(self, callCount, detailed, cb=None):
        """
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
        self.chrome.send('Profiler.startPreciseCoverage', params=msg_dict)


    def startTypeProfile(self, cb=None):
        self.chrome.send('Profiler.startTypeProfile')


    def stop(self, cb=None):
        def cb_wrapper(res):
            res['profile'] = Types.Profile.safe_create(res['profile'])
            cb(res)
        self.chrome.send('Profiler.stop', cb=cb_wrapper)


    def stopPreciseCoverage(self, cb=None):
        self.chrome.send('Profiler.stopPreciseCoverage')


    def stopTypeProfile(self, cb=None):
        self.chrome.send('Profiler.stopTypeProfile')


    def takePreciseCoverage(self, cb=None):
        def cb_wrapper(res):
            res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
            cb(res)
        self.chrome.send('Profiler.takePreciseCoverage', cb=cb_wrapper)


    def takeTypeProfile(self, cb=None):
        def cb_wrapper(res):
            res['result'] = Types.ScriptTypeProfile.safe_create_from_list(res['result'])
            cb(res)
        self.chrome.send('Profiler.takeTypeProfile', cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

