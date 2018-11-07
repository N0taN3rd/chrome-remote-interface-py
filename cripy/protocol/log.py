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

__all__ = ["Log"]


@attr.dataclass(slots=True)
class Log(object):
    """
    Provides access to log entries.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["Runtime", "Network"]

    def clear(self) -> Awaitable[Optional[dict]]:
        """
        Clears the log.
        """
        return self.client.send("Log.clear")

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        return self.client.send("Log.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
        """
        return self.client.send("Log.enable")

    def startViolationsReport(self, config: List[dict]) -> Awaitable[Optional[dict]]:
        """
        start violation reporting.

        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict["config"] = config
        return self.client.send("Log.startViolationsReport", msg_dict)

    def stopViolationsReport(self) -> Awaitable[Optional[dict]]:
        """
        Stop violation reporting.
        """
        return self.client.send("Log.stopViolationsReport")

    def entryAdded(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when new message was logged.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Log.entryAdded", _cb)

            return future

        self.client.on("Log.entryAdded", cb)
