from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class ProfileNode(ChromeTypeBase):

    def __init__(
        self,
        id: int,
        callFrame: "Runtime.CallFrame",
        hitCount: Optional[int] = None,
        children: Optional[List["int"]] = None,
        deoptReason: Optional[str] = None,
        positionTicks: Optional[List["PositionTickInfo"]] = None,
    ) -> None:
        super().__init__()
        self.id: int = id
        self.callFrame: Runtime.CallFrame = callFrame
        self.hitCount: Optional[int] = hitCount
        self.children: Optional[List[int]] = children
        self.deoptReason: Optional[str] = deoptReason
        self.positionTicks: Optional[List[PositionTickInfo]] = positionTicks


class Profile(ChromeTypeBase):

    def __init__(
        self,
        nodes: List["ProfileNode"],
        startTime: float,
        endTime: float,
        samples: Optional[List["int"]] = None,
        timeDeltas: Optional[List["int"]] = None,
    ) -> None:
        super().__init__()
        self.nodes: List[ProfileNode] = nodes
        self.startTime: float = startTime
        self.endTime: float = endTime
        self.samples: Optional[List[int]] = samples
        self.timeDeltas: Optional[List[int]] = timeDeltas


class PositionTickInfo(ChromeTypeBase):

    def __init__(self, line: int, ticks: int) -> None:
        super().__init__()
        self.line: int = line
        self.ticks: int = ticks


class CoverageRange(ChromeTypeBase):

    def __init__(self, startOffset: int, endOffset: int, count: int) -> None:
        super().__init__()
        self.startOffset: int = startOffset
        self.endOffset: int = endOffset
        self.count: int = count


class FunctionCoverage(ChromeTypeBase):

    def __init__(
        self, functionName: str, ranges: List["CoverageRange"], isBlockCoverage: bool
    ) -> None:
        super().__init__()
        self.functionName: str = functionName
        self.ranges: List[CoverageRange] = ranges
        self.isBlockCoverage: bool = isBlockCoverage


class ScriptCoverage(ChromeTypeBase):

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        url: str,
        functions: List["FunctionCoverage"],
    ) -> None:
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.functions: List[FunctionCoverage] = functions


class TypeObject(ChromeTypeBase):

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name


class TypeProfileEntry(ChromeTypeBase):

    def __init__(self, offset: int, types: List["TypeObject"]) -> None:
        super().__init__()
        self.offset: int = offset
        self.types: List[TypeObject] = types


class ScriptTypeProfile(ChromeTypeBase):

    def __init__(
        self, scriptId: "Runtime.ScriptId", url: str, entries: List["TypeProfileEntry"]
    ) -> None:
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.entries: List[TypeProfileEntry] = entries
