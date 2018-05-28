from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.runtime import types as Runtime

# DOM breakpoint type.
DOMBreakpointType = str


class EventListener(ChromeTypeBase):
    """Object event listener."""

    def __init__(self, type: str, useCapture: bool, passive: bool, once: bool, scriptId: 'Runtime.ScriptId', lineNumber: int, columnNumber: int, handler: Optional['Runtime.RemoteObject'] = None, originalHandler: Optional['Runtime.RemoteObject'] = None, backendNodeId: Optional['DOM.BackendNodeId'] = None) -> None:
        """
        :param type: `EventListener`'s type.
        :type str:
        :param useCapture: `EventListener`'s useCapture.
        :type bool:
        :param passive: `EventListener`'s passive flag.
        :type bool:
        :param once: `EventListener`'s once flag.
        :type bool:
        :param scriptId: Script id of the handler code.
        :type Runtime.ScriptId:
        :param lineNumber: Line number in the script (0-based).
        :type int:
        :param columnNumber: Column number in the script (0-based).
        :type int:
        :param handler: Event handler function value.
        :type Runtime.RemoteObject:
        :param originalHandler: Event original handler function value.
        :type Runtime.RemoteObject:
        :param backendNodeId: Node the listener is added to (if any).
        :type DOM.BackendNodeId:
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


