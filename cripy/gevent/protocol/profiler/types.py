from cripy.gevent.protocol.runtime import types as Runtime

__all__ = [
    "TypeProfileEntry",
    "TypeObject",
    "ScriptTypeProfile",
    "ScriptCoverage",
    "ProfileNode",
    "Profile",
    "PositionTickInfo",
    "FunctionCoverage",
    "CoverageRange",
]


class TypeProfileEntry(object):
    """
    Source offset and types for a parameter or return value.
    """

    def __init__(self, offset, types):
        """
        :param offset: Source offset of the parameter or end of function for return values.
        :type offset: int
        :param types: The types for this parameter or return value.
        :type types: List[dict]
        """
        super().__init__()
        self.offset = offset
        self.types = TypeObject.safe_create_from_list(types)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.offset is not None:
            repr_args.append("offset={!r}".format(self.offset))
        if self.types is not None:
            repr_args.append("types={!r}".format(self.types))
        return "TypeProfileEntry(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = TypeProfileEntry(**init)
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
                list_of_self.append(TypeProfileEntry.safe_create(it))
            return list_of_self
        else:
            return init


class TypeObject(object):
    """
    Describes a type collected during runtime.
    """

    def __init__(self, name):
        """
        :param name: Name of a type collected with type profiling.
        :type name: str
        """
        super().__init__()
        self.name = name

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        return "TypeObject(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = TypeObject(**init)
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
                list_of_self.append(TypeObject.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptTypeProfile(object):
    """
    Type profile data collected during runtime for a JavaScript script.
    """

    def __init__(self, scriptId, url, entries):
        """
        :param scriptId: JavaScript script id.
        :type scriptId: str
        :param url: JavaScript script name or url.
        :type url: str
        :param entries: Type profile entries for parameters and return values of the functions in the script.
        :type entries: List[dict]
        """
        super().__init__()
        self.scriptId = scriptId
        self.url = url
        self.entries = TypeProfileEntry.safe_create_from_list(entries)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.entries is not None:
            repr_args.append("entries={!r}".format(self.entries))
        return "ScriptTypeProfile(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScriptTypeProfile(**init)
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
                list_of_self.append(ScriptTypeProfile.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptCoverage(object):
    """
    Coverage data for a JavaScript script.
    """

    def __init__(self, scriptId, url, functions):
        """
        :param scriptId: JavaScript script id.
        :type scriptId: str
        :param url: JavaScript script name or url.
        :type url: str
        :param functions: Functions contained in the script that has coverage data.
        :type functions: List[dict]
        """
        super().__init__()
        self.scriptId = scriptId
        self.url = url
        self.functions = FunctionCoverage.safe_create_from_list(functions)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.functions is not None:
            repr_args.append("functions={!r}".format(self.functions))
        return "ScriptCoverage(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScriptCoverage(**init)
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
                list_of_self.append(ScriptCoverage.safe_create(it))
            return list_of_self
        else:
            return init


class ProfileNode(object):
    """
    Profile node. Holds callsite information, execution statistics and child nodes.
    """

    def __init__(
        self,
        id,
        callFrame,
        hitCount=None,
        children=None,
        deoptReason=None,
        positionTicks=None,
    ):
        """
        :param id: Unique id of the node.
        :type id: int
        :param callFrame: Function location.
        :type callFrame: dict
        :param hitCount: Number of samples where this node was on top of the call stack.
        :type hitCount: Optional[int]
        :param children: Child node ids.
        :type children: Optional[List[int]]
        :param deoptReason: The reason of being not optimized. The function may be deoptimized or marked as don't optimize.
        :type deoptReason: Optional[str]
        :param positionTicks: An array of source position ticks.
        :type positionTicks: Optional[List[dict]]
        """
        super().__init__()
        self.id = id
        self.callFrame = Runtime.CallFrame.safe_create(callFrame)
        self.hitCount = hitCount
        self.children = children
        self.deoptReason = deoptReason
        self.positionTicks = PositionTickInfo.safe_create_from_list(positionTicks)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.callFrame is not None:
            repr_args.append("callFrame={!r}".format(self.callFrame))
        if self.hitCount is not None:
            repr_args.append("hitCount={!r}".format(self.hitCount))
        if self.children is not None:
            repr_args.append("children={!r}".format(self.children))
        if self.deoptReason is not None:
            repr_args.append("deoptReason={!r}".format(self.deoptReason))
        if self.positionTicks is not None:
            repr_args.append("positionTicks={!r}".format(self.positionTicks))
        return "ProfileNode(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ProfileNode(**init)
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
                list_of_self.append(ProfileNode.safe_create(it))
            return list_of_self
        else:
            return init


class Profile(object):
    """
    Profile.
    """

    def __init__(self, nodes, startTime, endTime, samples=None, timeDeltas=None):
        """
        :param nodes: The list of profile nodes. First item is the root node.
        :type nodes: List[dict]
        :param startTime: Profiling start timestamp in microseconds.
        :type startTime: float
        :param endTime: Profiling end timestamp in microseconds.
        :type endTime: float
        :param samples: Ids of samples top nodes.
        :type samples: Optional[List[int]]
        :param timeDeltas: Time intervals between adjacent samples in microseconds. The first delta is relative to the profile startTime.
        :type timeDeltas: Optional[List[int]]
        """
        super().__init__()
        self.nodes = ProfileNode.safe_create_from_list(nodes)
        self.startTime = startTime
        self.endTime = endTime
        self.samples = samples
        self.timeDeltas = timeDeltas

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodes is not None:
            repr_args.append("nodes={!r}".format(self.nodes))
        if self.startTime is not None:
            repr_args.append("startTime={!r}".format(self.startTime))
        if self.endTime is not None:
            repr_args.append("endTime={!r}".format(self.endTime))
        if self.samples is not None:
            repr_args.append("samples={!r}".format(self.samples))
        if self.timeDeltas is not None:
            repr_args.append("timeDeltas={!r}".format(self.timeDeltas))
        return "Profile(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Profile(**init)
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
                list_of_self.append(Profile.safe_create(it))
            return list_of_self
        else:
            return init


class PositionTickInfo(object):
    """
    Specifies a number of samples attributed to a certain source position.
    """

    def __init__(self, line, ticks):
        """
        :param line: Source line number (1-based).
        :type line: int
        :param ticks: Number of samples attributed to the source line.
        :type ticks: int
        """
        super().__init__()
        self.line = line
        self.ticks = ticks

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.line is not None:
            repr_args.append("line={!r}".format(self.line))
        if self.ticks is not None:
            repr_args.append("ticks={!r}".format(self.ticks))
        return "PositionTickInfo(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PositionTickInfo(**init)
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
                list_of_self.append(PositionTickInfo.safe_create(it))
            return list_of_self
        else:
            return init


class FunctionCoverage(object):
    """
    Coverage data for a JavaScript function.
    """

    def __init__(self, functionName, ranges, isBlockCoverage):
        """
        :param functionName: JavaScript function name.
        :type functionName: str
        :param ranges: Source ranges inside the function with coverage data.
        :type ranges: List[dict]
        :param isBlockCoverage: Whether coverage data for this function has block granularity.
        :type isBlockCoverage: bool
        """
        super().__init__()
        self.functionName = functionName
        self.ranges = CoverageRange.safe_create_from_list(ranges)
        self.isBlockCoverage = isBlockCoverage

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.functionName is not None:
            repr_args.append("functionName={!r}".format(self.functionName))
        if self.ranges is not None:
            repr_args.append("ranges={!r}".format(self.ranges))
        if self.isBlockCoverage is not None:
            repr_args.append("isBlockCoverage={!r}".format(self.isBlockCoverage))
        return "FunctionCoverage(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FunctionCoverage(**init)
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
                list_of_self.append(FunctionCoverage.safe_create(it))
            return list_of_self
        else:
            return init


class CoverageRange(object):
    """
    Coverage data for a source range.
    """

    def __init__(self, startOffset, endOffset, count):
        """
        :param startOffset: JavaScript script source offset for the range start.
        :type startOffset: int
        :param endOffset: JavaScript script source offset for the range end.
        :type endOffset: int
        :param count: Collected execution count of the source range.
        :type count: int
        """
        super().__init__()
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.count = count

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.startOffset is not None:
            repr_args.append("startOffset={!r}".format(self.startOffset))
        if self.endOffset is not None:
            repr_args.append("endOffset={!r}".format(self.endOffset))
        if self.count is not None:
            repr_args.append("count={!r}".format(self.count))
        return "CoverageRange(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = CoverageRange(**init)
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
                list_of_self.append(CoverageRange.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "TypeProfileEntry": TypeProfileEntry,
    "TypeObject": TypeObject,
    "ScriptTypeProfile": ScriptTypeProfile,
    "ScriptCoverage": ScriptCoverage,
    "ProfileNode": ProfileNode,
    "Profile": Profile,
    "PositionTickInfo": PositionTickInfo,
    "FunctionCoverage": FunctionCoverage,
    "CoverageRange": CoverageRange,
}
