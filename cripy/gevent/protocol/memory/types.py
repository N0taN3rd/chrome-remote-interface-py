
__all__ = [
    "SamplingProfileNode",
    "SamplingProfile",
    "MEMORY_TYPE_TO_OBJECT"
]


class SamplingProfileNode(object):
    """
    Heap profile sample.
    """

    __slots__ = ["size", "total", "stack"]

    def __init__(self, size, total, stack):
        """
        :param size: Size of the sampled allocation.
        :type size: float
        :param total: Total bytes attributed to this sample.
        :type total: float
        :param stack: Execution stack at the point of allocation.
        :type stack: List[str]
        """
        super(SamplingProfileNode, self).__init__()
        self.size = size
        self.total = total
        self.stack = stack

    def __repr__(self):
        repr_args = []
        if self.size is not None:
            repr_args.append("size={!r}".format(self.size))
        if self.total is not None:
            repr_args.append("total={!r}".format(self.total))
        if self.stack is not None:
            repr_args.append("stack={!r}".format(self.stack))
        return "SamplingProfileNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SamplingProfileNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SamplingProfileNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SamplingProfileNode if creation did not fail
        :rtype: Optional[Union[dict, SamplingProfileNode]]
        """
        if init is not None:
            try:
                ourselves = SamplingProfileNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SamplingProfileNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SamplingProfileNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SamplingProfileNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, SamplingProfileNode]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingProfileNode.safe_create(it))
            return list_of_self
        else:
            return init


class SamplingProfile(object):
    """
    Array of heap profile samples.
    """

    __slots__ = ["samples"]

    def __init__(self, samples):
        """
        :param samples: The samples
        :type samples: List[dict]
        """
        super(SamplingProfile, self).__init__()
        self.samples = SamplingProfileNode.safe_create_from_list(samples)

    def __repr__(self):
        repr_args = []
        if self.samples is not None:
            repr_args.append("samples={!r}".format(self.samples))
        return "SamplingProfile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SamplingProfile from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SamplingProfile
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SamplingProfile if creation did not fail
        :rtype: Optional[Union[dict, SamplingProfile]]
        """
        if init is not None:
            try:
                ourselves = SamplingProfile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SamplingProfiles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SamplingProfile instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SamplingProfile instances if creation did not fail
        :rtype: Optional[List[Union[dict, SamplingProfile]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingProfile.safe_create(it))
            return list_of_self
        else:
            return init


MEMORY_TYPE_TO_OBJECT = {
    "SamplingProfileNode": SamplingProfileNode,
    "SamplingProfile": SamplingProfile,
}
