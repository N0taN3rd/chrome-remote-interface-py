"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Memory"]


@attr.dataclass(slots=True, cmp=False)
class Memory(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def getDOMCounters(self) -> Awaitable[Dict]:
        return self.client.send("Memory.getDOMCounters")

    def prepareForLeakDetection(self) -> Awaitable[Dict]:
        return self.client.send("Memory.prepareForLeakDetection")

    def forciblyPurgeJavaScriptMemory(self) -> Awaitable[Dict]:
        """
        Simulate OomIntervention by purging V8 memory.
        """
        return self.client.send("Memory.forciblyPurgeJavaScriptMemory")

    def setPressureNotificationsSuppressed(self, suppressed: bool) -> Awaitable[Dict]:
        """
        Enable/disable suppressing memory pressure notifications in all processes.

        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict["suppressed"] = suppressed
        return self.client.send("Memory.setPressureNotificationsSuppressed", msg_dict)

    def simulatePressureNotification(self, level: str) -> Awaitable[Dict]:
        """
        Simulate a memory pressure notification in all processes.

        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict["level"] = level
        return self.client.send("Memory.simulatePressureNotification", msg_dict)

    def startSampling(
        self,
        samplingInterval: Optional[int] = None,
        suppressRandomness: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Start collecting native memory profile.

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
        return self.client.send("Memory.startSampling", msg_dict)

    def stopSampling(self) -> Awaitable[Dict]:
        """
        Stop collecting native memory profile.
        """
        return self.client.send("Memory.stopSampling")

    def getAllTimeSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile
collected since renderer process startup.
        """
        return self.client.send("Memory.getAllTimeSamplingProfile")

    def getBrowserSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile
collected since browser process startup.
        """
        return self.client.send("Memory.getBrowserSamplingProfile")

    def getSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile collected since last
`startSampling` call.
        """
        return self.client.send("Memory.getSamplingProfile")
