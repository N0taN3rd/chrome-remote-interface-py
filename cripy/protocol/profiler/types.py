from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class ProfileNode(ChromeTypeBase):
    """Profile node. Holds callsite information, execution statistics and child nodes."""

    def __init__(
        self,
        id: int,
        callFrame: "Runtime.CallFrame",
        hitCount: Optional[int] = None,
        children: Optional[List["int"]] = None,
        deoptReason: Optional[str] = None,
        positionTicks: Optional[List["PositionTickInfo"]] = None,
    ) -> None:
        """
        :param id: Unique id of the node.
        :param callFrame: Function location.
        :param hitCount: Number of samples where this node was on top of the call stack.
        :param children: Child node ids.
        :param deoptReason: The reason of being not optimized. The function may be deoptimized or marked as don't
optimize.
        :param positionTicks: An array of source position ticks.
        """
        super().__init__()
        self.id: int = id
        self.callFrame: Runtime.CallFrame = callFrame
        self.hitCount: Optional[int] = hitCount
        self.children: Optional[List[int]] = children
        self.deoptReason: Optional[str] = deoptReason
        self.positionTicks: Optional[List[PositionTickInfo]] = positionTicks


class Profile(ChromeTypeBase):
    """Profile."""

    def __init__(
        self,
        nodes: List["ProfileNode"],
        startTime: float,
        endTime: float,
        samples: Optional[List["int"]] = None,
        timeDeltas: Optional[List["int"]] = None,
    ) -> None:
        """
        :param nodes: The list of profile nodes. First item is the root node.
        :param startTime: Profiling start timestamp in microseconds.
        :param endTime: Profiling end timestamp in microseconds.
        :param samples: Ids of samples top nodes.
        :param timeDeltas: Time intervals between adjacent samples in microseconds. The first delta is relative to the
profile startTime.
        """
        super().__init__()
        self.nodes: List[ProfileNode] = nodes
        self.startTime: float = startTime
        self.endTime: float = endTime
        self.samples: Optional[List[int]] = samples
        self.timeDeltas: Optional[List[int]] = timeDeltas


class PositionTickInfo(ChromeTypeBase):
    """Specifies a number of samples attributed to a certain source position."""

    def __init__(self, line: int, ticks: int) -> None:
        """
        :param line: Source line number (1-based).
        :param ticks: Number of samples attributed to the source line.
        """
        super().__init__()
        self.line: int = line
        self.ticks: int = ticks


class CoverageRange(ChromeTypeBase):
    """Coverage data for a source range."""

    def __init__(self, startOffset: int, endOffset: int, count: int) -> None:
        """
        :param startOffset: JavaScript script source offset for the range start.
        :param endOffset: JavaScript script source offset for the range end.
        :param count: Collected execution count of the source range.
        """
        super().__init__()
        self.startOffset: int = startOffset
        self.endOffset: int = endOffset
        self.count: int = count


class FunctionCoverage(ChromeTypeBase):
    """Coverage data for a JavaScript function."""

    def __init__(
        self, functionName: str, ranges: List["CoverageRange"], isBlockCoverage: bool
    ) -> None:
        """
        :param functionName: JavaScript function name.
        :param ranges: Source ranges inside the function with coverage data.
        :param isBlockCoverage: Whether coverage data for this function has block granularity.
        """
        super().__init__()
        self.functionName: str = functionName
        self.ranges: List[CoverageRange] = ranges
        self.isBlockCoverage: bool = isBlockCoverage


class ScriptCoverage(ChromeTypeBase):
    """Coverage data for a JavaScript script."""

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        url: str,
        functions: List["FunctionCoverage"],
    ) -> None:
        """
        :param scriptId: JavaScript script id.
        :param url: JavaScript script name or url.
        :param functions: Functions contained in the script that has coverage data.
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.functions: List[FunctionCoverage] = functions


class TypeObject(ChromeTypeBase):
    """Describes a type collected during runtime."""

    def __init__(self, name: str) -> None:
        """
        :param name: Name of a type collected with type profiling.
        """
        super().__init__()
        self.name: str = name


class TypeProfileEntry(ChromeTypeBase):
    """Source offset and types for a parameter or return value."""

    def __init__(self, offset: int, types: List["TypeObject"]) -> None:
        """
        :param offset: Source offset of the parameter or end of function for return values.
        :param types: The types for this parameter or return value.
        """
        super().__init__()
        self.offset: int = offset
        self.types: List[TypeObject] = types


class ScriptTypeProfile(ChromeTypeBase):
    """Type profile data collected during runtime for a JavaScript script."""

    def __init__(
        self, scriptId: "Runtime.ScriptId", url: str, entries: List["TypeProfileEntry"]
    ) -> None:
        """
        :param scriptId: JavaScript script id.
        :param url: JavaScript script name or url.
        :param entries: Type profile entries for parameters and return values of the functions in the script.
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.entries: List[TypeProfileEntry] = entries
