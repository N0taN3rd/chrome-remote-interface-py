from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# Compression type to use for traces returned via streams.
StreamCompression = str


class MemoryDumpConfig(ChromeTypeBase, dict):
    """Configuration for memory dump. Used only when "memory-infra" category is enabled."""


class TraceConfig(ChromeTypeBase):
    pass
    def __init__(self, recordMode: Optional[str] = None, enableSampling: Optional[bool] = None, enableSystrace: Optional[bool] = None, enableArgumentFilter: Optional[bool] = None, includedCategories: Optional[List['str']] = None, excludedCategories: Optional[List['str']] = None, syntheticDelays: Optional[List['str']] = None, memoryDumpConfig: Optional['MemoryDumpConfig'] = None) -> None:
        """
        :param recordMode: Controls how the trace buffer stores data.
        :type recordMode: str
        :param enableSampling: Turns on JavaScript stack sampling.
        :type enableSampling: bool
        :param enableSystrace: Turns on system tracing.
        :type enableSystrace: bool
        :param enableArgumentFilter: Turns on argument filter.
        :type enableArgumentFilter: bool
        :param includedCategories: Included category filters.
        :type includedCategories: array
        :param excludedCategories: Excluded category filters.
        :type excludedCategories: array
        :param syntheticDelays: Configuration to synthesize the delays in tracing.
        :type syntheticDelays: array
        :param memoryDumpConfig: Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
        :type memoryDumpConfig: MemoryDumpConfig
        """
        super().__init__()
        self.recordMode: Optional[str] = recordMode
        self.enableSampling: Optional[bool] = enableSampling
        self.enableSystrace: Optional[bool] = enableSystrace
        self.enableArgumentFilter: Optional[bool] = enableArgumentFilter
        self.includedCategories: Optional[List[str]] = includedCategories
        self.excludedCategories: Optional[List[str]] = excludedCategories
        self.syntheticDelays: Optional[List[str]] = syntheticDelays
        self.memoryDumpConfig: Optional[MemoryDumpConfig] = memoryDumpConfig


