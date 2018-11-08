# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Debugger"]


@attr.dataclass(slots=True, cmp=False)
class Debugger(object):
    """
    Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing
breakpoints, stepping through execution, exploring stack traces, etc.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def continueToLocation(
        self, location: dict, targetCallFrames: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Continues execution until specific location is reached.

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
        return self.client.send("Debugger.continueToLocation", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables debugger for given page.
        """
        return self.client.send("Debugger.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables debugger for the given page. Clients should not assume that the debugging has been
enabled until the result for this command is received.
        """
        return self.client.send("Debugger.enable")

    def evaluateOnCallFrame(
        self,
        callFrameId: str,
        expression: str,
        objectGroup: Optional[str] = None,
        includeCommandLineAPI: Optional[bool] = None,
        silent: Optional[bool] = None,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
        throwOnSideEffect: Optional[bool] = None,
        timeout: Optional[float] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Evaluates expression on a given call frame.

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
        return self.client.send("Debugger.evaluateOnCallFrame", msg_dict)

    def getPossibleBreakpoints(
        self,
        start: dict,
        end: Optional[dict] = None,
        restrictToFunction: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Returns possible locations for breakpoint. scriptId in start and end range locations should be
the same.

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
        return self.client.send("Debugger.getPossibleBreakpoints", msg_dict)

    def getScriptSource(self, scriptId: str) -> Awaitable[Optional[dict]]:
        """
        Returns source for the script with given id.

        :param scriptId: Id of the script to get source for.
        :type scriptId: str
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        return self.client.send("Debugger.getScriptSource", msg_dict)

    def getStackTrace(self, stackTraceId: dict) -> Awaitable[Optional[dict]]:
        """
        Returns stack trace with given `stackTraceId`.

        :param stackTraceId: The stackTraceId
        :type stackTraceId: dict
        """
        msg_dict = dict()
        if stackTraceId is not None:
            msg_dict["stackTraceId"] = stackTraceId
        return self.client.send("Debugger.getStackTrace", msg_dict)

    def pause(self) -> Awaitable[Optional[dict]]:
        """
        Stops on the next JavaScript statement.
        """
        return self.client.send("Debugger.pause")

    def pauseOnAsyncCall(self, parentStackTraceId: dict) -> Awaitable[Optional[dict]]:
        """
        :param parentStackTraceId: Debugger will pause when async call with given stack trace is started.
        :type parentStackTraceId: dict
        """
        msg_dict = dict()
        if parentStackTraceId is not None:
            msg_dict["parentStackTraceId"] = parentStackTraceId
        return self.client.send("Debugger.pauseOnAsyncCall", msg_dict)

    def removeBreakpoint(self, breakpointId: str) -> Awaitable[Optional[dict]]:
        """
        Removes JavaScript breakpoint.

        :param breakpointId: The breakpointId
        :type breakpointId: str
        """
        msg_dict = dict()
        if breakpointId is not None:
            msg_dict["breakpointId"] = breakpointId
        return self.client.send("Debugger.removeBreakpoint", msg_dict)

    def restartFrame(self, callFrameId: str) -> Awaitable[Optional[dict]]:
        """
        Restarts particular call frame from the beginning.

        :param callFrameId: Call frame identifier to evaluate on.
        :type callFrameId: str
        """
        msg_dict = dict()
        if callFrameId is not None:
            msg_dict["callFrameId"] = callFrameId
        return self.client.send("Debugger.restartFrame", msg_dict)

    def resume(self) -> Awaitable[Optional[dict]]:
        """
        Resumes JavaScript execution.
        """
        return self.client.send("Debugger.resume")

    def scheduleStepIntoAsync(self) -> Awaitable[Optional[dict]]:
        """
        This method is deprecated - use Debugger.stepInto with breakOnAsyncCall and
Debugger.pauseOnAsyncTask instead. Steps into next scheduled async task if any is scheduled
before next pause. Returns success when async task is actually scheduled, returns error if no
task were scheduled or another scheduleStepIntoAsync was called.
        """
        return self.client.send("Debugger.scheduleStepIntoAsync")

    def searchInContent(
        self,
        scriptId: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Searches for given string in script content.

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
        return self.client.send("Debugger.searchInContent", msg_dict)

    def setAsyncCallStackDepth(self, maxDepth: int) -> Awaitable[Optional[dict]]:
        """
        Enables or disables async call stacks tracking.

        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        msg_dict = dict()
        if maxDepth is not None:
            msg_dict["maxDepth"] = maxDepth
        return self.client.send("Debugger.setAsyncCallStackDepth", msg_dict)

    def setBlackboxPatterns(self, patterns: List[str]) -> Awaitable[Optional[dict]]:
        """
        Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
scripts with url matching one of the patterns. VM will try to leave blackboxed script by
performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        :type patterns: List[str]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict["patterns"] = patterns
        return self.client.send("Debugger.setBlackboxPatterns", msg_dict)

    def setBlackboxedRanges(
        self, scriptId: str, positions: List[dict]
    ) -> Awaitable[Optional[dict]]:
        """
        Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
Positions array contains positions where blackbox state is changed. First interval isn't
blackboxed. Array should be sorted.

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
        return self.client.send("Debugger.setBlackboxedRanges", msg_dict)

    def setBreakpoint(
        self, location: dict, condition: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Sets JavaScript breakpoint at a given location.

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
        return self.client.send("Debugger.setBreakpoint", msg_dict)

    def setBreakpointByUrl(
        self,
        lineNumber: int,
        url: Optional[str] = None,
        urlRegex: Optional[str] = None,
        scriptHash: Optional[str] = None,
        columnNumber: Optional[int] = None,
        condition: Optional[str] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
command is issued, all existing parsed scripts will have breakpoints resolved and returned in
`locations` property. Further matching script parsing will result in subsequent
`breakpointResolved` events issued. This logical breakpoint will survive page reloads.

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
        return self.client.send("Debugger.setBreakpointByUrl", msg_dict)

    def setBreakpointOnFunctionCall(
        self, objectId: str, condition: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Sets JavaScript breakpoint before each call to the given function.
If another function was created from the same source as a given one,
calling it will also trigger the breakpoint.

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
        return self.client.send("Debugger.setBreakpointOnFunctionCall", msg_dict)

    def setBreakpointsActive(self, active: bool) -> Awaitable[Optional[dict]]:
        """
        Activates / deactivates all breakpoints on the page.

        :param active: New value for breakpoints active state.
        :type active: bool
        """
        msg_dict = dict()
        if active is not None:
            msg_dict["active"] = active
        return self.client.send("Debugger.setBreakpointsActive", msg_dict)

    def setPauseOnExceptions(self, state: str) -> Awaitable[Optional[dict]]:
        """
        Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or
no exceptions. Initial pause on exceptions state is `none`.

        :param state: Pause on exceptions mode.
        :type state: str
        """
        msg_dict = dict()
        if state is not None:
            msg_dict["state"] = state
        return self.client.send("Debugger.setPauseOnExceptions", msg_dict)

    def setReturnValue(self, newValue: dict) -> Awaitable[Optional[dict]]:
        """
        Changes return value in top frame. Available only at return break position.

        :param newValue: New return value.
        :type newValue: dict
        """
        msg_dict = dict()
        if newValue is not None:
            msg_dict["newValue"] = newValue
        return self.client.send("Debugger.setReturnValue", msg_dict)

    def setScriptSource(
        self, scriptId: str, scriptSource: str, dryRun: Optional[bool] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Edits JavaScript source live.

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
        return self.client.send("Debugger.setScriptSource", msg_dict)

    def setSkipAllPauses(self, skip: bool) -> Awaitable[Optional[dict]]:
        """
        Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

        :param skip: New value for skip pauses state.
        :type skip: bool
        """
        msg_dict = dict()
        if skip is not None:
            msg_dict["skip"] = skip
        return self.client.send("Debugger.setSkipAllPauses", msg_dict)

    def setVariableValue(
        self, scopeNumber: int, variableName: str, newValue: dict, callFrameId: str
    ) -> Awaitable[Optional[dict]]:
        """
        Changes value of variable in a callframe. Object-based scopes are not supported and must be
mutated manually.

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
        return self.client.send("Debugger.setVariableValue", msg_dict)

    def stepInto(
        self, breakOnAsyncCall: Optional[bool] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Steps into the function call.

        :param breakOnAsyncCall: Debugger will issue additional Debugger.paused notification if any async task is scheduled before next pause.
        :type breakOnAsyncCall: Optional[bool]
        """
        msg_dict = dict()
        if breakOnAsyncCall is not None:
            msg_dict["breakOnAsyncCall"] = breakOnAsyncCall
        return self.client.send("Debugger.stepInto", msg_dict)

    def stepOut(self) -> Awaitable[Optional[dict]]:
        """
        Steps out of the function call.
        """
        return self.client.send("Debugger.stepOut")

    def stepOver(self) -> Awaitable[Optional[dict]]:
        """
        Steps over the statement.
        """
        return self.client.send("Debugger.stepOver")

    def breakpointResolved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when breakpoint is resolved to an actual script and location.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Debugger.breakpointResolved", _cb)

            return future

        self.client.on("Debugger.breakpointResolved", cb)

    def paused(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Debugger.paused", _cb)

            return future

        self.client.on("Debugger.paused", cb)

    def resumed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when the virtual machine resumed execution.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Debugger.resumed", _cb)

            return future

        self.client.on("Debugger.resumed", cb)

    def scriptFailedToParse(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when virtual machine fails to parse the script.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Debugger.scriptFailedToParse", _cb)

            return future

        self.client.on("Debugger.scriptFailedToParse", cb)

    def scriptParsed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when virtual machine parses script. This event is also fired for all known and uncollected
        scripts upon enabling debugger.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Debugger.scriptParsed", _cb)

            return future

        self.client.on("Debugger.scriptParsed", cb)
