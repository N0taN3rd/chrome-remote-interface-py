from typing import Any, List, Optional, Union
from cripy.async.protocol.memory import types as Types

__all__ = ["Memory"]


class Memory(object):
    def __init__(self, chrome):
        """
        Construct a new Memory object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def getDOMCounters(self) -> Optional[dict]:
        mayberes = await self.chrome.send('Memory.getDOMCounters')
        res = await mayberes
        return res

    async def prepareForLeakDetection(self) -> Optional[dict]:
        mayberes = await self.chrome.send('Memory.prepareForLeakDetection')
        return mayberes

    async def setPressureNotificationsSuppressed(self, suppressed: bool) -> Optional[dict]:
        """
        Enable/disable suppressing memory pressure notifications in all processes.

        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict['suppressed'] = suppressed
        mayberes = await self.chrome.send('Memory.setPressureNotificationsSuppressed', msg_dict)
        return mayberes

    async def simulatePressureNotification(self, level: str) -> Optional[dict]:
        """
        Simulate a memory pressure notification in all processes.

        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict['level'] = level
        mayberes = await self.chrome.send('Memory.simulatePressureNotification', msg_dict)
        return mayberes

    async def startSampling(self, samplingInterval: Optional[int] = None, suppressRandomness: Optional[bool] = None) -> Optional[dict]:
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
        mayberes = await self.chrome.send('Memory.startSampling', msg_dict)
        return mayberes

    async def stopSampling(self) -> Optional[dict]:
        """
        Stop collecting native memory profile.
        """
        mayberes = await self.chrome.send('Memory.stopSampling')
        return mayberes

    async def getAllTimeSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile
collected since renderer process startup.
        """
        mayberes = await self.chrome.send('Memory.getAllTimeSamplingProfile')
        res = await mayberes
        res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
        return res

    async def getBrowserSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile
collected since browser process startup.
        """
        mayberes = await self.chrome.send('Memory.getBrowserSamplingProfile')
        res = await mayberes
        res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
        return res

    async def getSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile collected since last
`startSampling` call.
        """
        mayberes = await self.chrome.send('Memory.getSamplingProfile')
        res = await mayberes
        res['profile'] = Types.SamplingProfile.safe_create(res['profile'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

