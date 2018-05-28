from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase

UnserializableValue = TypeVar("UnserializableValue", str, str)
"""Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`, `-Infinity`, and bigint literals."""

UniqueDebuggerId = TypeVar("UniqueDebuggerId", str, str)
"""Unique identifier of current debugger."""

Timestamp = TypeVar("Timestamp", float, float)
"""Number of milliseconds since epoch."""

TimeDelta = TypeVar("TimeDelta", float, float)
"""Number of milliseconds."""

ScriptId = TypeVar("ScriptId", str, str)
"""Unique script identifier."""

RemoteObjectId = TypeVar("RemoteObjectId", str, str)
"""Unique object identifier."""

ExecutionContextId = TypeVar("ExecutionContextId", int, int)
"""Id of an execution context."""


class StackTraceId(ChromeTypeBase):
    """If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages."""
    def __init__(self, id: str, debuggerId: Optional['UniqueDebuggerId'] = None) -> None:
        """
        :param id: The id
        :type id: str
        :param debuggerId: The debuggerId
        :type debuggerId: UniqueDebuggerId
        """
        super().__init__()
        self.id: str = id
        self.debuggerId: Optional[UniqueDebuggerId] = debuggerId


class StackTrace(ChromeTypeBase):
    """Call frames for assertions or error messages."""
    def __init__(self, callFrames: List['CallFrame'], description: Optional[str] = None, parent: Optional['StackTrace'] = None, parentId: Optional['StackTraceId'] = None) -> None:
        """
        :param description: String label of this stack trace. For async traces this may be a name of the function that initiated the async call.
        :type description: str
        :param callFrames: JavaScript function name.
        :type callFrames: array
        :param parent: Asynchronous JavaScript stack trace that preceded this stack, if available.
        :type parent: StackTrace
        :param parentId: Asynchronous JavaScript stack trace that preceded this stack, if available.
        :type parentId: StackTraceId
        """
        super().__init__()
        self.description: Optional[str] = description
        self.callFrames: List[CallFrame] = callFrames
        self.parent: Optional[StackTrace] = parent
        self.parentId: Optional[StackTraceId] = parentId


class RemoteObject(ChromeTypeBase):
    """Mirror object referencing original JavaScript object."""
    def __init__(self, type: str, subtype: Optional[str] = None, className: Optional[str] = None, value: Optional[Any] = None, unserializableValue: Optional['UnserializableValue'] = None, description: Optional[str] = None, objectId: Optional['RemoteObjectId'] = None, preview: Optional['ObjectPreview'] = None, customPreview: Optional['CustomPreview'] = None) -> None:
        """
        :param type: Object type.
        :type type: str
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: str
        :param className: Object class (constructor) name. Specified for `object` type values only.
        :type className: str
        :param value: Remote object value in case of primitive values or JSON values (if it was requested).
        :type value: Any
        :param unserializableValue: Primitive value which can not be JSON-stringified does not have `value`, but gets this property.
        :type unserializableValue: UnserializableValue
        :param description: String representation of the object.
        :type description: str
        :param objectId: Unique object identifier (for non-primitive values).
        :type objectId: RemoteObjectId
        :param preview: Preview containing abbreviated property values. Specified for `object` type values only.
        :type preview: ObjectPreview
        :param customPreview: The customPreview
        :type customPreview: CustomPreview
        """
        super().__init__()
        self.type: str = type
        self.subtype: Optional[str] = subtype
        self.className: Optional[str] = className
        self.value: Optional[Any] = value
        self.unserializableValue: Optional[UnserializableValue] = unserializableValue
        self.description: Optional[str] = description
        self.objectId: Optional[RemoteObjectId] = objectId
        self.preview: Optional[ObjectPreview] = preview
        self.customPreview: Optional[CustomPreview] = customPreview


class PropertyPreview(ChromeTypeBase):
    def __init__(self, name: str, type: str, value: Optional[str] = None, valuePreview: Optional['ObjectPreview'] = None, subtype: Optional[str] = None) -> None:
        """
        :param name: Property name.
        :type name: str
        :param type: Object type. Accessor means that the property itself is an accessor property.
        :type type: str
        :param value: User-friendly property value string.
        :type value: str
        :param valuePreview: Nested value preview.
        :type valuePreview: ObjectPreview
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: str
        """
        super().__init__()
        self.name: str = name
        self.type: str = type
        self.value: Optional[str] = value
        self.valuePreview: Optional[ObjectPreview] = valuePreview
        self.subtype: Optional[str] = subtype


