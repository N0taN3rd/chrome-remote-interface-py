from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime

HeapSnapshotObjectId = TypeVar("HeapSnapshotObjectId", str, str) # Heap snapshot object id.


class SamplingHeapProfileNode(ProtocolType):
    """
    Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.
    """

    def __init__(self, callFrame: Union['Runtime.CallFrame', dict], selfSize: float, children: List[Union['SamplingHeapProfileNode', dict]]) -> None:
        """
        :param callFrame: Function location.
        :type callFrame: dict
        :param selfSize: Allocations size in bytes for the node excluding children.
        :type selfSize: float
        :param children: Child nodes.
        :type children: List[dict]
        """
        super().__init__()
        self.callFrame = Runtime.CallFrame.safe_create(callFrame)
        self.selfSize = selfSize
        self.children = SamplingHeapProfileNode.safe_create_from_list(children)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SamplingHeapProfileNode']:
        if init is not None:
            return SamplingHeapProfileNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SamplingHeapProfileNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingHeapProfileNode(**it))
            return list_of_self
        else:
            return init


class SamplingHeapProfile(ProtocolType):
    """
    Profile.
    """

    def __init__(self, head: Union['SamplingHeapProfileNode', dict]) -> None:
        """
        :param head: The head
        :type head: dict
        """
        super().__init__()
        self.head = SamplingHeapProfileNode.safe_create(head)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SamplingHeapProfile']:
        if init is not None:
            return SamplingHeapProfile(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SamplingHeapProfile']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingHeapProfile(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SamplingHeapProfileNode": SamplingHeapProfileNode,
    "SamplingHeapProfile": SamplingHeapProfile,
}
