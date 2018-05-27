from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

Item = list


class StorageId(ChromeTypeBase):

    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        super().__init__()
        self.securityOrigin: str = securityOrigin
        self.isLocalStorage: bool = isLocalStorage
