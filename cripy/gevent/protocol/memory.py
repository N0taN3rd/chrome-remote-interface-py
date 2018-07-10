__all__ = ["Memory"]


class Memory(object):
    def __init__(self, chrome):
        """
        Construct a new Memory object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def getDOMCounters(self):
        wres = self.chrome.send('Memory.getDOMCounters')
        return wres.get()

    def prepareForLeakDetection(self):
        wres = self.chrome.send('Memory.prepareForLeakDetection')
        return wres.get()

    def setPressureNotificationsSuppressed(self, suppressed):
        """
        Enable/disable suppressing memory pressure notifications in all processes.

        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict['suppressed'] = suppressed
        wres = self.chrome.send('Memory.setPressureNotificationsSuppressed', msg_dict)
        return wres.get()

    def simulatePressureNotification(self, level):
        """
        Simulate a memory pressure notification in all processes.

        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict['level'] = level
        wres = self.chrome.send('Memory.simulatePressureNotification', msg_dict)
        return wres.get()

    def startSampling(self, samplingInterval=None, suppressRandomness=None):
        """
        Start collecting native memory profile.

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
        wres = self.chrome.send('Memory.startSampling', msg_dict)
        return wres.get()

    def stopSampling(self):
        """
        Stop collecting native memory profile.
        """
        wres = self.chrome.send('Memory.stopSampling')
        return wres.get()

    def getAllTimeSamplingProfile(self):
        """
        Retrieve native memory allocations profile
collected since renderer process startup.
        """
        wres = self.chrome.send('Memory.getAllTimeSamplingProfile')
        return wres.get()

    def getBrowserSamplingProfile(self):
        """
        Retrieve native memory allocations profile
collected since browser process startup.
        """
        wres = self.chrome.send('Memory.getBrowserSamplingProfile')
        return wres.get()

    def getSamplingProfile(self):
        """
        Retrieve native memory allocations profile collected since last
`startSampling` call.
        """
        wres = self.chrome.send('Memory.getSamplingProfile')
        return wres.get()


