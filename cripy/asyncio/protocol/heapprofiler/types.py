from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.runtime import types as Runtime

__all__ = [
    "SamplingHeapProfileNode",
    "SamplingHeapProfile",
    "HEAPPROFILER_TYPES_TO_OBJECT"
]


class SamplingHeapProfileNode(object):
    """
    Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.
    """

    __slots__ = ["callFrame", "selfSize", "children"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.callFrame is not None:
            repr_args.append("callFrame={!r}".format(self.callFrame))
        if self.selfSize is not None:
            repr_args.append("selfSize={!r}".format(self.selfSize))
        if self.children is not None:
            repr_args.append("children={!r}".format(self.children))
        return "SamplingHeapProfileNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SamplingHeapProfileNode', dict]]:
        """
        Safely create SamplingHeapProfileNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SamplingHeapProfileNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SamplingHeapProfileNode if creation did not fail
        :rtype: Optional[Union[dict, SamplingHeapProfileNode]]
        """
        if init is not None:
            try:
                ourselves = SamplingHeapProfileNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SamplingHeapProfileNode', dict]]]:
        """
        Safely create a new list SamplingHeapProfileNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SamplingHeapProfileNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SamplingHeapProfileNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, SamplingHeapProfileNode]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingHeapProfileNode.safe_create(it))
            return list_of_self
        else:
            return init


class SamplingHeapProfile(object):
    """
    Profile.
    """

    __slots__ = ["head"]

    def __init__(self, head: Union['SamplingHeapProfileNode', dict]) -> None:
        """
        :param head: The head
        :type head: dict
        """
        super().__init__()
        self.head = SamplingHeapProfileNode.safe_create(head)

    def __repr__(self) -> str:
        repr_args = []
        if self.head is not None:
            repr_args.append("head={!r}".format(self.head))
        return "SamplingHeapProfile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SamplingHeapProfile', dict]]:
        """
        Safely create SamplingHeapProfile from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SamplingHeapProfile
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SamplingHeapProfile if creation did not fail
        :rtype: Optional[Union[dict, SamplingHeapProfile]]
        """
        if init is not None:
            try:
                ourselves = SamplingHeapProfile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SamplingHeapProfile', dict]]]:
        """
        Safely create a new list SamplingHeapProfiles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SamplingHeapProfile instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SamplingHeapProfile instances if creation did not fail
        :rtype: Optional[List[Union[dict, SamplingHeapProfile]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingHeapProfile.safe_create(it))
            return list_of_self
        else:
            return init


HEAPPROFILER_TYPES_TO_OBJECT = {
    "SamplingHeapProfileNode": SamplingHeapProfileNode,
    "SamplingHeapProfile": SamplingHeapProfile,
}
