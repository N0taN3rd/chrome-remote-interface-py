from cripy.sync.protocol.runtime import events as Events
from cripy.sync.protocol.runtime import types as Types

__all__ = ["Runtime"] + Events.__all__ + Types.__all__ 


class Runtime(object):
    """
    Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def awaitPromise(self, promiseObjectId, returnByValue, generatePreview, cb=None):
        """
        :param promiseObjectId: Identifier of the promise.
        :type promiseObjectId: str
        :param returnByValue: Whether the result is expected to be a JSON object that should be sent by value.
        :type returnByValue: Optional[bool]
        :param generatePreview: Whether preview should be generated for the result.
        :type generatePreview: Optional[bool]
        """
        def cb_wrapper(res):
            res['result'] = Types.RemoteObject.safe_create(res['result'])
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
        msg_dict = dict()
        if promiseObjectId is not None:
            msg_dict['promiseObjectId'] = promiseObjectId
        if returnByValue is not None:
            msg_dict['returnByValue'] = returnByValue
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        self.chrome.send('Runtime.awaitPromise', params=msg_dict, cb=cb_wrapper)


    def callFunctionOn(self, functionDeclaration, objectId, arguments, silent, returnByValue, generatePreview, userGesture, awaitPromise, executionContextId, objectGroup, cb=None):
        """
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
        def cb_wrapper(res):
            res['result'] = Types.RemoteObject.safe_create(res['result'])
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
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
        self.chrome.send('Runtime.callFunctionOn', params=msg_dict, cb=cb_wrapper)


    def compileScript(self, expression, sourceURL, persistScript, executionContextId, cb=None):
        """
        :param expression: Expression to compile.
        :type expression: str
        :param sourceURL: Source url to be set for the script.
        :type sourceURL: str
        :param persistScript: Specifies whether the compiled script should be persisted.
        :type persistScript: bool
        :param executionContextId: Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
        :type executionContextId: Optional[int]
        """
        def cb_wrapper(res):
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
        msg_dict = dict()
        if expression is not None:
            msg_dict['expression'] = expression
        if sourceURL is not None:
            msg_dict['sourceURL'] = sourceURL
        if persistScript is not None:
            msg_dict['persistScript'] = persistScript
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        self.chrome.send('Runtime.compileScript', params=msg_dict, cb=cb_wrapper)


    def disable(self, cb=None):
        self.chrome.send('Runtime.disable')


    def discardConsoleEntries(self, cb=None):
        self.chrome.send('Runtime.discardConsoleEntries')


    def enable(self, cb=None):
        self.chrome.send('Runtime.enable')


    def evaluate(self, expression, objectGroup, includeCommandLineAPI, silent, contextId, returnByValue, generatePreview, userGesture, awaitPromise, throwOnSideEffect, timeout, cb=None):
        """
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
        def cb_wrapper(res):
            res['result'] = Types.RemoteObject.safe_create(res['result'])
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
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
        self.chrome.send('Runtime.evaluate', params=msg_dict, cb=cb_wrapper)


    def getIsolateId(self, cb=None):
        def cb_wrapper(res):
            cb(res)
        self.chrome.send('Runtime.getIsolateId', cb=cb_wrapper)


    def getHeapUsage(self, cb=None):
        def cb_wrapper(res):
            cb(res)
        self.chrome.send('Runtime.getHeapUsage', cb=cb_wrapper)


    def getProperties(self, objectId, ownProperties, accessorPropertiesOnly, generatePreview, cb=None):
        """
        :param objectId: Identifier of the object to return properties for.
        :type objectId: str
        :param ownProperties: If true, returns properties belonging only to the element itself, not to its prototype chain.
        :type ownProperties: Optional[bool]
        :param accessorPropertiesOnly: If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
        :type accessorPropertiesOnly: Optional[bool]
        :param generatePreview: Whether preview should be generated for the results.
        :type generatePreview: Optional[bool]
        """
        def cb_wrapper(res):
            res['result'] = Types.PropertyDescriptor.safe_create_from_list(res['result'])
            res['internalProperties'] = Types.InternalPropertyDescriptor.safe_create_from_list(res['internalProperties'])
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if ownProperties is not None:
            msg_dict['ownProperties'] = ownProperties
        if accessorPropertiesOnly is not None:
            msg_dict['accessorPropertiesOnly'] = accessorPropertiesOnly
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        self.chrome.send('Runtime.getProperties', params=msg_dict, cb=cb_wrapper)


    def globalLexicalScopeNames(self, executionContextId, cb=None):
        """
        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :type executionContextId: Optional[int]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        self.chrome.send('Runtime.globalLexicalScopeNames', params=msg_dict, cb=cb_wrapper)


    def queryObjects(self, prototypeObjectId, objectGroup, cb=None):
        """
        :param prototypeObjectId: Identifier of the prototype to return objects for.
        :type prototypeObjectId: str
        :param objectGroup: Symbolic group name that can be used to release the results.
        :type objectGroup: Optional[str]
        """
        def cb_wrapper(res):
            res['objects'] = Types.RemoteObject.safe_create(res['objects'])
            cb(res)
        msg_dict = dict()
        if prototypeObjectId is not None:
            msg_dict['prototypeObjectId'] = prototypeObjectId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        self.chrome.send('Runtime.queryObjects', params=msg_dict, cb=cb_wrapper)


    def releaseObject(self, objectId, cb=None):
        """
        :param objectId: Identifier of the object to release.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('Runtime.releaseObject', params=msg_dict)


    def releaseObjectGroup(self, objectGroup, cb=None):
        """
        :param objectGroup: Symbolic object group name.
        :type objectGroup: str
        """
        msg_dict = dict()
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        self.chrome.send('Runtime.releaseObjectGroup', params=msg_dict)


    def runIfWaitingForDebugger(self, cb=None):
        self.chrome.send('Runtime.runIfWaitingForDebugger')


    def runScript(self, scriptId, executionContextId, objectGroup, silent, includeCommandLineAPI, returnByValue, generatePreview, awaitPromise, cb=None):
        """
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
        def cb_wrapper(res):
            res['result'] = Types.RemoteObject.safe_create(res['result'])
            res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
            cb(res)
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
        self.chrome.send('Runtime.runScript', params=msg_dict, cb=cb_wrapper)


    def setAsyncCallStackDepth(self, maxDepth, cb=None):
        """
        :param maxDepth: Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default).
        :type maxDepth: int
        """
        msg_dict = dict()
        if maxDepth is not None:
            msg_dict['maxDepth'] = maxDepth
        self.chrome.send('Runtime.setAsyncCallStackDepth', params=msg_dict)


    def setCustomObjectFormatterEnabled(self, enabled, cb=None):
        """
        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        self.chrome.send('Runtime.setCustomObjectFormatterEnabled', params=msg_dict)


    def setMaxCallStackSizeToCapture(self, size, cb=None):
        """
        :param size: The size
        :type size: int
        """
        msg_dict = dict()
        if size is not None:
            msg_dict['size'] = size
        self.chrome.send('Runtime.setMaxCallStackSizeToCapture', params=msg_dict)


    def terminateExecution(self, cb=None):
        self.chrome.send('Runtime.terminateExecution')


    def addBinding(self, name, executionContextId, cb=None):
        """
        :param name: The name
        :type name: str
        :param executionContextId: The executionContextId
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        self.chrome.send('Runtime.addBinding', params=msg_dict)


    def removeBinding(self, name, cb=None):
        """
        :param name: The name
        :type name: str
        """
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('Runtime.removeBinding', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

