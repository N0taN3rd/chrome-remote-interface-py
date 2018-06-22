
__all__ = [
    "Domain",
    "SCHEMA_TYPE_TO_OBJECT"
]


class Domain(object):
    """
    Description of the protocol domain.
    """

    __slots__ = ["name", "version"]

    def __init__(self, name, version):
        """
        :param name: Domain name.
        :type name: str
        :param version: Domain version.
        :type version: str
        """
        super(Domain, self).__init__()
        self.name = name
        self.version = version

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.version is not None:
            repr_args.append("version={!r}".format(self.version))
        return "Domain(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Domain from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Domain
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Domain if creation did not fail
        :rtype: Optional[Union[dict, Domain]]
        """
        if init is not None:
            try:
                ourselves = Domain(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Domains from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Domain instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Domain instances if creation did not fail
        :rtype: Optional[List[Union[dict, Domain]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Domain.safe_create(it))
            return list_of_self
        else:
            return init


SCHEMA_TYPE_TO_OBJECT = {
    "Domain": Domain,
}
