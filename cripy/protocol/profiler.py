"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Profiler"]


class Profiler:
    """
    Domain Dependencies: 
      * Runtime
      * Debugger
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Profiler

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-disable`

        :return: The results of the command
        """
        return self.client.send("Profiler.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-enable`

        :return: The results of the command
        """
        return self.client.send("Profiler.enable", {})

    def getBestEffortCoverage(self) -> Awaitable[Dict]:
        """
        Collect coverage data for the current isolate. The coverage data may be incomplete due to
        garbage collection.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-getBestEffortCoverage`

        :return: The results of the command
        """
        return self.client.send("Profiler.getBestEffortCoverage", {})

    def setSamplingInterval(self, interval: int) -> Awaitable[Dict]:
        """
        Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-setSamplingInterval`

        :param interval: New sampling interval in microseconds.
        :return: The results of the command
        """
        return self.client.send("Profiler.setSamplingInterval", {"interval": interval})

    def start(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-start`

        :return: The results of the command
        """
        return self.client.send("Profiler.start", {})

    def startPreciseCoverage(
        self, callCount: Optional[bool] = None, detailed: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
        coverage may be incomplete. Enabling prevents running optimized code and resets execution
        counters.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-startPreciseCoverage`

        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :param detailed: Collect block-based coverage.
        :return: The results of the command
        """
        msg = {}
        if callCount is not None:
            msg["callCount"] = callCount
        if detailed is not None:
            msg["detailed"] = detailed
        return self.client.send("Profiler.startPreciseCoverage", msg)

    def startTypeProfile(self) -> Awaitable[Dict]:
        """
        Enable type profile.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-startTypeProfile`

        :return: The results of the command
        """
        return self.client.send("Profiler.startTypeProfile", {})

    def stop(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-stop`

        :return: The results of the command
        """
        return self.client.send("Profiler.stop", {})

    def stopPreciseCoverage(self) -> Awaitable[Dict]:
        """
        Disable precise code coverage. Disabling releases unnecessary execution count records and allows
        executing optimized code.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-stopPreciseCoverage`

        :return: The results of the command
        """
        return self.client.send("Profiler.stopPreciseCoverage", {})

    def stopTypeProfile(self) -> Awaitable[Dict]:
        """
        Disable type profile. Disabling releases type profile data collected so far.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-stopTypeProfile`

        :return: The results of the command
        """
        return self.client.send("Profiler.stopTypeProfile", {})

    def takePreciseCoverage(self) -> Awaitable[Dict]:
        """
        Collect coverage data for the current isolate, and resets execution counters. Precise code
        coverage needs to have started.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-takePreciseCoverage`

        :return: The results of the command
        """
        return self.client.send("Profiler.takePreciseCoverage", {})

    def takeTypeProfile(self) -> Awaitable[Dict]:
        """
        Collect type profile.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#method-takeTypeProfile`

        :return: The results of the command
        """
        return self.client.send("Profiler.takeTypeProfile", {})

    def consoleProfileFinished(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#event-consoleProfileFinished`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Profiler.consoleProfileFinished"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def consoleProfileStarted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Sent when new profile recording is started using console.profile() call.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Profiler#event-consoleProfileStarted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Profiler.consoleProfileStarted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
