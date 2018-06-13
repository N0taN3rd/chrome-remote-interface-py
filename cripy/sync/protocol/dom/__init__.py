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

    def collectClassNamesFromSubtree(self, nodeId):
        """
        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        def cb(res):
            self.chrome.emit('DOM.collectClassNamesFromSubtree', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.collectClassNamesFromSubtree', params=msg_dict, cb=cb)


    def copyTo(self, nodeId, targetNodeId, insertBeforeNodeId):
        """
        :param nodeId: Id of the node to copy.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the copy into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop the copy before this node (if absent, the copy becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        def cb(res):
            self.chrome.emit('DOM.copyTo', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        self.chrome.send('DOM.copyTo', params=msg_dict, cb=cb)


    def describeNode(self, nodeId, backendNodeId, objectId, depth, pierce):
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
        def cb(res):
            res['node'] = Types.Node.safe_create(res['node'])
            self.chrome.emit('DOM.describeNode', res)
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
        self.chrome.send('DOM.describeNode', params=msg_dict, cb=cb)


    def disable(self):
        self.chrome.send('DOM.disable')


    def discardSearchResults(self, searchId):
        """
        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        self.chrome.send('DOM.discardSearchResults', params=msg_dict)


    def enable(self):
        self.chrome.send('DOM.enable')


    def focus(self, nodeId, backendNodeId, objectId):
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


    def getAttributes(self, nodeId):
        """
        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        def cb(res):
            self.chrome.emit('DOM.getAttributes', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.getAttributes', params=msg_dict, cb=cb)


    def getBoxModel(self, nodeId, backendNodeId, objectId):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        def cb(res):
            res['model'] = Types.BoxModel.safe_create(res['model'])
            self.chrome.emit('DOM.getBoxModel', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.getBoxModel', params=msg_dict, cb=cb)


    def getDocument(self, depth, pierce):
        """
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        def cb(res):
            res['root'] = Types.Node.safe_create(res['root'])
            self.chrome.emit('DOM.getDocument', res)
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.getDocument', params=msg_dict, cb=cb)


    def getFlattenedDocument(self, depth, pierce):
        """
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        def cb(res):
            res['nodes'] = Types.Node.safe_create_from_list(res['nodes'])
            self.chrome.emit('DOM.getFlattenedDocument', res)
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        self.chrome.send('DOM.getFlattenedDocument', params=msg_dict, cb=cb)


    def getNodeForLocation(self, x, y, includeUserAgentShadowDOM):
        """
        :param x: X coordinate.
        :type x: int
        :param y: Y coordinate.
        :type y: int
        :param includeUserAgentShadowDOM: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        def cb(res):
            self.chrome.emit('DOM.getNodeForLocation', res)
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        self.chrome.send('DOM.getNodeForLocation', params=msg_dict, cb=cb)


    def getOuterHTML(self, nodeId, backendNodeId, objectId):
        """
        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        def cb(res):
            self.chrome.emit('DOM.getOuterHTML', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.getOuterHTML', params=msg_dict, cb=cb)


    def getRelayoutBoundary(self, nodeId):
        """
        :param nodeId: Id of the node.
        :type nodeId: int
        """
        def cb(res):
            self.chrome.emit('DOM.getRelayoutBoundary', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.getRelayoutBoundary', params=msg_dict, cb=cb)


    def getSearchResults(self, searchId, fromIndex, toIndex):
        """
        :param searchId: Unique search session identifier.
        :type searchId: str
        :param fromIndex: Start index of the search result to be returned.
        :type fromIndex: int
        :param toIndex: End index of the search result to be returned.
        :type toIndex: int
        """
        def cb(res):
            self.chrome.emit('DOM.getSearchResults', res)
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        if fromIndex is not None:
            msg_dict['fromIndex'] = fromIndex
        if toIndex is not None:
            msg_dict['toIndex'] = toIndex
        self.chrome.send('DOM.getSearchResults', params=msg_dict, cb=cb)


    def hideHighlight(self):
        self.chrome.send('DOM.hideHighlight')


    def highlightNode(self):
        self.chrome.send('DOM.highlightNode')


    def highlightRect(self):
        self.chrome.send('DOM.highlightRect')


    def markUndoableState(self):
        self.chrome.send('DOM.markUndoableState')


    def moveTo(self, nodeId, targetNodeId, insertBeforeNodeId):
        """
        :param nodeId: Id of the node to move.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the moved node into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop node before this one (if absent, the moved node becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        def cb(res):
            self.chrome.emit('DOM.moveTo', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        self.chrome.send('DOM.moveTo', params=msg_dict, cb=cb)


    def performSearch(self, query, includeUserAgentShadowDOM):
        """
        :param query: Plain text or query selector or XPath search query.
        :type query: str
        :param includeUserAgentShadowDOM: True to search in user agent shadow DOM.
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        def cb(res):
            self.chrome.emit('DOM.performSearch', res)
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        self.chrome.send('DOM.performSearch', params=msg_dict, cb=cb)


    def pushNodeByPathToFrontend(self, path):
        """
        :param path: Path to node in the proprietary format.
        :type path: str
        """
        def cb(res):
            self.chrome.emit('DOM.pushNodeByPathToFrontend', res)
        msg_dict = dict()
        if path is not None:
            msg_dict['path'] = path
        self.chrome.send('DOM.pushNodeByPathToFrontend', params=msg_dict, cb=cb)


    def pushNodesByBackendIdsToFrontend(self, backendNodeIds):
        """
        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        def cb(res):
            self.chrome.emit('DOM.pushNodesByBackendIdsToFrontend', res)
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict['backendNodeIds'] = backendNodeIds
        self.chrome.send('DOM.pushNodesByBackendIdsToFrontend', params=msg_dict, cb=cb)


    def querySelector(self, nodeId, selector):
        """
        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        def cb(res):
            self.chrome.emit('DOM.querySelector', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('DOM.querySelector', params=msg_dict, cb=cb)


    def querySelectorAll(self, nodeId, selector):
        """
        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        def cb(res):
            self.chrome.emit('DOM.querySelectorAll', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('DOM.querySelectorAll', params=msg_dict, cb=cb)


    def redo(self):
        self.chrome.send('DOM.redo')


    def removeAttribute(self, nodeId, name):
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


    def removeNode(self, nodeId):
        """
        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.removeNode', params=msg_dict)


    def requestChildNodes(self, nodeId, depth, pierce):
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


    def requestNode(self, objectId):
        """
        :param objectId: JavaScript object id to convert into node.
        :type objectId: str
        """
        def cb(res):
            self.chrome.emit('DOM.requestNode', res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('DOM.requestNode', params=msg_dict, cb=cb)


    def resolveNode(self, nodeId, backendNodeId, objectGroup):
        """
        :param nodeId: Id of the node to resolve.
        :type nodeId: Optional[int]
        :param backendNodeId: Backend identifier of the node to resolve.
        :type backendNodeId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        def cb(res):
            res['object'] = Runtime.RemoteObject.safe_create(res['object'])
            self.chrome.emit('DOM.resolveNode', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        self.chrome.send('DOM.resolveNode', params=msg_dict, cb=cb)


    def setAttributeValue(self, nodeId, name, value):
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


    def setAttributesAsText(self, nodeId, text, name):
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


    def setFileInputFiles(self, files, nodeId, backendNodeId, objectId):
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


    def setInspectedNode(self, nodeId):
        """
        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('DOM.setInspectedNode', params=msg_dict)


    def setNodeName(self, nodeId, name):
        """
        :param nodeId: Id of the node to set name for.
        :type nodeId: int
        :param name: New node's name.
        :type name: str
        """
        def cb(res):
            self.chrome.emit('DOM.setNodeName', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if name is not None:
            msg_dict['name'] = name
        self.chrome.send('DOM.setNodeName', params=msg_dict, cb=cb)


    def setNodeValue(self, nodeId, value):
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


    def setOuterHTML(self, nodeId, outerHTML):
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


    def undo(self):
        self.chrome.send('DOM.undo')


    def getFrameOwner(self, frameId):
        """
        :param frameId: The frameId
        :type frameId: str
        """
        def cb(res):
            self.chrome.emit('DOM.getFrameOwner', res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('DOM.getFrameOwner', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

