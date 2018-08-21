from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Tethering"]


@attr.dataclass(slots=True)
class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    client: "Client" = attr.ib(repr=False)

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
