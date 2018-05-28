from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.runtime import types as Runtime

DOMBreakpointType = TypeVar("DOMBreakpointType", str, str)
"""DOM breakpoint type."""


class EventListener(ChromeTypeBase):
    """Object event listener."""
    def __init__(self, type: str, useCapture: bool, passive: bool, once: bool, scriptId: 'Runtime.ScriptId', lineNumber: int, columnNumber: int, handler: Optional['Runtime.RemoteObject'] = None, originalHandler: Optional['Runtime.RemoteObject'] = None, backendNodeId: Optional['DOM.BackendNodeId'] = None) -> None:
        """
        :param type: `EventListener`'s type.
        :type type: str
        :param useCapture: `EventListener`'s useCapture.
        :type useCapture: bool
        :param passive: `EventListener`'s passive flag.
        :type passive: bool
        :param once: `EventListener`'s once flag.
        :type once: bool
        :param scriptId: Script id of the handler code.
        :type scriptId: Runtime.ScriptId
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: int
        :param handler: Event handler function value.
        :type handler: Runtime.RemoteObject
        :param originalHandler: Event original handler function value.
        :type originalHandler: Runtime.RemoteObject
        :param backendNodeId: Node the listener is added to (if any).
        :type backendNodeId: DOM.BackendNodeId
        """
        super().__init__()
        self.type: str = type
        self.useCapture: bool = useCapture
        self.passive: bool = passive
        self.once: bool = once
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber
        self.handler: Optional[Runtime.RemoteObject] = handler
        self.originalHandler: Optional[Runtime.RemoteObject] = originalHandler
        self.backendNodeId: Optional[DOM.BackendNodeId] = backendNodeId


