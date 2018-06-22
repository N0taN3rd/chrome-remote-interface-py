
__all__ = [
    "Metric",
    "PERFORMANCE_TYPE_TO_OBJECT"
]


class Metric(object):
    """
    Run-time execution metric.
    """

    __slots__ = ["name", "value"]

    def __init__(self, name, value):
        """
        :param name: Metric name.
        :type name: str
        :param value: Metric value.
        :type value: float
        """
        super(Metric, self).__init__()
        self.name = name
        self.value = value

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "Metric(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Metric from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Metric
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Metric if creation did not fail
        :rtype: Optional[Union[dict, Metric]]
        """
        if init is not None:
            try:
                ourselves = Metric(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Metrics from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Metric instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Metric instances if creation did not fail
        :rtype: Optional[List[Union[dict, Metric]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Metric.safe_create(it))
            return list_of_self
        else:
            return init


PERFORMANCE_TYPE_TO_OBJECT = {
    "Metric": Metric,
}
