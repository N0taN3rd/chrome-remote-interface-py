# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["SystemInfo"]


@attr.dataclass(slots=True, cmp=False)
class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def getInfo(self) -> Awaitable[Optional[dict]]:
        """
        Returns information about the system.
        """
        return self.client.send("SystemInfo.getInfo")
