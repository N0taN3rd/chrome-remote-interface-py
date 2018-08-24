# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Memory"]


class Memory(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def getDOMCounters(self) -> Optional[dict]:
        res = await self.client.send("Memory.getDOMCounters")
        return res

    async def prepareForLeakDetection(self) -> Optional[dict]:
        res = await self.client.send("Memory.prepareForLeakDetection")
        return res

    async def setPressureNotificationsSuppressed(
        self, suppressed: bool
    ) -> Optional[dict]:
        """
        Enable/disable suppressing memory pressure notifications in all processes.

        :param suppressed: If true, memory pressure notifications will be suppressed.
        :type suppressed: bool
        """
        msg_dict = dict()
        if suppressed is not None:
            msg_dict["suppressed"] = suppressed
        res = await self.client.send(
            "Memory.setPressureNotificationsSuppressed", msg_dict
        )
        return res

    async def simulatePressureNotification(self, level: str) -> Optional[dict]:
        """
        Simulate a memory pressure notification in all processes.

        :param level: Memory pressure level of the notification.
        :type level: str
        """
        msg_dict = dict()
        if level is not None:
            msg_dict["level"] = level
        res = await self.client.send("Memory.simulatePressureNotification", msg_dict)
        return res

    async def startSampling(
        self,
        samplingInterval: Optional[int] = None,
        suppressRandomness: Optional[bool] = None,
    ) -> Optional[dict]:
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
        res = await self.client.send("Memory.startSampling", msg_dict)
        return res

    async def stopSampling(self) -> Optional[dict]:
        """
        Stop collecting native memory profile.
        """
        res = await self.client.send("Memory.stopSampling")
        return res

    async def getAllTimeSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile
collected since renderer process startup.
        """
        res = await self.client.send("Memory.getAllTimeSamplingProfile")
        return res

    async def getBrowserSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile
collected since browser process startup.
        """
        res = await self.client.send("Memory.getBrowserSamplingProfile")
        return res

    async def getSamplingProfile(self) -> Optional[dict]:
        """
        Retrieve native memory allocations profile collected since last
`startSampling` call.
        """
        res = await self.client.send("Memory.getSamplingProfile")
        return res

    def __repr__(self):
        return f"Memory()"
