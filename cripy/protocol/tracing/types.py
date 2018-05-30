from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class TraceConfig(ProtocolType):
    def __init__(self, recordMode: Optional[str] = None, enableSampling: Optional[bool] = None, enableSystrace: Optional[bool] = None, enableArgumentFilter: Optional[bool] = None, includedCategories: Optional[List[str]] = None, excludedCategories: Optional[List[str]] = None, syntheticDelays: Optional[List[str]] = None, memoryDumpConfig: Optional[Union['MemoryDumpConfig', dict]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TraceConfig', dict]]:
        if init is not None:
             try:
                ourselves = TraceConfig(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TraceConfig', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TraceConfig.safe_create(it))
            return list_of_self
        else:
            return init


class MemoryDumpConfig(ProtocolType, dict):
    """
    Configuration for memory dump. Used only when "memory-infra" category is enabled.
    """

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['MemoryDumpConfig', dict]]:
        if init is not None:
             try:
                ourselves = MemoryDumpConfig(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['MemoryDumpConfig', dict]]]:
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
