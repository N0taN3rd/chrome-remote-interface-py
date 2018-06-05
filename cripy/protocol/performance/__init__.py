from typing import Any, List, Optional, Union
from cripy.protocol.performance import events as Events
from cripy.protocol.performance import types as Types


class Performance(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Performance.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Performance.enable")
        return mayberes

    async def getMetrics(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Performance.getMetrics")
        res = await mayberes
        res["metrics"] = Types.Metric.safe_create_from_list(res["metrics"])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
