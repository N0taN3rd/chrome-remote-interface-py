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
        super().__init__()
        self.header: str = header
        self.hasBody: bool = hasBody
        self.formatterObjectId: RemoteObjectId = formatterObjectId
        self.bindRemoteObjectFunctionId: RemoteObjectId = bindRemoteObjectFunctionId
        self.configObjectId: Optional[RemoteObjectId] = configObjectId


class ObjectPreview(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        overflow: bool,
        properties: List["PropertyPreview"],
        subtype: Optional[str] = None,
        description: Optional[str] = None,
        entries: Optional[List["EntryPreview"]] = None,
    ) -> None:
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
        super().__init__()
        self.key: Optional[ObjectPreview] = key
        self.value: ObjectPreview = value


class PropertyDescriptor(ChromeTypeBase):

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

    def __init__(self, name: str, value: Optional["RemoteObject"] = None) -> None:
        super().__init__()
        self.name: str = name
        self.value: Optional[RemoteObject] = value


class CallArgument(ChromeTypeBase):

    def __init__(
        self,
        value: Optional[Any] = None,
        unserializableValue: Optional["UnserializableValue"] = None,
        objectId: Optional["RemoteObjectId"] = None,
    ) -> None:
        super().__init__()
        self.value: Optional[Any] = value
        self.unserializableValue: Optional[UnserializableValue] = unserializableValue
        self.objectId: Optional[RemoteObjectId] = objectId


class ExecutionContextDescription(ChromeTypeBase):

    def __init__(
        self,
        id: "ExecutionContextId",
        origin: str,
        name: str,
        auxData: Optional[dict] = None,
    ) -> None:
        super().__init__()
        self.id: ExecutionContextId = id
        self.origin: str = origin
        self.name: str = name
        self.auxData: Optional[dict] = auxData


class ExceptionDetails(ChromeTypeBase):

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

    def __init__(
        self,
        functionName: str,
        scriptId: "ScriptId",
        url: str,
        lineNumber: int,
        columnNumber: int,
    ) -> None:
        super().__init__()
        self.functionName: str = functionName
        self.scriptId: ScriptId = scriptId
        self.url: str = url
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class StackTrace(ChromeTypeBase):

    def __init__(
        self,
        callFrames: List["CallFrame"],
        description: Optional[str] = None,
        parent: Optional["StackTrace"] = None,
        parentId: Optional["StackTraceId"] = None,
    ) -> None:
        super().__init__()
        self.description: Optional[str] = description
        self.callFrames: List[CallFrame] = callFrames
        self.parent: Optional[StackTrace] = parent
        self.parentId: Optional[StackTraceId] = parentId


class StackTraceId(ChromeTypeBase):

    def __init__(
        self, id: str, debuggerId: Optional["UniqueDebuggerId"] = None
    ) -> None:
        super().__init__()
        self.id: str = id
        self.debuggerId: Optional[UniqueDebuggerId] = debuggerId
