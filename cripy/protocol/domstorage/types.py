from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

Item = TypeVar("Item", list, list) # DOM Storage item.


class StorageId(ProtocolType):
    """
    DOM Storage identifier.
    """

    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        """
        :param securityOrigin: Security origin for the storage.
        :type securityOrigin: str
        :param isLocalStorage: Whether the storage is local storage (not session storage).
        :type isLocalStorage: bool
        """
        super().__init__()
        self.securityOrigin = securityOrigin
        self.isLocalStorage = isLocalStorage

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StorageId']:
        if init is not None:
            return StorageId(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StorageId']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StorageId(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "StorageId": StorageId,
}
