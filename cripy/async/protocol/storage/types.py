from typing import Any, List, Optional, Union

__all__ = [
    "UsageForType",
    "STORAGE_TYPES_TO_OBJECT"
]


class UsageForType(object):
    """
    Usage for a storage type.
    """

    __slots__ = ["storageType", "usage"]

    def __init__(self, storageType: str, usage: float) -> None:
        """
        :param storageType: Name of storage type.
        :type storageType: str
        :param usage: Storage usage (bytes).
        :type usage: float
        """
        super().__init__()
        self.storageType = storageType
        self.usage = usage

    def __repr__(self) -> str:
        repr_args = []
        if self.storageType is not None:
            repr_args.append("storageType={!r}".format(self.storageType))
        if self.usage is not None:
            repr_args.append("usage={!r}".format(self.usage))
        return "UsageForType(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['UsageForType', dict]]:
        """
        Safely create UsageForType from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of UsageForType
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of UsageForType if creation did not fail
        :rtype: Optional[Union[dict, UsageForType]]
        """
        if init is not None:
            try:
                ourselves = UsageForType(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['UsageForType', dict]]]:
        """
        Safely create a new list UsageForTypes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list UsageForType instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of UsageForType instances if creation did not fail
        :rtype: Optional[List[Union[dict, UsageForType]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(UsageForType.safe_create(it))
            return list_of_self
        else:
            return init


STORAGE_TYPES_TO_OBJECT = {
    "UsageForType": UsageForType,
}
