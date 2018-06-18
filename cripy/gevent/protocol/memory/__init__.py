from cripy.gevent.protocol.memory import types as Types

__all__ = ["Memory"] + Types.__all__


class Memory(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def getDOMCounters(self):
        wres = self.chrome.send("Memory.getDOMCounters")
        res = wres.get()
        return res

    def prepareForLeakDetection(self):
        wres = self.chrome.send("Memory.prepareForLeakDetection")
        return wres.get()

    def setPressureNotificationsSuppressed(self, suppressed):
        """
        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict["suppressed"] = suppressed
        wres = self.chrome.send("Memory.setPressureNotificationsSuppressed", msg_dict)
        return wres.get()

    def simulatePressureNotification(self, level):
        """
        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict["level"] = level
        wres = self.chrome.send("Memory.simulatePressureNotification", msg_dict)
        return wres.get()

    def startSampling(self, samplingInterval=None, suppressRandomness=None):
        """
        :param samplingInterval: Average number of bytes between samples.
        :type samplingInterval: Optional[int]
        :param suppressRandomness: Do not randomize intervals between samples.
        :type suppressRandomness: Optional[bool]
        """
        msg_dict = dict()
        if samplingInterval is not None:
            msg_dict["samplingInterval"] = samplingInterval
        if suppressRandomness is not None:
            msg_dict["suppressRandomness"] = suppressRandomness
        wres = self.chrome.send("Memory.startSampling", msg_dict)
        return wres.get()

    def stopSampling(self):
        wres = self.chrome.send("Memory.stopSampling")
        return wres.get()

    def getAllTimeSamplingProfile(self):
        wres = self.chrome.send("Memory.getAllTimeSamplingProfile")
        res = wres.get()
        res["profile"] = Types.SamplingProfile.safe_create(res["profile"])
        return res

    def getBrowserSamplingProfile(self):
        wres = self.chrome.send("Memory.getBrowserSamplingProfile")
        res = wres.get()
        res["profile"] = Types.SamplingProfile.safe_create(res["profile"])
        return res

    def getSamplingProfile(self):
        wres = self.chrome.send("Memory.getSamplingProfile")
        res = wres.get()
        res["profile"] = Types.SamplingProfile.safe_create(res["profile"])
        return res

    @staticmethod
    def get_event_classes():
        return None
