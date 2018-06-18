from typing import Any, List, Optional, Union
from cripy.async.protocol.console import events as Events
from cripy.async.protocol.console import types as Types


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ["Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def clearMessages(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Console.clearMessages")
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Console.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Console.enable")
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
