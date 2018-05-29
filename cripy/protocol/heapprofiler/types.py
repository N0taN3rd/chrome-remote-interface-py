from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime

HeapSnapshotObjectId = TypeVar("HeapSnapshotObjectId", str, str)
"""Heap snapshot object id."""


class SamplingHeapProfileNode(ProtocolType):
    """Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes."""

    def __init__(
        self,
        callFrame: "Runtime.CallFrame",
        selfSize: float,
        children: List[Union["SamplingHeapProfileNode", dict]],
    ) -> None:
        """
        :param callFrame: Function location.
        :type callFrame: Runtime.CallFrame
        :param selfSize: Allocations size in bytes for the node excluding children.
        :type selfSize: float
        :param children: Child nodes.
        :type children: array
        """
        super().__init__()
        self.callFrame: Runtime.CallFrame = callFrame
        self.selfSize: float = selfSize
        self.children: List[SamplingHeapProfileNode] = children


class SamplingHeapProfile(ProtocolType):
    """Profile."""

    def __init__(self, head: "SamplingHeapProfileNode") -> None:
        """
        :param head: The head
        :type head: SamplingHeapProfileNode
        """
        super().__init__()
        self.head: SamplingHeapProfileNode = head


OBJECT_LIST = {
    "SamplingHeapProfileNode": SamplingHeapProfileNode,
    "SamplingHeapProfile": SamplingHeapProfile,
}
