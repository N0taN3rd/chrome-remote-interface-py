"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Console"]


class Console:
    """
    This domain is deprecated - use Runtime or Log instead.
     
    Domain Dependencies: 
      * Runtime
    Status: Deprecated
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Console`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Console

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clearMessages(self) -> Awaitable[Dict]:
        """
        Does nothing.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Console#method-clearMessages`

        :return: The results of the command
        """
        return self.client.send("Console.clearMessages", {})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables console domain, prevents further console messages from being reported to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Console#method-disable`

        :return: The results of the command
        """
        return self.client.send("Console.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
        `messageAdded` notification.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Console#method-enable`

        :return: The results of the command
        """
        return self.client.send("Console.enable", {})

    def messageAdded(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when new console message is added.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Console#event-messageAdded`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Console.messageAdded"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
