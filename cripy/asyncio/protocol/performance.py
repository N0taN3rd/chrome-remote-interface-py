from typing import Any, List, Optional, Union


__all__ = ["Performance"]


class Performance(object):

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
        return res

    def metrics(self, fn, once=False) -> None:
        """
        Current values of the metrics.
        """
        if once:
            self.chrome.once("Performance.metrics", fn)
        else:
            self.chrome.on("Performance.metrics", fn)



