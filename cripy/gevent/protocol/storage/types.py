
__all__ = ["UsageForType"]


class UsageForType(object):
    """
    Usage for a storage type.
    """

    def __init__(self, storageType, usage):
        """
        :param storageType: Name of storage type.
        :type storageType: str
        :param usage: Storage usage (bytes).
        :type usage: float
        """
        super().__init__()
        self.storageType = storageType
        self.usage = usage

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.storageType is not None:
            repr_args.append("storageType={!r}".format(self.storageType))
        if self.usage is not None:
            repr_args.append("usage={!r}".format(self.usage))
        return "UsageForType(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = UsageForType(**init)
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
                list_of_self.append(UsageForType.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"UsageForType": UsageForType}
