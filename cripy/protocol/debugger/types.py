from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime

CallFrameId = TypeVar("CallFrameId", str, str) # Call frame identifier.

BreakpointId = TypeVar("BreakpointId", str, str) # Breakpoint identifier.


class SearchMatch(ProtocolType):
    """
    Search match for resource.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SearchMatch']:
        if init is not None:
            return SearchMatch(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SearchMatch']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SearchMatch(**it))
            return list_of_self
        else:
            return init


class ScriptPosition(ProtocolType):
    """
    Location in the source code.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScriptPosition']:
        if init is not None:
            return ScriptPosition(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScriptPosition']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScriptPosition(**it))
            return list_of_self
        else:
            return init


class Scope(ProtocolType):
    """
    Scope description.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Scope']:
        if init is not None:
            return Scope(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Scope']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Scope(**it))
            return list_of_self
        else:
            return init


class Location(ProtocolType):
    """
    Location in the source code.
    """

    def __init__(self, scriptId: Runtime.ScriptId, lineNumber: int, columnNumber: Optional[int] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Location']:
        if init is not None:
            return Location(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Location']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Location(**it))
            return list_of_self
        else:
            return init


class CallFrame(ProtocolType):
    """
    JavaScript call frame. Array of call frames form the call stack.
    """

    def __init__(self, callFrameId: CallFrameId, functionName: str, location: Union['Location', dict], url: str, scopeChain: List[Union['Scope', dict]], this: Union['Runtime.RemoteObject', dict], functionLocation: Optional[Union['Location', dict]] = None, returnValue: Optional[Union['Runtime.RemoteObject', dict]] = None) -> None:
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


class BreakLocation(ProtocolType):
    def __init__(self, scriptId: Runtime.ScriptId, lineNumber: int, columnNumber: Optional[int] = None, type: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['BreakLocation']:
        if init is not None:
            return BreakLocation(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['BreakLocation']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BreakLocation(**it))
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
