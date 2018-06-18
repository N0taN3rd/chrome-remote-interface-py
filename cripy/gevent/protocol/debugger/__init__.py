from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.debugger import events as Events
from cripy.gevent.protocol.debugger import types as Types

__all__ = ["Debugger"] + Events.__all__ + Types.__all__


class Debugger(object):
    """
    Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing
breakpoints, stepping through execution, exploring stack traces, etc.
    """

    dependencies = ["Runtime"]

    def __init__(self, chrome):
        self.chrome = chrome

    def continueToLocation(self, location, targetCallFrames=None):
        """
        :param location: Location to continue to.
        :type location: dict
        :param targetCallFrames: The targetCallFrames
        :type targetCallFrames: Optional[str]
        """
        msg_dict = dict()
        if location is not None:
            msg_dict["location"] = location
        if targetCallFrames is not None:
            msg_dict["targetCallFrames"] = targetCallFrames
        wres = self.chrome.send("Debugger.continueToLocation", msg_dict)
        return wres.get()

    def disable(self):
        wres = self.chrome.send("Debugger.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Debugger.enable")
        res = wres.get()
        return res

    def evaluateOnCallFrame(
        self,
        callFrameId,
        expression,
        objectGroup=None,
        includeCommandLineAPI=None,
        silent=None,
        returnByValue=None,
        generatePreview=None,
        throwOnSideEffect=None,
        timeout=None,
    ):
        """
        :param callFrameId: Call frame identifier to evaluate on.
        :type callFrameId: str
        :param expression: Expression to evaluate.
        :type expression: str
        :param objectGroup: String object group name to put result into (allows rapid releasing resulting object handles using `releaseObjectGroup`).
        :type objectGroup: Optional[str]
        :param includeCommandLineAPI: Specifies whether command line API should be available to the evaluated expression, defaults to false.
        :type includeCommandLineAPI: Optional[bool]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :type throwOnSideEffect: Optional[bool]
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :type timeout: Optional[float]
        """
        msg_dict = dict()
        if callFrameId is not None:
            msg_dict["callFrameId"] = callFrameId
        if expression is not None:
            msg_dict["expression"] = expression
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        if includeCommandLineAPI is not None:
            msg_dict["includeCommandLineAPI"] = includeCommandLineAPI
        if silent is not None:
            msg_dict["silent"] = silent
        if returnByValue is not None:
            msg_dict["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        if throwOnSideEffect is not None:
            msg_dict["throwOnSideEffect"] = throwOnSideEffect
        if timeout is not None:
            msg_dict["timeout"] = timeout
        wres = self.chrome.send("Debugger.evaluateOnCallFrame", msg_dict)
        res = wres.get()
        res["result"] = Runtime.RemoteObject.safe_create(res["result"])
        res["exceptionDetails"] = Runtime.ExceptionDetails.safe_create(
            res["exceptionDetails"]
        )
        return res

    def getPossibleBreakpoints(self, start, end=None, restrictToFunction=None):
        """
        :param start: Start of range to search possible breakpoint locations in.
        :type start: dict
        :param end: End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range.
        :type end: Optional[dict]
        :param restrictToFunction: Only consider locations which are in the same (non-nested) function as start.
        :type restrictToFunction: Optional[bool]
        """
        msg_dict = dict()
        if start is not None:
            msg_dict["start"] = start
        if end is not None:
            msg_dict["end"] = end
        if restrictToFunction is not None:
            msg_dict["restrictToFunction"] = restrictToFunction
        wres = self.chrome.send("Debugger.getPossibleBreakpoints", msg_dict)
        res = wres.get()
        res["locations"] = Types.BreakLocation.safe_create_from_list(res["locations"])
        return res

    def getScriptSource(self, scriptId):
        """
        :param scriptId: Id of the script to get source for.
        :type scriptId: str
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        wres = self.chrome.send("Debugger.getScriptSource", msg_dict)
        res = wres.get()
        return res

    def getStackTrace(self, stackTraceId):
        """
        :param stackTraceId: The stackTraceId
        :type stackTraceId: dict
        """
        msg_dict = dict()
        if stackTraceId is not None:
            msg_dict["stackTraceId"] = stackTraceId
        wres = self.chrome.send("Debugger.getStackTrace", msg_dict)
        res = wres.get()
        res["stackTrace"] = Runtime.StackTrace.safe_create(res["stackTrace"])
        return res

    def pause(self):
        wres = self.chrome.send("Debugger.pause")
        return wres.get()

    def pauseOnAsyncCall(self, parentStackTraceId):
        """
        :param parentStackTraceId: Debugger will pause when async call with given stack trace is started.
        :type parentStackTraceId: dict
        """
        msg_dict = dict()
        if parentStackTraceId is not None:
            msg_dict["parentStackTraceId"] = parentStackTraceId
        wres = self.chrome.send("Debugger.pauseOnAsyncCall", msg_dict)
        return wres.get()

    def removeBreakpoint(self, breakpointId):
        """
        :param breakpointId: The breakpointId
        :type breakpointId: str
        """
        msg_dict = dict()
        if breakpointId is not None:
            msg_dict["breakpointId"] = breakpointId
        wres = self.chrome.send("Debugger.removeBreakpoint", msg_dict)
        return wres.get()

    def restartFrame(self, callFrameId):
        """
        :param callFrameId: Call frame identifier to evaluate on.
        :type callFrameId: str
        """
        msg_dict = dict()
        if callFrameId is not None:
            msg_dict["callFrameId"] = callFrameId
        wres = self.chrome.send("Debugger.restartFrame", msg_dict)
        res = wres.get()
        res["callFrames"] = Types.CallFrame.safe_create_from_list(res["callFrames"])
        res["asyncStackTrace"] = Runtime.StackTrace.safe_create(res["asyncStackTrace"])
        res["asyncStackTraceId"] = Runtime.StackTraceId.safe_create(
            res["asyncStackTraceId"]
        )
        return res

    def resume(self):
        wres = self.chrome.send("Debugger.resume")
        return wres.get()

    def scheduleStepIntoAsync(self):
        wres = self.chrome.send("Debugger.scheduleStepIntoAsync")
        return wres.get()

    def searchInContent(self, scriptId, query, caseSensitive=None, isRegex=None):
        """
        :param scriptId: Id of the script to search in.
        :type scriptId: str
        :param query: String to search for.
        :type query: str
        :param caseSensitive: If true, search is case sensitive.
        :type caseSensitive: Optional[bool]
        :param isRegex: If true, treats string parameter as regex.
        :type isRegex: Optional[bool]
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        if query is not None:
            msg_dict["query"] = query
        if caseSensitive is not None:
            msg_dict["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg_dict["isRegex"] = isRegex
        wres = self.chrome.send("Debugger.searchInContent", msg_dict)
        res = wres.get()
        res["result"] = Types.SearchMatch.safe_create_from_list(res["result"])
        return res

    def setAsyncCallStackDepth(self, maxDepth):
        """
        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        msg_dict = dict()
        if maxDepth is not None:
            msg_dict["maxDepth"] = maxDepth
        wres = self.chrome.send("Debugger.setAsyncCallStackDepth", msg_dict)
        return wres.get()

    def setBlackboxPatterns(self, patterns):
        """
        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        :type patterns: List[str]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict["patterns"] = patterns
        wres = self.chrome.send("Debugger.setBlackboxPatterns", msg_dict)
        return wres.get()

    def setBlackboxedRanges(self, scriptId, positions):
        """
        :param scriptId: Id of the script.
        :type scriptId: str
        :param positions: The positions
        :type positions: List[dict]
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        if positions is not None:
            msg_dict["positions"] = positions
        wres = self.chrome.send("Debugger.setBlackboxedRanges", msg_dict)
        return wres.get()

    def setBreakpoint(self, location, condition=None):
        """
        :param location: Location to set breakpoint in.
        :type location: dict
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        :type condition: Optional[str]
        """
        msg_dict = dict()
        if location is not None:
            msg_dict["location"] = location
        if condition is not None:
            msg_dict["condition"] = condition
        wres = self.chrome.send("Debugger.setBreakpoint", msg_dict)
        res = wres.get()
        res["actualLocation"] = Types.Location.safe_create(res["actualLocation"])
        return res

    def setBreakpointByUrl(
        self,
        lineNumber,
        url=None,
        urlRegex=None,
        scriptHash=None,
        columnNumber=None,
        condition=None,
    ):
        """
        :param lineNumber: Line number to set breakpoint at.
        :type lineNumber: int
        :param url: URL of the resources to set breakpoint on.
        :type url: Optional[str]
        :param urlRegex: Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or `urlRegex` must be specified.
        :type urlRegex: Optional[str]
        :param scriptHash: Script hash of the resources to set breakpoint on.
        :type scriptHash: Optional[str]
        :param columnNumber: Offset in the line to set breakpoint at.
        :type columnNumber: Optional[int]
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
        :type condition: Optional[str]
        """
        msg_dict = dict()
        if lineNumber is not None:
            msg_dict["lineNumber"] = lineNumber
        if url is not None:
            msg_dict["url"] = url
        if urlRegex is not None:
            msg_dict["urlRegex"] = urlRegex
        if scriptHash is not None:
            msg_dict["scriptHash"] = scriptHash
        if columnNumber is not None:
            msg_dict["columnNumber"] = columnNumber
        if condition is not None:
            msg_dict["condition"] = condition
        wres = self.chrome.send("Debugger.setBreakpointByUrl", msg_dict)
        res = wres.get()
        res["locations"] = Types.Location.safe_create_from_list(res["locations"])
        return res

    def setBreakpointOnFunctionCall(self, objectId, condition=None):
        """
        :param objectId: Function object id.
        :type objectId: str
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will stop on the breakpoint if this expression evaluates to true.
        :type condition: Optional[str]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if condition is not None:
            msg_dict["condition"] = condition
        wres = self.chrome.send("Debugger.setBreakpointOnFunctionCall", msg_dict)
        res = wres.get()
        return res

    def setBreakpointsActive(self, active):
        """
        :param active: New value for breakpoints active state.
        :type active: bool
        """
        msg_dict = dict()
        if active is not None:
            msg_dict["active"] = active
        wres = self.chrome.send("Debugger.setBreakpointsActive", msg_dict)
        return wres.get()

    def setPauseOnExceptions(self, state):
        """
        :param state: Pause on exceptions mode.
        :type state: str
        """
        msg_dict = dict()
        if state is not None:
            msg_dict["state"] = state
        wres = self.chrome.send("Debugger.setPauseOnExceptions", msg_dict)
        return wres.get()

    def setReturnValue(self, newValue):
        """
        :param newValue: New return value.
        :type newValue: dict
        """
        msg_dict = dict()
        if newValue is not None:
            msg_dict["newValue"] = newValue
        wres = self.chrome.send("Debugger.setReturnValue", msg_dict)
        return wres.get()

    def setScriptSource(self, scriptId, scriptSource, dryRun=None):
        """
        :param scriptId: Id of the script to edit.
        :type scriptId: str
        :param scriptSource: New content of the script.
        :type scriptSource: str
        :param dryRun: If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code.
        :type dryRun: Optional[bool]
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        if scriptSource is not None:
            msg_dict["scriptSource"] = scriptSource
        if dryRun is not None:
            msg_dict["dryRun"] = dryRun
        wres = self.chrome.send("Debugger.setScriptSource", msg_dict)
        res = wres.get()
        res["callFrames"] = Types.CallFrame.safe_create_from_list(res["callFrames"])
        res["asyncStackTrace"] = Runtime.StackTrace.safe_create(res["asyncStackTrace"])
        res["asyncStackTraceId"] = Runtime.StackTraceId.safe_create(
            res["asyncStackTraceId"]
        )
        res["exceptionDetails"] = Runtime.ExceptionDetails.safe_create(
            res["exceptionDetails"]
        )
        return res

    def setSkipAllPauses(self, skip):
        """
        :param skip: New value for skip pauses state.
        :type skip: bool
        """
        msg_dict = dict()
        if skip is not None:
            msg_dict["skip"] = skip
        wres = self.chrome.send("Debugger.setSkipAllPauses", msg_dict)
        return wres.get()

    def setVariableValue(self, scopeNumber, variableName, newValue, callFrameId):
        """
        :param scopeNumber: 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually.
        :type scopeNumber: int
        :param variableName: Variable name.
        :type variableName: str
        :param newValue: New variable value.
        :type newValue: dict
        :param callFrameId: Id of callframe that holds variable.
        :type callFrameId: str
        """
        msg_dict = dict()
        if scopeNumber is not None:
            msg_dict["scopeNumber"] = scopeNumber
        if variableName is not None:
            msg_dict["variableName"] = variableName
        if newValue is not None:
            msg_dict["newValue"] = newValue
        if callFrameId is not None:
            msg_dict["callFrameId"] = callFrameId
        wres = self.chrome.send("Debugger.setVariableValue", msg_dict)
        return wres.get()

    def stepInto(self, breakOnAsyncCall=None):
        """
        :param breakOnAsyncCall: Debugger will issue additional Debugger.paused notification if any async task is scheduled before next pause.
        :type breakOnAsyncCall: Optional[bool]
        """
        msg_dict = dict()
        if breakOnAsyncCall is not None:
            msg_dict["breakOnAsyncCall"] = breakOnAsyncCall
        wres = self.chrome.send("Debugger.stepInto", msg_dict)
        return wres.get()

    def stepOut(self):
        wres = self.chrome.send("Debugger.stepOut")
        return wres.get()

    def stepOver(self):
        wres = self.chrome.send("Debugger.stepOver")
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
