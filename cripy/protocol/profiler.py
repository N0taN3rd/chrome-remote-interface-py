# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import (
    Awaitable,
    Any,
    Callable,
    ClassVar,
    List,
    Optional,
    Union,
    TYPE_CHECKING,
)

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Profiler"]


@attr.dataclass(slots=True)
class Profiler(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["Runtime", "Debugger"]

    def disable(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Profiler.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Profiler.enable")

    def getBestEffortCoverage(self) -> Awaitable[Optional[dict]]:
        """
        Collect coverage data for the current isolate. The coverage data may be incomplete due to
garbage collection.
        """
        return self.client.send("Profiler.getBestEffortCoverage")

    def setSamplingInterval(self, interval: int) -> Awaitable[Optional[dict]]:
        """
        Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.

        :param interval: New sampling interval in microseconds.
        :type interval: int
        """
        msg_dict = dict()
        if interval is not None:
            msg_dict["interval"] = interval
        return self.client.send("Profiler.setSamplingInterval", msg_dict)

    def start(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Profiler.start")

    def startPreciseCoverage(
        self, callCount: Optional[bool] = None, detailed: Optional[bool] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
coverage may be incomplete. Enabling prevents running optimized code and resets execution
counters.

        :param callCount: Collect accurate call counts beyond simple 'covered' or 'not covered'.
        :type callCount: Optional[bool]
        :param detailed: Collect block-based coverage.
        :type detailed: Optional[bool]
        """
        msg_dict = dict()
        if callCount is not None:
            msg_dict["callCount"] = callCount
        if detailed is not None:
            msg_dict["detailed"] = detailed
        return self.client.send("Profiler.startPreciseCoverage", msg_dict)

    def startTypeProfile(self) -> Awaitable[Optional[dict]]:
        """
        Enable type profile.
        """
        return self.client.send("Profiler.startTypeProfile")

    def stop(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Profiler.stop")

    def stopPreciseCoverage(self) -> Awaitable[Optional[dict]]:
        """
        Disable precise code coverage. Disabling releases unnecessary execution count records and allows
executing optimized code.
        """
        return self.client.send("Profiler.stopPreciseCoverage")

    def stopTypeProfile(self) -> Awaitable[Optional[dict]]:
        """
        Disable type profile. Disabling releases type profile data collected so far.
        """
        return self.client.send("Profiler.stopTypeProfile")

    def takePreciseCoverage(self) -> Awaitable[Optional[dict]]:
        """
        Collect coverage data for the current isolate, and resets execution counters. Precise code
coverage needs to have started.
        """
        return self.client.send("Profiler.takePreciseCoverage")

    def takeTypeProfile(self) -> Awaitable[Optional[dict]]:
        """
        Collect type profile.
        """
        return self.client.send("Profiler.takeTypeProfile")

    def consoleProfileFinished(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Profiler.consoleProfileFinished", _cb)

            return future

        self.client.on("Profiler.consoleProfileFinished", cb)

    def consoleProfileStarted(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Sent when new profile recording is started using console.profile() call.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Profiler.consoleProfileStarted", _cb)

            return future

        self.client.on("Profiler.consoleProfileStarted", cb)
