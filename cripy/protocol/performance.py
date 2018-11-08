# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Performance"]


@attr.dataclass(slots=True, cmp=False)
class Performance(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disable collecting and reporting metrics.
        """
        return self.client.send("Performance.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enable collecting and reporting metrics.
        """
        return self.client.send("Performance.enable")

    def setTimeDomain(self, timeDomain: str) -> Awaitable[Optional[dict]]:
        """
        Sets time domain to use for collecting and reporting duration metrics.
Note that this must be called before enabling metrics collection. Calling
this method while metrics collection is enabled returns an error.

        :param timeDomain: Time domain
        :type timeDomain: str
        """
        msg_dict = dict()
        if timeDomain is not None:
            msg_dict["timeDomain"] = timeDomain
        return self.client.send("Performance.setTimeDomain", msg_dict)

    def getMetrics(self) -> Awaitable[Optional[dict]]:
        """
        Retrieve current values of run-time metrics.
        """
        return self.client.send("Performance.getMetrics")

    def metrics(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Current values of the metrics.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Performance.metrics", _cb)

            return future

        self.client.on("Performance.metrics", cb)
