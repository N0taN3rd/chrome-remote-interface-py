"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Runtime"]


class Runtime:
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
    Evaluation results are returned as mirror object that expose object type, string representation
    and unique identifier that can be used for further object reference. Original objects are
    maintained in memory unless they are either explicitly released or are released along with the
    other objects in their object group.
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Runtime

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def awaitPromise(
        self,
        promiseObjectId: str,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Add handler to promise with given promise object id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-awaitPromise`

        :param promiseObjectId: Identifier of the promise.
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :param generatePreview: Whether preview should be generated for the result.
        :return: The results of the command
        """
        msg = {"promiseObjectId": promiseObjectId}
        if returnByValue is not None:
            msg["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        return self.client.send("Runtime.awaitPromise", msg)

    def callFunctionOn(
        self,
        functionDeclaration: str,
        objectId: Optional[str] = None,
        arguments: Optional[List[Dict[str, Any]]] = None,
        silent: Optional[bool] = None,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
        userGesture: Optional[bool] = None,
        awaitPromise: Optional[bool] = None,
        executionContextId: Optional[int] = None,
        objectGroup: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Calls function with given declaration on the given object. Object group of the result is
        inherited from the target object.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-callFunctionOn`

        :param functionDeclaration: Declaration of the function to call.
        :param objectId: Identifier of the object to call function on. Either objectId or executionContextId should
         be specified.
        :param arguments: Call arguments. All call arguments must belong to the same JavaScript world as the target
         object.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
         execution. Overrides `setPauseOnException` state.
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :param generatePreview: Whether preview should be generated for the result.
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is
         resolved.
        :param executionContextId: Specifies execution context which global object will be used to call function on. Either
         executionContextId or objectId should be specified.
        :param objectGroup: Symbolic group name that can be used to release multiple objects. If objectGroup is not
         specified and objectId is, objectGroup will be inherited from object.
        :return: The results of the command
        """
        msg = {"functionDeclaration": functionDeclaration}
        if objectId is not None:
            msg["objectId"] = objectId
        if arguments is not None:
            msg["arguments"] = arguments
        if silent is not None:
            msg["silent"] = silent
        if returnByValue is not None:
            msg["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        if userGesture is not None:
            msg["userGesture"] = userGesture
        if awaitPromise is not None:
            msg["awaitPromise"] = awaitPromise
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        return self.client.send("Runtime.callFunctionOn", msg)

    def compileScript(
        self,
        expression: str,
        sourceURL: str,
        persistScript: bool,
        executionContextId: Optional[int] = None,
    ) -> Awaitable[Dict]:
        """
        Compiles expression.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-compileScript`

        :param expression: Expression to compile.
        :param sourceURL: Source url to be set for the script.
        :param persistScript: Specifies whether the compiled script should be persisted.
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the
         evaluation will be performed in the context of the inspected page.
        :return: The results of the command
        """
        msg = {
            "expression": expression,
            "sourceURL": sourceURL,
            "persistScript": persistScript,
        }
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        return self.client.send("Runtime.compileScript", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables reporting of execution contexts creation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-disable`

        :return: The results of the command
        """
        return self.client.send("Runtime.disable", {})

    def discardConsoleEntries(self) -> Awaitable[Dict]:
        """
        Discards collected exceptions and console API calls.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-discardConsoleEntries`

        :return: The results of the command
        """
        return self.client.send("Runtime.discardConsoleEntries", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables reporting of execution contexts creation by means of `executionContextCreated` event.
        When the reporting gets enabled the event will be sent immediately for each existing execution
        context.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-enable`

        :return: The results of the command
        """
        return self.client.send("Runtime.enable", {})

    def evaluate(
        self,
        expression: str,
        objectGroup: Optional[str] = None,
        includeCommandLineAPI: Optional[bool] = None,
        silent: Optional[bool] = None,
        contextId: Optional[int] = None,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
        userGesture: Optional[bool] = None,
        awaitPromise: Optional[bool] = None,
        throwOnSideEffect: Optional[bool] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Evaluates expression on global object.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-evaluate`

        :param expression: Expression to evaluate.
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
         execution. Overrides `setPauseOnException` state.
        :param contextId: Specifies in which execution context to perform evaluation. If the parameter is omitted the
         evaluation will be performed in the context of the inspected page.
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :param generatePreview: Whether preview should be generated for the result.
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is
         resolved.
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :return: The results of the command
        """
        msg = {"expression": expression}
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        if includeCommandLineAPI is not None:
            msg["includeCommandLineAPI"] = includeCommandLineAPI
        if silent is not None:
            msg["silent"] = silent
        if contextId is not None:
            msg["contextId"] = contextId
        if returnByValue is not None:
            msg["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        if userGesture is not None:
            msg["userGesture"] = userGesture
        if awaitPromise is not None:
            msg["awaitPromise"] = awaitPromise
        if throwOnSideEffect is not None:
            msg["throwOnSideEffect"] = throwOnSideEffect
        if timeout is not None:
            msg["timeout"] = timeout
        return self.client.send("Runtime.evaluate", msg)

    def getIsolateId(self) -> Awaitable[Dict]:
        """
        Returns the isolate id.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-getIsolateId`

        :return: The results of the command
        """
        return self.client.send("Runtime.getIsolateId", {})

    def getHeapUsage(self) -> Awaitable[Dict]:
        """
        Returns the JavaScript heap usage.
        It is the total usage of the corresponding isolate not scoped to a particular Runtime.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-getHeapUsage`

        :return: The results of the command
        """
        return self.client.send("Runtime.getHeapUsage", {})

    def getProperties(
        self,
        objectId: str,
        ownProperties: Optional[bool] = None,
        accessorPropertiesOnly: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Returns properties of a given object. Object group of the result is inherited from the target
        object.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-getProperties`

        :param objectId: Identifier of the object to return properties for.
        :param ownProperties: If true, returns properties belonging only to the element itself, not to its prototype
         chain.
        :param accessorPropertiesOnly: If true, returns accessor properties (with getter/setter) only; internal properties are not
         returned either.
        :param generatePreview: Whether preview should be generated for the results.
        :return: The results of the command
        """
        msg = {"objectId": objectId}
        if ownProperties is not None:
            msg["ownProperties"] = ownProperties
        if accessorPropertiesOnly is not None:
            msg["accessorPropertiesOnly"] = accessorPropertiesOnly
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        return self.client.send("Runtime.getProperties", msg)

    def globalLexicalScopeNames(
        self, executionContextId: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        Returns all let, const and class variables from global scope.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-globalLexicalScopeNames`

        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :return: The results of the command
        """
        msg = {}
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        return self.client.send("Runtime.globalLexicalScopeNames", msg)

    def queryObjects(
        self, prototypeObjectId: str, objectGroup: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-queryObjects`

        :param prototypeObjectId: Identifier of the prototype to return objects for.
        :param objectGroup: Symbolic group name that can be used to release the results.
        :return: The results of the command
        """
        msg = {"prototypeObjectId": prototypeObjectId}
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        return self.client.send("Runtime.queryObjects", msg)

    def releaseObject(self, objectId: str) -> Awaitable[Dict]:
        """
        Releases remote object with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-releaseObject`

        :param objectId: Identifier of the object to release.
        :return: The results of the command
        """
        return self.client.send("Runtime.releaseObject", {"objectId": objectId})

    def releaseObjectGroup(self, objectGroup: str) -> Awaitable[Dict]:
        """
        Releases all remote objects that belong to a given group.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-releaseObjectGroup`

        :param objectGroup: Symbolic object group name.
        :return: The results of the command
        """
        return self.client.send(
            "Runtime.releaseObjectGroup", {"objectGroup": objectGroup}
        )

    def runIfWaitingForDebugger(self) -> Awaitable[Dict]:
        """
        Tells inspected instance to run if it was waiting for debugger to attach.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-runIfWaitingForDebugger`

        :return: The results of the command
        """
        return self.client.send("Runtime.runIfWaitingForDebugger", {})

    def runScript(
        self,
        scriptId: str,
        executionContextId: Optional[int] = None,
        objectGroup: Optional[str] = None,
        silent: Optional[bool] = None,
        includeCommandLineAPI: Optional[bool] = None,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
        awaitPromise: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Runs script with given id in a given context.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-runScript`

        :param scriptId: Id of the script to run.
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the
         evaluation will be performed in the context of the inspected page.
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause
         execution. Overrides `setPauseOnException` state.
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :param generatePreview: Whether preview should be generated for the result.
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is
         resolved.
        :return: The results of the command
        """
        msg = {"scriptId": scriptId}
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        if silent is not None:
            msg["silent"] = silent
        if includeCommandLineAPI is not None:
            msg["includeCommandLineAPI"] = includeCommandLineAPI
        if returnByValue is not None:
            msg["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg["generatePreview"] = generatePreview
        if awaitPromise is not None:
            msg["awaitPromise"] = awaitPromise
        return self.client.send("Runtime.runScript", msg)

    def setAsyncCallStackDepth(self, maxDepth: int) -> Awaitable[Dict]:
        """
        Enables or disables async call stacks tracking.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-setAsyncCallStackDepth`

        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
         call stacks (default).
        :return: The results of the command
        """
        return self.client.send(
            "Runtime.setAsyncCallStackDepth", {"maxDepth": maxDepth}
        )

    def setCustomObjectFormatterEnabled(self, enabled: bool) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-setCustomObjectFormatterEnabled`

        :param enabled: The enabled
        :return: The results of the command
        """
        return self.client.send(
            "Runtime.setCustomObjectFormatterEnabled", {"enabled": enabled}
        )

    def setMaxCallStackSizeToCapture(self, size: int) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-setMaxCallStackSizeToCapture`

        :param size: The size
        :return: The results of the command
        """
        return self.client.send("Runtime.setMaxCallStackSizeToCapture", {"size": size})

    def terminateExecution(self) -> Awaitable[Dict]:
        """
        Terminate current or next JavaScript execution.
        Will cancel the termination when the outer-most script execution ends.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-terminateExecution`

        :return: The results of the command
        """
        return self.client.send("Runtime.terminateExecution", {})

    def addBinding(
        self, name: str, executionContextId: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        If executionContextId is empty, adds binding with the given name on the
        global objects of all inspected contexts, including those created later,
        bindings survive reloads.
        If executionContextId is specified, adds binding only on global object of
        given execution context.
        Binding function takes exactly one argument, this argument should be string,
        in case of any other input, function throws an exception.
        Each binding function call produces Runtime.bindingCalled notification.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-addBinding`

        :param name: The name
        :param executionContextId: The executionContextId
        :return: The results of the command
        """
        msg = {"name": name}
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        return self.client.send("Runtime.addBinding", msg)

    def removeBinding(self, name: str) -> Awaitable[Dict]:
        """
        This method does not remove binding function from global object but
        unsubscribes current runtime agent from Runtime.bindingCalled notifications.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#method-removeBinding`

        :param name: The name
        :return: The results of the command
        """
        return self.client.send("Runtime.removeBinding", {"name": name})

    def bindingCalled(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Notification is issued every time when binding is called.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-bindingCalled`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.bindingCalled"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def consoleAPICalled(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when console API was called.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-consoleAPICalled`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.consoleAPICalled"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def exceptionRevoked(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when unhandled exception was revoked.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-exceptionRevoked`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.exceptionRevoked"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def exceptionThrown(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when exception was thrown and unhandled.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-exceptionThrown`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.exceptionThrown"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def executionContextCreated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when new execution context is created.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-executionContextCreated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.executionContextCreated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def executionContextDestroyed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when execution context is destroyed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-executionContextDestroyed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.executionContextDestroyed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def executionContextsCleared(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Issued when all executionContexts were cleared in browser

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-executionContextsCleared`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.executionContextsCleared"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def inspectRequested(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when object should be inspected (for example, as a result of inspect() command line API
        call).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Runtime#event-inspectRequested`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Runtime.inspectRequested"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
