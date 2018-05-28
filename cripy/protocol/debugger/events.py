from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.debugger.types import (
    Location,
    BreakpointId,
)


class BreakpointResolvedEvent(BaseEvent):
    """Fired when breakpoint is resolved to an actual script and location."""

    event: str = "Debugger.breakpointResolved"

    def __init__(self, breakpointId: BreakpointId, location: Location) -> None:
        """
        :param breakpointId: Breakpoint unique identifier.
        :type breakpointId: BreakpointId
        :param location: Actual breakpoint location.
        :type location: Location
        """
        super().__init__()
        self.breakpointId: BreakpointId = breakpointId
        self.location: Location = location


class PausedEvent(BaseEvent):
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

    event: str = "Debugger.paused"

    def __init__(self, callFrames: List[CallFrame], reason: str, data: Optional[dict] = None, hitBreakpoints: Optional[List[str]] = None, asyncStackTrace: Optional[Runtime.StackTrace] = None, asyncStackTraceId: Optional[Runtime.StackTraceId] = None, asyncCallStackTraceId: Optional[Runtime.StackTraceId] = None) -> None:
        """
        :param callFrames: Call stack the virtual machine stopped on.
        :type callFrames: array
        :param reason: Pause reason.
        :type reason: str
        :param data: Object containing break-specific auxiliary properties.
        :type data: dict
        :param hitBreakpoints: Hit breakpoints IDs
        :type hitBreakpoints: array
        :param asyncStackTrace: Async stack trace, if any.
        :type asyncStackTrace: Runtime.StackTrace
        :param asyncStackTraceId: Async stack trace, if any.
        :type asyncStackTraceId: Runtime.StackTraceId
        :param asyncCallStackTraceId: Just scheduled async call will have this stack trace as parent stack during async execution. This field is available only after `Debugger.stepInto` call with `breakOnAsynCall` flag.
        :type asyncCallStackTraceId: Runtime.StackTraceId
        """
        super().__init__()
        self.callFrames: List[CallFrame] = callFrames
        self.reason: str = reason
        self.data: Optional[dict] = data
        self.hitBreakpoints: Optional[List[str]] = hitBreakpoints
        self.asyncStackTrace: Optional[Runtime.StackTrace] = asyncStackTrace
        self.asyncStackTraceId: Optional[Runtime.StackTraceId] = asyncStackTraceId
        self.asyncCallStackTraceId: Optional[Runtime.StackTraceId] = asyncCallStackTraceId


class ResumedEvent(BaseEvent):
    """Fired when the virtual machine resumed execution."""

    event: str = "Debugger.resumed"

    def __init__(self, ) -> None:
        super().__init__()


class ScriptFailedToParseEvent(BaseEvent):
    """Fired when virtual machine fails to parse the script."""

    event: str = "Debugger.scriptFailedToParse"

    def __init__(self, scriptId: Runtime.ScriptId, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: Runtime.ExecutionContextId, hash: str, executionContextAuxData: Optional[dict] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Runtime.StackTrace] = None) -> None:
        """
        :param scriptId: Identifier of the script parsed.
        :type scriptId: Runtime.ScriptId
        :param url: URL or name of the script parsed (if any).
        :type url: str
        :param startLine: Line offset of the script within the resource with given URL (for script tags).
        :type startLine: int
        :param startColumn: Column offset of the script within the resource with given URL.
        :type startColumn: int
        :param endLine: Last line of the script.
        :type endLine: int
        :param endColumn: Length of the last line of the script.
        :type endColumn: int
        :param executionContextId: Specifies script creation context.
        :type executionContextId: Runtime.ExecutionContextId
        :param hash: Content hash of the script.
        :type hash: str
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: dict
        :param sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: str
        :param hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: bool
        :param isModule: True, if this script is ES6 module.
        :type isModule: bool
        :param length: This script length.
        :type length: int
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Runtime.StackTrace
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.startLine: int = startLine
        self.startColumn: int = startColumn
        self.endLine: int = endLine
        self.endColumn: int = endColumn
        self.executionContextId: Runtime.ExecutionContextId = executionContextId
        self.hash: str = hash
        self.executionContextAuxData: Optional[dict] = executionContextAuxData
        self.sourceMapURL: Optional[str] = sourceMapURL
        self.hasSourceURL: Optional[bool] = hasSourceURL
        self.isModule: Optional[bool] = isModule
        self.length: Optional[int] = length
        self.stackTrace: Optional[Runtime.StackTrace] = stackTrace


class ScriptParsedEvent(BaseEvent):
    """Fired when virtual machine parses script.
	This event is also fired for all known and uncollected scripts upon enabling debugger."""

    event: str = "Debugger.scriptParsed"

    def __init__(self, scriptId: Runtime.ScriptId, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: Runtime.ExecutionContextId, hash: str, executionContextAuxData: Optional[dict] = None, isLiveEdit: Optional[bool] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Runtime.StackTrace] = None) -> None:
        """
        :param scriptId: Identifier of the script parsed.
        :type scriptId: Runtime.ScriptId
        :param url: URL or name of the script parsed (if any).
        :type url: str
        :param startLine: Line offset of the script within the resource with given URL (for script tags).
        :type startLine: int
        :param startColumn: Column offset of the script within the resource with given URL.
        :type startColumn: int
        :param endLine: Last line of the script.
        :type endLine: int
        :param endColumn: Length of the last line of the script.
        :type endColumn: int
        :param executionContextId: Specifies script creation context.
        :type executionContextId: Runtime.ExecutionContextId
        :param hash: Content hash of the script.
        :type hash: str
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: dict
        :param isLiveEdit: True, if this script is generated as a result of the live edit operation.
        :type isLiveEdit: bool
        :param sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: str
        :param hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: bool
        :param isModule: True, if this script is ES6 module.
        :type isModule: bool
        :param length: This script length.
        :type length: int
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Runtime.StackTrace
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.url: str = url
        self.startLine: int = startLine
        self.startColumn: int = startColumn
        self.endLine: int = endLine
        self.endColumn: int = endColumn
        self.executionContextId: Runtime.ExecutionContextId = executionContextId
        self.hash: str = hash
        self.executionContextAuxData: Optional[dict] = executionContextAuxData
        self.isLiveEdit: Optional[bool] = isLiveEdit
        self.sourceMapURL: Optional[str] = sourceMapURL
        self.hasSourceURL: Optional[bool] = hasSourceURL
        self.isModule: Optional[bool] = isModule
        self.length: Optional[int] = length
        self.stackTrace: Optional[Runtime.StackTrace] = stackTrace


EVENT_TO_CLASS = {
   "Debugger.breakpointResolved": BreakpointResolvedEvent,
   "Debugger.paused": PausedEvent,
   "Debugger.resumed": ResumedEvent,
   "Debugger.scriptFailedToParse": ScriptFailedToParseEvent,
   "Debugger.scriptParsed": ScriptParsedEvent,
}

