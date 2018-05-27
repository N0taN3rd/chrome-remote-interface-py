from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.runtime import types as Runtime

DOMBreakpointType = str


class EventListener(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        useCapture: bool,
        passive: bool,
        once: bool,
        scriptId: "Runtime.ScriptId",
        lineNumber: int,
        columnNumber: int,
        handler: Optional["Runtime.RemoteObject"] = None,
        originalHandler: Optional["Runtime.RemoteObject"] = None,
        backendNodeId: Optional["DOM.BackendNodeId"] = None,
    ) -> None:
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
