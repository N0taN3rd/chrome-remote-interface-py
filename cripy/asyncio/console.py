from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Console"]


@attr.dataclass(slots=True)
class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["Runtime"]

    async def clearMessages(self) -> Optional[dict]:
        """
        Does nothing.
        """
        res = await self.client.send("Console.clearMessages")
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables console domain, prevents further console messages from being reported to the client.
        """
        res = await self.client.send("Console.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        res = await self.client.send("Console.enable")
        return res

    def messageAdded(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when new console message is added.
        """
        if once:
            self.client.once("Console.messageAdded", fn)
        else:
            self.client.on("Console.messageAdded", fn)
