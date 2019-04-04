"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Memory"]


class Memory:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Memory`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Memory

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def getDOMCounters(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-getDOMCounters`

        :return: The results of the command
        """
        return self.client.send("Memory.getDOMCounters", {})

    def prepareForLeakDetection(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-prepareForLeakDetection`

        :return: The results of the command
        """
        return self.client.send("Memory.prepareForLeakDetection", {})

    def forciblyPurgeJavaScriptMemory(self) -> Awaitable[Dict]:
        """
        Simulate OomIntervention by purging V8 memory.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-forciblyPurgeJavaScriptMemory`

        :return: The results of the command
        """
        return self.client.send("Memory.forciblyPurgeJavaScriptMemory", {})

    def setPressureNotificationsSuppressed(self, suppressed: bool) -> Awaitable[Dict]:
        """
        Enable/disable suppressing memory pressure notifications in all processes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-setPressureNotificationsSuppressed`

        :param suppressed: If true, memory pressure notifications will be suppressed.
        :return: The results of the command
        """
        return self.client.send(
            "Memory.setPressureNotificationsSuppressed", {"suppressed": suppressed}
        )

    def simulatePressureNotification(self, level: str) -> Awaitable[Dict]:
        """
        Simulate a memory pressure notification in all processes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-simulatePressureNotification`

        :param level: Memory pressure level of the notification.
        :return: The results of the command
        """
        return self.client.send("Memory.simulatePressureNotification", {"level": level})

    def startSampling(
        self,
        samplingInterval: Optional[int] = None,
        suppressRandomness: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Start collecting native memory profile.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-startSampling`

        :param samplingInterval: Average number of bytes between samples.
        :param suppressRandomness: Do not randomize intervals between samples.
        :return: The results of the command
        """
        msg = {}
        if samplingInterval is not None:
            msg["samplingInterval"] = samplingInterval
        if suppressRandomness is not None:
            msg["suppressRandomness"] = suppressRandomness
        return self.client.send("Memory.startSampling", msg)

    def stopSampling(self) -> Awaitable[Dict]:
        """
        Stop collecting native memory profile.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-stopSampling`

        :return: The results of the command
        """
        return self.client.send("Memory.stopSampling", {})

    def getAllTimeSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile
        collected since renderer process startup.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-getAllTimeSamplingProfile`

        :return: The results of the command
        """
        return self.client.send("Memory.getAllTimeSamplingProfile", {})

    def getBrowserSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile
        collected since browser process startup.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-getBrowserSamplingProfile`

        :return: The results of the command
        """
        return self.client.send("Memory.getBrowserSamplingProfile", {})

    def getSamplingProfile(self) -> Awaitable[Dict]:
        """
        Retrieve native memory allocations profile collected since last
        `startSampling` call.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Memory#method-getSamplingProfile`

        :return: The results of the command
        """
        return self.client.send("Memory.getSamplingProfile", {})
