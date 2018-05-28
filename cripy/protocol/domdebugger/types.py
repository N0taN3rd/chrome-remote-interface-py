from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.dom import types as DOM

# DOM breakpoint type.
DOMBreakpointType = str


class EventListener(ChromeTypeBase):
    """Object event listener."""
    def __init__(self, type: str, useCapture: bool, passive: bool, once: bool, scriptId: 'Runtime.ScriptId', lineNumber: int, columnNumber: int, handler: Optional['Runtime.RemoteObject'] = None, originalHandler: Optional['Runtime.RemoteObject'] = None, backendNodeId: Optional['DOM.BackendNodeId'] = None) -> None:
        """
        :param str type: `EventListener`'s type.
        :param bool useCapture: `EventListener`'s useCapture.
        :param bool passive: `EventListener`'s passive flag.
        :param bool once: `EventListener`'s once flag.
        :param Runtime.ScriptId scriptId: Script id of the handler code.
        :param int lineNumber: Line number in the script (0-based).
        :param int columnNumber: Column number in the script (0-based).
        :param Runtime.RemoteObject handler: Event handler function value.
        :param Runtime.RemoteObject originalHandler: Event original handler function value.
        :param DOM.BackendNodeId backendNodeId: Node the listener is added to (if any).
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


