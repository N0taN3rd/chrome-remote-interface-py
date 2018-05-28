from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

# Heap snapshot object id.
HeapSnapshotObjectId = str


class SamplingHeapProfileNode(ChromeTypeBase):
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""

    def __init__(self, callFrame: 'Runtime.CallFrame', selfSize: float, children: List['SamplingHeapProfileNode']) -> None:
        """
        :param callFrame: Function location.
        :type Runtime.CallFrame:
        :param selfSize: Allocations size in bytes for the node excluding children.
        :type float:
        :param children: Child nodes.
        :type array:
        """
        super().__init__()
        self.callFrame: Runtime.CallFrame = callFrame
        self.selfSize: float = selfSize
        self.children: List[SamplingHeapProfileNode] = children


class SamplingHeapProfile(ChromeTypeBase):
    """Profile."""

    def __init__(self, head: 'SamplingHeapProfileNode') -> None:
        """
        :param head: The head
        :type SamplingHeapProfileNode:
        """
        super().__init__()
        self.head: SamplingHeapProfileNode = head


