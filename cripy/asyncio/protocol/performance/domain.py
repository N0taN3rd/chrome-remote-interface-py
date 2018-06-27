from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.performance import events as Events
from cripy.asyncio.protocol.performance import types as Types

__all__ = ["Performance"]


class Performance(object):
    events = Events.PERFORMANCE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Performance object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        """
        Disable collecting and reporting metrics.
        """
        res = await self.chrome.send('Performance.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enable collecting and reporting metrics.
        """
        res = await self.chrome.send('Performance.enable')
        return res

    async def getMetrics(self) -> Optional[dict]:
        """
        Retrieve current values of run-time metrics.
        """
        res = await self.chrome.send('Performance.getMetrics')
        res['metrics'] = Types.Metric.safe_create_from_list(res['metrics'])
        return res

    def metrics(self, fn, once=False):
        if once:
            self.chrome.once("Performance.metrics", fn)
        else:
            self.chrome.on("Performance.metrics", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.PERFORMANCE_EVENTS_TO_CLASS

