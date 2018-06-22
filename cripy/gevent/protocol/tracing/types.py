
__all__ = [
    "TraceConfig",
    "MemoryDumpConfig",
    "TRACING_TYPE_TO_OBJECT"
]


class TraceConfig(object):
    __slots__ = ["recordMode", "enableSampling", "enableSystrace", "enableArgumentFilter", "includedCategories", "excludedCategories", "syntheticDelays", "memoryDumpConfig"]

    def __init__(self, recordMode=None, enableSampling=None, enableSystrace=None, enableArgumentFilter=None, includedCategories=None, excludedCategories=None, syntheticDelays=None, memoryDumpConfig=None):
        """
        :param recordMode: Controls how the trace buffer stores data.
        :type recordMode: Optional[str]
        :param enableSampling: Turns on JavaScript stack sampling.
        :type enableSampling: Optional[bool]
        :param enableSystrace: Turns on system tracing.
        :type enableSystrace: Optional[bool]
        :param enableArgumentFilter: Turns on argument filter.
        :type enableArgumentFilter: Optional[bool]
        :param includedCategories: Included category filters.
        :type includedCategories: Optional[List[str]]
        :param excludedCategories: Excluded category filters.
        :type excludedCategories: Optional[List[str]]
        :param syntheticDelays: Configuration to synthesize the delays in tracing.
        :type syntheticDelays: Optional[List[str]]
        :param memoryDumpConfig: Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
        :type memoryDumpConfig: Optional[dict]
        """
        super(TraceConfig, self).__init__()
        self.recordMode = recordMode
        self.enableSampling = enableSampling
        self.enableSystrace = enableSystrace
        self.enableArgumentFilter = enableArgumentFilter
        self.includedCategories = includedCategories
        self.excludedCategories = excludedCategories
        self.syntheticDelays = syntheticDelays
        self.memoryDumpConfig = MemoryDumpConfig.safe_create(memoryDumpConfig)

    def __repr__(self):
        repr_args = []
        if self.recordMode is not None:
            repr_args.append("recordMode={!r}".format(self.recordMode))
        if self.enableSampling is not None:
            repr_args.append("enableSampling={!r}".format(self.enableSampling))
        if self.enableSystrace is not None:
            repr_args.append("enableSystrace={!r}".format(self.enableSystrace))
        if self.enableArgumentFilter is not None:
            repr_args.append("enableArgumentFilter={!r}".format(self.enableArgumentFilter))
        if self.includedCategories is not None:
            repr_args.append("includedCategories={!r}".format(self.includedCategories))
        if self.excludedCategories is not None:
            repr_args.append("excludedCategories={!r}".format(self.excludedCategories))
        if self.syntheticDelays is not None:
            repr_args.append("syntheticDelays={!r}".format(self.syntheticDelays))
        if self.memoryDumpConfig is not None:
            repr_args.append("memoryDumpConfig={!r}".format(self.memoryDumpConfig))
        return "TraceConfig(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TraceConfig from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TraceConfig
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TraceConfig if creation did not fail
        :rtype: Optional[Union[dict, TraceConfig]]
        """
        if init is not None:
            try:
                ourselves = TraceConfig(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list TraceConfigs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TraceConfig instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TraceConfig instances if creation did not fail
        :rtype: Optional[List[Union[dict, TraceConfig]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TraceConfig.safe_create(it))
            return list_of_self
        else:
            return init


class MemoryDumpConfig(dict):
    """
    Configuration for memory dump. Used only when "memory-infra" category is enabled.
    """


    def __repr__(self):
        return "MemoryDumpConfig(dict)"

    @staticmethod
    def safe_create(init):
        """
        Safely create MemoryDumpConfig from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of MemoryDumpConfig
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of MemoryDumpConfig if creation did not fail
        :rtype: Optional[Union[dict, MemoryDumpConfig]]
        """
        if init is not None:
            try:
                ourselves = MemoryDumpConfig(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list MemoryDumpConfigs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list MemoryDumpConfig instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of MemoryDumpConfig instances if creation did not fail
        :rtype: Optional[List[Union[dict, MemoryDumpConfig]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MemoryDumpConfig.safe_create(it))
            return list_of_self
        else:
            return init


TRACING_TYPE_TO_OBJECT = {
    "TraceConfig": TraceConfig,
    "MemoryDumpConfig": MemoryDumpConfig,
}
