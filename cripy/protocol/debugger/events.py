from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class BreakpointResolvedEvent(BaseEvent):
    """Fired when breakpoint is resolved to an actual script and location."""

    event: str = "Debugger.breakpointResolved"

    def __init__(self) -> None:
        """
        :param breakpointId: Breakpoint unique identifier.
        :type BreakpointId:
        :param location: Actual breakpoint location.
        :type Location:
        """
        super().__init__()


class PausedEvent(BaseEvent):
    """Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria."""

    event: str = "Debugger.paused"

    def __init__(self) -> None:
        """
        :param callFrames: Call stack the virtual machine stopped on.
        :type array:
        :param reason: Pause reason.
        :type str:
        :param data: Object containing break-specific auxiliary properties.
        :type dict:
        :param hitBreakpoints: Hit breakpoints IDs
        :type array:
        :param asyncStackTrace: Async stack trace, if any.
        :type Runtime.StackTrace:
        :param asyncStackTraceId: Async stack trace, if any.
        :type Runtime.StackTraceId:
        :param asyncCallStackTraceId: Just scheduled async call will have this stack trace as parent stack during async
        execution. This field is available only after `Debugger.stepInto` call with
        `breakOnAsynCall` flag.
        :type Runtime.StackTraceId:
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
        :param scriptId: Identifier of the script parsed.
        :type Runtime.ScriptId:
        :param url: URL or name of the script parsed (if any).
        :type str:
        :param startLine: Line offset of the script within the resource with given URL (for script tags).
        :type int:
        :param startColumn: Column offset of the script within the resource with given URL.
        :type int:
        :param endLine: Last line of the script.
        :type int:
        :param endColumn: Length of the last line of the script.
        :type int:
        :param executionContextId: Specifies script creation context.
        :type Runtime.ExecutionContextId:
        :param hash: Content hash of the script.
        :type str:
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type dict:
        :param sourceMapURL: URL of source map associated with script (if any).
        :type str:
        :param hasSourceURL: True, if this script has sourceURL.
        :type bool:
        :param isModule: True, if this script is ES6 module.
        :type bool:
        :param length: This script length.
        :type int:
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if
        available.
        :type Runtime.StackTrace:
        """
        super().__init__()


class ScriptParsedEvent(BaseEvent):
    """Fired when virtual machine parses script.
	This event is also fired for all known and uncollected scripts upon enabling debugger."""

    event: str = "Debugger.scriptParsed"

    def __init__(self) -> None:
        """
        :param scriptId: Identifier of the script parsed.
        :type Runtime.ScriptId:
        :param url: URL or name of the script parsed (if any).
        :type str:
        :param startLine: Line offset of the script within the resource with given URL (for script tags).
        :type int:
        :param startColumn: Column offset of the script within the resource with given URL.
        :type int:
        :param endLine: Last line of the script.
        :type int:
        :param endColumn: Length of the last line of the script.
        :type int:
        :param executionContextId: Specifies script creation context.
        :type Runtime.ExecutionContextId:
        :param hash: Content hash of the script.
        :type str:
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type dict:
        :param isLiveEdit: True, if this script is generated as a result of the live edit operation.
        :type bool:
        :param sourceMapURL: URL of source map associated with script (if any).
        :type str:
        :param hasSourceURL: True, if this script has sourceURL.
        :type bool:
        :param isModule: True, if this script is ES6 module.
        :type bool:
        :param length: This script length.
        :type int:
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if
        available.
        :type Runtime.StackTrace:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Debugger.breakpointResolved": BreakpointResolvedEvent,
   "Debugger.paused": PausedEvent,
   "Debugger.resumed": ResumedEvent,
   "Debugger.scriptFailedToParse": ScriptFailedToParseEvent,
   "Debugger.scriptParsed": ScriptParsedEvent,
}

