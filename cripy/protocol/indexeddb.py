# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["IndexedDB"]


@attr.dataclass(slots=True)
class IndexedDB(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["Runtime"]

    def clearObjectStore(
        self, securityOrigin: str, databaseName: str, objectStoreName: str
    ) -> Awaitable[Optional[dict]]:
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
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        if objectStoreName is not None:
            msg_dict["objectStoreName"] = objectStoreName
        return self.client.send("IndexedDB.clearObjectStore", msg_dict)

    def deleteDatabase(
        self, securityOrigin: str, databaseName: str
    ) -> Awaitable[Optional[dict]]:
        """
        Deletes a database.

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
        return self.client.send("IndexedDB.deleteDatabase", msg_dict)

    def deleteObjectStoreEntries(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        keyRange: dict,
    ) -> Awaitable[Optional[dict]]:
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
            msg_dict["securityOrigin"] = securityOrigin
        if databaseName is not None:
            msg_dict["databaseName"] = databaseName
        if objectStoreName is not None:
            msg_dict["objectStoreName"] = objectStoreName
        if keyRange is not None:
            msg_dict["keyRange"] = keyRange
        return self.client.send("IndexedDB.deleteObjectStoreEntries", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables events from backend.
        """
        return self.client.send("IndexedDB.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables events from backend.
        """
        return self.client.send("IndexedDB.enable")

    def requestData(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        indexName: str,
        skipCount: int,
        pageSize: int,
        keyRange: Optional[dict] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("IndexedDB.requestData", msg_dict)

    def requestDatabase(
        self, securityOrigin: str, databaseName: str
    ) -> Awaitable[Optional[dict]]:
        """
        Requests database with given name in given frame.

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
        return self.client.send("IndexedDB.requestDatabase", msg_dict)

    def requestDatabaseNames(self, securityOrigin: str) -> Awaitable[Optional[dict]]:
        """
        Requests database names for given security origin.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict["securityOrigin"] = securityOrigin
        return self.client.send("IndexedDB.requestDatabaseNames", msg_dict)
