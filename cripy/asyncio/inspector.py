from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Inspector"]


@attr.dataclass(slots=True)
class Inspector(object):
    client: "Client" = attr.ib(repr=False)

    async def disable(self) -> Optional[dict]:
        """
        Disables inspector domain notifications.
        """
        res = await self.client.send("Inspector.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables inspector domain notifications.
        """
        res = await self.client.send("Inspector.enable")
        return res

    def detached(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when remote debugging connection is about to be terminated. Contains detach reason.
        """
        if once:
            self.client.once("Inspector.detached", fn)
        else:
            self.client.on("Inspector.detached", fn)

    def targetCrashed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when debugging target has crashed
        """
        if once:
            self.client.once("Inspector.targetCrashed", fn)
        else:
            self.client.on("Inspector.targetCrashed", fn)

    def targetReloadedAfterCrash(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when debugging target has reloaded after crash
        """
        if once:
            self.client.once("Inspector.targetReloadedAfterCrash", fn)
        else:
            self.client.on("Inspector.targetReloadedAfterCrash", fn)
