"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Log"]


class Log:
    """
    Provides access to log entries.
     
    Domain Dependencies: 
      * Runtime
      * Network
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Log`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Log

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clear(self) -> Awaitable[Dict]:
        """
        Clears the log.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#method-clear`

        :return: The results of the command
        """
        return self.client.send("Log.clear", {})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables log domain, prevents further log entries from being reported to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#method-disable`

        :return: The results of the command
        """
        return self.client.send("Log.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
        `entryAdded` notification.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#method-enable`

        :return: The results of the command
        """
        return self.client.send("Log.enable", {})

    def startViolationsReport(self, config: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        start violation reporting.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#method-startViolationsReport`

        :param config: Configuration for violations.
        :return: The results of the command
        """
        return self.client.send("Log.startViolationsReport", {"config": config})

    def stopViolationsReport(self) -> Awaitable[Dict]:
        """
        Stop violation reporting.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#method-stopViolationsReport`

        :return: The results of the command
        """
        return self.client.send("Log.stopViolationsReport", {})

    def entryAdded(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when new message was logged.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Log#event-entryAdded`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Log.entryAdded"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
