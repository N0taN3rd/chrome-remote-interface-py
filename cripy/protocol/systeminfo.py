# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["SystemInfo"]


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def getInfo(self) -> Optional[dict]:
        """
        Returns information about the system.
        """
        res = await self.client.send("SystemInfo.getInfo")
        return res

    def __repr__(self):
        return f"SystemInfo()"
