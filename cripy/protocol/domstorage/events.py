from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DomStorageItemAddedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemAdded"

    def __init__(self) -> None:
        """
        :param storageId: The storageId
        :type StorageId:
        :param key: The key
        :type str:
        :param newValue: The newValue
        :type str:
        """
        super().__init__()


class DomStorageItemRemovedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemRemoved"

    def __init__(self) -> None:
        """
        :param storageId: The storageId
        :type StorageId:
        :param key: The key
        :type str:
        """
        super().__init__()


class DomStorageItemUpdatedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemUpdated"

    def __init__(self) -> None:
        """
        :param storageId: The storageId
        :type StorageId:
        :param key: The key
        :type str:
        :param oldValue: The oldValue
        :type str:
        :param newValue: The newValue
        :type str:
        """
        super().__init__()


class DomStorageItemsClearedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemsCleared"

    def __init__(self) -> None:
        """
        :param storageId: The storageId
        :type StorageId:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
   "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
   "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
   "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

