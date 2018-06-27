from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.indexeddb import types as Types

__all__ = ["IndexedDB"]


class IndexedDB(object):
    dependencies = ['Runtime']

    def __init__(self, chrome):
        """
        Construct a new IndexedDB object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clearObjectStore(self, securityOrigin: str, databaseName: str, objectStoreName: str) -> Optional[dict]:
        """
        Clears all entries from an object store.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        res = await self.chrome.send('IndexedDB.clearObjectStore', msg_dict)
        return res

    async def deleteDatabase(self, securityOrigin: str, databaseName: str) -> Optional[dict]:
        """
        Deletes a database.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        res = await self.chrome.send('IndexedDB.deleteDatabase', msg_dict)
        return res

    async def deleteObjectStoreEntries(self, securityOrigin: str, databaseName: str, objectStoreName: str, keyRange: dict) -> Optional[dict]:
        """
        Delete a range of entries from an object store

        :param securityOrigin: The securityOrigin
        :type securityOrigin: str
        :param databaseName: The databaseName
        :type databaseName: str
        :param objectStoreName: The objectStoreName
        :type objectStoreName: str
        :param keyRange: Range of entry keys to delete
        :type keyRange: dict
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        if keyRange is not None:
            msg_dict['keyRange'] = keyRange
        res = await self.chrome.send('IndexedDB.deleteObjectStoreEntries', msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables events from backend.
        """
        res = await self.chrome.send('IndexedDB.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables events from backend.
        """
        res = await self.chrome.send('IndexedDB.enable')
        return res

    async def requestData(self, securityOrigin: str, databaseName: str, objectStoreName: str, indexName: str, skipCount: int, pageSize: int, keyRange: Optional[dict] = None) -> Optional[dict]:
        """
        Requests data from object store or index.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        :param indexName: Index name, empty string for object store data requests.
        :type indexName: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        :param keyRange: Key range.
        :type keyRange: Optional[dict]
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        if indexName is not None:
            msg_dict['indexName'] = indexName
        if skipCount is not None:
            msg_dict['skipCount'] = skipCount
        if pageSize is not None:
            msg_dict['pageSize'] = pageSize
        if keyRange is not None:
            msg_dict['keyRange'] = keyRange
        res = await self.chrome.send('IndexedDB.requestData', msg_dict)
        res['objectStoreDataEntries'] = Types.DataEntry.safe_create_from_list(res['objectStoreDataEntries'])
        return res

    async def requestDatabase(self, securityOrigin: str, databaseName: str) -> Optional[dict]:
        """
        Requests database with given name in given frame.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        res = await self.chrome.send('IndexedDB.requestDatabase', msg_dict)
        res['databaseWithObjectStores'] = Types.DatabaseWithObjectStores.safe_create(res['databaseWithObjectStores'])
        return res

    async def requestDatabaseNames(self, securityOrigin: str) -> Optional[dict]:
        """
        Requests database names for given security origin.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        res = await self.chrome.send('IndexedDB.requestDatabaseNames', msg_dict)
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
        return None

