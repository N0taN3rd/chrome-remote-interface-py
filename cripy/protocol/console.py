"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Console"]


@attr.dataclass(slots=True, cmp=False)
class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def clearMessages(self) -> Awaitable[Dict]:
        """
        Does nothing.
        """
        return self.client.send("Console.clearMessages")

    def disable(self) -> Awaitable[Dict]:
        """
        Disables console domain, prevents further console messages from being reported to the client.
        """
        return self.client.send("Console.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        return self.client.send("Console.enable")

    def messageAdded(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when new console message is added.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Console.messageAdded", _cb)

            return future

        self.client.on("Console.messageAdded", cb)
        return lambda: self.client.remove_listener("Console.messageAdded", cb)
