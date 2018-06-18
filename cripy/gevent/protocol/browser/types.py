
__all__ = ["Histogram", "Bucket", "Bounds"]


class Histogram(object):
    """
    Chrome histogram.
    """

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
        super().__init__()
        self.name = name
        self.sum = sum
        self.count = count
        self.buckets = Bucket.safe_create_from_list(buckets)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

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
        return "Histogram(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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

    def __init__(self, low, high, count):
        """
        :param low: Minimum value (inclusive).
        :type low: int
        :param high: Maximum value (exclusive).
        :type high: int
        :param count: Number of samples.
        :type count: int
        """
        super().__init__()
        self.low = low
        self.high = high
        self.count = count

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.low is not None:
            repr_args.append("low={!r}".format(self.low))
        if self.high is not None:
            repr_args.append("high={!r}".format(self.high))
        if self.count is not None:
            repr_args.append("count={!r}".format(self.count))
        return "Bucket(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        super().__init__()
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.windowState = windowState

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

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
        return "Bounds(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Bounds.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"Histogram": Histogram, "Bucket": Bucket, "Bounds": Bounds}
