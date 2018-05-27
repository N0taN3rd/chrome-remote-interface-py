from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

HeapSnapshotObjectId = str


class SamplingHeapProfileNode(ChromeTypeBase):
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""

    def __init__(
        self,
        callFrame: "Runtime.CallFrame",
        selfSize: float,
        children: List["SamplingHeapProfileNode"],
    ) -> None:
        """
        :param callFrame: Function location.
        :param selfSize: Allocations size in bytes for the node excluding children.
        :param children: Child nodes.
        """
        super().__init__()
        self.callFrame: Runtime.CallFrame = callFrame
        self.selfSize: float = selfSize
        self.children: List[SamplingHeapProfileNode] = children


class SamplingHeapProfile(ChromeTypeBase):
    """Profile."""

    def __init__(self, head: "SamplingHeapProfileNode") -> None:
        """
        :param head: The head
        """
        super().__init__()
        self.head: SamplingHeapProfileNode = head
