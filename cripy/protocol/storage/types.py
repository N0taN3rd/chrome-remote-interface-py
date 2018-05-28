from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

StorageType = TypeVar("StorageType", str, str)
"""Enum of possible storage types."""


class UsageForType(ChromeTypeBase):
    """Usage for a storage type."""
    def __init__(self, storageType: 'StorageType', usage: float) -> None:
        """
        :param storageType: Name of storage type.
        :type storageType: StorageType
        :param usage: Storage usage (bytes).
        :type usage: float
        """
        super().__init__()
        self.storageType: StorageType = storageType
        self.usage: float = usage


