# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Database"]


class Database(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def disable(self) -> Optional[dict]:
        """
        Disables database tracking, prevents database events from being sent to the client.
        """
        res = await self.client.send("Database.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables database tracking, database events will now be delivered to the client.
        """
        res = await self.client.send("Database.enable")
        return res

    async def executeSQL(self, databaseId: str, query: str) -> Optional[dict]:
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
        res = await self.client.send("Database.executeSQL", msg_dict)
        return res

    async def getDatabaseTableNames(self, databaseId: str) -> Optional[dict]:
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict["databaseId"] = databaseId
        res = await self.client.send("Database.getDatabaseTableNames", msg_dict)
        return res

    def addDatabase(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("Database.addDatabase", fn)
        else:
            self.client.on("Database.addDatabase", fn)

    def __repr__(self):
        return f"Database()"
