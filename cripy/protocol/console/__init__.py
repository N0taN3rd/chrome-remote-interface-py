from typing import Any, List, Optional, Union
from cripy.protocol.console import events as Events
from cripy.protocol.console import types as Types


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ['Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    async def clearMessages(self) -> Optional[dict]:
        res = await self.chrome.send('Console.clearMessages')
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Console.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Console.enable')
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

