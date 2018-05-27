from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

StreamCompression = str


class MemoryDumpConfig(ChromeTypeBase):

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
        super().__init__()
        self.recordMode: Optional[str] = recordMode
        self.enableSampling: Optional[bool] = enableSampling
        self.enableSystrace: Optional[bool] = enableSystrace
        self.enableArgumentFilter: Optional[bool] = enableArgumentFilter
        self.includedCategories: Optional[List[str]] = includedCategories
        self.excludedCategories: Optional[List[str]] = excludedCategories
        self.syntheticDelays: Optional[List[str]] = syntheticDelays
        self.memoryDumpConfig: Optional[MemoryDumpConfig] = memoryDumpConfig
