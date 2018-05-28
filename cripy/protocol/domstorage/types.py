from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

Item = TypeVar("Item", list, list)
"""DOM Storage item."""


class StorageId(ChromeTypeBase):
    """DOM Storage identifier."""
    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        """
        :param securityOrigin: Security origin for the storage.
        :type securityOrigin: str
        :param isLocalStorage: Whether the storage is local storage (not session storage).
        :type isLocalStorage: bool
        """
        super().__init__()
        self.securityOrigin: str = securityOrigin
        self.isLocalStorage: bool = isLocalStorage


