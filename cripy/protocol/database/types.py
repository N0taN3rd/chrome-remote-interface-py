from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


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
    def safe_create(init: Optional[dict]) -> Optional[Union['Error', dict]]:
        if init is not None:
            try:
                ourselves = Error(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Error', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Error.safe_create(it))
            return list_of_self
        else:
            return init


class Database(ProtocolType):
    """
    Database object.
    """

    def __init__(self, id: str, domain: str, name: str, version: str) -> None:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['Database', dict]]:
        if init is not None:
            try:
                ourselves = Database(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Database', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Database.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Error": Error,
    "Database": Database,
}
