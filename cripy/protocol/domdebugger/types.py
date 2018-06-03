from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.dom import types as DOM


class EventListener(ProtocolType):
    """
    Object event listener.
    """

    def __init__(self, type: str, useCapture: bool, passive: bool, once: bool, scriptId: str, lineNumber: int, columnNumber: int, handler: Optional[Union['Runtime.RemoteObject', dict]] = None, originalHandler: Optional[Union['Runtime.RemoteObject', dict]] = None, backendNodeId: Optional[int] = None) -> None:
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
        :type scriptId: str
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: int
        :param handler: Event handler function value.
        :type handler: Optional[dict]
        :param originalHandler: Event original handler function value.
        :type originalHandler: Optional[dict]
        :param backendNodeId: Node the listener is added to (if any).
        :type backendNodeId: Optional[int]
        """
        super().__init__()
        self.type = type
        self.useCapture = useCapture
        self.passive = passive
        self.once = once
        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.handler = Runtime.RemoteObject.safe_create(handler)
        self.originalHandler = Runtime.RemoteObject.safe_create(originalHandler)
        self.backendNodeId = backendNodeId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['EventListener', dict]]:
        if init is not None:
            try:
                ourselves = EventListener(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['EventListener', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EventListener.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "EventListener": EventListener,
}
