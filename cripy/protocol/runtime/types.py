from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

ScriptId = str

RemoteObjectId = str

UnserializableValue = str

ExecutionContextId = int

Timestamp = float

TimeDelta = float

UniqueDebuggerId = str


class RemoteObject(ChromeTypeBase):
    """Mirror object referencing original JavaScript object."""

    def __init__(
        self,
        type: str,
        subtype: Optional[str] = None,
        className: Optional[str] = None,
        value: Optional[Any] = None,
        unserializableValue: Optional["UnserializableValue"] = None,
        description: Optional[str] = None,
        objectId: Optional["RemoteObjectId"] = None,
        preview: Optional["ObjectPreview"] = None,
        customPreview: Optional["CustomPreview"] = None,
    ) -> None:
        """
        :param type: Object type.
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :param className: Object class (constructor) name. Specified for `object` type values only.
        :param value: Remote object value in case of primitive values or JSON values (if it was requested).
        :param unserializableValue: Primitive value which can not be JSON-stringified does not have `value`, but gets this
property.
        :param description: String representation of the object.
        :param objectId: Unique object identifier (for non-primitive values).
        :param preview: Preview containing abbreviated property values. Specified for `object` type values only.
        :param customPreview: The customPreview
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


class CustomPreview(ChromeTypeBase):

    def __init__(
        self,
        header: str,
        hasBody: bool,
        formatterObjectId: "RemoteObjectId",
        bindRemoteObjectFunctionId: "RemoteObjectId",
        configObjectId: Optional["RemoteObjectId"] = None,
    ) -> None:
        """
        :param header: The header
        :param hasBody: The hasBody
        :param formatterObjectId: The formatterObjectId
        :param bindRemoteObjectFunctionId: The bindRemoteObjectFunctionId
        :param configObjectId: The configObjectId
        """
        super().__init__()
        self.header: str = header
        self.hasBody: bool = hasBody
        self.formatterObjectId: RemoteObjectId = formatterObjectId
        self.bindRemoteObjectFunctionId: RemoteObjectId = bindRemoteObjectFunctionId
        self.configObjectId: Optional[RemoteObjectId] = configObjectId


class ObjectPreview(ChromeTypeBase):
    """Object containing abbreviated remote object value."""

    def __init__(
        self,
        type: str,
        overflow: bool,
        properties: List["PropertyPreview"],
        subtype: Optional[str] = None,
        description: Optional[str] = None,
        entries: Optional[List["EntryPreview"]] = None,
    ) -> None:
        """
        :param type: Object type.
        :param subtype: Object subtype hint. Specified for `object` type values only.
        :param description: String representation of the object.
        :param overflow: True iff some of the properties or entries of the original object did not fit.
        :param properties: List of the properties.
        :param entries: List of the entries. Specified for `map` and `set` subtype values only.
        """
        super().__init__()
        self.type: str = type
        self.subtype: Optional[str] = subtype
        self.description: Optional[str] = description
        self.overflow: bool = overflow
        self.properties: List[PropertyPreview] = properties
        self.entries: Optional[List[EntryPreview]] = entries


class PropertyPreview(ChromeTypeBase):

    def __init__(
        self,
        name: str,
        type: str,
        value: Optional[str] = None,
        valuePreview: Optional["ObjectPreview"] = None,
        subtype: Optional[str] = None,
    ) -> None:
        """
        :param name: Property name.
        :param type: Object type. Accessor means that the property itself is an accessor property.
        :param value: User-friendly property value string.
        :param valuePreview: Nested value preview.
        :param subtype: Object subtype hint. Specified for `object` type values only.
        """
        super().__init__()
        self.name: str = name
        self.type: str = type
        self.value: Optional[str] = value
        self.valuePreview: Optional[ObjectPreview] = valuePreview
        self.subtype: Optional[str] = subtype


class EntryPreview(ChromeTypeBase):

    def __init__(
        self, value: "ObjectPreview", key: Optional["ObjectPreview"] = None
    ) -> None:
        """
        :param key: Preview of the key. Specified for map-like collection entries.
        :param value: Preview of the value.
        """
        super().__init__()
        self.key: Optional[ObjectPreview] = key
        self.value: ObjectPreview = value


class PropertyDescriptor(ChromeTypeBase):
    """Object property descriptor."""

    def __init__(
        self,
        name: str,
        configurable: bool,
        enumerable: bool,
        value: Optional["RemoteObject"] = None,
        writable: Optional[bool] = None,
        get: Optional["RemoteObject"] = None,
        set: Optional["RemoteObject"] = None,
        wasThrown: Optional[bool] = None,
        isOwn: Optional[bool] = None,
        symbol: Optional["RemoteObject"] = None,
    ) -> None:
        """
        :param name: Property name or symbol description.
        :param value: The value associated with the property.
        :param writable: True if the value associated with the property may be changed (data descriptors only).
        :param get: A function which serves as a getter for the property, or `undefined` if there is no getter
(accessor descriptors only).
        :param set: A function which serves as a setter for the property, or `undefined` if there is no setter
