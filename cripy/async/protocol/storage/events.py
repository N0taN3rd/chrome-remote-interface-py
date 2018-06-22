from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.storage.types import *

__all__ = [
    "CacheStorageContentUpdatedEvent",
    "CacheStorageListUpdatedEvent",
    "IndexedDBContentUpdatedEvent",
    "IndexedDBListUpdatedEvent",
    "STORAGE_EVENTS_TO_CLASS",
    "STORAGE_EVENTS_NS"
]

class CacheStorageContentUpdatedEvent(object):
    """
    A cache's contents have been modified.
    """

    event = "Storage.cacheStorageContentUpdated"

    __slots__ = ["origin", "cacheName"]

    def __init__(self, origin: str, cacheName: str) -> None:
        """
        Create a new instance of CacheStorageContentUpdatedEvent

        :param origin: Origin to update.
        :type origin: str
        :param cacheName: Name of cache in origin.
        :type cacheName: str
        """
        super().__init__()
        self.origin = origin
        self.cacheName = cacheName

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.cacheName is not None:
            repr_args.append("cacheName={!r}".format(self.cacheName))
        return "CacheStorageContentUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CacheStorageContentUpdatedEvent', dict]]:
        """
        Safely create CacheStorageContentUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CacheStorageContentUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CacheStorageContentUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, CacheStorageContentUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = CacheStorageContentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CacheStorageContentUpdatedEvent', dict]]]:
        """
        Safely create a new list CacheStorageContentUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CacheStorageContentUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CacheStorageContentUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, CacheStorageContentUpdatedEvent]]]
        """
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

    __slots__ = ["origin"]

    def __init__(self, origin: str) -> None:
        """
        Create a new instance of CacheStorageListUpdatedEvent

        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin = origin

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        return "CacheStorageListUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CacheStorageListUpdatedEvent', dict]]:
        """
        Safely create CacheStorageListUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CacheStorageListUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CacheStorageListUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, CacheStorageListUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = CacheStorageListUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CacheStorageListUpdatedEvent', dict]]]:
        """
        Safely create a new list CacheStorageListUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CacheStorageListUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CacheStorageListUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, CacheStorageListUpdatedEvent]]]
        """
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

    __slots__ = ["origin", "databaseName", "objectStoreName"]

    def __init__(self, origin: str, databaseName: str, objectStoreName: str) -> None:
        """
        Create a new instance of IndexedDBContentUpdatedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.databaseName is not None:
            repr_args.append("databaseName={!r}".format(self.databaseName))
        if self.objectStoreName is not None:
            repr_args.append("objectStoreName={!r}".format(self.objectStoreName))
        return "IndexedDBContentUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['IndexedDBContentUpdatedEvent', dict]]:
        """
        Safely create IndexedDBContentUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of IndexedDBContentUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of IndexedDBContentUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, IndexedDBContentUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = IndexedDBContentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['IndexedDBContentUpdatedEvent', dict]]]:
        """
        Safely create a new list IndexedDBContentUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list IndexedDBContentUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of IndexedDBContentUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, IndexedDBContentUpdatedEvent]]]
        """
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

    __slots__ = ["origin"]

    def __init__(self, origin: str) -> None:
        """
        Create a new instance of IndexedDBListUpdatedEvent

        :param origin: Origin to update.
        :type origin: str
        """
        super().__init__()
        self.origin = origin

    def __repr__(self) -> str:
        repr_args = []
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        return "IndexedDBListUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['IndexedDBListUpdatedEvent', dict]]:
        """
        Safely create IndexedDBListUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of IndexedDBListUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of IndexedDBListUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, IndexedDBListUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = IndexedDBListUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['IndexedDBListUpdatedEvent', dict]]]:
        """
        Safely create a new list IndexedDBListUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list IndexedDBListUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of IndexedDBListUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, IndexedDBListUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(IndexedDBListUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


STORAGE_EVENTS_TO_CLASS = {
   "Storage.cacheStorageContentUpdated": CacheStorageContentUpdatedEvent,
   "Storage.cacheStorageListUpdated": CacheStorageListUpdatedEvent,
   "Storage.indexedDBContentUpdated": IndexedDBContentUpdatedEvent,
   "Storage.indexedDBListUpdated": IndexedDBListUpdatedEvent,
}

StorageNS = namedtuple("StorageNS", ["CacheStorageContentUpdated", "CacheStorageListUpdated", "IndexedDBContentUpdated", "IndexedDBListUpdated"])

STORAGE_EVENTS_NS = StorageNS(
  CacheStorageContentUpdated="Storage.cacheStorageContentUpdated",
  CacheStorageListUpdated="Storage.cacheStorageListUpdated",
  IndexedDBContentUpdated="Storage.indexedDBContentUpdated",
  IndexedDBListUpdated="Storage.indexedDBListUpdated",
)
