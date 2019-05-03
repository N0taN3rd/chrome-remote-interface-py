"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Tethering"]


class Tethering:
    """
    The Tethering domain defines methods and events for browser port binding.
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Tethering`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Tethering

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def bind(self, port: int) -> Awaitable[Dict]:
        """
        Request browser port binding.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tethering#method-bind`

        :param port: Port number to bind.
        :return: The results of the command
        """
        return self.client.send("Tethering.bind", {"port": port})

    def unbind(self, port: int) -> Awaitable[Dict]:
        """
        Request browser port unbinding.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tethering#method-unbind`

        :param port: Port number to unbind.
        :return: The results of the command
        """
        return self.client.send("Tethering.unbind", {"port": port})

    def accepted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Informs that port was successfully bound and got a specified connection id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Tethering#event-accepted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Tethering.accepted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