class PropertyDescriptor(ChromeTypeBase):
    """Object property descriptor."""
    def __init__(self, name: str, configurable: bool, enumerable: bool, value: Optional['RemoteObject'] = None, writable: Optional[bool] = None, get: Optional['RemoteObject'] = None, set: Optional['RemoteObject'] = None, wasThrown: Optional[bool] = None, isOwn: Optional[bool] = None, symbol: Optional['RemoteObject'] = None) -> None:
        """
        :param name: Property name or symbol description.
        :type name: str
        :param value: The value associated with the property.
        :type value: RemoteObject
        :param writable: True if the value associated with the property may be changed (data descriptors only).
        :type writable: bool
        :param get: A function which serves as a getter for the property, or `undefined` if there is no getter (accessor descriptors only).
        :type get: RemoteObject
        :param set: A function which serves as a setter for the property, or `undefined` if there is no setter (accessor descriptors only).
        :type set: RemoteObject
        :param configurable: True if the type of this property descriptor may be changed and if the property may be deleted from the corresponding object.
        :type configurable: bool
        :param enumerable: True if this property shows up during enumeration of the properties on the corresponding object.
        :type enumerable: bool
        :param wasThrown: True if the result was thrown during the evaluation.
        :type wasThrown: bool
        :param isOwn: True if the property is owned for the object.
        :type isOwn: bool
        :param symbol: Property symbol object, if the property is of the `symbol` type.
        :type symbol: RemoteObject
        """
        super().__init__()
        self.name: str = name
        self.value: Optional[RemoteObject] = value
        self.writable: Optional[bool] = writable
        self.get: Optional[RemoteObject] = get
        self.set: Optional[RemoteObject] = set
        self.configurable: bool = configurable
        self.enumerable: bool = enumerable
        self.wasThrown: Optional[bool] = wasThrown
        self.isOwn: Optional[bool] = isOwn
        self.symbol: Optional[RemoteObject] = symbol


class ObjectPreview(ChromeTypeBase):
    """Object containing abbreviated remote object value."""
    def __init__(self, type: str, overflow: bool, properties: List['PropertyPreview'], subtype: Optional[str] = None, description: Optional[str] = None, entries: Optional[List['EntryPreview']] = None) -> None:
        """
        :param type: Object type.
        :type type: str
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :type subtype: str
        :param description: String representation of the object.
        :type description: str
        :param overflow: True iff some of the properties or entries of the original object did not fit.
        :type overflow: bool
        :param properties: List of the properties.
        :type properties: array
        :param entries: List of the entries. Specified for `map` and `set` subtype values only.
        :type entries: array
        """
        super().__init__()
        self.type: str = type
        self.subtype: Optional[str] = subtype
        self.description: Optional[str] = description
        self.overflow: bool = overflow
        self.properties: List[PropertyPreview] = properties
        self.entries: Optional[List[EntryPreview]] = entries


class InternalPropertyDescriptor(ChromeTypeBase):
    """Object internal property descriptor. This property isn't normally visible in JavaScript code."""
    def __init__(self, name: str, value: Optional['RemoteObject'] = None) -> None:
        """
        :param name: Conventional property name.
        :type name: str
        :param value: The value associated with the property.
        :type value: RemoteObject
        """
        super().__init__()
        self.name: str = name
        self.value: Optional[RemoteObject] = value


class ExecutionContextDescription(ChromeTypeBase):
    """Description of an isolated world."""
    def __init__(self, id: 'ExecutionContextId', origin: str, name: str, auxData: Optional[dict] = None) -> None:
        """
        :param id: Unique id of the execution context. It can be used to specify in which execution context script evaluation should be performed.
        :type id: ExecutionContextId
        :param origin: Execution context origin.
        :type origin: str
        :param name: Human readable name describing given context.
        :type name: str
        :param auxData: Embedder-specific auxiliary data.
        :type auxData: dict
        """
        super().__init__()
        self.id: ExecutionContextId = id
        self.origin: str = origin
        self.name: str = name
        self.auxData: Optional[dict] = auxData


