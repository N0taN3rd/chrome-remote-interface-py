from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.domdebugger import types as Types

__all__ = ["DOMDebugger"]+ Types.__all__ 


class DOMDebugger(object):
    """
    DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
execution will stop on these operations as if there was a regular breakpoint set.
    """

    dependencies = ['DOM', 'Debugger']

    def __init__(self, chrome):
        self.chrome = chrome

    def getEventListeners(self, objectId, depth, pierce):
        """
        :param objectId: Identifier of the object to return listeners for.
        :type objectId: str
        :param depth: The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled.
        :type pierce: Optional[bool]
        """
        def cb(res):
            res['listeners'] = Types.EventListener.safe_create_from_list(res['listeners'])
            self.chrome.emit('DOMDebugger.getEventListeners', res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOMDebugger.getEventListeners', params=msg_dict, cb=cb)


    def removeDOMBreakpoint(self, nodeId, type):
        """
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
        self.chrome.send('DOMDebugger.removeDOMBreakpoint', params=msg_dict)


    def removeEventListenerBreakpoint(self, eventName, targetName):
        """
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
        self.chrome.send('DOMDebugger.removeEventListenerBreakpoint', params=msg_dict)


    def removeInstrumentationBreakpoint(self, eventName):
        """
        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        self.chrome.send('DOMDebugger.removeInstrumentationBreakpoint', params=msg_dict)


    def removeXHRBreakpoint(self, url):
        """
        :param url: Resource URL substring.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        self.chrome.send('DOMDebugger.removeXHRBreakpoint', params=msg_dict)


    def setDOMBreakpoint(self, nodeId, type):
        """
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
        self.chrome.send('DOMDebugger.setDOMBreakpoint', params=msg_dict)


    def setEventListenerBreakpoint(self, eventName, targetName):
        """
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
        self.chrome.send('DOMDebugger.setEventListenerBreakpoint', params=msg_dict)


    def setInstrumentationBreakpoint(self, eventName):
        """
        :param eventName: Instrumentation name to stop on.
        :type eventName: str
        """
        msg_dict = dict()
        if eventName is not None:
            msg_dict['eventName'] = eventName
        self.chrome.send('DOMDebugger.setInstrumentationBreakpoint', params=msg_dict)


    def setXHRBreakpoint(self, url):
        """
        :param url: Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
        :type url: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        self.chrome.send('DOMDebugger.setXHRBreakpoint', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return None

