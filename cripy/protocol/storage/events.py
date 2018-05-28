from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class CacheStorageContentUpdatedEvent(BaseEvent):
    """A cache's contents have been modified."""

    event: str = "Storage.cacheStorageContentUpdated"

    def __init__(self) -> None:
        """
        :param origin: Origin to update.
        :type str:
        :param cacheName: Name of cache in origin.
        :type str:
        """
        super().__init__()


class CacheStorageListUpdatedEvent(BaseEvent):
    """A cache has been added/deleted."""

    event: str = "Storage.cacheStorageListUpdated"

    def __init__(self) -> None:
        """
        :param origin: Origin to update.
        :type str:
        """
        super().__init__()


class IndexedDBContentUpdatedEvent(BaseEvent):
    """The origin's IndexedDB object store has been modified."""

    event: str = "Storage.indexedDBContentUpdated"

    def __init__(self) -> None:
        """
        :param origin: Origin to update.
        :type str:
        :param databaseName: Database to update.
        :type str:
        :param objectStoreName: ObjectStore to update.
        :type str:
        """
        super().__init__()


class IndexedDBListUpdatedEvent(BaseEvent):
    """The origin's IndexedDB database list has been modified."""

    event: str = "Storage.indexedDBListUpdated"

    def __init__(self) -> None:
        """
        :param origin: Origin to update.
        :type str:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Storage.cacheStorageContentUpdated": CacheStorageContentUpdatedEvent,
   "Storage.cacheStorageListUpdated": CacheStorageListUpdatedEvent,
   "Storage.indexedDBContentUpdated": IndexedDBContentUpdatedEvent,
   "Storage.indexedDBListUpdated": IndexedDBListUpdatedEvent,
}

