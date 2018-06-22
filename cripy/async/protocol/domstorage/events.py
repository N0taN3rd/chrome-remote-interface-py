from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.domstorage.types import *

__all__ = [
    "DomStorageItemAddedEvent",
    "DomStorageItemRemovedEvent",
    "DomStorageItemUpdatedEvent",
    "DomStorageItemsClearedEvent",
    "DOMSTORAGE_EVENTS_TO_CLASS",
    "DOMSTORAGE_EVENTS_NS"
]

class DomStorageItemAddedEvent(object):

    event = "DOMStorage.domStorageItemAdded"

    __slots__ = ["storageId", "key", "newValue"]

    def __init__(self, storageId: Union[StorageId, dict], key: str, newValue: str) -> None:
        """
        Create a new instance of DomStorageItemAddedEvent

        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key
        self.newValue = newValue

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.newValue is not None:
            repr_args.append("newValue={!r}".format(self.newValue))
        return "DomStorageItemAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DomStorageItemAddedEvent', dict]]:
        """
        Safely create DomStorageItemAddedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DomStorageItemAddedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DomStorageItemAddedEvent if creation did not fail
        :rtype: Optional[Union[dict, DomStorageItemAddedEvent]]
        """
        if init is not None:
            try:
                ourselves = DomStorageItemAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DomStorageItemAddedEvent', dict]]]:
        """
        Safely create a new list DomStorageItemAddedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DomStorageItemAddedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DomStorageItemAddedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DomStorageItemAddedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemRemovedEvent(object):

    event = "DOMStorage.domStorageItemRemoved"

    __slots__ = ["storageId", "key"]

    def __init__(self, storageId: Union[StorageId, dict], key: str) -> None:
        """
        Create a new instance of DomStorageItemRemovedEvent

        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        return "DomStorageItemRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DomStorageItemRemovedEvent', dict]]:
        """
        Safely create DomStorageItemRemovedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DomStorageItemRemovedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DomStorageItemRemovedEvent if creation did not fail
        :rtype: Optional[Union[dict, DomStorageItemRemovedEvent]]
        """
        if init is not None:
            try:
                ourselves = DomStorageItemRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DomStorageItemRemovedEvent', dict]]]:
        """
        Safely create a new list DomStorageItemRemovedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DomStorageItemRemovedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DomStorageItemRemovedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DomStorageItemRemovedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemUpdatedEvent(object):

    event = "DOMStorage.domStorageItemUpdated"

    __slots__ = ["storageId", "key", "oldValue", "newValue"]

    def __init__(self, storageId: Union[StorageId, dict], key: str, oldValue: str, newValue: str) -> None:
        """
        Create a new instance of DomStorageItemUpdatedEvent

        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param oldValue: The oldValue
        :type oldValue: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key
        self.oldValue = oldValue
        self.newValue = newValue

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.oldValue is not None:
            repr_args.append("oldValue={!r}".format(self.oldValue))
        if self.newValue is not None:
            repr_args.append("newValue={!r}".format(self.newValue))
        return "DomStorageItemUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DomStorageItemUpdatedEvent', dict]]:
        """
        Safely create DomStorageItemUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DomStorageItemUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DomStorageItemUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, DomStorageItemUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = DomStorageItemUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DomStorageItemUpdatedEvent', dict]]]:
        """
        Safely create a new list DomStorageItemUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DomStorageItemUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DomStorageItemUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DomStorageItemUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DomStorageItemsClearedEvent(object):

    event = "DOMStorage.domStorageItemsCleared"

    __slots__ = ["storageId"]

    def __init__(self, storageId: Union[StorageId, dict]) -> None:
        """
        Create a new instance of DomStorageItemsClearedEvent

        :param storageId: The storageId
        :type storageId: dict
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)

    def __repr__(self) -> str:
        repr_args = []
        if self.storageId is not None:
            repr_args.append("storageId={!r}".format(self.storageId))
        return "DomStorageItemsClearedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DomStorageItemsClearedEvent', dict]]:
        """
        Safely create DomStorageItemsClearedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DomStorageItemsClearedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DomStorageItemsClearedEvent if creation did not fail
        :rtype: Optional[Union[dict, DomStorageItemsClearedEvent]]
        """
        if init is not None:
            try:
                ourselves = DomStorageItemsClearedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DomStorageItemsClearedEvent', dict]]]:
        """
        Safely create a new list DomStorageItemsClearedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DomStorageItemsClearedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DomStorageItemsClearedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DomStorageItemsClearedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemsClearedEvent.safe_create(it))
            return list_of_self
        else:
            return init


DOMSTORAGE_EVENTS_TO_CLASS = {
   "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
   "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
   "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
   "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

DOMStorageNS = namedtuple("DOMStorageNS", ["DomStorageItemAdded", "DomStorageItemRemoved", "DomStorageItemUpdated", "DomStorageItemsCleared"])

DOMSTORAGE_EVENTS_NS = DOMStorageNS(
  DomStorageItemAdded="DOMStorage.domStorageItemAdded",
  DomStorageItemRemoved="DOMStorage.domStorageItemRemoved",
  DomStorageItemUpdated="DOMStorage.domStorageItemUpdated",
  DomStorageItemsCleared="DOMStorage.domStorageItemsCleared",
)
