# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Schema"]


@attr.dataclass(slots=True)
class Schema(object):
    """
    This domain is deprecated.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def getDomains(self) -> Awaitable[Optional[dict]]:
        """
        Returns supported domains.
        """
        return self.client.send("Schema.getDomains")
