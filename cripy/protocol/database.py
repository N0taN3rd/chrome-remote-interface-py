# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Database"]


@attr.dataclass(slots=True, cmp=False)
class Database(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables database tracking, prevents database events from being sent to the client.
        """
        return self.client.send("Database.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables database tracking, database events will now be delivered to the client.
        """
        return self.client.send("Database.enable")

    def executeSQL(self, databaseId: str, query: str) -> Awaitable[Optional[dict]]:
        """
        :param databaseId: The databaseId
        :type databaseId: str
        :param query: The query
        :type query: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict["databaseId"] = databaseId
        if query is not None:
            msg_dict["query"] = query
        return self.client.send("Database.executeSQL", msg_dict)

    def getDatabaseTableNames(self, databaseId: str) -> Awaitable[Optional[dict]]:
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict["databaseId"] = databaseId
        return self.client.send("Database.getDatabaseTableNames", msg_dict)

    def addDatabase(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Database.addDatabase", _cb)

            return future

        self.client.on("Database.addDatabase", cb)
