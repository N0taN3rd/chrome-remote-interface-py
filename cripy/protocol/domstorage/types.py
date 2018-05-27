from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

Item = list


class StorageId(ChromeTypeBase):
    """DOM Storage identifier."""

    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        """
        :param securityOrigin: Security origin for the storage.
        :param isLocalStorage: Whether the storage is local storage (not session storage).
        """
        super().__init__()
        self.securityOrigin: str = securityOrigin
        self.isLocalStorage: bool = isLocalStorage
