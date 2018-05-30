from typing import Any, List, Optional, Union
from cripy.protocol.inspector import events as Events


class Inspector(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Inspector.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Inspector.enable')
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

