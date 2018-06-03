from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime


class TypeProfileEntry(ProtocolType):
    """
    Source offset and types for a parameter or return value.
    """

    def __init__(self, offset: int, types: List[Union['TypeObject', dict]]) -> None:
        """
        :param offset: Source offset of the parameter or end of function for return values.
        :type offset: int
        :param types: The types for this parameter or return value.
        :type types: List[dict]
        """
        super().__init__()
        self.offset = offset
        self.types = TypeObject.safe_create_from_list(types)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TypeProfileEntry', dict]]:
        if init is not None:
            try:
                ourselves = TypeProfileEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TypeProfileEntry', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TypeProfileEntry.safe_create(it))
            return list_of_self
        else:
            return init


class TypeObject(ProtocolType):
    """
    Describes a type collected during runtime.
    """

    def __init__(self, name: str) -> None:
        """
        :param name: Name of a type collected with type profiling.
        :type name: str
        """
        super().__init__()
        self.name = name

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TypeObject', dict]]:
        if init is not None:
            try:
                ourselves = TypeObject(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TypeObject', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TypeObject.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptTypeProfile(ProtocolType):
    """
    Type profile data collected during runtime for a JavaScript script.
    """

    def __init__(self, scriptId: str, url: str, entries: List[Union['TypeProfileEntry', dict]]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptTypeProfile', dict]]:
        if init is not None:
            try:
                ourselves = ScriptTypeProfile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScriptTypeProfile', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptTypeProfile.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptCoverage(ProtocolType):
    """
    Coverage data for a JavaScript script.
    """

    def __init__(self, scriptId: str, url: str, functions: List[Union['FunctionCoverage', dict]]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptCoverage', dict]]:
        if init is not None:
            try:
                ourselves = ScriptCoverage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScriptCoverage', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptCoverage.safe_create(it))
            return list_of_self
        else:
            return init


class ProfileNode(ProtocolType):
    """
    Profile node. Holds callsite information, execution statistics and child nodes.
    """

    def __init__(self, id: int, callFrame: Union['Runtime.CallFrame', dict], hitCount: Optional[int] = None, children: Optional[List[int]] = None, deoptReason: Optional[str] = None, positionTicks: Optional[List[Union['PositionTickInfo', dict]]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ProfileNode', dict]]:
        if init is not None:
            try:
                ourselves = ProfileNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ProfileNode', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ProfileNode.safe_create(it))
            return list_of_self
        else:
            return init


class Profile(ProtocolType):
    """
    Profile.
    """

    def __init__(self, nodes: List[Union['ProfileNode', dict]], startTime: float, endTime: float, samples: Optional[List[int]] = None, timeDeltas: Optional[List[int]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Profile', dict]]:
        if init is not None:
            try:
                ourselves = Profile(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Profile', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Profile.safe_create(it))
            return list_of_self
        else:
            return init


class PositionTickInfo(ProtocolType):
    """
    Specifies a number of samples attributed to a certain source position.
    """

    def __init__(self, line: int, ticks: int) -> None:
        """
        :param line: Source line number (1-based).
        :type line: int
        :param ticks: Number of samples attributed to the source line.
        :type ticks: int
        """
        super().__init__()
        self.line = line
        self.ticks = ticks

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PositionTickInfo', dict]]:
        if init is not None:
            try:
                ourselves = PositionTickInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['PositionTickInfo', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PositionTickInfo.safe_create(it))
            return list_of_self
        else:
            return init


class FunctionCoverage(ProtocolType):
    """
    Coverage data for a JavaScript function.
    """

    def __init__(self, functionName: str, ranges: List[Union['CoverageRange', dict]], isBlockCoverage: bool) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FunctionCoverage', dict]]:
        if init is not None:
            try:
                ourselves = FunctionCoverage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FunctionCoverage', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FunctionCoverage.safe_create(it))
            return list_of_self
        else:
            return init


class CoverageRange(ProtocolType):
    """
    Coverage data for a source range.
    """

    def __init__(self, startOffset: int, endOffset: int, count: int) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CoverageRange', dict]]:
        if init is not None:
            try:
                ourselves = CoverageRange(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CoverageRange', dict]]]:
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
