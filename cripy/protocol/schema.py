"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Schema"]


@attr.dataclass(slots=True, cmp=False)
class Schema(object):
    """
    This domain is deprecated.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def getDomains(self) -> Awaitable[Dict]:
        """
        Returns supported domains.
        """
        return self.client.send("Schema.getDomains")
