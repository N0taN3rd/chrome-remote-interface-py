from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

DatabaseId = str


class Database(ChromeTypeBase):
    """Database object."""

    def __init__(self, id: "DatabaseId", domain: str, name: str, version: str) -> None:
        """
        :param id: Database ID.
        :param domain: Database domain.
        :param name: Database name.
        :param version: Database version.
        """
        super().__init__()
        self.id: DatabaseId = id
        self.domain: str = domain
        self.name: str = name
        self.version: str = version


class Error(ChromeTypeBase):
    """Database error."""

    def __init__(self, message: str, code: int) -> None:
        """
        :param message: Error message.
        :param code: Error code.
        """
        super().__init__()
        self.message: str = message
        self.code: int = code
