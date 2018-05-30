from typing import Any, List, Optional, Union
from cripy.protocol.database import events as Events
from cripy.protocol.database import types as Types


class Database(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Database.disable')
        return res

    async def enable(self) -> Optional[dict]:
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
        res['sqlError'] = Types.Error.safe_create(res['sqlError'])
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

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

