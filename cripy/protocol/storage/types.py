from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

StorageType = str


class UsageForType(ChromeTypeBase):
    """Usage for a storage type."""

    def __init__(self, storageType: "StorageType", usage: float) -> None:
        """
        :param storageType: Name of storage type.
        :param usage: Storage usage (bytes).
        """
        super().__init__()
        self.storageType: StorageType = storageType
        self.usage: float = usage
