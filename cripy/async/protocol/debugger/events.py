from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.runtime import types as Runtime
from cripy.async.protocol.debugger.types import *

__all__ = [
    "BreakpointResolvedEvent",
    "PausedEvent",
    "ResumedEvent",
    "ScriptFailedToParseEvent",
    "ScriptParsedEvent",
    "DEBUGGER_EVENTS_TO_CLASS",
    "DEBUGGER_EVENTS_NS"
]

class BreakpointResolvedEvent(object):
    """
    Fired when breakpoint is resolved to an actual script and location.
    """

    event = "Debugger.breakpointResolved"

    __slots__ = ["breakpointId", "location"]

    def __init__(self, breakpointId: str, location: Union[Location, dict]) -> None:
        """
        Create a new instance of BreakpointResolvedEvent

        :param breakpointId: Breakpoint unique identifier.
        :type breakpointId: str
        :param location: Actual breakpoint location.
        :type location: dict
        """
        super().__init__()
        self.breakpointId = breakpointId
        self.location = Location.safe_create(location)

    def __repr__(self) -> str:
        repr_args = []
        if self.breakpointId is not None:
            repr_args.append("breakpointId={!r}".format(self.breakpointId))
        if self.location is not None:
            repr_args.append("location={!r}".format(self.location))
        return "BreakpointResolvedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['BreakpointResolvedEvent', dict]]:
        """
        Safely create BreakpointResolvedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of BreakpointResolvedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of BreakpointResolvedEvent if creation did not fail
        :rtype: Optional[Union[dict, BreakpointResolvedEvent]]
        """
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
        """
        Safely create a new list BreakpointResolvedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list BreakpointResolvedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of BreakpointResolvedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, BreakpointResolvedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BreakpointResolvedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class PausedEvent(object):
    """
    Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.
    """

    event = "Debugger.paused"

    __slots__ = ["callFrames", "reason", "data", "hitBreakpoints", "asyncStackTrace", "asyncStackTraceId", "asyncCallStackTraceId"]

    def __init__(self, callFrames: List[Union[CallFrame, dict]], reason: str, data: Optional[dict] = None, hitBreakpoints: Optional[List[str]] = None, asyncStackTrace: Optional[Union[Runtime.StackTrace, dict]] = None, asyncStackTraceId: Optional[Union[Runtime.StackTraceId, dict]] = None, asyncCallStackTraceId: Optional[Union[Runtime.StackTraceId, dict]] = None) -> None:
        """
        Create a new instance of PausedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.callFrames is not None:
            repr_args.append("callFrames={!r}".format(self.callFrames))
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        if self.data is not None:
            repr_args.append("data={!r}".format(self.data))
        if self.hitBreakpoints is not None:
            repr_args.append("hitBreakpoints={!r}".format(self.hitBreakpoints))
        if self.asyncStackTrace is not None:
            repr_args.append("asyncStackTrace={!r}".format(self.asyncStackTrace))
        if self.asyncStackTraceId is not None:
            repr_args.append("asyncStackTraceId={!r}".format(self.asyncStackTraceId))
        if self.asyncCallStackTraceId is not None:
            repr_args.append("asyncCallStackTraceId={!r}".format(self.asyncCallStackTraceId))
        return "PausedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PausedEvent', dict]]:
        """
        Safely create PausedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of PausedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of PausedEvent if creation did not fail
        :rtype: Optional[Union[dict, PausedEvent]]
        """
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
        """
        Safely create a new list PausedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list PausedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of PausedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, PausedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PausedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResumedEvent(dict):
    """
    Fired when the virtual machine resumed execution.
    """

    event = "Debugger.resumed"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "ResumedEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ResumedEvent', dict]]:
        """
        Safely create ResumedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ResumedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ResumedEvent if creation did not fail
        :rtype: Optional[Union[dict, ResumedEvent]]
        """
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
        """
        Safely create a new list ResumedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ResumedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ResumedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ResumedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResumedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptFailedToParseEvent(object):
    """
    Fired when virtual machine fails to parse the script.
    """

    event = "Debugger.scriptFailedToParse"

    __slots__ = ["scriptId", "url", "startLine", "startColumn", "endLine", "endColumn", "executionContextId", "hash", "executionContextAuxData", "sourceMapURL", "hasSourceURL", "isModule", "length", "stackTrace"]

    def __init__(self, scriptId: str, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: int, hash: str, executionContextAuxData: Optional[dict] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
        """
        Create a new instance of ScriptFailedToParseEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.startLine is not None:
            repr_args.append("startLine={!r}".format(self.startLine))
        if self.startColumn is not None:
            repr_args.append("startColumn={!r}".format(self.startColumn))
        if self.endLine is not None:
            repr_args.append("endLine={!r}".format(self.endLine))
        if self.endColumn is not None:
            repr_args.append("endColumn={!r}".format(self.endColumn))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        if self.hash is not None:
            repr_args.append("hash={!r}".format(self.hash))
        if self.executionContextAuxData is not None:
            repr_args.append("executionContextAuxData={!r}".format(self.executionContextAuxData))
        if self.sourceMapURL is not None:
            repr_args.append("sourceMapURL={!r}".format(self.sourceMapURL))
        if self.hasSourceURL is not None:
            repr_args.append("hasSourceURL={!r}".format(self.hasSourceURL))
        if self.isModule is not None:
            repr_args.append("isModule={!r}".format(self.isModule))
        if self.length is not None:
            repr_args.append("length={!r}".format(self.length))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        return "ScriptFailedToParseEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptFailedToParseEvent', dict]]:
        """
        Safely create ScriptFailedToParseEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScriptFailedToParseEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScriptFailedToParseEvent if creation did not fail
        :rtype: Optional[Union[dict, ScriptFailedToParseEvent]]
        """
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
        """
        Safely create a new list ScriptFailedToParseEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScriptFailedToParseEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScriptFailedToParseEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScriptFailedToParseEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptFailedToParseEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptParsedEvent(object):
    """
    Fired when virtual machine parses script.
	This event is also fired for all known and uncollected scripts upon enabling debugger.
    """

    event = "Debugger.scriptParsed"

    __slots__ = ["scriptId", "url", "startLine", "startColumn", "endLine", "endColumn", "executionContextId", "hash", "executionContextAuxData", "isLiveEdit", "sourceMapURL", "hasSourceURL", "isModule", "length", "stackTrace"]

    def __init__(self, scriptId: str, url: str, startLine: int, startColumn: int, endLine: int, endColumn: int, executionContextId: int, hash: str, executionContextAuxData: Optional[dict] = None, isLiveEdit: Optional[bool] = None, sourceMapURL: Optional[str] = None, hasSourceURL: Optional[bool] = None, isModule: Optional[bool] = None, length: Optional[int] = None, stackTrace: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
        """
        Create a new instance of ScriptParsedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.startLine is not None:
            repr_args.append("startLine={!r}".format(self.startLine))
        if self.startColumn is not None:
            repr_args.append("startColumn={!r}".format(self.startColumn))
        if self.endLine is not None:
            repr_args.append("endLine={!r}".format(self.endLine))
        if self.endColumn is not None:
            repr_args.append("endColumn={!r}".format(self.endColumn))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        if self.hash is not None:
            repr_args.append("hash={!r}".format(self.hash))
        if self.executionContextAuxData is not None:
            repr_args.append("executionContextAuxData={!r}".format(self.executionContextAuxData))
        if self.isLiveEdit is not None:
            repr_args.append("isLiveEdit={!r}".format(self.isLiveEdit))
        if self.sourceMapURL is not None:
            repr_args.append("sourceMapURL={!r}".format(self.sourceMapURL))
        if self.hasSourceURL is not None:
            repr_args.append("hasSourceURL={!r}".format(self.hasSourceURL))
        if self.isModule is not None:
            repr_args.append("isModule={!r}".format(self.isModule))
        if self.length is not None:
            repr_args.append("length={!r}".format(self.length))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        return "ScriptParsedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptParsedEvent', dict]]:
        """
        Safely create ScriptParsedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScriptParsedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScriptParsedEvent if creation did not fail
        :rtype: Optional[Union[dict, ScriptParsedEvent]]
        """
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
        """
        Safely create a new list ScriptParsedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScriptParsedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScriptParsedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScriptParsedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptParsedEvent.safe_create(it))
            return list_of_self
        else:
            return init


DEBUGGER_EVENTS_TO_CLASS = {
   "Debugger.breakpointResolved": BreakpointResolvedEvent,
   "Debugger.paused": PausedEvent,
   "Debugger.resumed": ResumedEvent,
   "Debugger.scriptFailedToParse": ScriptFailedToParseEvent,
   "Debugger.scriptParsed": ScriptParsedEvent,
}

DebuggerNS = namedtuple("DebuggerNS", ["BreakpointResolved", "Paused", "Resumed", "ScriptFailedToParse", "ScriptParsed"])

DEBUGGER_EVENTS_NS = DebuggerNS(
  BreakpointResolved="Debugger.breakpointResolved",
  Paused="Debugger.paused",
  Resumed="Debugger.resumed",
  ScriptFailedToParse="Debugger.scriptFailedToParse",
  ScriptParsed="Debugger.scriptParsed",
)
