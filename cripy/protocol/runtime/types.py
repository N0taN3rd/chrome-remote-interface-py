from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

UnserializableValue = TypeVar("UnserializableValue", str, str) # Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals.

UniqueDebuggerId = TypeVar("UniqueDebuggerId", str, str) # Unique identifier of current debugger.

Timestamp = TypeVar("Timestamp", float, float) # Number of milliseconds since epoch.

TimeDelta = TypeVar("TimeDelta", float, float) # Number of milliseconds.

ScriptId = TypeVar("ScriptId", str, str) # Unique script identifier.

RemoteObjectId = TypeVar("RemoteObjectId", str, str) # Unique object identifier.

ExecutionContextId = TypeVar("ExecutionContextId", int, int) # Id of an execution context.


class StackTraceId(ProtocolType):
    """
    If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.
    """

    def __init__(self, id: str, debuggerId: Optional[UniqueDebuggerId] = None) -> None:
        """
        :param id: The id
        :type id: str
        :param debuggerId: The debuggerId
        :type debuggerId: Optional[str]
        """
        super().__init__()
        self.id = id
        self.debuggerId = debuggerId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StackTraceId']:
        if init is not None:
            return StackTraceId(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StackTraceId']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StackTraceId(**it))
            return list_of_self
        else:
            return init


class StackTrace(ProtocolType):
    """
    Call frames for assertions or error messages.
    """

    def __init__(self, callFrames: List[Union['CallFrame', dict]], description: Optional[str] = None, parent: Optional[Union['StackTrace', dict]] = None, parentId: Optional[Union['StackTraceId', dict]] = None) -> None:
        """
        :param description: String label of this stack trace. For async traces this may be a name of the function that initiated the async call.
        :type description: Optional[str]
        :param callFrames: JavaScript function name.
        :type callFrames: List[dict]
        :param parent: Asynchronous JavaScript stack trace that preceded this stack, if available.
        :type parent: Optional[dict]
        :param parentId: Asynchronous JavaScript stack trace that preceded this stack, if available.
        :type parentId: Optional[dict]
        """
        super().__init__()
        self.description = description
        self.callFrames = CallFrame.safe_create_from_list(callFrames)
        self.parent = StackTrace.safe_create(parent)
        self.parentId = StackTraceId.safe_create(parentId)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StackTrace']:
        if init is not None:
            return StackTrace(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StackTrace']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StackTrace(**it))
            return list_of_self
        else:
            return init


class RemoteObject(ProtocolType):
    """
    Mirror object referencing original JavaScript object.
    """

    def __init__(self, type: str, subtype: Optional[str] = None, className: Optional[str] = None, value: Optional[Any] = None, unserializableValue: Optional[UnserializableValue] = None, description: Optional[str] = None, objectId: Optional[RemoteObjectId] = None, preview: Optional[Union['ObjectPreview', dict]] = None, customPreview: Optional[Union['CustomPreview', dict]] = None) -> None:
        """
        :param type: Object type.
        :type type: str
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: Optional[str]
        :param className: Object class (constructor) name. Specified for `object` type values only.
        :type className: Optional[str]
        :param value: Remote object value in case of primitive values or JSON values (if it was requested).
        :type value: Optional[Any]
        :param unserializableValue: Primitive value which can not be JSON-stringified does not have `value`, but gets this property.
        :type unserializableValue: Optional[str]
        :param description: String representation of the object.
        :type description: Optional[str]
        :param objectId: Unique object identifier (for non-primitive values).
        :type objectId: Optional[str]
        :param preview: Preview containing abbreviated property values. Specified for `object` type values only.
        :type preview: Optional[dict]
        :param customPreview: The customPreview
        :type customPreview: Optional[dict]
        """
        super().__init__()
        self.type = type
        self.subtype = subtype
        self.className = className
        self.value = value
        self.unserializableValue = unserializableValue
        self.description = description
        self.objectId = objectId
        self.preview = ObjectPreview.safe_create(preview)
        self.customPreview = CustomPreview.safe_create(customPreview)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RemoteObject']:
        if init is not None:
            return RemoteObject(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RemoteObject']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RemoteObject(**it))
            return list_of_self
        else:
            return init


class PropertyPreview(ProtocolType):
    def __init__(self, name: str, type: str, value: Optional[str] = None, valuePreview: Optional[Union['ObjectPreview', dict]] = None, subtype: Optional[str] = None) -> None:
        """
        :param name: Property name.
        :type name: str
        :param type: Object type. Accessor means that the property itself is an accessor property.
        :type type: str
        :param value: User-friendly property value string.
        :type value: Optional[str]
        :param valuePreview: Nested value preview.
        :type valuePreview: Optional[dict]
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: Optional[str]
        """
        super().__init__()
        self.name = name
        self.type = type
        self.value = value
        self.valuePreview = ObjectPreview.safe_create(valuePreview)
        self.subtype = subtype

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PropertyPreview']:
        if init is not None:
            return PropertyPreview(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PropertyPreview']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PropertyPreview(**it))
            return list_of_self
        else:
            return init


class PropertyDescriptor(ProtocolType):
    """
    Object property descriptor.
    """

    def __init__(self, name: str, configurable: bool, enumerable: bool, value: Optional[Union['RemoteObject', dict]] = None, writable: Optional[bool] = None, get: Optional[Union['RemoteObject', dict]] = None, set: Optional[Union['RemoteObject', dict]] = None, wasThrown: Optional[bool] = None, isOwn: Optional[bool] = None, symbol: Optional[Union['RemoteObject', dict]] = None) -> None:
        """
        :param name: Property name or symbol description.
        :type name: str
        :param value: The value associated with the property.
        :type value: Optional[dict]
        :param writable: True if the value associated with the property may be changed (data descriptors only).
        :type writable: Optional[bool]
        :param get: A function which serves as a getter for the property, or `undefined` if there is no getter (accessor descriptors only).
        :type get: Optional[dict]
        :param set: A function which serves as a setter for the property, or `undefined` if there is no setter (accessor descriptors only).
        :type set: Optional[dict]
        :param configurable: True if the type of this property descriptor may be changed and if the property may be deleted from the corresponding object.
        :type configurable: bool
        :param enumerable: True if this property shows up during enumeration of the properties on the corresponding object.
        :type enumerable: bool
        :param wasThrown: True if the result was thrown during the evaluation.
        :type wasThrown: Optional[bool]
        :param isOwn: True if the property is owned for the object.
        :type isOwn: Optional[bool]
        :param symbol: Property symbol object, if the property is of the `symbol` type.
        :type symbol: Optional[dict]
        """
        super().__init__()
        self.name = name
        self.value = RemoteObject.safe_create(value)
        self.writable = writable
        self.get = RemoteObject.safe_create(get)
        self.set = RemoteObject.safe_create(set)
        self.configurable = configurable
        self.enumerable = enumerable
        self.wasThrown = wasThrown
        self.isOwn = isOwn
        self.symbol = RemoteObject.safe_create(symbol)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PropertyDescriptor']:
        if init is not None:
            return PropertyDescriptor(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PropertyDescriptor']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PropertyDescriptor(**it))
            return list_of_self
        else:
            return init


class ObjectPreview(ProtocolType):
    """
    Object containing abbreviated remote object value.
    """

    def __init__(self, type: str, overflow: bool, properties: List[Union['PropertyPreview', dict]], subtype: Optional[str] = None, description: Optional[str] = None, entries: Optional[List[Union['EntryPreview', dict]]] = None) -> None:
        """
        :param type: Object type.
        :type type: str
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: Optional[str]
        :param description: String representation of the object.
        :type description: Optional[str]
        :param overflow: True iff some of the properties or entries of the original object did not fit.
        :type overflow: bool
        :param properties: List of the properties.
        :type properties: List[dict]
        :param entries: List of the entries. Specified for `map` and `set` subtype values only.
        :type entries: Optional[List[dict]]
        """
        super().__init__()
        self.type = type
        self.subtype = subtype
        self.description = description
        self.overflow = overflow
        self.properties = PropertyPreview.safe_create_from_list(properties)
        self.entries = EntryPreview.safe_create_from_list(entries)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ObjectPreview']:
        if init is not None:
            return ObjectPreview(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ObjectPreview']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectPreview(**it))
            return list_of_self
        else:
            return init


class InternalPropertyDescriptor(ProtocolType):
    """
    Object internal property descriptor. This property isn't normally visible in JavaScript code.
    """

    def __init__(self, name: str, value: Optional[Union['RemoteObject', dict]] = None) -> None:
        """
        :param name: Conventional property name.
        :type name: str
        :param value: The value associated with the property.
        :type value: Optional[dict]
        """
        super().__init__()
        self.name = name
        self.value = RemoteObject.safe_create(value)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InternalPropertyDescriptor']:
        if init is not None:
            return InternalPropertyDescriptor(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InternalPropertyDescriptor']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InternalPropertyDescriptor(**it))
            return list_of_self
        else:
            return init


class ExecutionContextDescription(ProtocolType):
    """
    Description of an isolated world.
    """

    def __init__(self, id: ExecutionContextId, origin: str, name: str, auxData: Optional[dict] = None) -> None:
        """
        :param id: Unique id of the execution context. It can be used to specify in which execution context script evaluation should be performed.
        :type id: int
        :param origin: Execution context origin.
        :type origin: str
        :param name: Human readable name describing given context.
        :type name: str
        :param auxData: Embedder-specific auxiliary data.
        :type auxData: Optional[dict]
        """
        super().__init__()
        self.id = id
        self.origin = origin
        self.name = name
        self.auxData = auxData

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExecutionContextDescription']:
        if init is not None:
            return ExecutionContextDescription(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExecutionContextDescription']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextDescription(**it))
            return list_of_self
        else:
            return init


class ExceptionDetails(ProtocolType):
    """
    Detailed information about exception (or error) that was thrown during script compilation or
execution.
    """

    def __init__(self, exceptionId: int, text: str, lineNumber: int, columnNumber: int, scriptId: Optional[ScriptId] = None, url: Optional[str] = None, stackTrace: Optional[Union['StackTrace', dict]] = None, exception: Optional[Union['RemoteObject', dict]] = None, executionContextId: Optional[ExecutionContextId] = None) -> None:
        """
        :param exceptionId: Exception id.
        :type exceptionId: int
        :param text: Exception text, which should be used together with exception object when available.
        :type text: str
        :param lineNumber: Line number of the exception location (0-based).
        :type lineNumber: int
        :param columnNumber: Column number of the exception location (0-based).
        :type columnNumber: int
        :param scriptId: Script ID of the exception location.
        :type scriptId: Optional[str]
        :param url: URL of the exception location, to be used when the script was not reported.
        :type url: Optional[str]
        :param stackTrace: JavaScript stack trace if available.
        :type stackTrace: Optional[dict]
        :param exception: Exception object if available.
        :type exception: Optional[dict]
        :param executionContextId: Identifier of the context where exception happened.
        :type executionContextId: Optional[int]
        """
        super().__init__()
        self.exceptionId = exceptionId
        self.text = text
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.scriptId = scriptId
        self.url = url
        self.stackTrace = StackTrace.safe_create(stackTrace)
        self.exception = RemoteObject.safe_create(exception)
        self.executionContextId = executionContextId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExceptionDetails']:
        if init is not None:
            return ExceptionDetails(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExceptionDetails']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionDetails(**it))
            return list_of_self
        else:
            return init


class EntryPreview(ProtocolType):
    def __init__(self, value: Union['ObjectPreview', dict], key: Optional[Union['ObjectPreview', dict]] = None) -> None:
        """
        :param key: Preview of the key. Specified for map-like collection entries.
        :type key: Optional[dict]
        :param value: Preview of the value.
        :type value: dict
        """
        super().__init__()
        self.key = ObjectPreview.safe_create(key)
        self.value = ObjectPreview.safe_create(value)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['EntryPreview']:
        if init is not None:
            return EntryPreview(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['EntryPreview']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryPreview(**it))
            return list_of_self
        else:
            return init


class CustomPreview(ProtocolType):
    def __init__(self, header: str, hasBody: bool, formatterObjectId: RemoteObjectId, bindRemoteObjectFunctionId: RemoteObjectId, configObjectId: Optional[RemoteObjectId] = None) -> None:
        """
        :param header: The header
        :type header: str
        :param hasBody: The hasBody
        :type hasBody: bool
        :param formatterObjectId: The formatterObjectId
        :type formatterObjectId: str
        :param bindRemoteObjectFunctionId: The bindRemoteObjectFunctionId
        :type bindRemoteObjectFunctionId: str
        :param configObjectId: The configObjectId
        :type configObjectId: Optional[str]
        """
        super().__init__()
        self.header = header
        self.hasBody = hasBody
        self.formatterObjectId = formatterObjectId
        self.bindRemoteObjectFunctionId = bindRemoteObjectFunctionId
        self.configObjectId = configObjectId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CustomPreview']:
        if init is not None:
            return CustomPreview(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CustomPreview']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CustomPreview(**it))
            return list_of_self
        else:
            return init


class CallFrame(ProtocolType):
    """
    Stack entry for runtime errors and assertions.
    """

    def __init__(self, functionName: str, scriptId: ScriptId, url: str, lineNumber: int, columnNumber: int) -> None:
        """
        :param functionName: JavaScript function name.
        :type functionName: str
        :param scriptId: JavaScript script id.
        :type scriptId: str
        :param url: JavaScript script name or url.
        :type url: str
        :param lineNumber: JavaScript script line number (0-based).
        :type lineNumber: int
        :param columnNumber: JavaScript script column number (0-based).
        :type columnNumber: int
        """
        super().__init__()
        self.functionName = functionName
        self.scriptId = scriptId
        self.url = url
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CallFrame']:
        if init is not None:
            return CallFrame(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CallFrame']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CallFrame(**it))
            return list_of_self
        else:
            return init


class CallArgument(ProtocolType):
    """
    Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified.
    """

    def __init__(self, value: Optional[Any] = None, unserializableValue: Optional[UnserializableValue] = None, objectId: Optional[RemoteObjectId] = None) -> None:
        """
        :param value: Primitive value or serializable javascript object.
        :type value: Optional[Any]
        :param unserializableValue: Primitive value which can not be JSON-stringified.
        :type unserializableValue: Optional[str]
        :param objectId: Remote object handle.
        :type objectId: Optional[str]
        """
        super().__init__()
        self.value = value
        self.unserializableValue = unserializableValue
        self.objectId = objectId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CallArgument']:
        if init is not None:
            return CallArgument(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CallArgument']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CallArgument(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "StackTraceId": StackTraceId,
    "StackTrace": StackTrace,
    "RemoteObject": RemoteObject,
    "PropertyPreview": PropertyPreview,
    "PropertyDescriptor": PropertyDescriptor,
    "ObjectPreview": ObjectPreview,
    "InternalPropertyDescriptor": InternalPropertyDescriptor,
    "ExecutionContextDescription": ExecutionContextDescription,
    "ExceptionDetails": ExceptionDetails,
    "EntryPreview": EntryPreview,
    "CustomPreview": CustomPreview,
    "CallFrame": CallFrame,
    "CallArgument": CallArgument,
}
