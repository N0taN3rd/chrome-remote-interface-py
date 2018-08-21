from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Schema"]


@attr.dataclass(slots=True)
class Schema(object):
    """
    This domain is deprecated.
    """

    client: "Client" = attr.ib(repr=False)

    async def getDomains(self) -> Optional[dict]:
        """
        Returns supported domains.
        """
        res = await self.client.send("Schema.getDomains")
        return res
