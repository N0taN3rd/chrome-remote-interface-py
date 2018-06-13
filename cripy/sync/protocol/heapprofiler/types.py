from cripy.sync.protocol.runtime import types as Runtime

__all__ = [
    "SamplingHeapProfileNode",
    "SamplingHeapProfile",
]


class SamplingHeapProfileNode(object):
    """
    Sampling Heap Profile node. Holds callsite information, allocation statistics and child nodes.
    """

    def __init__(self, callFrame, selfSize, children):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.callFrame is not None:
            repr_args.append("callFrame={!r}".format(self.callFrame))
        if self.selfSize is not None:
            repr_args.append("selfSize={!r}".format(self.selfSize))
        if self.children is not None:
            repr_args.append("children={!r}".format(self.children))
        return "SamplingHeapProfileNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = SamplingHeapProfileNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, head):
        """
        :param head: The head
        :type head: dict
        """
        super().__init__()
        self.head = SamplingHeapProfileNode.safe_create(head)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.head is not None:
            repr_args.append("head={!r}".format(self.head))
        return "SamplingHeapProfile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = SamplingHeapProfile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SamplingHeapProfile.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SamplingHeapProfileNode": SamplingHeapProfileNode,
    "SamplingHeapProfile": SamplingHeapProfile,
}
