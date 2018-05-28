from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DomStorageItemAddedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemAdded"

    def __init__(self) -> None:
        """
        :param StorageId storageId: The storageId
        :type storageId: StorageId
        :param str key: The key
        :type key: str
        :param str newValue: The newValue
        :type newValue: str
        """
        super().__init__()


class DomStorageItemRemovedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemRemoved"

    def __init__(self) -> None:
        """
        :param StorageId storageId: The storageId
        :type storageId: StorageId
        :param str key: The key
        :type key: str
        """
        super().__init__()


class DomStorageItemUpdatedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemUpdated"

    def __init__(self) -> None:
        """
        :param StorageId storageId: The storageId
        :type storageId: StorageId
        :param str key: The key
        :type key: str
        :param str oldValue: The oldValue
        :type oldValue: str
        :param str newValue: The newValue
        :type newValue: str
        """
        super().__init__()


class DomStorageItemsClearedEvent(BaseEvent):

    event: str = "DOMStorage.domStorageItemsCleared"

    def __init__(self) -> None:
        """
        :param StorageId storageId: The storageId
        :type storageId: StorageId
        """
        super().__init__()


EVENT_TO_CLASS = {
   "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
   "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
   "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
   "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

