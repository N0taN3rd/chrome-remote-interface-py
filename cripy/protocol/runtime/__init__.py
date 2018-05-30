from typing import Any, List, Optional, Union
from cripy.protocol.runtime import events as Events
from cripy.protocol.runtime import types as Types


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

    async def awaitPromise(self, promiseObjectId: str, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('Runtime.awaitPromise', msg_dict)
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def callFunctionOn(self, functionDeclaration: str, objectId: Optional[str] = None, arguments: Optional[List[dict]] = None, silent: Optional[bool] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, userGesture: Optional[bool] = None, awaitPromise: Optional[bool] = None, executionContextId: Optional[int] = None, objectGroup: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('Runtime.callFunctionOn', msg_dict)
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def compileScript(self, expression: str, sourceURL: str, persistScript: bool, executionContextId: Optional[int] = None) -> Optional[dict]:
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
        msg_dict = dict()
        if expression is not None:
            msg_dict['expression'] = expression
        if sourceURL is not None:
            msg_dict['sourceURL'] = sourceURL
        if persistScript is not None:
            msg_dict['persistScript'] = persistScript
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        res = await self.chrome.send('Runtime.compileScript', msg_dict)
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.disable')
        return res

    async def discardConsoleEntries(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.discardConsoleEntries')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.enable')
        return res

    async def evaluate(self, expression: str, objectGroup: Optional[str] = None, includeCommandLineAPI: Optional[bool] = None, silent: Optional[bool] = None, contextId: Optional[int] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, userGesture: Optional[bool] = None, awaitPromise: Optional[bool] = None, throwOnSideEffect: Optional[bool] = None, timeout: Optional[float] = None) -> Optional[dict]:
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
        res = await self.chrome.send('Runtime.evaluate', msg_dict)
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def getIsolateId(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.getIsolateId')
        return res

    async def getHeapUsage(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.getHeapUsage')
        return res

    async def getProperties(self, objectId: str, ownProperties: Optional[bool] = None, accessorPropertiesOnly: Optional[bool] = None, generatePreview: Optional[bool] = None) -> Optional[dict]:
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
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if ownProperties is not None:
            msg_dict['ownProperties'] = ownProperties
        if accessorPropertiesOnly is not None:
            msg_dict['accessorPropertiesOnly'] = accessorPropertiesOnly
        if generatePreview is not None:
            msg_dict['generatePreview'] = generatePreview
        res = await self.chrome.send('Runtime.getProperties', msg_dict)
        res['result'] = Types.PropertyDescriptor.safe_create_from_list(res['result'])
        res['internalProperties'] = Types.InternalPropertyDescriptor.safe_create_from_list(res['internalProperties'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def globalLexicalScopeNames(self, executionContextId: Optional[int] = None) -> Optional[dict]:
        """
        :param executionContextId: Specifies in which execution context to lookup global scope variables.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if executionContextId is not None:
            msg_dict['executionContextId'] = executionContextId
        res = await self.chrome.send('Runtime.globalLexicalScopeNames', msg_dict)
        return res

    async def queryObjects(self, prototypeObjectId: str, objectGroup: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('Runtime.queryObjects', msg_dict)
        res['objects'] = Types.RemoteObject.safe_create(res['objects'])
        return res

    async def releaseObject(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: Identifier of the object to release.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        res = await self.chrome.send('Runtime.releaseObject', msg_dict)
        return res

    async def releaseObjectGroup(self, objectGroup: str) -> Optional[dict]:
        """
        :param objectGroup: Symbolic object group name.
        :type objectGroup: str
        """
        msg_dict = dict()
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        res = await self.chrome.send('Runtime.releaseObjectGroup', msg_dict)
        return res

    async def runIfWaitingForDebugger(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.runIfWaitingForDebugger')
        return res

    async def runScript(self, scriptId: str, executionContextId: Optional[int] = None, objectGroup: Optional[str] = None, silent: Optional[bool] = None, includeCommandLineAPI: Optional[bool] = None, returnByValue: Optional[bool] = None, generatePreview: Optional[bool] = None, awaitPromise: Optional[bool] = None) -> Optional[dict]:
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
        res = await self.chrome.send('Runtime.runScript', msg_dict)
        res['result'] = Types.RemoteObject.safe_create(res['result'])
        res['exceptionDetails'] = Types.ExceptionDetails.safe_create(res['exceptionDetails'])
        return res

    async def setCustomObjectFormatterEnabled(self, enabled: bool) -> Optional[dict]:
        """
        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        res = await self.chrome.send('Runtime.setCustomObjectFormatterEnabled', msg_dict)
        return res

    async def terminateExecution(self) -> Optional[dict]:
        res = await self.chrome.send('Runtime.terminateExecution')
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

