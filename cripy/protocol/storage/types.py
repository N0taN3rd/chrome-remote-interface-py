from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

StorageType = str


class UsageForType(ChromeTypeBase):

    def __init__(self, storageType: "StorageType", usage: float) -> None:
        super().__init__()
        self.storageType: StorageType = storageType
        self.usage: float = usage
