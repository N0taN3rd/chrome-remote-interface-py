from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# Unique identifier of Database object.
DatabaseId = str


class Database(ChromeTypeBase):
    """Database object."""

    def __init__(self, id: 'DatabaseId', domain: str, name: str, version: str) -> None:
        """
        :param id: Database ID.
        :type DatabaseId:
        :param domain: Database domain.
        :type str:
        :param name: Database name.
        :type str:
        :param version: Database version.
        :type str:
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
        :type str:
        :param code: Error code.
        :type int:
        """
        super().__init__()
        self.message: str = message
        self.code: int = code


