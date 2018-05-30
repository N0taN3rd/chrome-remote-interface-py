from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

StorageType = TypeVar("StorageType", str, str) # Enum of possible storage types.


class UsageForType(ProtocolType):
    """
    Usage for a storage type.
    """

    def __init__(self, storageType: StorageType, usage: float) -> None:
        """
        :param storageType: Name of storage type.
        :type storageType: str
        :param usage: Storage usage (bytes).
        :type usage: float
        """
        super().__init__()
        self.storageType = storageType
        self.usage = usage

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['UsageForType']:
        if init is not None:
            return UsageForType(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['UsageForType']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(UsageForType(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "UsageForType": UsageForType,
}
