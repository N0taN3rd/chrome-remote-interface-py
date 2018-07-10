from typing import Any, List, Optional, Union


__all__ = ["Database"]


class Database(object):

    def __init__(self, chrome):
        """
        Construct a new Database object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        """
        Disables database tracking, prevents database events from being sent to the client.
        """
        res = await self.chrome.send('Database.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables database tracking, database events will now be delivered to the client.
        """
        res = await self.chrome.send('Database.enable')
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
            msg_dict['databaseId'] = databaseId
        if query is not None:
            msg_dict['query'] = query
        res = await self.chrome.send('Database.executeSQL', msg_dict)
        return res

    async def getDatabaseTableNames(self, databaseId: str) -> Optional[dict]:
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        res = await self.chrome.send('Database.getDatabaseTableNames', msg_dict)
        return res

    def addDatabase(self, fn, once=False) -> None:
        if once:
            self.chrome.once("Database.addDatabase", fn)
        else:
            self.chrome.on("Database.addDatabase", fn)



