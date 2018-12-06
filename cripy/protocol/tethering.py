"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Tethering"]


@attr.dataclass(slots=True, cmp=False)
class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def bind(self, port: int) -> Awaitable[Dict]:
        """
        Request browser port binding.

        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        return self.client.send("Tethering.bind", msg_dict)

    def unbind(self, port: int) -> Awaitable[Dict]:
        """
        Request browser port unbinding.

        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict["port"] = port
        return self.client.send("Tethering.unbind", msg_dict)

    def accepted(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Informs that port was successfully bound and got a specified connection id.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Tethering.accepted", _cb)

            return future

        self.client.on("Tethering.accepted", cb)
        return lambda: self.client.remove_listener("Tethering.accepted", cb)
