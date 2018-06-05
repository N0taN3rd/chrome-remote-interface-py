from typing import Any, List, Optional, Union
from cripy.protocol.systeminfo import types as Types


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    async def getInfo(self) -> Optional[dict]:
        mayberes = await self.chrome.send("SystemInfo.getInfo")
        res = await mayberes
        res["gpu"] = Types.GPUInfo.safe_create(res["gpu"])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
