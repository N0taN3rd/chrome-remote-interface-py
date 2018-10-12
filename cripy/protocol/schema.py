# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Schema"]


class Schema(object):
    """
    This domain is deprecated.
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def getDomains(self) -> Optional[dict]:
        """
        Returns supported domains.
        """
        res = await self.client.send("Schema.getDomains")
        return res

    def __repr__(self):
        return f"Schema()"
