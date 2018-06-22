
__all__ = [
    "ScreenshotParams",
    "HEADLESSEXPERIMENTAL_TYPE_TO_OBJECT"
]


class ScreenshotParams(object):
    """
    Encoding options for a screenshot.
    """

    __slots__ = ["format", "quality"]

    def __init__(self, format=None, quality=None):
        """
        :param format: Image compression format (defaults to png).
        :type format: Optional[str]
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: Optional[int]
        """
        super(ScreenshotParams, self).__init__()
        self.format = format
        self.quality = quality

    def __repr__(self):
        repr_args = []
        if self.format is not None:
            repr_args.append("format={!r}".format(self.format))
        if self.quality is not None:
            repr_args.append("quality={!r}".format(self.quality))
        return "ScreenshotParams(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ScreenshotParams from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreenshotParams
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreenshotParams if creation did not fail
        :rtype: Optional[Union[dict, ScreenshotParams]]
        """
        if init is not None:
            try:
                ourselves = ScreenshotParams(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ScreenshotParamss from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreenshotParams instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreenshotParams instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreenshotParams]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenshotParams.safe_create(it))
            return list_of_self
        else:
            return init


HEADLESSEXPERIMENTAL_TYPE_TO_OBJECT = {
    "ScreenshotParams": ScreenshotParams,
}
