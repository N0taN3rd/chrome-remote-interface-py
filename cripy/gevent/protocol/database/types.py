
__all__ = ["Error", "Database"]


class Error(object):
    """
    Database error.
    """

    def __init__(self, message, code):
        """
        :param message: Error message.
        :type message: str
        :param code: Error code.
        :type code: int
        """
        super().__init__()
        self.message = message
        self.code = code

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.code is not None:
            repr_args.append("code={!r}".format(self.code))
        return "Error(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Error(**init)
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
                list_of_self.append(Error.safe_create(it))
            return list_of_self
        else:
            return init


class Database(object):
    """
    Database object.
    """

    def __init__(self, id, domain, name, version):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.domain is not None:
            repr_args.append("domain={!r}".format(self.domain))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.version is not None:
            repr_args.append("version={!r}".format(self.version))
        return "Database(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Database(**init)
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
                list_of_self.append(Database.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"Error": Error, "Database": Database}
