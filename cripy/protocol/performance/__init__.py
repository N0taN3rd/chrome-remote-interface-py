from typing import Any, List, Optional, Union
from cripy.protocol.performance import events as Events
from cripy.protocol.performance import types as Types


class Performance(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Performance.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Performance.enable')
        return res

    async def getMetrics(self) -> Optional[dict]:
        res = await self.chrome.send('Performance.getMetrics')
        res['metrics'] = Types.Metric.safe_create_from_list(res['metrics'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

