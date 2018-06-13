
__all__ = [
    "TraceConfig",
    "MemoryDumpConfig",
]


class TraceConfig(object):
    def __init__(self, recordMode, enableSampling, enableSystrace, enableArgumentFilter, includedCategories, excludedCategories, syntheticDelays, memoryDumpConfig):
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
        super().__init__()
        self.recordMode = recordMode
        self.enableSampling = enableSampling
        self.enableSystrace = enableSystrace
        self.enableArgumentFilter = enableArgumentFilter
        self.includedCategories = includedCategories
        self.excludedCategories = excludedCategories
        self.syntheticDelays = syntheticDelays
        self.memoryDumpConfig = MemoryDumpConfig.safe_create(memoryDumpConfig)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MemoryDumpConfig.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "TraceConfig": TraceConfig,
    "MemoryDumpConfig": MemoryDumpConfig,
}
