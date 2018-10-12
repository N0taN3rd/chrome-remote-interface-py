# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Performance"]


class Performance(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def disable(self) -> Optional[dict]:
        """
        Disable collecting and reporting metrics.
        """
        res = await self.client.send("Performance.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enable collecting and reporting metrics.
        """
        res = await self.client.send("Performance.enable")
        return res

    async def getMetrics(self) -> Optional[dict]:
        """
        Retrieve current values of run-time metrics.
        """
        res = await self.client.send("Performance.getMetrics")
        return res

    def metrics(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Current values of the metrics.
        """
        if once:
            self.client.once("Performance.metrics", fn)
        else:
            self.client.on("Performance.metrics", fn)

    def __repr__(self):
        return f"Performance()"
