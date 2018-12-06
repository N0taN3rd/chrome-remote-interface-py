"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Log"]


@attr.dataclass(slots=True, cmp=False)
class Log(object):
    """
    Provides access to log entries.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def clear(self) -> Awaitable[Dict]:
        """
        Clears the log.
        """
        return self.client.send("Log.clear")

    def disable(self) -> Awaitable[Dict]:
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        return self.client.send("Log.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
        """
        return self.client.send("Log.enable")

    def startViolationsReport(self, config: List[dict]) -> Awaitable[Dict]:
        """
        start violation reporting.

        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict["config"] = config
        return self.client.send("Log.startViolationsReport", msg_dict)

    def stopViolationsReport(self) -> Awaitable[Dict]:
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

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Log.entryAdded", _cb)

            return future

        self.client.on("Log.entryAdded", cb)
        return lambda: self.client.remove_listener("Log.entryAdded", cb)
