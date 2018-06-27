from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.dom import types as DOM
from cripy.asyncio.protocol.runtime import types as Runtime
from cripy.asyncio.protocol.domdebugger import types as Types

__all__ = ["DOMDebugger"]


class DOMDebugger(object):
    """
    DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.
    """

    dependencies = ['DOM', 'Debugger']

    def __init__(self, chrome):
        """
        Construct a new DOMDebugger object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def getEventListeners(self, objectId: str, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Optional[dict]:
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
            msg_dict['objectId'] = objectId
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        res = await self.chrome.send('DOMDebugger.getEventListeners', msg_dict)
        res['listeners'] = Types.EventListener.safe_create_from_list(res['listeners'])
        return res

    async def removeDOMBreakpoint(self, nodeId: int, type: str) -> Optional[dict]:
        """
        Removes DOM breakpoint that was set using `setDOMBreakpoint`.

        :param nodeId: Identifier of the node to remove breakpoint from.
        :type nodeId: int
        :param type: Type of the breakpoint to remove.
        :type type: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if type is not None:
            msg_dict['type'] = type
        res = await self.chrome.send('DOMDebugger.removeDOMBreakpoint', msg_dict)
        return res

    async def removeEventListenerBreakpoint(self, eventName: str, targetName: Optional[str] = None) -> Optional[dict]:
        """
        Removes breakpoint on particular DOM event.

        :param eventName: Event name.
        :type eventName: str
        :param targetName: EventTarget interface name.
        :type targetName: Optional[str]
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        if targetName is not None:
            msg_dict['targetName'] = targetName
        res = await self.chrome.send('DOMDebugger.removeEventListenerBreakpoint', msg_dict)
        return res

    async def removeInstrumentationBreakpoint(self, eventName: str) -> Optional[dict]:
        """
        Removes breakpoint on particular native event.

        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        res = await self.chrome.send('DOMDebugger.removeInstrumentationBreakpoint', msg_dict)
        return res

    async def removeXHRBreakpoint(self, url: str) -> Optional[dict]:
        """
        Removes breakpoint from XMLHttpRequest.

        :param url: Resource URL substring.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        res = await self.chrome.send('DOMDebugger.removeXHRBreakpoint', msg_dict)
        return res

    async def setDOMBreakpoint(self, nodeId: int, type: str) -> Optional[dict]:
        """
        Sets breakpoint on particular operation with DOM.

        :param nodeId: Identifier of the node to set breakpoint on.
        :type nodeId: int
        :param type: Type of the operation to stop upon.
        :type type: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if type is not None:
            msg_dict['type'] = type
        res = await self.chrome.send('DOMDebugger.setDOMBreakpoint', msg_dict)
        return res

    async def setEventListenerBreakpoint(self, eventName: str, targetName: Optional[str] = None) -> Optional[dict]:
        """
        Sets breakpoint on particular DOM event.

        :param eventName: DOM Event name to stop on (any DOM event will do).
        :type eventName: str
        :param targetName: EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any EventTarget.
        :type targetName: Optional[str]
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        if targetName is not None:
            msg_dict['targetName'] = targetName
        res = await self.chrome.send('DOMDebugger.setEventListenerBreakpoint', msg_dict)
        return res

    async def setInstrumentationBreakpoint(self, eventName: str) -> Optional[dict]:
        """
        Sets breakpoint on particular native event.

        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        res = await self.chrome.send('DOMDebugger.setInstrumentationBreakpoint', msg_dict)
        return res

    async def setXHRBreakpoint(self, url: str) -> Optional[dict]:
        """
        Sets breakpoint on XMLHttpRequest.

        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        res = await self.chrome.send('DOMDebugger.setXHRBreakpoint', msg_dict)
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

