from cripy.gevent.protocol.runtime import events as Events
from cripy.gevent.protocol.runtime import types as Types

__all__ = ["Runtime"]


class Runtime(object):
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.
    """

    events = Events.RUNTIME_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Runtime object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def awaitPromise(self, promiseObjectId, returnByValue=None, generatePreview=None):
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
            msg_dict['promiseObjectId'] = promiseObjectId
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        wres = self.chrome.send('Runtime.awaitPromise', msg_dict)
        res = wres.get()
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def callFunctionOn(self, functionDeclaration, objectId=None, arguments=None, silent=None, returnByValue=None, generatePreview=None, userGesture=None, awaitPromise=None, executionContextId=None, objectGroup=None):
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
            msg_dict['functionDeclaration'] = functionDeclaration
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if arguments is not None:
            msg_dict['arguments'] = arguments
        if silent is not None:
            msg_dict['silent'] = silent
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if userGesture is not None:
            msg_dict['userGesture'] = userGesture
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        wres = self.chrome.send('Runtime.callFunctionOn', msg_dict)
        res = wres.get()
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def compileScript(self, expression, sourceURL, persistScript, executionContextId=None):
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
            msg_dict['expression'] = expression
        if sourceURL is not None:
            msg_dict['sourceURL'] = sourceURL
        if persistScript is not None:
            msg_dict['persistScript'] = persistScript
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        wres = self.chrome.send('Runtime.compileScript', msg_dict)
        res = wres.get()
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def disable(self):
        """
        Disables reporting of execution contexts creation.
        """
        wres = self.chrome.send('Runtime.disable')
        return wres.get()

    def discardConsoleEntries(self):
        """
        Discards collected exceptions and console API calls.
        """
        wres = self.chrome.send('Runtime.discardConsoleEntries')
        return wres.get()

    def enable(self):
        """
        Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.
        """
        wres = self.chrome.send('Runtime.enable')
        return wres.get()

    def evaluate(self, expression, objectGroup=None, includeCommandLineAPI=None, silent=None, contextId=None, returnByValue=None, generatePreview=None, userGesture=None, awaitPromise=None, throwOnSideEffect=None, timeout=None):
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
            msg_dict['expression'] = expression
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        if includeCommandLineAPI is not None:
            msg_dict['includeCommandLineAPI'] = includeCommandLineAPI
        if silent is not None:
            msg_dict['silent'] = silent
        if contextId is not None:
            msg_dict['contextId'] = contextId
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if userGesture is not None:
            msg_dict['userGesture'] = userGesture
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        if throwOnSideEffect is not None:
            msg_dict['throwOnSideEffect'] = throwOnSideEffect
        if timeout is not None:
            msg_dict['timeout'] = timeout
        wres = self.chrome.send('Runtime.evaluate', msg_dict)
        res = wres.get()
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def getIsolateId(self):
        """
        Returns the isolate id.
        """
        wres = self.chrome.send('Runtime.getIsolateId')
        res = wres.get()
        return res

    def getHeapUsage(self):
        """
        Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.
        """
        wres = self.chrome.send('Runtime.getHeapUsage')
        res = wres.get()
        return res

    def getProperties(self, objectId, ownProperties=None, accessorPropertiesOnly=None, generatePreview=None):
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
            msg_dict['objectId'] = objectId
        if ownProperties is not None:
            msg_dict['ownProperties'] = ownProperties
        if accessorPropertiesOnly is not None:
            msg_dict['accessorPropertiesOnly'] = accessorPropertiesOnly
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        wres = self.chrome.send('Runtime.getProperties', msg_dict)
        res = wres.get()
        res['result'] = Types.PropertyDescriptor.safe_create_from_list(res['result'])
        res['internalProperties'] = Types.InternalPropertyDescriptor.safe_create_from_list(res['internalProperties'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def globalLexicalScopeNames(self, executionContextId=None):
        """
        Returns all let, const and class variables from global scope.

        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        wres = self.chrome.send('Runtime.globalLexicalScopeNames', msg_dict)
        res = wres.get()
        return res

    def queryObjects(self, prototypeObjectId, objectGroup=None):
        """
        :param prototypeObjectId: Identifier of the prototype to return objects for.
        :type prototypeObjectId: str
        :param objectGroup: Symbolic group name that can be used to release the results.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if prototypeObjectId is not None:
            msg_dict['prototypeObjectId'] = prototypeObjectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        wres = self.chrome.send('Runtime.queryObjects', msg_dict)
        res = wres.get()
        res['objects'] = Types.RemoteObject.safe_create(res['objects'])
        return res

    def releaseObject(self, objectId):
        """
        Releases remote object with given id.

        :param objectId: Identifier of the object to release.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        wres = self.chrome.send('Runtime.releaseObject', msg_dict)
        return wres.get()

    def releaseObjectGroup(self, objectGroup):
        """
        Releases all remote objects that belong to a given group.

        :param objectGroup: Symbolic object group name.
        :type objectGroup: str
        """
        msg_dict = dict()
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        wres = self.chrome.send('Runtime.releaseObjectGroup', msg_dict)
        return wres.get()

    def runIfWaitingForDebugger(self):
        """
        Tells inspected instance to run if it was waiting for debugger to attach.
        """
        wres = self.chrome.send('Runtime.runIfWaitingForDebugger')
        return wres.get()

    def runScript(self, scriptId, executionContextId=None, objectGroup=None, silent=None, includeCommandLineAPI=None, returnByValue=None, generatePreview=None, awaitPromise=None):
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
            msg_dict['scriptId'] = scriptId
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        if silent is not None:
            msg_dict['silent'] = silent
        if includeCommandLineAPI is not None:
            msg_dict['includeCommandLineAPI'] = includeCommandLineAPI
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        if awaitPromise is not None:
            msg_dict['awaitPromise'] = awaitPromise
        wres = self.chrome.send('Runtime.runScript', msg_dict)
        res = wres.get()
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    def setCustomObjectFormatterEnabled(self, enabled):
        """
        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        wres = self.chrome.send('Runtime.setCustomObjectFormatterEnabled', msg_dict)
        return wres.get()

    def terminateExecution(self):
        """
        Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.
        """
        wres = self.chrome.send('Runtime.terminateExecution')
        return wres.get()

    def consoleAPICalled(self, fn, once=False):
        self.chrome.on("Runtime.consoleAPICalled", fn, once=once)

    def exceptionRevoked(self, fn, once=False):
        self.chrome.on("Runtime.exceptionRevoked", fn, once=once)

    def exceptionThrown(self, fn, once=False):
        self.chrome.on("Runtime.exceptionThrown", fn, once=once)

    def executionContextCreated(self, fn, once=False):
        self.chrome.on("Runtime.executionContextCreated", fn, once=once)

    def executionContextDestroyed(self, fn, once=False):
        self.chrome.on("Runtime.executionContextDestroyed", fn, once=once)

    def executionContextsCleared(self, fn, once=False):
        self.chrome.on("Runtime.executionContextsCleared", fn, once=once)

    def inspectRequested(self, fn, once=False):
        self.chrome.on("Runtime.inspectRequested", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.RUNTIME_EVENTS_TO_CLASS

