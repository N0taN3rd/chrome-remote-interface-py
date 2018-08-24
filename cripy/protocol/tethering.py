# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Tethering"]


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def bind(self, port: int) -> Optional[dict]:
        """
        Request browser port binding.

        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        res = await self.client.send("Tethering.bind", msg_dict)
        return res

    async def unbind(self, port: int) -> Optional[dict]:
        """
        Request browser port unbinding.

        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        res = await self.client.send("Tethering.unbind", msg_dict)
        return res

    def accepted(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Informs that port was successfully bound and got a specified connection id.
        """
        if once:
            self.client.once("Tethering.accepted", fn)
        else:
            self.client.on("Tethering.accepted", fn)

    def __repr__(self):
        return f"Tethering()"
