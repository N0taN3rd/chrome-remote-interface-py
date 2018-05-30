from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

DatabaseId = TypeVar("DatabaseId", str, str) # Unique identifier of Database object.


class Error(ProtocolType):
    """
    Database error.
    """

    def __init__(self, message: str, code: int) -> None:
        """
        :param message: Error message.
        :type message: str
        :param code: Error code.
        :type code: int
        """
        super().__init__()
        self.message = message
        self.code = code

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Error']:
        if init is not None:
            return Error(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Error']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Error(**it))
            return list_of_self
        else:
            return init


class Database(ProtocolType):
    """
    Database object.
    """

    def __init__(self, id: DatabaseId, domain: str, name: str, version: str) -> None:
        """
        :param id: Database ID.
        :type id: str
        :param domain: Database domain.
        :type domain: str
        :param name: Database name.
        :type name: str
        :param version: Database version.
        :type version: str
        """
        super().__init__()
        self.id = id
        self.domain = domain
        self.name = name
        self.version = version

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Database']:
        if init is not None:
            return Database(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Database']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Database(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Error": Error,
    "Database": Database,
}
