from typing import Any, List, Optional, Union
from cripy.async.protocol.log import events as Events
from cripy.async.protocol.log import types as Types


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ["Runtime", "Network"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def clear(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Log.clear")
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Log.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Log.enable")
        return mayberes

    async def startViolationsReport(self, config: List[dict]) -> Optional[dict]:
        """
        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict["config"] = config
        mayberes = await self.chrome.send("Log.startViolationsReport", msg_dict)
        return mayberes

    async def stopViolationsReport(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Log.stopViolationsReport")
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
