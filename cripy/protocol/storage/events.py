from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class CacheStorageContentUpdatedEvent(BaseEvent):
    """A cache's contents have been modified."""

    event: str = "Storage.cacheStorageContentUpdated"

    def __init__(self, origin: str, cacheName: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        :param cacheName: Name of cache in origin.
        :type cacheName: str
        """
        super().__init__()
        self.origin: str = origin
        self.cacheName: str = cacheName


class CacheStorageListUpdatedEvent(BaseEvent):
    """A cache has been added/deleted."""

    event: str = "Storage.cacheStorageListUpdated"

    def __init__(self, origin: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin: str = origin


class IndexedDBContentUpdatedEvent(BaseEvent):
    """The origin's IndexedDB object store has been modified."""

    event: str = "Storage.indexedDBContentUpdated"

    def __init__(self, origin: str, databaseName: str, objectStoreName: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        :param databaseName: Database to update.
        :type databaseName: str
        :param objectStoreName: ObjectStore to update.
        :type objectStoreName: str
        """
        super().__init__()
        self.origin: str = origin
        self.databaseName: str = databaseName
        self.objectStoreName: str = objectStoreName


class IndexedDBListUpdatedEvent(BaseEvent):
    """The origin's IndexedDB database list has been modified."""

    event: str = "Storage.indexedDBListUpdated"

    def __init__(self, origin: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin: str = origin


EVENT_TO_CLASS = {
   "Storage.cacheStorageContentUpdated": CacheStorageContentUpdatedEvent,
   "Storage.cacheStorageListUpdated": CacheStorageListUpdatedEvent,
   "Storage.indexedDBContentUpdated": IndexedDBContentUpdatedEvent,
   "Storage.indexedDBListUpdated": IndexedDBListUpdatedEvent,
}

