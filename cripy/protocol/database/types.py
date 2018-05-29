from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType

DatabaseId = TypeVar("DatabaseId", str, str)
"""Unique identifier of Database object."""


class Error(ProtocolType):
    """Database error."""

    def __init__(self, message: str, code: int) -> None:
        """
        :param message: Error message.
        :type message: str
        :param code: Error code.
        :type code: int
        """
        super().__init__()
        self.message: str = message
        self.code: int = code


class Database(ProtocolType):
    """Database object."""

    def __init__(self, id: "DatabaseId", domain: str, name: str, version: str) -> None:
        """
        :param id: Database ID.
        :type id: DatabaseId
        :param domain: Database domain.
        :type domain: str
        :param name: Database name.
        :type name: str
        :param version: Database version.
        :type version: str
        """
        super().__init__()
        self.id: DatabaseId = id
        self.domain: str = domain
        self.name: str = name
        self.version: str = version


OBJECT_LIST = {"Error": Error, "Database": Database}
