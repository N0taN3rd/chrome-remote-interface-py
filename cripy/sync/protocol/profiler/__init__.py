from cripy.sync.protocol.profiler import events as Events
from cripy.sync.protocol.profiler import types as Types

__all__ = ["Profiler"] + Events.__all__ + Types.__all__ 


class Profiler(object):
    dependencies = ['Runtime', 'Debugger']

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('Profiler.disable')


    def enable(self):
        self.chrome.send('Profiler.enable')


    def getBestEffortCoverage(self):
        def cb(res):
            res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
            self.chrome.emit('Profiler.getBestEffortCoverage', res)
        self.chrome.send('Profiler.getBestEffortCoverage', cb=cb)


    def setSamplingInterval(self, interval):
        """
        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict['interval'] = interval
        self.chrome.send('Profiler.setSamplingInterval', params=msg_dict)


    def start(self):
        self.chrome.send('Profiler.start')


    def startPreciseCoverage(self, callCount, detailed):
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


    def startTypeProfile(self):
        self.chrome.send('Profiler.startTypeProfile')


    def stop(self):
        def cb(res):
            res['profile'] = Types.Profile.safe_create(res['profile'])
            self.chrome.emit('Profiler.stop', res)
        self.chrome.send('Profiler.stop', cb=cb)


    def stopPreciseCoverage(self):
        self.chrome.send('Profiler.stopPreciseCoverage')


    def stopTypeProfile(self):
        self.chrome.send('Profiler.stopTypeProfile')


    def takePreciseCoverage(self):
        def cb(res):
            res['result'] = Types.ScriptCoverage.safe_create_from_list(res['result'])
            self.chrome.emit('Profiler.takePreciseCoverage', res)
        self.chrome.send('Profiler.takePreciseCoverage', cb=cb)


    def takeTypeProfile(self):
        def cb(res):
            res['result'] = Types.ScriptTypeProfile.safe_create_from_list(res['result'])
            self.chrome.emit('Profiler.takeTypeProfile', res)
        self.chrome.send('Profiler.takeTypeProfile', cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

