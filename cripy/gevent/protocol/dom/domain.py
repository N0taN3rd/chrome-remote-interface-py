from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.dom import events as Events
from cripy.gevent.protocol.dom import types as Types

__all__ = ["DOM"]


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

    events = Events.DOM_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new DOM object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def collectClassNamesFromSubtree(self, nodeId):
        """
        Collects class names for the node with given id and all of it's child nodes.

        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('DOM.collectClassNamesFromSubtree', msg_dict)
        res = wres.get()
        return res

    def copyTo(self, nodeId, targetNodeId, insertBeforeNodeId=None):
        """
        Creates a deep copy of the specified node and places it into the target container before the
given anchor.

        :param nodeId: Id of the node to copy.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the copy into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop the copy before this node (if absent, the copy becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        wres = self.chrome.send('DOM.copyTo', msg_dict)
        res = wres.get()
        return res

    def describeNode(self, nodeId=None, backendNodeId=None, objectId=None, depth=None, pierce=None):
        """
        Describes node given its id, does not require domain to be enabled. Does not start tracking any
objects, can be used for automation.

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
        wres = self.chrome.send('DOM.describeNode', msg_dict)
        res = wres.get()
        res['node'] = Types.Node.safe_create(res['node'])
        return res

    def disable(self):
        """
        Disables DOM agent for the given page.
        """
        wres = self.chrome.send('DOM.disable')
        return wres.get()

    def discardSearchResults(self, searchId):
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer
be called for that search.

        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        wres = self.chrome.send('DOM.discardSearchResults', msg_dict)
        return wres.get()

    def enable(self):
        """
        Enables DOM agent for the given page.
        """
        wres = self.chrome.send('DOM.enable')
        return wres.get()

    def focus(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Focuses the given element.

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
        wres = self.chrome.send('DOM.focus', msg_dict)
        return wres.get()

    def getAttributes(self, nodeId):
        """
        Returns attributes for the specified node.

        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('DOM.getAttributes', msg_dict)
        res = wres.get()
        return res

    def getBoxModel(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Returns boxes for the given node.

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
        wres = self.chrome.send('DOM.getBoxModel', msg_dict)
        res = wres.get()
        res['model'] = Types.BoxModel.safe_create(res['model'])
        return res

    def getDocument(self, depth=None, pierce=None):
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        wres = self.chrome.send('DOM.getDocument', msg_dict)
        res = wres.get()
        res['root'] = Types.Node.safe_create(res['root'])
        return res

    def getFlattenedDocument(self, depth=None, pierce=None):
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if depth is not None:
            msg_dict['depth'] = depth
        if pierce is not None:
            msg_dict['pierce'] = pierce
        wres = self.chrome.send('DOM.getFlattenedDocument', msg_dict)
        res = wres.get()
        res['nodes'] = Types.Node.safe_create_from_list(res['nodes'])
        return res

    def getNodeForLocation(self, x, y, includeUserAgentShadowDOM=None):
        """
        Returns node id at given location.

        :param x: X coordinate.
        :type x: int
        :param y: Y coordinate.
        :type y: int
        :param includeUserAgentShadowDOM: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        msg_dict = dict()
        if x is not None:
            msg_dict['x'] = x
        if y is not None:
            msg_dict['y'] = y
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        wres = self.chrome.send('DOM.getNodeForLocation', msg_dict)
        res = wres.get()
        return res

    def getOuterHTML(self, nodeId=None, backendNodeId=None, objectId=None):
        """
        Returns node's HTML markup.

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
        wres = self.chrome.send('DOM.getOuterHTML', msg_dict)
        res = wres.get()
        return res

    def getRelayoutBoundary(self, nodeId):
        """
        Returns the id of the nearest ancestor that is a relayout boundary.

        :param nodeId: Id of the node.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('DOM.getRelayoutBoundary', msg_dict)
        res = wres.get()
        return res

    def getSearchResults(self, searchId, fromIndex, toIndex):
        """
        Returns search results from given `fromIndex` to given `toIndex` from the search with the given
identifier.

        :param searchId: Unique search session identifier.
        :type searchId: str
        :param fromIndex: Start index of the search result to be returned.
        :type fromIndex: int
        :param toIndex: End index of the search result to be returned.
        :type toIndex: int
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        if fromIndex is not None:
            msg_dict['fromIndex'] = fromIndex
        if toIndex is not None:
            msg_dict['toIndex'] = toIndex
        wres = self.chrome.send('DOM.getSearchResults', msg_dict)
        res = wres.get()
        return res

    def hideHighlight(self):
        """
        Hides any highlight.
        """
        wres = self.chrome.send('DOM.hideHighlight')
        return wres.get()

    def highlightNode(self):
        """
        Highlights DOM node.
        """
        wres = self.chrome.send('DOM.highlightNode')
        return wres.get()

    def highlightRect(self):
        """
        Highlights given rectangle.
        """
        wres = self.chrome.send('DOM.highlightRect')
        return wres.get()

    def markUndoableState(self):
        """
        Marks last undoable state.
        """
        wres = self.chrome.send('DOM.markUndoableState')
        return wres.get()

    def moveTo(self, nodeId, targetNodeId, insertBeforeNodeId=None):
        """
        Moves node into the new container, places it before the given anchor.

        :param nodeId: Id of the node to move.
        :type nodeId: int
        :param targetNodeId: Id of the element to drop the moved node into.
        :type targetNodeId: int
        :param insertBeforeNodeId: Drop node before this one (if absent, the moved node becomes the last child of `targetNodeId`).
        :type insertBeforeNodeId: Optional[int]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if targetNodeId is not None:
            msg_dict['targetNodeId'] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict['insertBeforeNodeId'] = insertBeforeNodeId
        wres = self.chrome.send('DOM.moveTo', msg_dict)
        res = wres.get()
        return res

    def performSearch(self, query, includeUserAgentShadowDOM=None):
        """
        Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
`cancelSearch` to end this search session.

        :param query: Plain text or query selector or XPath search query.
        :type query: str
        :param includeUserAgentShadowDOM: True to search in user agent shadow DOM.
        :type includeUserAgentShadowDOM: Optional[bool]
        """
        msg_dict = dict()
        if query is not None:
            msg_dict['query'] = query
        if includeUserAgentShadowDOM is not None:
            msg_dict['includeUserAgentShadowDOM'] = includeUserAgentShadowDOM
        wres = self.chrome.send('DOM.performSearch', msg_dict)
        res = wres.get()
        return res

    def pushNodeByPathToFrontend(self, path):
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath

        :param path: Path to node in the proprietary format.
        :type path: str
        """
        msg_dict = dict()
        if path is not None:
            msg_dict['path'] = path
        wres = self.chrome.send('DOM.pushNodeByPathToFrontend', msg_dict)
        res = wres.get()
        return res

    def pushNodesByBackendIdsToFrontend(self, backendNodeIds):
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.

        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict['backendNodeIds'] = backendNodeIds
        wres = self.chrome.send('DOM.pushNodesByBackendIdsToFrontend', msg_dict)
        res = wres.get()
        return res

    def querySelector(self, nodeId, selector):
        """
        Executes `querySelector` on a given node.

        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        wres = self.chrome.send('DOM.querySelector', msg_dict)
        res = wres.get()
        return res

    def querySelectorAll(self, nodeId, selector):
        """
        Executes `querySelectorAll` on a given node.

        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if selector is not None:
            msg_dict['selector'] = selector
        wres = self.chrome.send('DOM.querySelectorAll', msg_dict)
        res = wres.get()
        return res

    def redo(self):
        """
        Re-does the last undone action.
        """
        wres = self.chrome.send('DOM.redo')
        return wres.get()

    def removeAttribute(self, nodeId, name):
        """
        Removes attribute with given name from an element with given id.

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
        wres = self.chrome.send('DOM.removeAttribute', msg_dict)
        return wres.get()

    def removeNode(self, nodeId):
        """
        Removes node with given id.

        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('DOM.removeNode', msg_dict)
        return wres.get()

    def requestChildNodes(self, nodeId, depth=None, pierce=None):
        """
        Requests that children of the node with given id are returned to the caller in form of
`setChildNodes` events where not only immediate children are retrieved, but all children down to
the specified depth.

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
        wres = self.chrome.send('DOM.requestChildNodes', msg_dict)
        return wres.get()

    def requestNode(self, objectId):
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All
nodes that form the path from the node to the root are also sent to the client as a series of
`setChildNodes` notifications.

        :param objectId: JavaScript object id to convert into node.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        wres = self.chrome.send('DOM.requestNode', msg_dict)
        res = wres.get()
        return res

    def resolveNode(self, nodeId=None, backendNodeId=None, objectGroup=None):
        """
        Resolves the JavaScript node object for a given NodeId or BackendNodeId.

        :param nodeId: Id of the node to resolve.
        :type nodeId: Optional[int]
        :param backendNodeId: Backend identifier of the node to resolve.
        :type backendNodeId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if backendNodeId is not None:
            msg_dict['backendNodeId'] = backendNodeId
        if objectGroup is not None:
            msg_dict['objectGroup'] = objectGroup
        wres = self.chrome.send('DOM.resolveNode', msg_dict)
        res = wres.get()
        res['object'] = Runtime.RemoteObject.safe_create(res['object'])
        return res

    def setAttributeValue(self, nodeId, name, value):
        """
        Sets attribute for an element with given id.

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
        wres = self.chrome.send('DOM.setAttributeValue', msg_dict)
        return wres.get()

    def setAttributesAsText(self, nodeId, text, name=None):
        """
        Sets attributes on element with given id. This method is useful when user edits some existing
attribute value and types in several attribute name/value pairs.

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
        wres = self.chrome.send('DOM.setAttributesAsText', msg_dict)
        return wres.get()

    def setFileInputFiles(self, files, nodeId=None, backendNodeId=None, objectId=None):
        """
        Sets files for the given file input element.

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
        wres = self.chrome.send('DOM.setFileInputFiles', msg_dict)
        return wres.get()

    def setInspectedNode(self, nodeId):
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('DOM.setInspectedNode', msg_dict)
        return wres.get()

    def setNodeName(self, nodeId, name):
        """
        Sets node name for a node with given id.

        :param nodeId: Id of the node to set name for.
        :type nodeId: int
        :param name: New node's name.
        :type name: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if name is not None:
            msg_dict['name'] = name
        wres = self.chrome.send('DOM.setNodeName', msg_dict)
        res = wres.get()
        return res

    def setNodeValue(self, nodeId, value):
        """
        Sets node value for a node with given id.

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
        wres = self.chrome.send('DOM.setNodeValue', msg_dict)
        return wres.get()

    def setOuterHTML(self, nodeId, outerHTML):
        """
        Sets node HTML markup, returns new node id.

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
        wres = self.chrome.send('DOM.setOuterHTML', msg_dict)
        return wres.get()

    def undo(self):
        """
        Undoes the last performed action.
        """
        wres = self.chrome.send('DOM.undo')
        return wres.get()

    def getFrameOwner(self, frameId):
        """
        Returns iframe node that owns iframe with the given domain.

        :param frameId: The frameId
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        wres = self.chrome.send('DOM.getFrameOwner', msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.DOM_EVENTS_TO_CLASS

