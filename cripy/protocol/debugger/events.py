from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class BreakpointResolvedEvent(BaseEvent):
    """Fired when breakpoint is resolved to an actual script and location."""

    event: str = "Debugger.breakpointResolved"

    def __init__(self) -> None:
        """
        :param BreakpointId breakpointId: Breakpoint unique identifier.
        :type breakpointId: BreakpointId
        :param Location location: Actual breakpoint location.
        :type location: Location
        """
        super().__init__()


class PausedEvent(BaseEvent):
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

    event: str = "Debugger.paused"

    def __init__(self) -> None:
        """
        :param array callFrames: Call stack the virtual machine stopped on.
        :type callFrames: array
        :param str reason: Pause reason.
        :type reason: str
        :param dict data: Object containing break-specific auxiliary properties.
        :type data: dict
        :param array hitBreakpoints: Hit breakpoints IDs
        :type hitBreakpoints: array
        :param Runtime.StackTrace asyncStackTrace: Async stack trace, if any.
        :type asyncStackTrace: Runtime.StackTrace
        :param Runtime.StackTraceId asyncStackTraceId: Async stack trace, if any.
        :type asyncStackTraceId: Runtime.StackTraceId
        :param Runtime.StackTraceId asyncCallStackTraceId: Just scheduled async call will have this stack trace as parent stack during async execution. This field is available only after `Debugger.stepInto` call with `breakOnAsynCall` flag.
        :type asyncCallStackTraceId: Runtime.StackTraceId
        """
        super().__init__()


class ResumedEvent(BaseEvent):
    """Fired when the virtual machine resumed execution."""

    event: str = "Debugger.resumed"

    def __init__(self) -> None:
        super().__init__()


class ScriptFailedToParseEvent(BaseEvent):
    """Fired when virtual machine fails to parse the script."""

    event: str = "Debugger.scriptFailedToParse"

    def __init__(self) -> None:
        """
        :param Runtime.ScriptId scriptId: Identifier of the script parsed.
        :type scriptId: Runtime.ScriptId
        :param str url: URL or name of the script parsed (if any).
        :type url: str
        :param int startLine: Line offset of the script within the resource with given URL (for script tags).
        :type startLine: int
        :param int startColumn: Column offset of the script within the resource with given URL.
        :type startColumn: int
        :param int endLine: Last line of the script.
        :type endLine: int
        :param int endColumn: Length of the last line of the script.
        :type endColumn: int
        :param Runtime.ExecutionContextId executionContextId: Specifies script creation context.
        :type executionContextId: Runtime.ExecutionContextId
        :param str hash: Content hash of the script.
        :type hash: str
        :param dict executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: dict
        :param str sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: str
        :param bool hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: bool
        :param bool isModule: True, if this script is ES6 module.
        :type isModule: bool
        :param int length: This script length.
        :type length: int
        :param Runtime.StackTrace stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Runtime.StackTrace
        """
        super().__init__()


class ScriptParsedEvent(BaseEvent):
    """Fired when virtual machine parses script.
	This event is also fired for all known and uncollected scripts upon enabling debugger."""

    event: str = "Debugger.scriptParsed"

    def __init__(self) -> None:
        """
        :param Runtime.ScriptId scriptId: Identifier of the script parsed.
        :type scriptId: Runtime.ScriptId
        :param str url: URL or name of the script parsed (if any).
        :type url: str
        :param int startLine: Line offset of the script within the resource with given URL (for script tags).
        :type startLine: int
        :param int startColumn: Column offset of the script within the resource with given URL.
        :type startColumn: int
        :param int endLine: Last line of the script.
        :type endLine: int
        :param int endColumn: Length of the last line of the script.
        :type endColumn: int
        :param Runtime.ExecutionContextId executionContextId: Specifies script creation context.
        :type executionContextId: Runtime.ExecutionContextId
        :param str hash: Content hash of the script.
        :type hash: str
        :param dict executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: dict
        :param bool isLiveEdit: True, if this script is generated as a result of the live edit operation.
        :type isLiveEdit: bool
        :param str sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: str
        :param bool hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: bool
        :param bool isModule: True, if this script is ES6 module.
        :type isModule: bool
        :param int length: This script length.
        :type length: int
        :param Runtime.StackTrace stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Runtime.StackTrace
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Debugger.breakpointResolved": BreakpointResolvedEvent,
   "Debugger.paused": PausedEvent,
   "Debugger.resumed": ResumedEvent,
   "Debugger.scriptFailedToParse": ScriptFailedToParseEvent,
   "Debugger.scriptParsed": ScriptParsedEvent,
}

