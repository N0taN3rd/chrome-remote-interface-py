
__all__ = [
    "StackTraceId",
    "StackTrace",
    "RemoteObject",
    "PropertyPreview",
    "PropertyDescriptor",
    "ObjectPreview",
    "InternalPropertyDescriptor",
    "ExecutionContextDescription",
    "ExceptionDetails",
    "EntryPreview",
    "CustomPreview",
    "CallFrame",
    "CallArgument",
]


class StackTraceId(object):
    """
    If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.
    """

    def __init__(self, id, debuggerId):
        """
        :param id: The id
        :type id: str
        :param debuggerId: The debuggerId
        :type debuggerId: Optional[str]
        """
        super().__init__()
        self.id = id
        self.debuggerId = debuggerId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.debuggerId is not None:
            repr_args.append("debuggerId={!r}".format(self.debuggerId))
        return "StackTraceId(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StackTraceId(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StackTraceId.safe_create(it))
            return list_of_self
        else:
            return init


class StackTrace(object):
    """
    Call frames for assertions or error messages.
    """

    def __init__(self, callFrames, description, parent, parentId):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.description is not None:
            repr_args.append("description={!r}".format(self.description))
        if self.callFrames is not None:
            repr_args.append("callFrames={!r}".format(self.callFrames))
        if self.parent is not None:
            repr_args.append("parent={!r}".format(self.parent))
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        return "StackTrace(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StackTrace(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StackTrace.safe_create(it))
            return list_of_self
        else:
            return init


class RemoteObject(object):
    """
    Mirror object referencing original JavaScript object.
    """

    def __init__(self, type, subtype, className, value, unserializableValue, description, objectId, preview, customPreview):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.subtype is not None:
            repr_args.append("subtype={!r}".format(self.subtype))
        if self.className is not None:
            repr_args.append("className={!r}".format(self.className))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.unserializableValue is not None:
            repr_args.append("unserializableValue={!r}".format(self.unserializableValue))
        if self.description is not None:
            repr_args.append("description={!r}".format(self.description))
        if self.objectId is not None:
            repr_args.append("objectId={!r}".format(self.objectId))
        if self.preview is not None:
            repr_args.append("preview={!r}".format(self.preview))
        if self.customPreview is not None:
            repr_args.append("customPreview={!r}".format(self.customPreview))
        return "RemoteObject(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = RemoteObject(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RemoteObject.safe_create(it))
            return list_of_self
        else:
            return init


class PropertyPreview(object):
    def __init__(self, name, type, value, valuePreview, subtype):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.valuePreview is not None:
            repr_args.append("valuePreview={!r}".format(self.valuePreview))
        if self.subtype is not None:
            repr_args.append("subtype={!r}".format(self.subtype))
        return "PropertyPreview(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PropertyPreview(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PropertyPreview.safe_create(it))
            return list_of_self
        else:
            return init


class PropertyDescriptor(object):
    """
    Object property descriptor.
    """

    def __init__(self, name, configurable, enumerable, value, writable, get, set, wasThrown, isOwn, symbol):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.writable is not None:
            repr_args.append("writable={!r}".format(self.writable))
        if self.get is not None:
            repr_args.append("get={!r}".format(self.get))
        if self.set is not None:
            repr_args.append("set={!r}".format(self.set))
        if self.configurable is not None:
            repr_args.append("configurable={!r}".format(self.configurable))
        if self.enumerable is not None:
            repr_args.append("enumerable={!r}".format(self.enumerable))
        if self.wasThrown is not None:
            repr_args.append("wasThrown={!r}".format(self.wasThrown))
        if self.isOwn is not None:
            repr_args.append("isOwn={!r}".format(self.isOwn))
        if self.symbol is not None:
            repr_args.append("symbol={!r}".format(self.symbol))
        return "PropertyDescriptor(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PropertyDescriptor(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PropertyDescriptor.safe_create(it))
            return list_of_self
        else:
            return init


