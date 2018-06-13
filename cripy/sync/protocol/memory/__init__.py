from cripy.sync.protocol.memory import types as Types

__all__ = ["Memory"]+ Types.__all__ 


class Memory(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def getDOMCounters(self):
        def cb(res):
            self.chrome.emit('Memory.getDOMCounters', res)
        self.chrome.send('Memory.getDOMCounters', cb=cb)


    def prepareForLeakDetection(self):
        self.chrome.send('Memory.prepareForLeakDetection')


    def setPressureNotificationsSuppressed(self, suppressed):
        """
        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict['suppressed'] = suppressed
        self.chrome.send('Memory.setPressureNotificationsSuppressed', params=msg_dict)


    def simulatePressureNotification(self, level):
        """
        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict['level'] = level
        self.chrome.send('Memory.simulatePressureNotification', params=msg_dict)


    def startSampling(self, samplingInterval, suppressRandomness):
        """
        :param samplingInterval: Average number of bytes between samples.
        :type samplingInterval: Optional[int]
        :param suppressRandomness: Do not randomize intervals between samples.
        :type suppressRandomness: Optional[bool]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict['samplingInterval'] = samplingInterval
        if suppressRandomness is not None:
            msg_dict['suppressRandomness'] = suppressRandomness
        self.chrome.send('Memory.startSampling', params=msg_dict)


    def stopSampling(self):
        self.chrome.send('Memory.stopSampling')


    def getAllTimeSamplingProfile(self):
        def cb(res):
            res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
            self.chrome.emit('Memory.getAllTimeSamplingProfile', res)
        self.chrome.send('Memory.getAllTimeSamplingProfile', cb=cb)


    def getBrowserSamplingProfile(self):
        def cb(res):
            res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
            self.chrome.emit('Memory.getBrowserSamplingProfile', res)
        self.chrome.send('Memory.getBrowserSamplingProfile', cb=cb)


    def getSamplingProfile(self):
        def cb(res):
            res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
            self.chrome.emit('Memory.getSamplingProfile', res)
        self.chrome.send('Memory.getSamplingProfile', cb=cb)


    @staticmethod
    def get_event_classes():
        return None

