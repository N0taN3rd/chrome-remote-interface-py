# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Runtime"]


@attr.dataclass(slots=True)
class Runtime(object):
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def awaitPromise(
        self,
        promiseObjectId: str,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Add handler to promise with given promise object id.

        :param promiseObjectId: Identifier of the promise.
        :type promiseObjectId: str
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        """
        msg_dict = dict()
        if promiseObjectId is not None:
            msg_dict["promiseObjectId"] = promiseObjectId
        if returnByValue is not None:
            msg_dict["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        return self.client.send("Runtime.awaitPromise", msg_dict)

    def callFunctionOn(
        self,
        functionDeclaration: str,
        objectId: Optional[str] = None,
        arguments: Optional[List[dict]] = None,
        silent: Optional[bool] = None,
        returnByValue: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
        userGesture: Optional[bool] = None,
        awaitPromise: Optional[bool] = None,
        executionContextId: Optional[int] = None,
        objectGroup: Optional[str] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Calls function with given declaration on the given object. Object group of the result is
inherited from the target object.

        :param functionDeclaration: Declaration of the function to call.
        :type functionDeclaration: str
        :param objectId: Identifier of the object to call function on. Either objectId or executionContextId should be specified.
        :type objectId: Optional[str]
        :param arguments: Call arguments. All call arguments must belong to the same JavaScript world as the target object.
        :type arguments: Optional[List[dict]]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :type userGesture: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        :param executionContextId: Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified.
        :type executionContextId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if functionDeclaration is not None:
            msg_dict["functionDeclaration"] = functionDeclaration
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if arguments is not None:
            msg_dict["arguments"] = arguments
        if silent is not None:
            msg_dict["silent"] = silent
        if returnByValue is not None:
            msg_dict["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        if userGesture is not None:
            msg_dict["userGesture"] = userGesture
        if awaitPromise is not None:
            msg_dict["awaitPromise"] = awaitPromise
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        return self.client.send("Runtime.callFunctionOn", msg_dict)

    def compileScript(
        self,
        expression: str,
        sourceURL: str,
        persistScript: bool,
        executionContextId: Optional[int] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Compiles expression.

        :param expression: Expression to compile.
        :type expression: str
        :param sourceURL: Source url to be set for the script.
        :type sourceURL: str
        :param persistScript: Specifies whether the compiled script should be persisted.
        :type persistScript: bool
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if expression is not None:
            msg_dict["expression"] = expression
        if sourceURL is not None:
            msg_dict["sourceURL"] = sourceURL
        if persistScript is not None:
            msg_dict["persistScript"] = persistScript
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        return self.client.send("Runtime.compileScript", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables reporting of execution contexts creation.
        """
        return self.client.send("Runtime.disable")

    def discardConsoleEntries(self) -> Awaitable[Optional[dict]]:
        """
        Discards collected exceptions and console API calls.
        """
        return self.client.send("Runtime.discardConsoleEntries")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.
        """
        return self.client.send("Runtime.enable")

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
        timeout: Optional[float] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Evaluates expression on global object.

        :param expression: Expression to evaluate.
        :type expression: str
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :type includeCommandLineAPI: Optional[bool]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param contextId: Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type contextId: Optional[int]
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param userGesture: Whether execution should be treated as initiated by user in the UI.
        :type userGesture: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        :param throwOnSideEffect: Whether to throw an exception if side effect cannot be ruled out during evaluation.
        :type throwOnSideEffect: Optional[bool]
        :param timeout: Terminate execution after timing out (number of milliseconds).
        :type timeout: Optional[float]
        """
        msg_dict = dict()
        if expression is not None:
            msg_dict["expression"] = expression
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        if includeCommandLineAPI is not None:
            msg_dict["includeCommandLineAPI"] = includeCommandLineAPI
        if silent is not None:
            msg_dict["silent"] = silent
        if contextId is not None:
            msg_dict["contextId"] = contextId
        if returnByValue is not None:
            msg_dict["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        if userGesture is not None:
            msg_dict["userGesture"] = userGesture
        if awaitPromise is not None:
            msg_dict["awaitPromise"] = awaitPromise
        if throwOnSideEffect is not None:
            msg_dict["throwOnSideEffect"] = throwOnSideEffect
        if timeout is not None:
            msg_dict["timeout"] = timeout
        return self.client.send("Runtime.evaluate", msg_dict)

    def getIsolateId(self) -> Awaitable[Optional[dict]]:
        """
        Returns the isolate id.
        """
        return self.client.send("Runtime.getIsolateId")

    def getHeapUsage(self) -> Awaitable[Optional[dict]]:
        """
        Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.
        """
        return self.client.send("Runtime.getHeapUsage")

    def getProperties(
        self,
        objectId: str,
        ownProperties: Optional[bool] = None,
        accessorPropertiesOnly: Optional[bool] = None,
        generatePreview: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Returns properties of a given object. Object group of the result is inherited from the target
object.

        :param objectId: Identifier of the object to return properties for.
        :type objectId: str
        :param ownProperties: If true, returns properties belonging only to the element itself, not to its prototype chain.
        :type ownProperties: Optional[bool]
        :param accessorPropertiesOnly: If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
        :type accessorPropertiesOnly: Optional[bool]
        :param generatePreview: Whether preview should be generated for the results.
        :type generatePreview: Optional[bool]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if ownProperties is not None:
            msg_dict["ownProperties"] = ownProperties
        if accessorPropertiesOnly is not None:
            msg_dict["accessorPropertiesOnly"] = accessorPropertiesOnly
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        return self.client.send("Runtime.getProperties", msg_dict)

    def globalLexicalScopeNames(
        self, executionContextId: Optional[int] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Returns all let, const and class variables from global scope.

        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        return self.client.send("Runtime.globalLexicalScopeNames", msg_dict)

    def queryObjects(
        self, prototypeObjectId: str, objectGroup: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        :param prototypeObjectId: Identifier of the prototype to return objects for.
        :type prototypeObjectId: str
        :param objectGroup: Symbolic group name that can be used to release the results.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if prototypeObjectId is not None:
            msg_dict["prototypeObjectId"] = prototypeObjectId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        return self.client.send("Runtime.queryObjects", msg_dict)

    def releaseObject(self, objectId: str) -> Awaitable[Optional[dict]]:
        """
        Releases remote object with given id.

        :param objectId: Identifier of the object to release.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        return self.client.send("Runtime.releaseObject", msg_dict)

    def releaseObjectGroup(self, objectGroup: str) -> Awaitable[Optional[dict]]:
        """
        Releases all remote objects that belong to a given group.

        :param objectGroup: Symbolic object group name.
        :type objectGroup: str
        """
        msg_dict = dict()
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        return self.client.send("Runtime.releaseObjectGroup", msg_dict)

    def runIfWaitingForDebugger(self) -> Awaitable[Optional[dict]]:
        """
        Tells inspected instance to run if it was waiting for debugger to attach.
        """
        return self.client.send("Runtime.runIfWaitingForDebugger")

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
    ) -> Awaitable[Optional[dict]]:
        """
        Runs script with given id in a given context.

        :param scriptId: Id of the script to run.
        :type scriptId: str
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type executionContextId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        :param silent: In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state.
        :type silent: Optional[bool]
        :param includeCommandLineAPI: Determines whether Command Line API should be available during the evaluation.
        :type includeCommandLineAPI: Optional[bool]
        :param returnByValue: Whether the result is expected to be a JSON object which should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        :param awaitPromise: Whether execution should `await` for resulting value and return once awaited promise is resolved.
        :type awaitPromise: Optional[bool]
        """
        msg_dict = dict()
        if scriptId is not None:
            msg_dict["scriptId"] = scriptId
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        if silent is not None:
            msg_dict["silent"] = silent
        if includeCommandLineAPI is not None:
            msg_dict["includeCommandLineAPI"] = includeCommandLineAPI
        if returnByValue is not None:
            msg_dict["returnByValue"] = returnByValue
        if generatePreview is not None:
            msg_dict["generatePreview"] = generatePreview
        if awaitPromise is not None:
            msg_dict["awaitPromise"] = awaitPromise
        return self.client.send("Runtime.runScript", msg_dict)

    def setAsyncCallStackDepth(self, maxDepth: int) -> Awaitable[Optional[dict]]:
        """
        Enables or disables async call stacks tracking.

        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        msg_dict = dict()
        if maxDepth is not None:
            msg_dict["maxDepth"] = maxDepth
        return self.client.send("Runtime.setAsyncCallStackDepth", msg_dict)

    def setCustomObjectFormatterEnabled(
        self, enabled: bool
    ) -> Awaitable[Optional[dict]]:
        """
        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        return self.client.send("Runtime.setCustomObjectFormatterEnabled", msg_dict)

    def setMaxCallStackSizeToCapture(self, size: int) -> Awaitable[Optional[dict]]:
        """
        :param size: The size
        :type size: int
        """
        msg_dict = dict()
        if size is not None:
            msg_dict["size"] = size
        return self.client.send("Runtime.setMaxCallStackSizeToCapture", msg_dict)

    def terminateExecution(self) -> Awaitable[Optional[dict]]:
        """
        Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.
        """
        return self.client.send("Runtime.terminateExecution")

    def addBinding(
        self, name: str, executionContextId: Optional[int] = None
    ) -> Awaitable[Optional[dict]]:
        """
        If executionContextId is empty, adds binding with the given name on the
global objects of all inspected contexts, including those created later,
bindings survive reloads.
If executionContextId is specified, adds binding only on global object of
given execution context.
Binding function takes exactly one argument, this argument should be string,
in case of any other input, function throws an exception.
Each binding function call produces Runtime.bindingCalled notification.

        :param name: The name
        :type name: str
        :param executionContextId: The executionContextId
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        return self.client.send("Runtime.addBinding", msg_dict)

    def removeBinding(self, name: str) -> Awaitable[Optional[dict]]:
        """
        This method does not remove binding function from global object but
unsubscribes current runtime agent from Runtime.bindingCalled notifications.

        :param name: The name
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        return self.client.send("Runtime.removeBinding", msg_dict)

    def bindingCalled(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Notification is issued every time when binding is called.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.bindingCalled", _cb)

            return future

        self.client.on("Runtime.bindingCalled", cb)

    def consoleAPICalled(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when console API was called.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.consoleAPICalled", _cb)

            return future

        self.client.on("Runtime.consoleAPICalled", cb)

    def exceptionRevoked(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when unhandled exception was revoked.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.exceptionRevoked", _cb)

            return future

        self.client.on("Runtime.exceptionRevoked", cb)

    def exceptionThrown(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when exception was thrown and unhandled.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.exceptionThrown", _cb)

            return future

        self.client.on("Runtime.exceptionThrown", cb)

    def executionContextCreated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when new execution context is created.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.executionContextCreated", _cb)

            return future

        self.client.on("Runtime.executionContextCreated", cb)

    def executionContextDestroyed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when execution context is destroyed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.executionContextDestroyed", _cb)

            return future

        self.client.on("Runtime.executionContextDestroyed", cb)

    def executionContextsCleared(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when all executionContexts were cleared in browser
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.executionContextsCleared", _cb)

            return future

        self.client.on("Runtime.executionContextsCleared", cb)

    def inspectRequested(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when object should be inspected (for example, as a result of inspect() command line API
        call).
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Runtime.inspectRequested", _cb)

            return future

        self.client.on("Runtime.inspectRequested", cb)
