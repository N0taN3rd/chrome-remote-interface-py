from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

BreakpointId = str

CallFrameId = str


class Location(ChromeTypeBase):

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        lineNumber: int,
        columnNumber: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber


class ScriptPosition(ChromeTypeBase):

    def __init__(self, lineNumber: int, columnNumber: int) -> None:
        super().__init__()
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class CallFrame(ChromeTypeBase):

    def __init__(
        self,
        callFrameId: "CallFrameId",
        functionName: str,
        location: "Location",
        url: str,
        scopeChain: List["Scope"],
        this: "Runtime.RemoteObject",
        functionLocation: Optional["Location"] = None,
        returnValue: Optional["Runtime.RemoteObject"] = None,
    ) -> None:
        super().__init__()
        self.callFrameId: CallFrameId = callFrameId
        self.functionName: str = functionName
        self.functionLocation: Optional[Location] = functionLocation
        self.location: Location = location
        self.url: str = url
        self.scopeChain: List[Scope] = scopeChain
        self.this: Runtime.RemoteObject = this
        self.returnValue: Optional[Runtime.RemoteObject] = returnValue


class Scope(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        object: "Runtime.RemoteObject",
        name: Optional[str] = None,
        startLocation: Optional["Location"] = None,
        endLocation: Optional["Location"] = None,
    ) -> None:
        super().__init__()
        self.type: str = type
        self.object: Runtime.RemoteObject = object
        self.name: Optional[str] = name
        self.startLocation: Optional[Location] = startLocation
        self.endLocation: Optional[Location] = endLocation


class SearchMatch(ChromeTypeBase):

    def __init__(self, lineNumber: float, lineContent: str) -> None:
        super().__init__()
        self.lineNumber: float = lineNumber
        self.lineContent: str = lineContent


class BreakLocation(ChromeTypeBase):

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        lineNumber: int,
        columnNumber: Optional[int] = None,
        type: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber
        self.type: Optional[str] = type
