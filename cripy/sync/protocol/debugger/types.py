from cripy.sync.protocol.runtime import types as Runtime

__all__ = [
    "SearchMatch",
    "ScriptPosition",
    "Scope",
    "Location",
    "CallFrame",
    "BreakLocation",
]


class SearchMatch(object):
    """
    Search match for resource.
    """

    def __init__(self, lineNumber, lineContent):
        """
        :param lineNumber: Line number in resource content.
        :type lineNumber: float
        :param lineContent: Line with match content.
        :type lineContent: str
        """
        super().__init__()
        self.lineNumber = lineNumber
        self.lineContent = lineContent

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.lineContent is not None:
            repr_args.append("lineContent={!r}".format(self.lineContent))
        return "SearchMatch(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = SearchMatch(**init)
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
                list_of_self.append(SearchMatch.safe_create(it))
            return list_of_self
        else:
            return init


class ScriptPosition(object):
    """
    Location in the source code.
    """

    def __init__(self, lineNumber, columnNumber):
        """
        :param lineNumber: The lineNumber
        :type lineNumber: int
        :param columnNumber: The columnNumber
        :type columnNumber: int
        """
        super().__init__()
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
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "ScriptPosition(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScriptPosition(**init)
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
                list_of_self.append(ScriptPosition.safe_create(it))
            return list_of_self
        else:
            return init


class Scope(object):
    """
    Scope description.
    """

    def __init__(self, type, object, name, startLocation, endLocation):
        """
        :param type: Scope type.
        :type type: str
        :param object: Object representing the scope. For `global` and `with` scopes it represents the actual object; for the rest of the scopes, it is artificial transient object enumerating scope variables as its properties.
        :type object: dict
        :param name: The name
        :type name: Optional[str]
        :param startLocation: Location in the source code where scope starts
        :type startLocation: Optional[dict]
        :param endLocation: Location in the source code where scope ends
        :type endLocation: Optional[dict]
        """
        super().__init__()
        self.type = type
        self.object = Runtime.RemoteObject.safe_create(object)
        self.name = name
        self.startLocation = Location.safe_create(startLocation)
        self.endLocation = Location.safe_create(endLocation)

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
        if self.object is not None:
            repr_args.append("object={!r}".format(self.object))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.startLocation is not None:
            repr_args.append("startLocation={!r}".format(self.startLocation))
        if self.endLocation is not None:
            repr_args.append("endLocation={!r}".format(self.endLocation))
        return "Scope(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Scope(**init)
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
                list_of_self.append(Scope.safe_create(it))
            return list_of_self
        else:
            return init


class Location(object):
    """
    Location in the source code.
    """

    def __init__(self, scriptId, lineNumber, columnNumber):
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :type scriptId: str
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: Optional[int]
        """
        super().__init__()
        self.scriptId = scriptId
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
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "Location(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Location(**init)
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
                list_of_self.append(Location.safe_create(it))
            return list_of_self
        else:
            return init


class CallFrame(object):
    """
    JavaScript call frame. Array of call frames form the call stack.
    """

    def __init__(self, callFrameId, functionName, location, url, scopeChain, this, functionLocation, returnValue):
        """
        :param callFrameId: Call frame identifier. This identifier is only valid while the virtual machine is paused.
        :type callFrameId: str
        :param functionName: Name of the JavaScript function called on this call frame.
        :type functionName: str
        :param functionLocation: Location in the source code.
        :type functionLocation: Optional[dict]
        :param location: Location in the source code.
        :type location: dict
        :param url: JavaScript script name or url.
        :type url: str
        :param scopeChain: Scope chain for this call frame.
        :type scopeChain: List[dict]
        :param this: `this` object for this call frame.
        :type this: dict
        :param returnValue: The value being returned, if the function is at return point.
        :type returnValue: Optional[dict]
        """
        super().__init__()
        self.callFrameId = callFrameId
        self.functionName = functionName
        self.functionLocation = Location.safe_create(functionLocation)
        self.location = Location.safe_create(location)
        self.url = url
        self.scopeChain = Scope.safe_create_from_list(scopeChain)
        self.this = Runtime.RemoteObject.safe_create(this)
        self.returnValue = Runtime.RemoteObject.safe_create(returnValue)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.callFrameId is not None:
            repr_args.append("callFrameId={!r}".format(self.callFrameId))
        if self.functionName is not None:
            repr_args.append("functionName={!r}".format(self.functionName))
        if self.functionLocation is not None:
            repr_args.append("functionLocation={!r}".format(self.functionLocation))
        if self.location is not None:
            repr_args.append("location={!r}".format(self.location))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.scopeChain is not None:
            repr_args.append("scopeChain={!r}".format(self.scopeChain))
        if self.this is not None:
            repr_args.append("this={!r}".format(self.this))
        if self.returnValue is not None:
            repr_args.append("returnValue={!r}".format(self.returnValue))
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


class BreakLocation(object):
    def __init__(self, scriptId, lineNumber, columnNumber, type):
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :type scriptId: str
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: Optional[int]
        :param type: The type
        :type type: Optional[str]
        """
        super().__init__()
        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.type = type

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        return "BreakLocation(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = BreakLocation(**init)
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
                list_of_self.append(BreakLocation.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SearchMatch": SearchMatch,
    "ScriptPosition": ScriptPosition,
    "Scope": Scope,
    "Location": Location,
    "CallFrame": CallFrame,
    "BreakLocation": BreakLocation,
}