class ExceptionDetails(ChromeTypeBase):
    """Detailed information about exception (or error) that was thrown during script compilation or
execution."""
    def __init__(self, exceptionId: int, text: str, lineNumber: int, columnNumber: int, scriptId: Optional['ScriptId'] = None, url: Optional[str] = None, stackTrace: Optional['StackTrace'] = None, exception: Optional['RemoteObject'] = None, executionContextId: Optional['ExecutionContextId'] = None) -> None:
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
        :type scriptId: ScriptId
        :param url: URL of the exception location, to be used when the script was not reported.
        :type url: str
        :param stackTrace: JavaScript stack trace if available.
        :type stackTrace: StackTrace
        :param exception: Exception object if available.
        :type exception: RemoteObject
        :param executionContextId: Identifier of the context where exception happened.
        :type executionContextId: ExecutionContextId
        """
        super().__init__()
        self.exceptionId: int = exceptionId
        self.text: str = text
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber
        self.scriptId: Optional[ScriptId] = scriptId
        self.url: Optional[str] = url
        self.stackTrace: Optional[StackTrace] = stackTrace
        self.exception: Optional[RemoteObject] = exception
        self.executionContextId: Optional[ExecutionContextId] = executionContextId


class EntryPreview(ChromeTypeBase):
    def __init__(self, value: 'ObjectPreview', key: Optional['ObjectPreview'] = None) -> None:
        """
        :param key: Preview of the key. Specified for map-like collection entries.
        :type key: ObjectPreview
        :param value: Preview of the value.
        :type value: ObjectPreview
        """
        super().__init__()
        self.key: Optional[ObjectPreview] = key
        self.value: ObjectPreview = value


class CustomPreview(ChromeTypeBase):
    def __init__(self, header: str, hasBody: bool, formatterObjectId: 'RemoteObjectId', bindRemoteObjectFunctionId: 'RemoteObjectId', configObjectId: Optional['RemoteObjectId'] = None) -> None:
        """
        :param header: The header
        :type header: str
        :param hasBody: The hasBody
        :type hasBody: bool
        :param formatterObjectId: The formatterObjectId
        :type formatterObjectId: RemoteObjectId
        :param bindRemoteObjectFunctionId: The bindRemoteObjectFunctionId
        :type bindRemoteObjectFunctionId: RemoteObjectId
        :param configObjectId: The configObjectId
        :type configObjectId: RemoteObjectId
        """
        super().__init__()
        self.header: str = header
        self.hasBody: bool = hasBody
        self.formatterObjectId: RemoteObjectId = formatterObjectId
        self.bindRemoteObjectFunctionId: RemoteObjectId = bindRemoteObjectFunctionId
        self.configObjectId: Optional[RemoteObjectId] = configObjectId


class CallFrame(ChromeTypeBase):
    """Stack entry for runtime errors and assertions."""
    def __init__(self, functionName: str, scriptId: 'ScriptId', url: str, lineNumber: int, columnNumber: int) -> None:
        """
        :param functionName: JavaScript function name.
        :type functionName: str
        :param scriptId: JavaScript script id.
        :type scriptId: ScriptId
        :param url: JavaScript script name or url.
        :type url: str
        :param lineNumber: JavaScript script line number (0-based).
        :type lineNumber: int
        :param columnNumber: JavaScript script column number (0-based).
        :type columnNumber: int
        """
        super().__init__()
        self.functionName: str = functionName
        self.scriptId: ScriptId = scriptId
        self.url: str = url
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class CallArgument(ChromeTypeBase):
    """Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified."""
    def __init__(self, value: Optional[Any] = None, unserializableValue: Optional['UnserializableValue'] = None, objectId: Optional['RemoteObjectId'] = None) -> None:
        """
        :param value: Primitive value or serializable javascript object.
        :type value: Any
        :param unserializableValue: Primitive value which can not be JSON-stringified.
        :type unserializableValue: UnserializableValue
        :param objectId: Remote object handle.
        :type objectId: RemoteObjectId
        """
        super().__init__()
        self.value: Optional[Any] = value
        self.unserializableValue: Optional[UnserializableValue] = unserializableValue
        self.objectId: Optional[RemoteObjectId] = objectId


