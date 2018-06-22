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
    "PROFILER_TYPE_TO_OBJECT"
]


class TypeProfileEntry(object):
    """
    Source offset and types for a parameter or return value.
    """

    __slots__ = ["offset", "types"]

    def __init__(self, offset, types):
        """
        :param offset: Source offset of the parameter or end of function for return values.
        :type offset: int
        :param types: The types for this parameter or return value.
        :type types: List[dict]
        """
        super(TypeProfileEntry, self).__init__()
        self.offset = offset
        self.types = TypeObject.safe_create_from_list(types)

    def __repr__(self):
        repr_args = []
        if self.offset is not None:
            repr_args.append("offset={!r}".format(self.offset))
        if self.types is not None:
            repr_args.append("types={!r}".format(self.types))
        return "TypeProfileEntry(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TypeProfileEntry from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TypeProfileEntry
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TypeProfileEntry if creation did not fail
        :rtype: Optional[Union[dict, TypeProfileEntry]]
        """
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
        """
        Safely create a new list TypeProfileEntrys from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TypeProfileEntry instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TypeProfileEntry instances if creation did not fail
        :rtype: Optional[List[Union[dict, TypeProfileEntry]]]
        """
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

    __slots__ = ["name"]

    def __init__(self, name):
        """
        :param name: Name of a type collected with type profiling.
        :type name: str
        """
        super(TypeObject, self).__init__()
        self.name = name

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        return "TypeObject(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create TypeObject from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TypeObject
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TypeObject if creation did not fail
        :rtype: Optional[Union[dict, TypeObject]]
        """
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
        """
        Safely create a new list TypeObjects from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TypeObject instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TypeObject instances if creation did not fail
        :rtype: Optional[List[Union[dict, TypeObject]]]
        """
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

    __slots__ = ["scriptId", "url", "entries"]

    def __init__(self, scriptId, url, entries):
        """
        :param scriptId: JavaScript script id.
        :type scriptId: str
        :param url: JavaScript script name or url.
        :type url: str
        :param entries: Type profile entries for parameters and return values of the functions in the script.
        :type entries: List[dict]
        """
        super(ScriptTypeProfile, self).__init__()
        self.scriptId = scriptId
        self.url = url
        self.entries = TypeProfileEntry.safe_create_from_list(entries)

    def __repr__(self):
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.entries is not None:
            repr_args.append("entries={!r}".format(self.entries))
        return "ScriptTypeProfile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ScriptTypeProfile from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScriptTypeProfile
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScriptTypeProfile if creation did not fail
        :rtype: Optional[Union[dict, ScriptTypeProfile]]
        """
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
        """
        Safely create a new list ScriptTypeProfiles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScriptTypeProfile instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScriptTypeProfile instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScriptTypeProfile]]]
        """
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

    __slots__ = ["scriptId", "url", "functions"]

    def __init__(self, scriptId, url, functions):
        """
        :param scriptId: JavaScript script id.
        :type scriptId: str
        :param url: JavaScript script name or url.
        :type url: str
        :param functions: Functions contained in the script that has coverage data.
        :type functions: List[dict]
        """
        super(ScriptCoverage, self).__init__()
        self.scriptId = scriptId
        self.url = url
        self.functions = FunctionCoverage.safe_create_from_list(functions)

    def __repr__(self):
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.functions is not None:
            repr_args.append("functions={!r}".format(self.functions))
        return "ScriptCoverage(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ScriptCoverage from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScriptCoverage
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScriptCoverage if creation did not fail
        :rtype: Optional[Union[dict, ScriptCoverage]]
        """
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
        """
        Safely create a new list ScriptCoverages from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScriptCoverage instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScriptCoverage instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScriptCoverage]]]
        """
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

    __slots__ = ["id", "callFrame", "hitCount", "children", "deoptReason", "positionTicks"]

    def __init__(self, id, callFrame, hitCount=None, children=None, deoptReason=None, positionTicks=None):
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
        super(ProfileNode, self).__init__()
        self.id = id
        self.callFrame = Runtime.CallFrame.safe_create(callFrame)
        self.hitCount = hitCount
        self.children = children
        self.deoptReason = deoptReason
        self.positionTicks = PositionTickInfo.safe_create_from_list(positionTicks)

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
        return "ProfileNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ProfileNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ProfileNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ProfileNode if creation did not fail
        :rtype: Optional[Union[dict, ProfileNode]]
        """
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
        """
        Safely create a new list ProfileNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ProfileNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ProfileNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, ProfileNode]]]
        """
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

    __slots__ = ["nodes", "startTime", "endTime", "samples", "timeDeltas"]

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
        super(Profile, self).__init__()
        self.nodes = ProfileNode.safe_create_from_list(nodes)
        self.startTime = startTime
        self.endTime = endTime
        self.samples = samples
        self.timeDeltas = timeDeltas

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
        return "Profile(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Profile from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Profile
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Profile if creation did not fail
        :rtype: Optional[Union[dict, Profile]]
        """
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
        """
        Safely create a new list Profiles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Profile instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Profile instances if creation did not fail
        :rtype: Optional[List[Union[dict, Profile]]]
        """
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

    __slots__ = ["line", "ticks"]

    def __init__(self, line, ticks):
        """
        :param line: Source line number (1-based).
        :type line: int
        :param ticks: Number of samples attributed to the source line.
        :type ticks: int
        """
        super(PositionTickInfo, self).__init__()
        self.line = line
        self.ticks = ticks

    def __repr__(self):
        repr_args = []
        if self.line is not None:
            repr_args.append("line={!r}".format(self.line))
        if self.ticks is not None:
            repr_args.append("ticks={!r}".format(self.ticks))
        return "PositionTickInfo(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create PositionTickInfo from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of PositionTickInfo
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of PositionTickInfo if creation did not fail
        :rtype: Optional[Union[dict, PositionTickInfo]]
        """
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
        """
        Safely create a new list PositionTickInfos from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list PositionTickInfo instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of PositionTickInfo instances if creation did not fail
        :rtype: Optional[List[Union[dict, PositionTickInfo]]]
        """
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

    __slots__ = ["functionName", "ranges", "isBlockCoverage"]

    def __init__(self, functionName, ranges, isBlockCoverage):
        """
        :param functionName: JavaScript function name.
        :type functionName: str
        :param ranges: Source ranges inside the function with coverage data.
        :type ranges: List[dict]
        :param isBlockCoverage: Whether coverage data for this function has block granularity.
        :type isBlockCoverage: bool
        """
        super(FunctionCoverage, self).__init__()
        self.functionName = functionName
        self.ranges = CoverageRange.safe_create_from_list(ranges)
        self.isBlockCoverage = isBlockCoverage

    def __repr__(self):
        repr_args = []
        if self.functionName is not None:
            repr_args.append("functionName={!r}".format(self.functionName))
        if self.ranges is not None:
            repr_args.append("ranges={!r}".format(self.ranges))
        if self.isBlockCoverage is not None:
            repr_args.append("isBlockCoverage={!r}".format(self.isBlockCoverage))
        return "FunctionCoverage(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create FunctionCoverage from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FunctionCoverage
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FunctionCoverage if creation did not fail
        :rtype: Optional[Union[dict, FunctionCoverage]]
        """
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
        """
        Safely create a new list FunctionCoverages from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FunctionCoverage instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FunctionCoverage instances if creation did not fail
        :rtype: Optional[List[Union[dict, FunctionCoverage]]]
        """
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

    __slots__ = ["startOffset", "endOffset", "count"]

    def __init__(self, startOffset, endOffset, count):
        """
        :param startOffset: JavaScript script source offset for the range start.
        :type startOffset: int
        :param endOffset: JavaScript script source offset for the range end.
        :type endOffset: int
        :param count: Collected execution count of the source range.
        :type count: int
        """
        super(CoverageRange, self).__init__()
        self.startOffset = startOffset
        self.endOffset = endOffset
        self.count = count

    def __repr__(self):
        repr_args = []
        if self.startOffset is not None:
            repr_args.append("startOffset={!r}".format(self.startOffset))
        if self.endOffset is not None:
            repr_args.append("endOffset={!r}".format(self.endOffset))
        if self.count is not None:
            repr_args.append("count={!r}".format(self.count))
        return "CoverageRange(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create CoverageRange from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CoverageRange
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CoverageRange if creation did not fail
        :rtype: Optional[Union[dict, CoverageRange]]
        """
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
        """
        Safely create a new list CoverageRanges from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CoverageRange instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CoverageRange instances if creation did not fail
        :rtype: Optional[List[Union[dict, CoverageRange]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CoverageRange.safe_create(it))
            return list_of_self
        else:
            return init


PROFILER_TYPE_TO_OBJECT = {
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
