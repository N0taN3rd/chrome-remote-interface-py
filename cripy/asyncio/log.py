from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Log"]


@attr.dataclass(slots=True)
class Log(object):
    """
    Provides access to log entries.
    """

    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["Runtime", "Network"]

    async def clear(self) -> Optional[dict]:
        """
        Clears the log.
        """
        res = await self.client.send("Log.clear")
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        res = await self.client.send("Log.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
        """
        res = await self.client.send("Log.enable")
        return res

    async def startViolationsReport(self, config: List[dict]) -> Optional[dict]:
        """
        start violation reporting.

        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict["config"] = config
        res = await self.client.send("Log.startViolationsReport", msg_dict)
        return res

    async def stopViolationsReport(self) -> Optional[dict]:
        """
        Stop violation reporting.
        """
        res = await self.client.send("Log.stopViolationsReport")
        return res

    def entryAdded(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when new message was logged.
        """
        if once:
            self.client.once("Log.entryAdded", fn)
        else:
            self.client.on("Log.entryAdded", fn)
