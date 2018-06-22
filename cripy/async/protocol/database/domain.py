from typing import Any, List, Optional, Union
from cripy.async.protocol.database import events as Events
from cripy.async.protocol.database import types as Types

__all__ = ["Database"]


class Database(object):
    events = Events.DATABASE_EVENTS_NS

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
        mayberes = await self.chrome.send('Database.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables database tracking, database events will now be delivered to the client.
        """
        mayberes = await self.chrome.send('Database.enable')
        return mayberes

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
        mayberes = await self.chrome.send('Database.executeSQL', msg_dict)
        res = await mayberes
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
        mayberes = await self.chrome.send('Database.getDatabaseTableNames', msg_dict)
        res = await mayberes
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.DATABASE_EVENTS_TO_CLASS

