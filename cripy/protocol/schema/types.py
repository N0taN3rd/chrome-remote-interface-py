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
    def safe_create(init: Optional[dict]) -> Optional[Union['Domain', dict]]:
        if init is not None:
            try:
                ourselves = Domain(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Domain', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Domain.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Domain": Domain,
}
