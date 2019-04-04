"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Debugger"]


class Debugger:
    """
    Debugger domain exposes JavaScript debugging capabilities. It allows setting and removing
    breakpoints, stepping through execution, exploring stack traces, etc.
     
    Domain Dependencies: 
      * Runtime
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Debugger

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def continueToLocation(
        self, location: Dict[str, Any], targetCallFrames: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Continues execution until specific location is reached.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-continueToLocation`

        :param location: Location to continue to.
        :param targetCallFrames: The targetCallFrames
        :return: The results of the command
        """
        msg = {"location": location}
        if targetCallFrames is not None:
            msg["targetCallFrames"] = targetCallFrames
        return self.client.send("Debugger.continueToLocation", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables debugger for given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-disable`

        :return: The results of the command
        """
        return self.client.send("Debugger.disable", {})

    def enable(
        self, maxScriptsCacheSize: Optional[Union[int, float]] = None
    ) -> Awaitable[Dict]:
        """
        Enables debugger for the given page. Clients should not assume that the debugging has been
        enabled until the result for this command is received.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-enable`

        :param maxScriptsCacheSize: The maximum size in bytes of collected scripts (not referenced by other heap objects)
         the debugger can hold. Puts no limit if paramter is omitted.
        :return: The results of the command
        """
        msg = {}
        if maxScriptsCacheSize is not None:
            msg["maxScriptsCacheSize"] = maxScriptsCacheSize
        return self.client.send("Debugger.enable", msg)

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
        timeout: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Evaluates expression on a given call frame.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-evaluateOnCallFrame`

        :param callFrameId: Call frame identifier to evaluate on.
        :param expression: Expression to evaluate.
        :param objectGroup: String object group name to put result into (allows rapid releasing resulting object handles
         using `releaseObjectGroup`).
        :param includeCommandLineAPI: Specifies whether command line API should be available to the evaluated expression, defaults
         to false.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
         execution. Overrides `setPauseOnException` state.
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :param generatePreview: Whether preview should be generated for the result.
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :return: The results of the command
        """
        msg = {"callFrameId": callFrameId, "expression": expression}
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        if includeCommandLineAPI is not None:
            msg["includeCommandLineAPI"] = includeCommandLineAPI
        if silent is not None:
            msg["silent"] = silent
        if returnByValue is not None:
            msg["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        if throwOnSideEffect is not None:
            msg["throwOnSideEffect"] = throwOnSideEffect
        if timeout is not None:
            msg["timeout"] = timeout
        return self.client.send("Debugger.evaluateOnCallFrame", msg)

    def getPossibleBreakpoints(
        self,
        start: Dict[str, Any],
        end: Optional[Dict[str, Any]] = None,
        restrictToFunction: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Returns possible locations for breakpoint. scriptId in start and end range locations should be
        the same.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-getPossibleBreakpoints`

        :param start: Start of range to search possible breakpoint locations in.
        :param end: End of range to search possible breakpoint locations in (excluding). When not specified, end
         of scripts is used as end of range.
        :param restrictToFunction: Only consider locations which are in the same (non-nested) function as start.
        :return: The results of the command
        """
        msg = {"start": start}
        if end is not None:
            msg["end"] = end
        if restrictToFunction is not None:
            msg["restrictToFunction"] = restrictToFunction
        return self.client.send("Debugger.getPossibleBreakpoints", msg)

    def getScriptSource(self, scriptId: str) -> Awaitable[Dict]:
        """
        Returns source for the script with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-getScriptSource`

        :param scriptId: Id of the script to get source for.
        :return: The results of the command
        """
        return self.client.send("Debugger.getScriptSource", {"scriptId": scriptId})

    def getStackTrace(self, stackTraceId: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Returns stack trace with given `stackTraceId`.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-getStackTrace`

        :param stackTraceId: The stackTraceId
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.getStackTrace", {"stackTraceId": stackTraceId}
        )

    def pause(self) -> Awaitable[Dict]:
        """
        Stops on the next JavaScript statement.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-pause`

        :return: The results of the command
        """
        return self.client.send("Debugger.pause", {})

    def pauseOnAsyncCall(self, parentStackTraceId: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-pauseOnAsyncCall`

        :param parentStackTraceId: Debugger will pause when async call with given stack trace is started.
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.pauseOnAsyncCall", {"parentStackTraceId": parentStackTraceId}
        )

    def removeBreakpoint(self, breakpointId: str) -> Awaitable[Dict]:
        """
        Removes JavaScript breakpoint.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-removeBreakpoint`

        :param breakpointId: The breakpointId
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.removeBreakpoint", {"breakpointId": breakpointId}
        )

    def restartFrame(self, callFrameId: str) -> Awaitable[Dict]:
        """
        Restarts particular call frame from the beginning.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-restartFrame`

        :param callFrameId: Call frame identifier to evaluate on.
        :return: The results of the command
        """
        return self.client.send("Debugger.restartFrame", {"callFrameId": callFrameId})

    def resume(self) -> Awaitable[Dict]:
        """
        Resumes JavaScript execution.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-resume`

        :return: The results of the command
        """
        return self.client.send("Debugger.resume", {})

    def searchInContent(
        self,
        scriptId: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Searches for given string in script content.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-searchInContent`

        :param scriptId: Id of the script to search in.
        :param query: String to search for.
        :param caseSensitive: If true, search is case sensitive.
        :param isRegex: If true, treats string parameter as regex.
        :return: The results of the command
        """
        msg = {"scriptId": scriptId, "query": query}
        if caseSensitive is not None:
            msg["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg["isRegex"] = isRegex
        return self.client.send("Debugger.searchInContent", msg)

    def setAsyncCallStackDepth(self, maxDepth: int) -> Awaitable[Dict]:
        """
        Enables or disables async call stacks tracking.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setAsyncCallStackDepth`

        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
         call stacks (default).
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.setAsyncCallStackDepth", {"maxDepth": maxDepth}
        )

    def setBlackboxPatterns(self, patterns: List[str]) -> Awaitable[Dict]:
        """
        Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
        scripts with url matching one of the patterns. VM will try to leave blackboxed script by
        performing 'step in' several times, finally resorting to 'step out' if unsuccessful.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBlackboxPatterns`

        :param patterns: Array of regexps that will be used to check script url for blackbox state.
        :return: The results of the command
        """
        return self.client.send("Debugger.setBlackboxPatterns", {"patterns": patterns})

    def setBlackboxedRanges(
        self, scriptId: str, positions: List[Dict[str, Any]]
    ) -> Awaitable[Dict]:
        """
        Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
        scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
        Positions array contains positions where blackbox state is changed. First interval isn't
        blackboxed. Array should be sorted.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBlackboxedRanges`

        :param scriptId: Id of the script.
        :param positions: The positions
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.setBlackboxedRanges",
            {"scriptId": scriptId, "positions": positions},
        )

    def setBreakpoint(
        self, location: Dict[str, Any], condition: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Sets JavaScript breakpoint at a given location.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBreakpoint`

        :param location: Location to set breakpoint in.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
         breakpoint if this expression evaluates to true.
        :return: The results of the command
        """
        msg = {"location": location}
        if condition is not None:
            msg["condition"] = condition
        return self.client.send("Debugger.setBreakpoint", msg)

    def setBreakpointByUrl(
        self,
        lineNumber: int,
        url: Optional[str] = None,
        urlRegex: Optional[str] = None,
        scriptHash: Optional[str] = None,
        columnNumber: Optional[int] = None,
        condition: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
        command is issued, all existing parsed scripts will have breakpoints resolved and returned in
        `locations` property. Further matching script parsing will result in subsequent
        `breakpointResolved` events issued. This logical breakpoint will survive page reloads.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBreakpointByUrl`

        :param lineNumber: Line number to set breakpoint at.
        :param url: URL of the resources to set breakpoint on.
        :param urlRegex: Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or
         `urlRegex` must be specified.
        :param scriptHash: Script hash of the resources to set breakpoint on.
        :param columnNumber: Offset in the line to set breakpoint at.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will only stop on the
         breakpoint if this expression evaluates to true.
        :return: The results of the command
        """
        msg = {"lineNumber": lineNumber}
        if url is not None:
            msg["url"] = url
        if urlRegex is not None:
            msg["urlRegex"] = urlRegex
        if scriptHash is not None:
            msg["scriptHash"] = scriptHash
        if columnNumber is not None:
            msg["columnNumber"] = columnNumber
        if condition is not None:
            msg["condition"] = condition
        return self.client.send("Debugger.setBreakpointByUrl", msg)

    def setBreakpointOnFunctionCall(
        self, objectId: str, condition: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Sets JavaScript breakpoint before each call to the given function.
        If another function was created from the same source as a given one,
        calling it will also trigger the breakpoint.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBreakpointOnFunctionCall`

        :param objectId: Function object id.
        :param condition: Expression to use as a breakpoint condition. When specified, debugger will
         stop on the breakpoint if this expression evaluates to true.
        :return: The results of the command
        """
        msg = {"objectId": objectId}
        if condition is not None:
            msg["condition"] = condition
        return self.client.send("Debugger.setBreakpointOnFunctionCall", msg)

    def setBreakpointsActive(self, active: bool) -> Awaitable[Dict]:
        """
        Activates / deactivates all breakpoints on the page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setBreakpointsActive`

        :param active: New value for breakpoints active state.
        :return: The results of the command
        """
        return self.client.send("Debugger.setBreakpointsActive", {"active": active})

    def setPauseOnExceptions(self, state: str) -> Awaitable[Dict]:
        """
        Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or
        no exceptions. Initial pause on exceptions state is `none`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setPauseOnExceptions`

        :param state: Pause on exceptions mode.
        :return: The results of the command
        """
        return self.client.send("Debugger.setPauseOnExceptions", {"state": state})

    def setReturnValue(self, newValue: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Changes return value in top frame. Available only at return break position.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setReturnValue`

        :param newValue: New return value.
        :return: The results of the command
        """
        return self.client.send("Debugger.setReturnValue", {"newValue": newValue})

    def setScriptSource(
        self, scriptId: str, scriptSource: str, dryRun: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Edits JavaScript source live.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setScriptSource`

        :param scriptId: Id of the script to edit.
        :param scriptSource: New content of the script.
        :param dryRun: If true the change will not actually be applied. Dry run may be used to get result
         description without actually modifying the code.
        :return: The results of the command
        """
        msg = {"scriptId": scriptId, "scriptSource": scriptSource}
        if dryRun is not None:
            msg["dryRun"] = dryRun
        return self.client.send("Debugger.setScriptSource", msg)

    def setSkipAllPauses(self, skip: bool) -> Awaitable[Dict]:
        """
        Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setSkipAllPauses`

        :param skip: New value for skip pauses state.
        :return: The results of the command
        """
        return self.client.send("Debugger.setSkipAllPauses", {"skip": skip})

    def setVariableValue(
        self,
        scopeNumber: int,
        variableName: str,
        newValue: Dict[str, Any],
        callFrameId: str,
    ) -> Awaitable[Dict]:
        """
        Changes value of variable in a callframe. Object-based scopes are not supported and must be
        mutated manually.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-setVariableValue`

        :param scopeNumber: 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch'
         scope types are allowed. Other scopes could be manipulated manually.
        :param variableName: Variable name.
        :param newValue: New variable value.
        :param callFrameId: Id of callframe that holds variable.
        :return: The results of the command
        """
        return self.client.send(
            "Debugger.setVariableValue",
            {
                "scopeNumber": scopeNumber,
                "variableName": variableName,
                "newValue": newValue,
                "callFrameId": callFrameId,
            },
        )

    def stepInto(self, breakOnAsyncCall: Optional[bool] = None) -> Awaitable[Dict]:
        """
        Steps into the function call.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-stepInto`

        :param breakOnAsyncCall: Debugger will issue additional Debugger.paused notification if any async task is scheduled
         before next pause.
        :return: The results of the command
        """
        msg = {}
        if breakOnAsyncCall is not None:
            msg["breakOnAsyncCall"] = breakOnAsyncCall
        return self.client.send("Debugger.stepInto", msg)

    def stepOut(self) -> Awaitable[Dict]:
        """
        Steps out of the function call.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-stepOut`

        :return: The results of the command
        """
        return self.client.send("Debugger.stepOut", {})

    def stepOver(self) -> Awaitable[Dict]:
        """
        Steps over the statement.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#method-stepOver`

        :return: The results of the command
        """
        return self.client.send("Debugger.stepOver", {})

    def breakpointResolved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when breakpoint is resolved to an actual script and location.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#event-breakpointResolved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Debugger.breakpointResolved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def paused(self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None) -> Any:
        """
        Fired when the virtual machine stopped on breakpoint or exception or any other stop criteria.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#event-paused`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Debugger.paused"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def resumed(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        Fired when the virtual machine resumed execution.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#event-resumed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Debugger.resumed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def scriptFailedToParse(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when virtual machine fails to parse the script.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#event-scriptFailedToParse`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Debugger.scriptFailedToParse"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def scriptParsed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when virtual machine parses script. This event is also fired for all known and uncollected
        scripts upon enabling debugger.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Debugger#event-scriptParsed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Debugger.scriptParsed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
