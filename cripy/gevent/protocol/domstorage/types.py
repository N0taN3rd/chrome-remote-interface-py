
__all__ = ["StorageId"]


class StorageId(object):
    """
    DOM Storage identifier.
    """

    def __init__(self, securityOrigin, isLocalStorage):
        """
        :param securityOrigin: Security origin for the storage.
        :type securityOrigin: str
        :param isLocalStorage: Whether the storage is local storage (not session storage).
        :type isLocalStorage: bool
        """
        super().__init__()
        self.securityOrigin = securityOrigin
        self.isLocalStorage = isLocalStorage

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.securityOrigin is not None:
            repr_args.append("securityOrigin={!r}".format(self.securityOrigin))
        if self.isLocalStorage is not None:
            repr_args.append("isLocalStorage={!r}".format(self.isLocalStorage))
        return "StorageId(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StorageId(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StorageId.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"StorageId": StorageId}
