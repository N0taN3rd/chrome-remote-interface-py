"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOMDebugger"]


class DOMDebugger:
    """
    DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
    execution will stop on these operations as if there was a regular breakpoint set.
     
    Domain Dependencies: 
      * DOM
      * Debugger
      * Runtime
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of DOMDebugger

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def getEventListeners(
        self, objectId: str, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Returns event listeners of the given object.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-getEventListeners`

        :param objectId: Identifier of the object to return listeners for.
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
         entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
         (default is false). Reports listeners for all contexts if pierce is enabled.
        :return: The results of the command
        """
        msg = {"objectId": objectId}
        if depth is not None:
            msg["depth"] = depth
        if pierce is not None:
            msg["pierce"] = pierce
        return self.client.send("DOMDebugger.getEventListeners", msg)

    def removeDOMBreakpoint(self, nodeId: int, type: str) -> Awaitable[Dict]:
        """
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-removeDOMBreakpoint`

        :param nodeId: Identifier of the node to remove breakpoint from.
        :param type: Type of the breakpoint to remove.
        :return: The results of the command
        """
        return self.client.send(
            "DOMDebugger.removeDOMBreakpoint", {"nodeId": nodeId, "type": type}
        )

    def removeEventListenerBreakpoint(
        self, eventName: str, targetName: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Removes breakpoint on particular DOM event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-removeEventListenerBreakpoint`

        :param eventName: Event name.
        :param targetName: EventTarget interface name.
        :return: The results of the command
        """
        msg = {"eventName": eventName}
        if targetName is not None:
            msg["targetName"] = targetName
        return self.client.send("DOMDebugger.removeEventListenerBreakpoint", msg)

    def removeInstrumentationBreakpoint(self, eventName: str) -> Awaitable[Dict]:
        """
        Removes breakpoint on particular native event.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-removeInstrumentationBreakpoint`

        :param eventName: Instrumentation name to stop on.
        :return: The results of the command
        """
        return self.client.send(
            "DOMDebugger.removeInstrumentationBreakpoint", {"eventName": eventName}
        )

    def removeXHRBreakpoint(self, url: str) -> Awaitable[Dict]:
        """
        Removes breakpoint from XMLHttpRequest.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-removeXHRBreakpoint`

        :param url: Resource URL substring.
        :return: The results of the command
        """
        return self.client.send("DOMDebugger.removeXHRBreakpoint", {"url": url})

    def setDOMBreakpoint(self, nodeId: int, type: str) -> Awaitable[Dict]:
        """
        Sets breakpoint on particular operation with DOM.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-setDOMBreakpoint`

        :param nodeId: Identifier of the node to set breakpoint on.
        :param type: Type of the operation to stop upon.
        :return: The results of the command
        """
        return self.client.send(
            "DOMDebugger.setDOMBreakpoint", {"nodeId": nodeId, "type": type}
        )

    def setEventListenerBreakpoint(
        self, eventName: str, targetName: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Sets breakpoint on particular DOM event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-setEventListenerBreakpoint`

        :param eventName: DOM Event name to stop on (any DOM event will do).
        :param targetName: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
         EventTarget.
        :return: The results of the command
        """
        msg = {"eventName": eventName}
        if targetName is not None:
            msg["targetName"] = targetName
        return self.client.send("DOMDebugger.setEventListenerBreakpoint", msg)

    def setInstrumentationBreakpoint(self, eventName: str) -> Awaitable[Dict]:
        """
        Sets breakpoint on particular native event.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-setInstrumentationBreakpoint`

        :param eventName: Instrumentation name to stop on.
        :return: The results of the command
        """
        return self.client.send(
            "DOMDebugger.setInstrumentationBreakpoint", {"eventName": eventName}
        )

    def setXHRBreakpoint(self, url: str) -> Awaitable[Dict]:
        """
        Sets breakpoint on XMLHttpRequest.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMDebugger#method-setXHRBreakpoint`

        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        :return: The results of the command
        """
        return self.client.send("DOMDebugger.setXHRBreakpoint", {"url": url})
