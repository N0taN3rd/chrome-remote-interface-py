from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.page import types as Page
from cripy.sync.protocol.dom import events as Events
from cripy.sync.protocol.dom import types as Types

__all__ = ["DOM"] + Events.__all__ + Types.__all__ 


class DOM(object):
    """
    This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object
that has an `id`. This `id` can be used to get additional information on the Node, resolve it into
the JavaScript object wrapper, etc. It is important that client receives DOM events only for the
nodes that are known to the client. Backend keeps track of the nodes that were sent to the client
and never sends the same node twice. It is client's responsibility to collect information about
the nodes that were sent to the client.<p>Note that `iframe` owner elements will return
corresponding document elements as their child nodes.</p>
    """

    dependencies = ['Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def collectClassNamesFromSubtree(self, nodeId, cb=None):
        """
        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.collectClassNamesFromSubtree', params=msg_dict, cb=cb_wrapper)


    def copyTo(self, nodeId, targetNodeId, insertBeforeNodeId, cb=None):
        """
        :param nodeId: Id of the node to copy.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the copy into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop the copy before this node (if absent, the copy becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        self.chrome.send('DOM.copyTo', params=msg_dict, cb=cb_wrapper)


    def describeNode(self, nodeId, backendNodeId, objectId, depth, pierce, cb=None):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        def cb_wrapper(res):
            res['node'] = Types.Node.safe_create(res['node'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.describeNode', params=msg_dict, cb=cb_wrapper)


    def disable(self, cb=None):
        self.chrome.send('DOM.disable')


    def discardSearchResults(self, searchId, cb=None):
        """
        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        self.chrome.send('DOM.discardSearchResults', params=msg_dict)


    def enable(self, cb=None):
        self.chrome.send('DOM.enable')


    def focus(self, nodeId, backendNodeId, objectId, cb=None):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.focus', params=msg_dict)


    def getAttributes(self, nodeId, cb=None):
        """
        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.getAttributes', params=msg_dict, cb=cb_wrapper)


    def getBoxModel(self, nodeId, backendNodeId, objectId, cb=None):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        def cb_wrapper(res):
            res['model'] = Types.BoxModel.safe_create(res['model'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.getBoxModel', params=msg_dict, cb=cb_wrapper)


    def getDocument(self, depth, pierce, cb=None):
        """
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        def cb_wrapper(res):
            res['root'] = Types.Node.safe_create(res['root'])
            cb(res)
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.getDocument', params=msg_dict, cb=cb_wrapper)


    def getFlattenedDocument(self, depth, pierce, cb=None):
        """
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        def cb_wrapper(res):
            res['nodes'] = Types.Node.safe_create_from_list(res['nodes'])
            cb(res)
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.getFlattenedDocument', params=msg_dict, cb=cb_wrapper)


    def getNodeForLocation(self, x, y, includeUserAgentShadowDOM, cb=None):
        """
        :param x: X coordinate.
        :type x: int
        :param y: Y coordinate.
        :type y: int
        :param includeUserAgentShadowDOM: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        self.chrome.send('DOM.getNodeForLocation', params=msg_dict, cb=cb_wrapper)


    def getOuterHTML(self, nodeId, backendNodeId, objectId, cb=None):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.getOuterHTML', params=msg_dict, cb=cb_wrapper)


    def getRelayoutBoundary(self, nodeId, cb=None):
        """
        :param nodeId: Id of the node.
        :type nodeId: int
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.getRelayoutBoundary', params=msg_dict, cb=cb_wrapper)


    def getSearchResults(self, searchId, fromIndex, toIndex, cb=None):
        """
        :param searchId: Unique search session identifier.
        :type searchId: str
        :param fromIndex: Start index of the search result to be returned.
        :type fromIndex: int
        :param toIndex: End index of the search result to be returned.
        :type toIndex: int
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        if fromIndex is not None:
            msg_dict['fromIndex'] = fromIndex
        if toIndex is not None:
            msg_dict['toIndex'] = toIndex
        self.chrome.send('DOM.getSearchResults', params=msg_dict, cb=cb_wrapper)


    def hideHighlight(self, cb=None):
        self.chrome.send('DOM.hideHighlight')


    def highlightNode(self, cb=None):
        self.chrome.send('DOM.highlightNode')


    def highlightRect(self, cb=None):
        self.chrome.send('DOM.highlightRect')


    def markUndoableState(self, cb=None):
        self.chrome.send('DOM.markUndoableState')


    def moveTo(self, nodeId, targetNodeId, insertBeforeNodeId, cb=None):
        """
        :param nodeId: Id of the node to move.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the moved node into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop node before this one (if absent, the moved node becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        self.chrome.send('DOM.moveTo', params=msg_dict, cb=cb_wrapper)


    def performSearch(self, query, includeUserAgentShadowDOM, cb=None):
        """
        :param query: Plain text or query selector or XPath search query.
        :type query: str
        :param includeUserAgentShadowDOM: True to search in user agent shadow DOM.
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        self.chrome.send('DOM.performSearch', params=msg_dict, cb=cb_wrapper)


    def pushNodeByPathToFrontend(self, path, cb=None):
        """
        :param path: Path to node in the proprietary format.
        :type path: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if path is not None:
            msg_dict['path'] = path
        self.chrome.send('DOM.pushNodeByPathToFrontend', params=msg_dict, cb=cb_wrapper)


    def pushNodesByBackendIdsToFrontend(self, backendNodeIds, cb=None):
        """
        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict['backendNodeIds'] = backendNodeIds
        self.chrome.send('DOM.pushNodesByBackendIdsToFrontend', params=msg_dict, cb=cb_wrapper)


    def querySelector(self, nodeId, selector, cb=None):
        """
        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('DOM.querySelector', params=msg_dict, cb=cb_wrapper)


    def querySelectorAll(self, nodeId, selector, cb=None):
        """
        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('DOM.querySelectorAll', params=msg_dict, cb=cb_wrapper)


    def redo(self, cb=None):
        self.chrome.send('DOM.redo')


    def removeAttribute(self, nodeId, name, cb=None):
        """
        :param nodeId: Id of the element to remove attribute from.
        :type nodeId: int
        :param name: Name of the attribute to remove.
        :type name: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('DOM.removeAttribute', params=msg_dict)


    def removeNode(self, nodeId, cb=None):
        """
        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.removeNode', params=msg_dict)


    def requestChildNodes(self, nodeId, depth, pierce, cb=None):
        """
        :param nodeId: Id of the node to get children for.
        :type nodeId: int
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false).
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.requestChildNodes', params=msg_dict)


    def requestNode(self, objectId, cb=None):
        """
        :param objectId: JavaScript object id to convert into node.
        :type objectId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.requestNode', params=msg_dict, cb=cb_wrapper)


    def resolveNode(self, nodeId, backendNodeId, objectGroup, cb=None):
        """
        :param nodeId: Id of the node to resolve.
        :type nodeId: Optional[int]
        :param backendNodeId: Backend identifier of the node to resolve.
        :type backendNodeId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        def cb_wrapper(res):
            res['object'] = Runtime.RemoteObject.safe_create(res['object'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        self.chrome.send('DOM.resolveNode', params=msg_dict, cb=cb_wrapper)


    def setAttributeValue(self, nodeId, name, value, cb=None):
        """
        :param nodeId: Id of the element to set attribute for.
        :type nodeId: int
        :param name: Attribute name.
        :type name: str
        :param value: Attribute value.
        :type value: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if name is not None:
            msg_dict['name'] = name
        if value is not None:
            msg_dict['value'] = value
        self.chrome.send('DOM.setAttributeValue', params=msg_dict)


    def setAttributesAsText(self, nodeId, text, name, cb=None):
        """
        :param nodeId: Id of the element to set attributes for.
        :type nodeId: int
        :param text: Text with a number of attributes. Will parse this text using HTML parser.
        :type text: str
        :param name: Attribute name to replace with new attributes derived from text in case text parsed successfully.
        :type name: Optional[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if text is not None:
            msg_dict['text'] = text
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('DOM.setAttributesAsText', params=msg_dict)


    def setFileInputFiles(self, files, nodeId, backendNodeId, objectId, cb=None):
        """
        :param files: Array of file paths to set.
        :type files: List[str]
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        msg_dict = dict()
        if files is not None:
            msg_dict['files'] = files
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.setFileInputFiles', params=msg_dict)


    def setInspectedNode(self, nodeId, cb=None):
        """
        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.setInspectedNode', params=msg_dict)


    def setNodeName(self, nodeId, name, cb=None):
        """
        :param nodeId: Id of the node to set name for.
        :type nodeId: int
        :param name: New node's name.
        :type name: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('DOM.setNodeName', params=msg_dict, cb=cb_wrapper)


    def setNodeValue(self, nodeId, value, cb=None):
        """
        :param nodeId: Id of the node to set value for.
        :type nodeId: int
        :param value: New node's value.
        :type value: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if value is not None:
            msg_dict['value'] = value
        self.chrome.send('DOM.setNodeValue', params=msg_dict)


    def setOuterHTML(self, nodeId, outerHTML, cb=None):
        """
        :param nodeId: Id of the node to set markup for.
        :type nodeId: int
        :param outerHTML: Outer HTML markup to set.
        :type outerHTML: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if outerHTML is not None:
            msg_dict['outerHTML'] = outerHTML
        self.chrome.send('DOM.setOuterHTML', params=msg_dict)


    def undo(self, cb=None):
        self.chrome.send('DOM.undo')


    def getFrameOwner(self, frameId, cb=None):
        """
        :param frameId: The frameId
        :type frameId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('DOM.getFrameOwner', params=msg_dict, cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

