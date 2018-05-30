from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.runtime import types as Runtime
try:
    from cripy.protocol.debugger.types import *
except ImportError:
    pass


class BreakpointResolvedEvent(BaseEvent):
    """
    Fired when breakpoint is resolved to an actual script and location.
    """

    event = "Debugger.breakpointResolved"

    def __init__(self, breakpointId: str, location: Union[Location, dict]) -> None:
        """
        :param breakpointId: Breakpoint unique identifier.
        :type breakpointId: str
        :param location: Actual breakpoint location.
        :type location: dict
        """
        super().__init__()
        self.breakpointId = breakpointId
        self.location = Location.safe_create(location)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['BreakpointResolvedEvent', dict]]:
        if init is not None:
            try:
                ourselves = BreakpointResolvedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['BreakpointResolvedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BreakpointResolvedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class PausedEvent(BaseEvent):
    """
    Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.
    """

    event = "Debugger.paused"

    def __init__(self, callFrames: List[Union[CallFrame, dict]], reason: str, data: Optional[dict] = None, hitBreakpoints: Optional[List[str]] = None, asyncStackTrace: Optional[Union[Runtime.StackTrace, dict]] = None, asyncStackTraceId: Optional[Union[Runtime.StackTraceId, dict]] = None, asyncCallStackTraceId: Optional[Union[Runtime.StackTraceId, dict]] = None) -> None:
        """
        :param callFrames: Call stack the virtual machine stopped on.
        :type callFrames: List[dict]
        :param reason: Pause reason.
        :type reason: str
        :param data: Object containing break-specific auxiliary properties.
        :type data: Optional[dict]
        :param hitBreakpoints: Hit breakpoints IDs
        :type hitBreakpoints: Optional[List[str]]
        :param asyncStackTrace: Async stack trace, if any.
        :type asyncStackTrace: Optional[dict]
        :param asyncStackTraceId: Async stack trace, if any.
        :type asyncStackTraceId: Optional[dict]
        :param asyncCallStackTraceId: Just scheduled async call will have this stack trace as parent stack during async execution. This field is available only after `Debugger.stepInto` call with `breakOnAsynCall` flag.
        :type asyncCallStackTraceId: Optional[dict]
        """
        super().__init__()
        self.callFrames = CallFrame.safe_create_from_list(callFrames)
        self.reason = reason
        self.data = data
        self.hitBreakpoints = hitBreakpoints
        self.asyncStackTrace = Runtime.StackTrace.safe_create(asyncStackTrace)
        self.asyncStackTraceId = Runtime.StackTraceId.safe_create(asyncStackTraceId)
        self.asyncCallStackTraceId = Runtime.StackTraceId.safe_create(asyncCallStackTraceId)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PausedEvent', dict]]:
        if init is not None:
            try:
                ourselves = PausedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['PausedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PausedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResumedEvent(BaseEvent, dict):
    """
    Fired when the virtual machine resumed execution.
    """

    event = "Debugger.resumed"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ResumedEvent', dict]]:
        if init is not None:
            try:
                ourselves = ResumedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ResumedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResumedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptFailedToParseEvent(BaseEvent):
    """
    Fired when virtual machine fails to parse the script.
    """

    event = "Debugger.scriptFailedToParse"

    def __init__(self, scriptId: str, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: int, hash: str, executionContextAuxData: Optional[dict] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
        """
        :param scriptId: Identifier of the script parsed.
        :type scriptId: str
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
        :type executionContextId: int
        :param hash: Content hash of the script.
        :type hash: str
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: Optional[dict]
        :param sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: Optional[str]
        :param hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: Optional[bool]
        :param isModule: True, if this script is ES6 module.
        :type isModule: Optional[bool]
        :param length: This script length.
        :type length: Optional[int]
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Optional[dict]
        """
        super().__init__()
        self.scriptId = scriptId
        self.url = url
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.executionContextId = executionContextId
        self.hash = hash
        self.executionContextAuxData = executionContextAuxData
        self.sourceMapURL = sourceMapURL
        self.hasSourceURL = hasSourceURL
        self.isModule = isModule
        self.length = length
        self.stackTrace = Runtime.StackTrace.safe_create(stackTrace)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptFailedToParseEvent', dict]]:
        if init is not None:
            try:
                ourselves = ScriptFailedToParseEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScriptFailedToParseEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptFailedToParseEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptParsedEvent(BaseEvent):
    """
    Fired when virtual machine parses script.
	This event is also fired for all known and uncollected scripts upon enabling debugger.
    """

    event = "Debugger.scriptParsed"

    def __init__(self, scriptId: str, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: int, hash: str, executionContextAuxData: Optional[dict] = None, isLiveEdit: Optional[bool] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
        """
        :param scriptId: Identifier of the script parsed.
        :type scriptId: str
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
        :type executionContextId: int
        :param hash: Content hash of the script.
        :type hash: str
        :param executionContextAuxData: Embedder-specific auxiliary data.
        :type executionContextAuxData: Optional[dict]
        :param isLiveEdit: True, if this script is generated as a result of the live edit operation.
        :type isLiveEdit: Optional[bool]
        :param sourceMapURL: URL of source map associated with script (if any).
        :type sourceMapURL: Optional[str]
        :param hasSourceURL: True, if this script has sourceURL.
        :type hasSourceURL: Optional[bool]
        :param isModule: True, if this script is ES6 module.
        :type isModule: Optional[bool]
        :param length: This script length.
        :type length: Optional[int]
        :param stackTrace: JavaScript top stack frame of where the script parsed event was triggered if available.
        :type stackTrace: Optional[dict]
        """
        super().__init__()
        self.scriptId = scriptId
        self.url = url
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.executionContextId = executionContextId
        self.hash = hash
        self.executionContextAuxData = executionContextAuxData
        self.isLiveEdit = isLiveEdit
        self.sourceMapURL = sourceMapURL
        self.hasSourceURL = hasSourceURL
        self.isModule = isModule
        self.length = length
        self.stackTrace = Runtime.StackTrace.safe_create(stackTrace)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptParsedEvent', dict]]:
        if init is not None:
            try:
                ourselves = ScriptParsedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScriptParsedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptParsedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Debugger.breakpointResolved": BreakpointResolvedEvent,
   "Debugger.paused": PausedEvent,
   "Debugger.resumed": ResumedEvent,
   "Debugger.scriptFailedToParse": ScriptFailedToParseEvent,
   "Debugger.scriptParsed": ScriptParsedEvent,
}

