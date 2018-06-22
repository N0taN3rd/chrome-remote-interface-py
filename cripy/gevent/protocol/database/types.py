
__all__ = [
    "Error",
    "DatabaseT",
    "DATABASE_TYPE_TO_OBJECT"
]


class Error(object):
    """
    Database error.
    """

    __slots__ = ["message", "code"]

    def __init__(self, message, code):
        """
        :param message: Error message.
        :type message: str
        :param code: Error code.
        :type code: int
        """
        super(Error, self).__init__()
        self.message = message
        self.code = code

    def __repr__(self):
        repr_args = []
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.code is not None:
            repr_args.append("code={!r}".format(self.code))
        return "Error(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Error from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Error
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Error if creation did not fail
        :rtype: Optional[Union[dict, Error]]
        """
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
        """
        Safely create a new list Errors from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Error instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Error instances if creation did not fail
        :rtype: Optional[List[Union[dict, Error]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Error.safe_create(it))
            return list_of_self
        else:
            return init


class DatabaseT(object):
    """
    Database object.
    """

    __slots__ = ["id", "domain", "name", "version"]

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
        super(DatabaseT, self).__init__()
        self.id = id
        self.domain = domain
        self.name = name
        self.version = version

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
        return "DatabaseT(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create DatabaseT from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DatabaseT
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DatabaseT if creation did not fail
        :rtype: Optional[Union[dict, DatabaseT]]
        """
        if init is not None:
            try:
                ourselves = DatabaseT(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list DatabaseTs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DatabaseT instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DatabaseT instances if creation did not fail
        :rtype: Optional[List[Union[dict, DatabaseT]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DatabaseT.safe_create(it))
            return list_of_self
        else:
            return init


DATABASE_TYPE_TO_OBJECT = {
    "Error": Error,
    "DatabaseT": DatabaseT,
}
