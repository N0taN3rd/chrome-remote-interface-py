
__all__ = [
    "Histogram",
    "Bucket",
    "Bounds",
    "BROWSER_TYPE_TO_OBJECT"
]


class Histogram(object):
    """
    Chrome histogram.
    """

    __slots__ = ["name", "sum", "count", "buckets"]

    def __init__(self, name, sum, count, buckets):
        """
        :param name: Name.
        :type name: str
        :param sum: Sum of sample values.
        :type sum: int
        :param count: Total number of samples.
        :type count: int
        :param buckets: Buckets.
        :type buckets: List[dict]
        """
        super(Histogram, self).__init__()
        self.name = name
        self.sum = sum
        self.count = count
        self.buckets = Bucket.safe_create_from_list(buckets)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.sum is not None:
            repr_args.append("sum={!r}".format(self.sum))
        if self.count is not None:
            repr_args.append("count={!r}".format(self.count))
        if self.buckets is not None:
            repr_args.append("buckets={!r}".format(self.buckets))
        return "Histogram(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Histogram from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Histogram
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Histogram if creation did not fail
        :rtype: Optional[Union[dict, Histogram]]
        """
        if init is not None:
            try:
                ourselves = Histogram(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Histograms from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Histogram instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Histogram instances if creation did not fail
        :rtype: Optional[List[Union[dict, Histogram]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Histogram.safe_create(it))
            return list_of_self
        else:
            return init


class Bucket(object):
    """
    Chrome histogram bucket.
    """

    __slots__ = ["low", "high", "count"]

    def __init__(self, low, high, count):
        """
        :param low: Minimum value (inclusive).
        :type low: int
        :param high: Maximum value (exclusive).
        :type high: int
        :param count: Number of samples.
        :type count: int
        """
        super(Bucket, self).__init__()
        self.low = low
        self.high = high
        self.count = count

    def __repr__(self):
        repr_args = []
        if self.low is not None:
            repr_args.append("low={!r}".format(self.low))
        if self.high is not None:
            repr_args.append("high={!r}".format(self.high))
        if self.count is not None:
            repr_args.append("count={!r}".format(self.count))
        return "Bucket(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Bucket from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Bucket
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Bucket if creation did not fail
        :rtype: Optional[Union[dict, Bucket]]
        """
        if init is not None:
            try:
                ourselves = Bucket(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Buckets from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Bucket instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Bucket instances if creation did not fail
        :rtype: Optional[List[Union[dict, Bucket]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Bucket.safe_create(it))
            return list_of_self
        else:
            return init


class Bounds(object):
    """
    Browser window bounds information
    """

    __slots__ = ["left", "top", "width", "height", "windowState"]

    def __init__(self, left=None, top=None, width=None, height=None, windowState=None):
        """
        :param left: The offset from the left edge of the screen to the window in pixels.
        :type left: Optional[int]
        :param top: The offset from the top edge of the screen to the window in pixels.
        :type top: Optional[int]
        :param width: The window width in pixels.
        :type width: Optional[int]
        :param height: The window height in pixels.
        :type height: Optional[int]
        :param windowState: The window state. Default to normal.
        :type windowState: Optional[str]
        """
        super(Bounds, self).__init__()
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.windowState = windowState

    def __repr__(self):
        repr_args = []
        if self.left is not None:
            repr_args.append("left={!r}".format(self.left))
        if self.top is not None:
            repr_args.append("top={!r}".format(self.top))
        if self.width is not None:
            repr_args.append("width={!r}".format(self.width))
        if self.height is not None:
            repr_args.append("height={!r}".format(self.height))
        if self.windowState is not None:
            repr_args.append("windowState={!r}".format(self.windowState))
        return "Bounds(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Bounds from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Bounds
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Bounds if creation did not fail
        :rtype: Optional[Union[dict, Bounds]]
        """
        if init is not None:
            try:
                ourselves = Bounds(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Boundss from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Bounds instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Bounds instances if creation did not fail
        :rtype: Optional[List[Union[dict, Bounds]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Bounds.safe_create(it))
            return list_of_self
        else:
            return init


BROWSER_TYPE_TO_OBJECT = {
    "Histogram": Histogram,
    "Bucket": Bucket,
    "Bounds": Bounds,
}
