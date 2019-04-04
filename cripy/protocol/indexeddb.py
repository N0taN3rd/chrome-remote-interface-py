"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["IndexedDB"]


class IndexedDB:
    """
    Domain Dependencies: 
      * Runtime
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of IndexedDB

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clearObjectStore(
        self, securityOrigin: str, databaseName: str, objectStoreName: str
    ) -> Awaitable[Dict]:
        """
        Clears all entries from an object store.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-clearObjectStore`

        :param securityOrigin: Security origin.
        :param databaseName: Database name.
        :param objectStoreName: Object store name.
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.clearObjectStore",
            {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
                "objectStoreName": objectStoreName,
            },
        )

    def deleteDatabase(self, securityOrigin: str, databaseName: str) -> Awaitable[Dict]:
        """
        Deletes a database.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-deleteDatabase`

        :param securityOrigin: Security origin.
        :param databaseName: Database name.
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.deleteDatabase",
            {"securityOrigin": securityOrigin, "databaseName": databaseName},
        )

    def deleteObjectStoreEntries(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        keyRange: Dict[str, Any],
    ) -> Awaitable[Dict]:
        """
        Delete a range of entries from an object store

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-deleteObjectStoreEntries`

        :param securityOrigin: The securityOrigin
        :param databaseName: The databaseName
        :param objectStoreName: The objectStoreName
        :param keyRange: Range of entry keys to delete
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.deleteObjectStoreEntries",
            {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
                "objectStoreName": objectStoreName,
                "keyRange": keyRange,
            },
        )

    def disable(self) -> Awaitable[Dict]:
        """
        Disables events from backend.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-disable`

        :return: The results of the command
        """
        return self.client.send("IndexedDB.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables events from backend.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-enable`

        :return: The results of the command
        """
        return self.client.send("IndexedDB.enable", {})

    def requestData(
        self,
        securityOrigin: str,
        databaseName: str,
        objectStoreName: str,
        indexName: str,
        skipCount: int,
        pageSize: int,
        keyRange: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Requests data from object store or index.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-requestData`

        :param securityOrigin: Security origin.
        :param databaseName: Database name.
        :param objectStoreName: Object store name.
        :param indexName: Index name, empty string for object store data requests.
        :param skipCount: Number of records to skip.
        :param pageSize: Number of records to fetch.
        :param keyRange: Key range.
        :return: The results of the command
        """
        msg = {
            "securityOrigin": securityOrigin,
            "databaseName": databaseName,
            "objectStoreName": objectStoreName,
            "indexName": indexName,
            "skipCount": skipCount,
            "pageSize": pageSize,
        }
        if keyRange is not None:
            msg["keyRange"] = keyRange
        return self.client.send("IndexedDB.requestData", msg)

    def getMetadata(
        self, securityOrigin: str, databaseName: str, objectStoreName: str
    ) -> Awaitable[Dict]:
        """
        Gets metadata of an object store

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-getMetadata`

        :param securityOrigin: Security origin.
        :param databaseName: Database name.
        :param objectStoreName: Object store name.
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.getMetadata",
            {
                "securityOrigin": securityOrigin,
                "databaseName": databaseName,
                "objectStoreName": objectStoreName,
            },
        )

    def requestDatabase(
        self, securityOrigin: str, databaseName: str
    ) -> Awaitable[Dict]:
        """
        Requests database with given name in given frame.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-requestDatabase`

        :param securityOrigin: Security origin.
        :param databaseName: Database name.
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.requestDatabase",
            {"securityOrigin": securityOrigin, "databaseName": databaseName},
        )

    def requestDatabaseNames(self, securityOrigin: str) -> Awaitable[Dict]:
        """
        Requests database names for given security origin.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IndexedDB#method-requestDatabaseNames`

        :param securityOrigin: Security origin.
        :return: The results of the command
        """
        return self.client.send(
            "IndexedDB.requestDatabaseNames", {"securityOrigin": securityOrigin}
        )
