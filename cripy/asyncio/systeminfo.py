from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["SystemInfo"]


@attr.dataclass(slots=True)
class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    client: "Client" = attr.ib(repr=False)

    async def getInfo(self) -> Optional[dict]:
        """
        Returns information about the system.
        """
        res = await self.client.send("SystemInfo.getInfo")
        return res