class ObjectPreview(object):
    """
    Object containing abbreviated remote object value.
    """

    def __init__(self, type, overflow, properties, subtype, description, entries):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.subtype is not None:
            repr_args.append("subtype={!r}".format(self.subtype))
        if self.description is not None:
            repr_args.append("description={!r}".format(self.description))
        if self.overflow is not None:
            repr_args.append("overflow={!r}".format(self.overflow))
        if self.properties is not None:
            repr_args.append("properties={!r}".format(self.properties))
        if self.entries is not None:
            repr_args.append("entries={!r}".format(self.entries))
        return "ObjectPreview(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ObjectPreview(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectPreview.safe_create(it))
            return list_of_self
        else:
            return init


class InternalPropertyDescriptor(object):
    """
    Object internal property descriptor. This property isn't normally visible in JavaScript code.
    """

    def __init__(self, name, value):
        """
        :param name: Conventional property name.
        :type name: str
        :param value: The value associated with the property.
        :type value: Optional[dict]
        """
        super().__init__()
        self.name = name
        self.value = RemoteObject.safe_create(value)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "InternalPropertyDescriptor(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = InternalPropertyDescriptor(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InternalPropertyDescriptor.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextDescription(object):
    """
    Description of an isolated world.
    """

    def __init__(self, id, origin, name, auxData):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.auxData is not None:
            repr_args.append("auxData={!r}".format(self.auxData))
        return "ExecutionContextDescription(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ExecutionContextDescription(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextDescription.safe_create(it))
            return list_of_self
        else:
            return init


class ExceptionDetails(object):
    """
    Detailed information about exception (or error) that was thrown during script compilation or
execution.
    """

    def __init__(self, exceptionId, text, lineNumber, columnNumber, scriptId, url, stackTrace, exception, executionContextId):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.exceptionId is not None:
            repr_args.append("exceptionId={!r}".format(self.exceptionId))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        if self.exception is not None:
            repr_args.append("exception={!r}".format(self.exception))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        return "ExceptionDetails(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ExceptionDetails(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionDetails.safe_create(it))
            return list_of_self
        else:
            return init


class EntryPreview(object):
    def __init__(self, value, key):
        """
        :param key: Preview of the key. Specified for map-like collection entries.
        :type key: Optional[dict]
        :param value: Preview of the value.
        :type value: dict
        """
        super().__init__()
        self.key = ObjectPreview.safe_create(key)
        self.value = ObjectPreview.safe_create(value)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "EntryPreview(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = EntryPreview(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EntryPreview.safe_create(it))
            return list_of_self
        else:
            return init


class CustomPreview(object):
    def __init__(self, header, hasBody, formatterObjectId, bindRemoteObjectFunctionId, configObjectId):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.header is not None:
            repr_args.append("header={!r}".format(self.header))
        if self.hasBody is not None:
            repr_args.append("hasBody={!r}".format(self.hasBody))
        if self.formatterObjectId is not None:
            repr_args.append("formatterObjectId={!r}".format(self.formatterObjectId))
        if self.bindRemoteObjectFunctionId is not None:
            repr_args.append("bindRemoteObjectFunctionId={!r}".format(self.bindRemoteObjectFunctionId))
        if self.configObjectId is not None:
            repr_args.append("configObjectId={!r}".format(self.configObjectId))
        return "CustomPreview(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = CustomPreview(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CustomPreview.safe_create(it))
            return list_of_self
        else:
            return init


class CallFrame(object):
    """
    Stack entry for runtime errors and assertions.
    """

    def __init__(self, functionName, scriptId, url, lineNumber, columnNumber):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.functionName is not None:
            repr_args.append("functionName={!r}".format(self.functionName))
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "CallFrame(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = CallFrame(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CallFrame.safe_create(it))
            return list_of_self
        else:
            return init


class CallArgument(object):
    """
    Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified.
    """

    def __init__(self, value, unserializableValue, objectId):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.unserializableValue is not None:
            repr_args.append("unserializableValue={!r}".format(self.unserializableValue))
        if self.objectId is not None:
            repr_args.append("objectId={!r}".format(self.objectId))
        return "CallArgument(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = CallArgument(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CallArgument.safe_create(it))
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
