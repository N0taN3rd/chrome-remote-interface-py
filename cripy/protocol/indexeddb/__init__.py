from typing import Any, List, Optional, Union
from cripy.protocol.indexeddb import types as Types


class IndexedDB(object):
    dependencies = ["Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def clearObjectStore(
        self, securityOrigin: str, databaseName: str, objectStoreName: str
    ) -> Optional[dict]:
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        if objectStoreName is not None:
            msg_dict["objectStoreName"] = objectStoreName
        mayberes = await self.chrome.send("IndexedDB.clearObjectStore", msg_dict)
        return mayberes

    async def deleteDatabase(
        self, securityOrigin: str, databaseName: str
    ) -> Optional[dict]:
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        mayberes = await self.chrome.send("IndexedDB.deleteDatabase", msg_dict)
        return mayberes

    async def deleteObjectStoreEntries(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        keyRange: dict,
    ) -> Optional[dict]:
        """
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
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        if objectStoreName is not None:
            msg_dict["objectStoreName"] = objectStoreName
        if keyRange is not None:
            msg_dict["keyRange"] = keyRange
        mayberes = await self.chrome.send(
            "IndexedDB.deleteObjectStoreEntries", msg_dict
        )
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("IndexedDB.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("IndexedDB.enable")
        return mayberes

    async def requestData(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        indexName: str,
        skipCount: int,
        pageSize: int,
        keyRange: Optional[dict] = None,
    ) -> Optional[dict]:
        """
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
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        if objectStoreName is not None:
            msg_dict["objectStoreName"] = objectStoreName
        if indexName is not None:
            msg_dict["indexName"] = indexName
        if skipCount is not None:
            msg_dict["skipCount"] = skipCount
        if pageSize is not None:
            msg_dict["pageSize"] = pageSize
        if keyRange is not None:
            msg_dict["keyRange"] = keyRange
        mayberes = await self.chrome.send("IndexedDB.requestData", msg_dict)
        res = await mayberes
        res["objectStoreDataEntries"] = Types.DataEntry.safe_create_from_list(
            res["objectStoreDataEntries"]
        )
        return res

    async def requestDatabase(
        self, securityOrigin: str, databaseName: str
    ) -> Optional[dict]:
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        mayberes = await self.chrome.send("IndexedDB.requestDatabase", msg_dict)
        res = await mayberes
        res["databaseWithObjectStores"] = Types.DatabaseWithObjectStores.safe_create(
            res["databaseWithObjectStores"]
        )
        return res

    async def requestDatabaseNames(self, securityOrigin: str) -> Optional[dict]:
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        mayberes = await self.chrome.send("IndexedDB.requestDatabaseNames", msg_dict)
        res = await mayberes
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
