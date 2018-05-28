from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# DOM Storage item.
Item = list


class StorageId(ChromeTypeBase):
    """DOM Storage identifier."""
    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        """
        :param str securityOrigin: Security origin for the storage.
        :param bool isLocalStorage: Whether the storage is local storage (not session storage).
        """
        super().__init__()
        self.securityOrigin: str = securityOrigin
        self.isLocalStorage: bool = isLocalStorage