(accessor descriptors only).
        :param configurable: True if the type of this property descriptor may be changed and if the property may be
deleted from the corresponding object.
        :param enumerable: True if this property shows up during enumeration of the properties on the corresponding
object.
        :param wasThrown: True if the result was thrown during the evaluation.
        :param isOwn: True if the property is owned for the object.
        :param symbol: Property symbol object, if the property is of the `symbol` type.
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


class InternalPropertyDescriptor(ChromeTypeBase):
    """Object internal property descriptor. This property isn't normally visible in JavaScript code."""

    def __init__(self, name: str, value: Optional["RemoteObject"] = None) -> None:
        """
        :param name: Conventional property name.
        :param value: The value associated with the property.
        """
        super().__init__()
        self.name: str = name
        self.value: Optional[RemoteObject] = value


class CallArgument(ChromeTypeBase):
    """Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified."""

    def __init__(
        self,
        value: Optional[Any] = None,
        unserializableValue: Optional["UnserializableValue"] = None,
        objectId: Optional["RemoteObjectId"] = None,
    ) -> None:
        """
        :param value: Primitive value or serializable javascript object.
        :param unserializableValue: Primitive value which can not be JSON-stringified.
        :param objectId: Remote object handle.
        """
        super().__init__()
        self.value: Optional[Any] = value
        self.unserializableValue: Optional[UnserializableValue] = unserializableValue
        self.objectId: Optional[RemoteObjectId] = objectId


class ExecutionContextDescription(ChromeTypeBase):
    """Description of an isolated world."""

    def __init__(
        self,
        id: "ExecutionContextId",
        origin: str,
        name: str,
        auxData: Optional[dict] = None,
    ) -> None:
        """
        :param id: Unique id of the execution context. It can be used to specify in which execution context
script evaluation should be performed.
        :param origin: Execution context origin.
        :param name: Human readable name describing given context.
        :param auxData: Embedder-specific auxiliary data.
        """
        super().__init__()
        self.id: ExecutionContextId = id
        self.origin: str = origin
        self.name: str = name
        self.auxData: Optional[dict] = auxData


class ExceptionDetails(ChromeTypeBase):
    """Detailed information about exception (or error) that was thrown during script compilation or
execution."""

    def __init__(
        self,
        exceptionId: int,
        text: str,
        lineNumber: int,
        columnNumber: int,
        scriptId: Optional["ScriptId"] = None,
        url: Optional[str] = None,
        stackTrace: Optional["StackTrace"] = None,
        exception: Optional["RemoteObject"] = None,
        executionContextId: Optional["ExecutionContextId"] = None,
    ) -> None:
        """
        :param exceptionId: Exception id.
        :param text: Exception text, which should be used together with exception object when available.
        :param lineNumber: Line number of the exception location (0-based).
        :param columnNumber: Column number of the exception location (0-based).
        :param scriptId: Script ID of the exception location.
        :param url: URL of the exception location, to be used when the script was not reported.
        :param stackTrace: JavaScript stack trace if available.
        :param exception: Exception object if available.
        :param executionContextId: Identifier of the context where exception happened.
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


class CallFrame(ChromeTypeBase):
    """Stack entry for runtime errors and assertions."""

    def __init__(
        self,
        functionName: str,
        scriptId: "ScriptId",
        url: str,
        lineNumber: int,
        columnNumber: int,
    ) -> None:
        """
        :param functionName: JavaScript function name.
        :param scriptId: JavaScript script id.
        :param url: JavaScript script name or url.
        :param lineNumber: JavaScript script line number (0-based).
        :param columnNumber: JavaScript script column number (0-based).
        """
        super().__init__()
        self.functionName: str = functionName
        self.scriptId: ScriptId = scriptId
        self.url: str = url
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class StackTrace(ChromeTypeBase):
    """Call frames for assertions or error messages."""

    def __init__(
        self,
        callFrames: List["CallFrame"],
        description: Optional[str] = None,
        parent: Optional["StackTrace"] = None,
        parentId: Optional["StackTraceId"] = None,
    ) -> None:
        """
        :param description: String label of this stack trace. For async traces this may be a name of the function that
initiated the async call.
        :param callFrames: JavaScript function name.
        :param parent: Asynchronous JavaScript stack trace that preceded this stack, if available.
        :param parentId: Asynchronous JavaScript stack trace that preceded this stack, if available.
        """
        super().__init__()
        self.description: Optional[str] = description
        self.callFrames: List[CallFrame] = callFrames
        self.parent: Optional[StackTrace] = parent
        self.parentId: Optional[StackTraceId] = parentId


class StackTraceId(ChromeTypeBase):
    """If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages."""

    def __init__(
        self, id: str, debuggerId: Optional["UniqueDebuggerId"] = None
    ) -> None:
        """
        :param id: The id
        :param debuggerId: The debuggerId
        """
        super().__init__()
        self.id: str = id
        self.debuggerId: Optional[UniqueDebuggerId] = debuggerId
