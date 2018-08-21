from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Performance"]


@attr.dataclass(slots=True)
class Performance(object):
    client: "Client" = attr.ib(repr=False)

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
