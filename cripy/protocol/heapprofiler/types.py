from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

HeapSnapshotObjectId = str


class SamplingHeapProfileNode(ChromeTypeBase):

    def __init__(
        self,
        callFrame: "Runtime.CallFrame",
        selfSize: float,
        children: List["SamplingHeapProfileNode"],
    ) -> None:
        super().__init__()
        self.callFrame: Runtime.CallFrame = callFrame
        self.selfSize: float = selfSize
        self.children: List[SamplingHeapProfileNode] = children


class SamplingHeapProfile(ChromeTypeBase):

    def __init__(self, head: "SamplingHeapProfileNode") -> None:
        super().__init__()
        self.head: SamplingHeapProfileNode = head
