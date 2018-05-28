from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.domstorage.types import (
    StorageId,
)


class DomStorageItemAddedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemAdded"

    def __init__(self, storageId: StorageId, key: str, newValue: str) -> None:
        """
        :param storageId: The storageId
        :type storageId: StorageId
        :param key: The key
        :type key: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId: StorageId = storageId
        self.key: str = key
        self.newValue: str = newValue


class DomStorageItemRemovedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemRemoved"

    def __init__(self, storageId: StorageId, key: str) -> None:
        """
        :param storageId: The storageId
        :type storageId: StorageId
        :param key: The key
        :type key: str
        """
        super().__init__()
        self.storageId: StorageId = storageId
        self.key: str = key


class DomStorageItemUpdatedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemUpdated"

    def __init__(self, storageId: StorageId, key: str, oldValue: str, newValue: str) -> None:
        """
        :param storageId: The storageId
        :type storageId: StorageId
        :param key: The key
        :type key: str
        :param oldValue: The oldValue
        :type oldValue: str
        :param newValue: The newValue
        :type newValue: str
        """
        super().__init__()
        self.storageId: StorageId = storageId
        self.key: str = key
        self.oldValue: str = oldValue
        self.newValue: str = newValue


class DomStorageItemsClearedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemsCleared"

    def __init__(self, storageId: StorageId) -> None:
        """
        :param storageId: The storageId
        :type storageId: StorageId
        """
        super().__init__()
        self.storageId: StorageId = storageId


EVENT_TO_CLASS = {
   "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
   "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
   "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
   "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

