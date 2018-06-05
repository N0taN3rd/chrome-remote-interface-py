from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.storage.types import *
except ImportError:
    pass


class CacheStorageContentUpdatedEvent(object):
    """
    A cache's contents have been modified.
    """

    event = "Storage.cacheStorageContentUpdated"

    def __init__(self, origin: str, cacheName: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        :param cacheName: Name of cache in origin.
        :type cacheName: str
        """
        super().__init__()
        self.origin = origin
        self.cacheName = cacheName

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.cacheName is not None:
            repr_args.append("cacheName={!r}".format(self.cacheName))
        return "CacheStorageContentUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["CacheStorageContentUpdatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = CacheStorageContentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CacheStorageContentUpdatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CacheStorageContentUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class CacheStorageListUpdatedEvent(object):
    """
    A cache has been added/deleted.
    """

    event = "Storage.cacheStorageListUpdated"

    def __init__(self, origin: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin = origin

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        return "CacheStorageListUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["CacheStorageListUpdatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = CacheStorageListUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CacheStorageListUpdatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CacheStorageListUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class IndexedDBContentUpdatedEvent(object):
    """
    The origin's IndexedDB object store has been modified.
    """

    event = "Storage.indexedDBContentUpdated"

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
        self.origin = origin
        self.databaseName = databaseName
        self.objectStoreName = objectStoreName

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.databaseName is not None:
            repr_args.append("databaseName={!r}".format(self.databaseName))
        if self.objectStoreName is not None:
            repr_args.append("objectStoreName={!r}".format(self.objectStoreName))
        return "IndexedDBContentUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["IndexedDBContentUpdatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = IndexedDBContentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["IndexedDBContentUpdatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(IndexedDBContentUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class IndexedDBListUpdatedEvent(object):
    """
    The origin's IndexedDB database list has been modified.
    """

    event = "Storage.indexedDBListUpdated"

    def __init__(self, origin: str) -> None:
        """
        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin = origin

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        return "IndexedDBListUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["IndexedDBListUpdatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = IndexedDBListUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["IndexedDBListUpdatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(IndexedDBListUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Storage.cacheStorageContentUpdated": CacheStorageContentUpdatedEvent,
    "Storage.cacheStorageListUpdated": CacheStorageListUpdatedEvent,
    "Storage.indexedDBContentUpdated": IndexedDBContentUpdatedEvent,
    "Storage.indexedDBListUpdated": IndexedDBListUpdatedEvent,
}

EVENT_NS = SimpleNamespace(
    CacheStorageContentUpdated="Storage.cacheStorageContentUpdated",
    CacheStorageListUpdated="Storage.cacheStorageListUpdated",
    IndexedDBContentUpdated="Storage.indexedDBContentUpdated",
    IndexedDBListUpdated="Storage.indexedDBListUpdated",
)
