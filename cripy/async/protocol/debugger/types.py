from typing import Any, List, Optional, Union
from cripy.async.protocol.runtime import types as Runtime

__all__ = [
    "SearchMatch",
    "ScriptPosition",
    "Scope",
    "Location",
    "CallFrame",
    "BreakLocation",
    "DEBUGGER_TYPES_TO_OBJECT"
]


class SearchMatch(object):
    """
    Search match for resource.
    """

    __slots__ = ["lineNumber", "lineContent"]

    def __init__(self, lineNumber: float, lineContent: str) -> None:
        """
        :param lineNumber: Line number in resource content.
        :type lineNumber: float
        :param lineContent: Line with match content.
        :type lineContent: str
        """
        super().__init__()
        self.lineNumber = lineNumber
        self.lineContent = lineContent

    def __repr__(self) -> str:
        repr_args = []
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.lineContent is not None:
            repr_args.append("lineContent={!r}".format(self.lineContent))
        return "SearchMatch(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SearchMatch', dict]]:
        """
        Safely create SearchMatch from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SearchMatch
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SearchMatch if creation did not fail
        :rtype: Optional[Union[dict, SearchMatch]]
        """
        if init is not None:
            try:
                ourselves = SearchMatch(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SearchMatch', dict]]]:
        """
        Safely create a new list SearchMatchs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SearchMatch instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SearchMatch instances if creation did not fail
        :rtype: Optional[List[Union[dict, SearchMatch]]]
        """
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

    __slots__ = ["lineNumber", "columnNumber"]

    def __init__(self, lineNumber: int, columnNumber: int) -> None:
        """
        :param lineNumber: The lineNumber
        :type lineNumber: int
        :param columnNumber: The columnNumber
        :type columnNumber: int
        """
        super().__init__()
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

    def __repr__(self) -> str:
        repr_args = []
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "ScriptPosition(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScriptPosition', dict]]:
        """
        Safely create ScriptPosition from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScriptPosition
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScriptPosition if creation did not fail
        :rtype: Optional[Union[dict, ScriptPosition]]
        """
        if init is not None:
            try:
                ourselves = ScriptPosition(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScriptPosition', dict]]]:
        """
        Safely create a new list ScriptPositions from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScriptPosition instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScriptPosition instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScriptPosition]]]
        """
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

    __slots__ = ["type", "object", "name", "startLocation", "endLocation"]

    def __init__(self, type: str, object: Union['Runtime.RemoteObject', dict], name: Optional[str] = None, startLocation: Optional[Union['Location', dict]] = None, endLocation: Optional[Union['Location', dict]] = None) -> None:
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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['Scope', dict]]:
        """
        Safely create Scope from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Scope
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Scope if creation did not fail
        :rtype: Optional[Union[dict, Scope]]
        """
        if init is not None:
            try:
                ourselves = Scope(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Scope', dict]]]:
        """
        Safely create a new list Scopes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Scope instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Scope instances if creation did not fail
        :rtype: Optional[List[Union[dict, Scope]]]
        """
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

    __slots__ = ["scriptId", "lineNumber", "columnNumber"]

    def __init__(self, scriptId: str, lineNumber: int, columnNumber: Optional[int] = None) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "Location(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Location', dict]]:
        """
        Safely create Location from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Location
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Location if creation did not fail
        :rtype: Optional[Union[dict, Location]]
        """
        if init is not None:
            try:
                ourselves = Location(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Location', dict]]]:
        """
        Safely create a new list Locations from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Location instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Location instances if creation did not fail
        :rtype: Optional[List[Union[dict, Location]]]
        """
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

    __slots__ = ["callFrameId", "functionName", "functionLocation", "location", "url", "scopeChain", "this", "returnValue"]

    def __init__(self, callFrameId: str, functionName: str, location: Union['Location', dict], url: str, scopeChain: List[Union['Scope', dict]], this: Union['Runtime.RemoteObject', dict], functionLocation: Optional[Union['Location', dict]] = None, returnValue: Optional[Union['Runtime.RemoteObject', dict]] = None) -> None:
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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['CallFrame', dict]]:
        """
        Safely create CallFrame from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CallFrame
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CallFrame if creation did not fail
        :rtype: Optional[Union[dict, CallFrame]]
        """
        if init is not None:
            try:
                ourselves = CallFrame(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CallFrame', dict]]]:
        """
        Safely create a new list CallFrames from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CallFrame instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CallFrame instances if creation did not fail
        :rtype: Optional[List[Union[dict, CallFrame]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CallFrame.safe_create(it))
            return list_of_self
        else:
            return init


class BreakLocation(object):
    __slots__ = ["scriptId", "lineNumber", "columnNumber", "type"]

    def __init__(self, scriptId: str, lineNumber: int, columnNumber: Optional[int] = None, type: Optional[str] = None) -> None:
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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['BreakLocation', dict]]:
        """
        Safely create BreakLocation from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of BreakLocation
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of BreakLocation if creation did not fail
        :rtype: Optional[Union[dict, BreakLocation]]
        """
        if init is not None:
            try:
                ourselves = BreakLocation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['BreakLocation', dict]]]:
        """
        Safely create a new list BreakLocations from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list BreakLocation instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of BreakLocation instances if creation did not fail
        :rtype: Optional[List[Union[dict, BreakLocation]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BreakLocation.safe_create(it))
            return list_of_self
        else:
            return init


DEBUGGER_TYPES_TO_OBJECT = {
    "SearchMatch": SearchMatch,
    "ScriptPosition": ScriptPosition,
    "Scope": Scope,
    "Location": Location,
    "CallFrame": CallFrame,
    "BreakLocation": BreakLocation,
}
