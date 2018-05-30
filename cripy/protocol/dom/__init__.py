from typing import Any, List, Optional, Union
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.page import types as Page
from cripy.protocol.dom import events as Events
from cripy.protocol.dom import types as Types


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

    async def collectClassNamesFromSubtree(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('DOM.collectClassNamesFromSubtree', msg_dict)
        return res

    async def copyTo(self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.copyTo', msg_dict)
        return res

    async def describeNode(self, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.describeNode', msg_dict)
        res['node'] = Types.Node.safe_create(res['node'])
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.disable')
        return res

    async def discardSearchResults(self, searchId: str) -> Optional[dict]:
        """
        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict['searchId'] = searchId
        res = await self.chrome.send('DOM.discardSearchResults', msg_dict)
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.enable')
        return res

    async def focus(self, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.focus', msg_dict)
        return res

    async def getAttributes(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('DOM.getAttributes', msg_dict)
        return res

    async def getBoxModel(self, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.getBoxModel', msg_dict)
        res['model'] = Types.BoxModel.safe_create(res['model'])
        return res

    async def getDocument(self, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.getDocument', msg_dict)
        res['root'] = Types.Node.safe_create(res['root'])
        return res

    async def getFlattenedDocument(self, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.getFlattenedDocument', msg_dict)
        res['nodes'] = Types.Node.safe_create_from_list(res['nodes'])
        return res

    async def getNodeForLocation(self, x: int, y: int, includeUserAgentShadowDOM: Optional[bool] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.getNodeForLocation', msg_dict)
        return res

    async def getOuterHTML(self, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.getOuterHTML', msg_dict)
        return res

    async def getRelayoutBoundary(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('DOM.getRelayoutBoundary', msg_dict)
        return res

    async def getSearchResults(self, searchId: str, fromIndex: int, toIndex: int) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.getSearchResults', msg_dict)
        return res

    async def hideHighlight(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.hideHighlight')
        return res

    async def highlightNode(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.highlightNode')
        return res

    async def highlightRect(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.highlightRect')
        return res

    async def markUndoableState(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.markUndoableState')
        return res

    async def moveTo(self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.moveTo', msg_dict)
        return res

    async def performSearch(self, query: str, includeUserAgentShadowDOM: Optional[bool] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.performSearch', msg_dict)
        return res

    async def pushNodeByPathToFrontend(self, path: str) -> Optional[dict]:
        """
        :param path: Path to node in the proprietary format.
        :type path: str
        """
        msg_dict = dict()
        if path is not None:
            msg_dict['path'] = path
        res = await self.chrome.send('DOM.pushNodeByPathToFrontend', msg_dict)
        return res

    async def pushNodesByBackendIdsToFrontend(self, backendNodeIds: List[int]) -> Optional[dict]:
        """
        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict['backendNodeIds'] = backendNodeIds
        res = await self.chrome.send('DOM.pushNodesByBackendIdsToFrontend', msg_dict)
        return res

    async def querySelector(self, nodeId: int, selector: str) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.querySelector', msg_dict)
        return res

    async def querySelectorAll(self, nodeId: int, selector: str) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.querySelectorAll', msg_dict)
        return res

    async def redo(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.redo')
        return res

    async def removeAttribute(self, nodeId: int, name: str) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.removeAttribute', msg_dict)
        return res

    async def removeNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('DOM.removeNode', msg_dict)
        return res

    async def requestChildNodes(self, nodeId: int, depth: Optional[int] = None, pierce: Optional[bool] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.requestChildNodes', msg_dict)
        return res

    async def requestNode(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: JavaScript object id to convert into node.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        res = await self.chrome.send('DOM.requestNode', msg_dict)
        return res

    async def resolveNode(self, nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectGroup: Optional[str] = None) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.resolveNode', msg_dict)
        res['object'] = Runtime.RemoteObject.safe_create(res['object'])
        return res

    async def setAttributeValue(self, nodeId: int, name: str, value: str) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.setAttributeValue', msg_dict)
        return res

    async def setAttributesAsText(self, nodeId: int, text: str, name: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.setAttributesAsText', msg_dict)
        return res

    async def setFileInputFiles(self, files: List[str], nodeId: Optional[int] = None, backendNodeId: Optional[int] = None, objectId: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.setFileInputFiles', msg_dict)
        return res

    async def setInspectedNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('DOM.setInspectedNode', msg_dict)
        return res

    async def setNodeName(self, nodeId: int, name: str) -> Optional[dict]:
        """
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
        res = await self.chrome.send('DOM.setNodeName', msg_dict)
        return res

    async def setNodeValue(self, nodeId: int, value: str) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.setNodeValue', msg_dict)
        return res

    async def setOuterHTML(self, nodeId: int, outerHTML: str) -> Optional[dict]:
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
        res = await self.chrome.send('DOM.setOuterHTML', msg_dict)
        return res

    async def undo(self) -> Optional[dict]:
        res = await self.chrome.send('DOM.undo')
        return res

    async def getFrameOwner(self, frameId: str) -> Optional[dict]:
        """
        :param frameId: The frameId
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        res = await self.chrome.send('DOM.getFrameOwner', msg_dict)
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

