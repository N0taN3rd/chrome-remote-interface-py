from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class Domain(ProtocolType):
    """
    Description of the protocol domain.
    """

    def __init__(self, name: str, version: str) -> None:
        """
        :param name: Domain name.
        :type name: str
        :param version: Domain version.
        :type version: str
        """
        super().__init__()
        self.name = name
        self.version = version

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Domain']:
        if init is not None:
            return Domain(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Domain']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Domain(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Domain": Domain,
}
