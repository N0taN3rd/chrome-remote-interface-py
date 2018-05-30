from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.domstorage.types import (
    StorageId,
)


class DomStorageItemAddedEvent(BaseEvent):

    event = "DOMStorage.domStorageItemAdded"

    def __init__(self, storageId: Union[StorageId, dict], key: str, newValue: str) -> None:
        """
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DomStorageItemAddedEvent']:
        if init is not None:
            return DomStorageItemAddedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DomStorageItemAddedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemAddedEvent(**it))
            return list_of_self
        else:
            return init


class DomStorageItemRemovedEvent(BaseEvent):

    event = "DOMStorage.domStorageItemRemoved"

    def __init__(self, storageId: Union[StorageId, dict], key: str) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)
        self.key = key

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DomStorageItemRemovedEvent']:
        if init is not None:
            return DomStorageItemRemovedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DomStorageItemRemovedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemRemovedEvent(**it))
            return list_of_self
        else:
            return init


class DomStorageItemUpdatedEvent(BaseEvent):

    event = "DOMStorage.domStorageItemUpdated"

    def __init__(self, storageId: Union[StorageId, dict], key: str, oldValue: str, newValue: str) -> None:
        """
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DomStorageItemUpdatedEvent']:
        if init is not None:
            return DomStorageItemUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DomStorageItemUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class DomStorageItemsClearedEvent(BaseEvent):

    event = "DOMStorage.domStorageItemsCleared"

    def __init__(self, storageId: Union[StorageId, dict]) -> None:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        super().__init__()
        self.storageId = StorageId.safe_create(storageId)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DomStorageItemsClearedEvent']:
        if init is not None:
            return DomStorageItemsClearedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DomStorageItemsClearedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomStorageItemsClearedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "DOMStorage.domStorageItemAdded": DomStorageItemAddedEvent,
   "DOMStorage.domStorageItemRemoved": DomStorageItemRemovedEvent,
   "DOMStorage.domStorageItemUpdated": DomStorageItemUpdatedEvent,
   "DOMStorage.domStorageItemsCleared": DomStorageItemsClearedEvent,
}

