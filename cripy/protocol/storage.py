"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Storage"]


class Storage:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Storage`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Storage

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clearDataForOrigin(self, origin: str, storageTypes: str) -> Awaitable[Dict]:
        """
        Clears storage for origin.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-clearDataForOrigin`

        :param origin: Security origin.
        :param storageTypes: Comma separated list of StorageType to clear.
        :return: The results of the command
        """
        return self.client.send(
            "Storage.clearDataForOrigin",
            {"origin": origin, "storageTypes": storageTypes},
        )

    def getUsageAndQuota(self, origin: str) -> Awaitable[Dict]:
        """
        Returns usage and quota in bytes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-getUsageAndQuota`

        :param origin: Security origin.
        :return: The results of the command
        """
        return self.client.send("Storage.getUsageAndQuota", {"origin": origin})

    def trackCacheStorageForOrigin(self, origin: str) -> Awaitable[Dict]:
        """
        Registers origin to be notified when an update occurs to its cache storage list.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-trackCacheStorageForOrigin`

        :param origin: Security origin.
        :return: The results of the command
        """
        return self.client.send(
            "Storage.trackCacheStorageForOrigin", {"origin": origin}
        )

    def trackIndexedDBForOrigin(self, origin: str) -> Awaitable[Dict]:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-trackIndexedDBForOrigin`

        :param origin: Security origin.
        :return: The results of the command
        """
        return self.client.send("Storage.trackIndexedDBForOrigin", {"origin": origin})

    def untrackCacheStorageForOrigin(self, origin: str) -> Awaitable[Dict]:
        """
        Unregisters origin from receiving notifications for cache storage.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-untrackCacheStorageForOrigin`

        :param origin: Security origin.
        :return: The results of the command
        """
        return self.client.send(
            "Storage.untrackCacheStorageForOrigin", {"origin": origin}
        )

    def untrackIndexedDBForOrigin(self, origin: str) -> Awaitable[Dict]:
        """
        Unregisters origin from receiving notifications for IndexedDB.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#method-untrackIndexedDBForOrigin`

        :param origin: Security origin.
        :return: The results of the command
        """
        return self.client.send("Storage.untrackIndexedDBForOrigin", {"origin": origin})

    def cacheStorageContentUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        A cache's contents have been modified.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#event-cacheStorageContentUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Storage.cacheStorageContentUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def cacheStorageListUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        A cache has been added/deleted.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#event-cacheStorageListUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Storage.cacheStorageListUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def indexedDBContentUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        The origin's IndexedDB object store has been modified.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#event-indexedDBContentUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Storage.indexedDBContentUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def indexedDBListUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        The origin's IndexedDB database list has been modified.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Storage#event-indexedDBListUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Storage.indexedDBListUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
