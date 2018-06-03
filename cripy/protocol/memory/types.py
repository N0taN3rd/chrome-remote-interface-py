from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class SamplingProfileNode(ProtocolType):
    """
    Heap profile sample.
    """

    def __init__(self, size: float, total: float, stack: List[str]) -> None:
        """
        :param size: Size of the sampled allocation.
        :type size: float
        :param total: Total bytes attributed to this sample.
        :type total: float
        :param stack: Execution stack at the point of allocation.
        :type stack: List[str]
        """
        super().__init__()
        self.size = size
        self.total = total
        self.stack = stack

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SamplingProfileNode', dict]]:
        if init is not None:
            try:
                ourselves = SamplingProfileNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SamplingProfileNode', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingProfileNode.safe_create(it))
            return list_of_self
        else:
            return init


class SamplingProfile(ProtocolType):
    """
    Array of heap profile samples.
    """

    def __init__(self, samples: List[Union['SamplingProfileNode', dict]]) -> None:
        """
        :param samples: The samples
        :type samples: List[dict]
        """
        super().__init__()
        self.samples = SamplingProfileNode.safe_create_from_list(samples)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SamplingProfile', dict]]:
        if init is not None:
            try:
                ourselves = SamplingProfile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SamplingProfile', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingProfile.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SamplingProfileNode": SamplingProfileNode,
    "SamplingProfile": SamplingProfile,
}
