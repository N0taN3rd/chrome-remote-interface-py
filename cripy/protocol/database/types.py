from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# Unique identifier of Database object.
DatabaseId = str


class Database(ChromeTypeBase):
    """Database object."""
    def __init__(self, id: 'DatabaseId', domain: str, name: str, version: str) -> None:
        """
        :param DatabaseId id: Database ID.
        :param str domain: Database domain.
        :param str name: Database name.
        :param str version: Database version.
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
        :param str message: Error message.
        :param int code: Error code.
        """
        super().__init__()
        self.message: str = message
        self.code: int = code


