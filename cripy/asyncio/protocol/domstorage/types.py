from typing import Any, List, Optional, Union

__all__ = [
    "StorageId",
    "DOMSTORAGE_TYPES_TO_OBJECT"
]


class StorageId(object):
    """
    DOM Storage identifier.
    """

    __slots__ = ["securityOrigin", "isLocalStorage"]

    def __init__(self, securityOrigin: str, isLocalStorage: bool) -> None:
        """
        :param securityOrigin: Security origin for the storage.
        :type securityOrigin: str
        :param isLocalStorage: Whether the storage is local storage (not session storage).
        :type isLocalStorage: bool
        """
        super().__init__()
        self.securityOrigin = securityOrigin
        self.isLocalStorage = isLocalStorage

    def __repr__(self) -> str:
        repr_args = []
        if self.securityOrigin is not None:
            repr_args.append("securityOrigin={!r}".format(self.securityOrigin))
        if self.isLocalStorage is not None:
            repr_args.append("isLocalStorage={!r}".format(self.isLocalStorage))
        return "StorageId(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StorageId', dict]]:
        """
        Safely create StorageId from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of StorageId
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of StorageId if creation did not fail
        :rtype: Optional[Union[dict, StorageId]]
        """
        if init is not None:
            try:
                ourselves = StorageId(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['StorageId', dict]]]:
        """
        Safely create a new list StorageIds from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list StorageId instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of StorageId instances if creation did not fail
        :rtype: Optional[List[Union[dict, StorageId]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StorageId.safe_create(it))
            return list_of_self
        else:
            return init


DOMSTORAGE_TYPES_TO_OBJECT = {
    "StorageId": StorageId,
}
