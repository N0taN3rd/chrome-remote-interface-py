from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

StreamCompression = str


class MemoryDumpConfig(ChromeTypeBase):
    """Configuration for memory dump. Used only when "memory-infra" category is enabled."""

    def __init__(self,) -> None:
        super().__init__()


class TraceConfig(ChromeTypeBase):

    def __init__(
        self,
        recordMode: Optional[str] = None,
        enableSampling: Optional[bool] = None,
        enableSystrace: Optional[bool] = None,
        enableArgumentFilter: Optional[bool] = None,
        includedCategories: Optional[List["str"]] = None,
        excludedCategories: Optional[List["str"]] = None,
        syntheticDelays: Optional[List["str"]] = None,
        memoryDumpConfig: Optional["MemoryDumpConfig"] = None,
    ) -> None:
        """
        :param recordMode: Controls how the trace buffer stores data.
        :param enableSampling: Turns on JavaScript stack sampling.
        :param enableSystrace: Turns on system tracing.
        :param enableArgumentFilter: Turns on argument filter.
        :param includedCategories: Included category filters.
        :param excludedCategories: Excluded category filters.
        :param syntheticDelays: Configuration to synthesize the delays in tracing.
        :param memoryDumpConfig: Configuration for memory dump triggers. Used only when "memory-infra" category is enabled.
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
