"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Performance"]


class Performance:
    """
    See `https://chromedevtools.github.io/devtools-protocol/tot/Performance`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Performance

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disable collecting and reporting metrics.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Performance#method-disable`

        :return: The results of the command
        """
        return self.client.send("Performance.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enable collecting and reporting metrics.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Performance#method-enable`

        :return: The results of the command
        """
        return self.client.send("Performance.enable", {})

    def setTimeDomain(self, timeDomain: str) -> Awaitable[Dict]:
        """
        Sets time domain to use for collecting and reporting duration metrics.
        Note that this must be called before enabling metrics collection. Calling
        this method while metrics collection is enabled returns an error.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Performance#method-setTimeDomain`

        :param timeDomain: Time domain
        :return: The results of the command
        """
        return self.client.send("Performance.setTimeDomain", {"timeDomain": timeDomain})

    def getMetrics(self) -> Awaitable[Dict]:
        """
        Retrieve current values of run-time metrics.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Performance#method-getMetrics`

        :return: The results of the command
        """
        return self.client.send("Performance.getMetrics", {})

    def metrics(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Current values of the metrics.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Performance#event-metrics`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Performance.metrics"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
