# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["DOMDebugger"]


@attr.dataclass(slots=True)
class DOMDebugger(object):
    """
    DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["DOM", "Debugger", "Runtime"]

    def getEventListeners(
        self, objectId: str, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Returns event listeners of the given object.

        :param objectId: Identifier of the object to return listeners for.
        :type objectId: str
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled.
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if depth is not None:
            msg_dict["depth"] = depth
        if pierce is not None:
            msg_dict["pierce"] = pierce
        return self.client.send("DOMDebugger.getEventListeners", msg_dict)

    def removeDOMBreakpoint(self, nodeId: int, type: str) -> Awaitable[Optional[dict]]:
        """
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.

        :param nodeId: Identifier of the node to remove breakpoint from.
        :type nodeId: int
        :param type: Type of the breakpoint to remove.
        :type type: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if type is not None:
            msg_dict["type"] = type
        return self.client.send("DOMDebugger.removeDOMBreakpoint", msg_dict)

    def removeEventListenerBreakpoint(
        self, eventName: str, targetName: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Removes breakpoint on particular DOM event.

        :param eventName: Event name.
        :type eventName: str
        :param targetName: EventTarget interface name.
        :type targetName: Optional[str]
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict["eventName"] = eventName
        if targetName is not None:
            msg_dict["targetName"] = targetName
        return self.client.send("DOMDebugger.removeEventListenerBreakpoint", msg_dict)

    def removeInstrumentationBreakpoint(
        self, eventName: str
    ) -> Awaitable[Optional[dict]]:
        """
        Removes breakpoint on particular native event.

        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict["eventName"] = eventName
        return self.client.send("DOMDebugger.removeInstrumentationBreakpoint", msg_dict)

    def removeXHRBreakpoint(self, url: str) -> Awaitable[Optional[dict]]:
        """
        Removes breakpoint from XMLHttpRequest.

        :param url: Resource URL substring.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict["url"] = url
        return self.client.send("DOMDebugger.removeXHRBreakpoint", msg_dict)

    def setDOMBreakpoint(self, nodeId: int, type: str) -> Awaitable[Optional[dict]]:
        """
        Sets breakpoint on particular operation with DOM.

        :param nodeId: Identifier of the node to set breakpoint on.
        :type nodeId: int
        :param type: Type of the operation to stop upon.
        :type type: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if type is not None:
            msg_dict["type"] = type
        return self.client.send("DOMDebugger.setDOMBreakpoint", msg_dict)

    def setEventListenerBreakpoint(
        self, eventName: str, targetName: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Sets breakpoint on particular DOM event.

        :param eventName: DOM Event name to stop on (any DOM event will do).
        :type eventName: str
        :param targetName: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any EventTarget.
        :type targetName: Optional[str]
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict["eventName"] = eventName
        if targetName is not None:
            msg_dict["targetName"] = targetName
        return self.client.send("DOMDebugger.setEventListenerBreakpoint", msg_dict)

    def setInstrumentationBreakpoint(self, eventName: str) -> Awaitable[Optional[dict]]:
        """
        Sets breakpoint on particular native event.

        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict["eventName"] = eventName
        return self.client.send("DOMDebugger.setInstrumentationBreakpoint", msg_dict)

    def setXHRBreakpoint(self, url: str) -> Awaitable[Optional[dict]]:
        """
        Sets breakpoint on XMLHttpRequest.

        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict["url"] = url
        return self.client.send("DOMDebugger.setXHRBreakpoint", msg_dict)
