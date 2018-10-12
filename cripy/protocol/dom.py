# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

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

    dependencies: ClassVar[List[str]] = ["Runtime"]

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def collectClassNamesFromSubtree(self, nodeId: int) -> Optional[dict]:
        """
        Collects class names for the node with given id and all of it's child nodes.

        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("DOM.collectClassNamesFromSubtree", msg_dict)
        return res

    async def copyTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if targetNodeId is not None:
            msg_dict["targetNodeId"] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict["insertBeforeNodeId"] = insertBeforeNodeId
        res = await self.client.send("DOM.copyTo", msg_dict)
        return res

    async def describeNode(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        depth: Optional[int] = None,
        pierce: Optional[bool] = None,
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if depth is not None:
            msg_dict["depth"] = depth
        if pierce is not None:
            msg_dict["pierce"] = pierce
        res = await self.client.send("DOM.describeNode", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables DOM agent for the given page.
        """
        res = await self.client.send("DOM.disable")
        return res

    async def discardSearchResults(self, searchId: str) -> Optional[dict]:
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer
be called for that search.

        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict["searchId"] = searchId
        res = await self.client.send("DOM.discardSearchResults", msg_dict)
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables DOM agent for the given page.
        """
        res = await self.client.send("DOM.enable")
        return res

    async def focus(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.focus", msg_dict)
        return res

    async def getAttributes(self, nodeId: int) -> Optional[dict]:
        """
        Returns attributes for the specified node.

        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("DOM.getAttributes", msg_dict)
        return res

    async def getBoxModel(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.getBoxModel", msg_dict)
        return res

    async def getContentQuads(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Returns quads that describe node position on the page. This method
might return multiple quads for inline nodes.

        :param nodeId: Identifier of the node.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: Optional[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.getContentQuads", msg_dict)
        return res

    async def getDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Optional[dict]:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if depth is not None:
            msg_dict["depth"] = depth
        if pierce is not None:
            msg_dict["pierce"] = pierce
        res = await self.client.send("DOM.getDocument", msg_dict)
        return res

    async def getFlattenedDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Optional[dict]:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
        :type depth: Optional[int]
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
        :type pierce: Optional[bool]
        """
        msg_dict = dict()
        if depth is not None:
            msg_dict["depth"] = depth
        if pierce is not None:
            msg_dict["pierce"] = pierce
        res = await self.client.send("DOM.getFlattenedDocument", msg_dict)
        return res

    async def getNodeForLocation(
        self, x: int, y: int, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Optional[dict]:
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
            msg_dict["x"] = x
        if y is not None:
            msg_dict["y"] = y
        if includeUserAgentShadowDOM is not None:
            msg_dict["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        res = await self.client.send("DOM.getNodeForLocation", msg_dict)
        return res

    async def getOuterHTML(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.getOuterHTML", msg_dict)
        return res

    async def getRelayoutBoundary(self, nodeId: int) -> Optional[dict]:
        """
        Returns the id of the nearest ancestor that is a relayout boundary.

        :param nodeId: Id of the node.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("DOM.getRelayoutBoundary", msg_dict)
        return res

    async def getSearchResults(
        self, searchId: str, fromIndex: int, toIndex: int
    ) -> Optional[dict]:
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
            msg_dict["searchId"] = searchId
        if fromIndex is not None:
            msg_dict["fromIndex"] = fromIndex
        if toIndex is not None:
            msg_dict["toIndex"] = toIndex
        res = await self.client.send("DOM.getSearchResults", msg_dict)
        return res

    async def hideHighlight(self) -> Optional[dict]:
        """
        Hides any highlight.
        """
        res = await self.client.send("DOM.hideHighlight")
        return res

    async def highlightNode(self) -> Optional[dict]:
        """
        Highlights DOM node.
        """
        res = await self.client.send("DOM.highlightNode")
        return res

    async def highlightRect(self) -> Optional[dict]:
        """
        Highlights given rectangle.
        """
        res = await self.client.send("DOM.highlightRect")
        return res

    async def markUndoableState(self) -> Optional[dict]:
        """
        Marks last undoable state.
        """
        res = await self.client.send("DOM.markUndoableState")
        return res

    async def moveTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if targetNodeId is not None:
            msg_dict["targetNodeId"] = targetNodeId
        if insertBeforeNodeId is not None:
            msg_dict["insertBeforeNodeId"] = insertBeforeNodeId
        res = await self.client.send("DOM.moveTo", msg_dict)
        return res

    async def performSearch(
        self, query: str, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Optional[dict]:
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
            msg_dict["query"] = query
        if includeUserAgentShadowDOM is not None:
            msg_dict["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        res = await self.client.send("DOM.performSearch", msg_dict)
        return res

    async def pushNodeByPathToFrontend(self, path: str) -> Optional[dict]:
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath

        :param path: Path to node in the proprietary format.
        :type path: str
        """
        msg_dict = dict()
        if path is not None:
            msg_dict["path"] = path
        res = await self.client.send("DOM.pushNodeByPathToFrontend", msg_dict)
        return res

    async def pushNodesByBackendIdsToFrontend(
        self, backendNodeIds: List[int]
    ) -> Optional[dict]:
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.

        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict["backendNodeIds"] = backendNodeIds
        res = await self.client.send("DOM.pushNodesByBackendIdsToFrontend", msg_dict)
        return res

    async def querySelector(self, nodeId: int, selector: str) -> Optional[dict]:
        """
        Executes `querySelector` on a given node.

        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if selector is not None:
            msg_dict["selector"] = selector
        res = await self.client.send("DOM.querySelector", msg_dict)
        return res

    async def querySelectorAll(self, nodeId: int, selector: str) -> Optional[dict]:
        """
        Executes `querySelectorAll` on a given node.

        :param nodeId: Id of the node to query upon.
        :type nodeId: int
        :param selector: Selector string.
        :type selector: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if selector is not None:
            msg_dict["selector"] = selector
        res = await self.client.send("DOM.querySelectorAll", msg_dict)
        return res

    async def redo(self) -> Optional[dict]:
        """
        Re-does the last undone action.
        """
        res = await self.client.send("DOM.redo")
        return res

    async def removeAttribute(self, nodeId: int, name: str) -> Optional[dict]:
        """
        Removes attribute with given name from an element with given id.

        :param nodeId: Id of the element to remove attribute from.
        :type nodeId: int
        :param name: Name of the attribute to remove.
        :type name: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if name is not None:
            msg_dict["name"] = name
        res = await self.client.send("DOM.removeAttribute", msg_dict)
        return res

    async def removeNode(self, nodeId: int) -> Optional[dict]:
        """
        Removes node with given id.

        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("DOM.removeNode", msg_dict)
        return res

    async def requestChildNodes(
        self, nodeId: int, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if depth is not None:
            msg_dict["depth"] = depth
        if pierce is not None:
            msg_dict["pierce"] = pierce
        res = await self.client.send("DOM.requestChildNodes", msg_dict)
        return res

    async def requestNode(self, objectId: str) -> Optional[dict]:
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All
nodes that form the path from the node to the root are also sent to the client as a series of
`setChildNodes` notifications.

        :param objectId: JavaScript object id to convert into node.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.requestNode", msg_dict)
        return res

    async def resolveNode(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectGroup: Optional[str] = None,
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        res = await self.client.send("DOM.resolveNode", msg_dict)
        return res

    async def setAttributeValue(
        self, nodeId: int, name: str, value: str
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if name is not None:
            msg_dict["name"] = name
        if value is not None:
            msg_dict["value"] = value
        res = await self.client.send("DOM.setAttributeValue", msg_dict)
        return res

    async def setAttributesAsText(
        self, nodeId: int, text: str, name: Optional[str] = None
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if text is not None:
            msg_dict["text"] = text
        if name is not None:
            msg_dict["name"] = name
        res = await self.client.send("DOM.setAttributesAsText", msg_dict)
        return res

    async def setFileInputFiles(
        self,
        files: List[str],
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Optional[dict]:
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
            msg_dict["files"] = files
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("DOM.setFileInputFiles", msg_dict)
        return res

    async def setInspectedNode(self, nodeId: int) -> Optional[dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("DOM.setInspectedNode", msg_dict)
        return res

    async def setNodeName(self, nodeId: int, name: str) -> Optional[dict]:
        """
        Sets node name for a node with given id.

        :param nodeId: Id of the node to set name for.
        :type nodeId: int
        :param name: New node's name.
        :type name: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if name is not None:
            msg_dict["name"] = name
        res = await self.client.send("DOM.setNodeName", msg_dict)
        return res

    async def setNodeValue(self, nodeId: int, value: str) -> Optional[dict]:
        """
        Sets node value for a node with given id.

        :param nodeId: Id of the node to set value for.
        :type nodeId: int
        :param value: New node's value.
        :type value: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if value is not None:
            msg_dict["value"] = value
        res = await self.client.send("DOM.setNodeValue", msg_dict)
        return res

    async def setOuterHTML(self, nodeId: int, outerHTML: str) -> Optional[dict]:
        """
        Sets node HTML markup, returns new node id.

        :param nodeId: Id of the node to set markup for.
        :type nodeId: int
        :param outerHTML: Outer HTML markup to set.
        :type outerHTML: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if outerHTML is not None:
            msg_dict["outerHTML"] = outerHTML
        res = await self.client.send("DOM.setOuterHTML", msg_dict)
        return res

    async def undo(self) -> Optional[dict]:
        """
        Undoes the last performed action.
        """
        res = await self.client.send("DOM.undo")
        return res

    async def getFrameOwner(self, frameId: str) -> Optional[dict]:
        """
        Returns iframe node that owns iframe with the given domain.

        :param frameId: The frameId
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        res = await self.client.send("DOM.getFrameOwner", msg_dict)
        return res

    def attributeModified(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when `Element`'s attribute is modified.
        """
        if once:
            self.client.once("DOM.attributeModified", fn)
        else:
            self.client.on("DOM.attributeModified", fn)

    def attributeRemoved(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when `Element`'s attribute is removed.
        """
        if once:
            self.client.once("DOM.attributeRemoved", fn)
        else:
            self.client.on("DOM.attributeRemoved", fn)

    def characterDataModified(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Mirrors `DOMCharacterDataModified` event.
        """
        if once:
            self.client.once("DOM.characterDataModified", fn)
        else:
            self.client.on("DOM.characterDataModified", fn)

    def childNodeCountUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when `Container`'s child node count has changed.
        """
        if once:
            self.client.once("DOM.childNodeCountUpdated", fn)
        else:
            self.client.on("DOM.childNodeCountUpdated", fn)

    def childNodeInserted(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Mirrors `DOMNodeInserted` event.
        """
        if once:
            self.client.once("DOM.childNodeInserted", fn)
        else:
            self.client.on("DOM.childNodeInserted", fn)

    def childNodeRemoved(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Mirrors `DOMNodeRemoved` event.
        """
        if once:
            self.client.once("DOM.childNodeRemoved", fn)
        else:
            self.client.on("DOM.childNodeRemoved", fn)

    def distributedNodesUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Called when distrubution is changed.
        """
        if once:
            self.client.once("DOM.distributedNodesUpdated", fn)
        else:
            self.client.on("DOM.distributedNodesUpdated", fn)

    def documentUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when `Document` has been totally updated. Node ids are no longer valid.
        """
        if once:
            self.client.once("DOM.documentUpdated", fn)
        else:
            self.client.on("DOM.documentUpdated", fn)

    def inlineStyleInvalidated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when `Element`'s inline style is modified via a CSS property modification.
        """
        if once:
            self.client.once("DOM.inlineStyleInvalidated", fn)
        else:
            self.client.on("DOM.inlineStyleInvalidated", fn)

    def pseudoElementAdded(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Called when a pseudo element is added to an element.
        """
        if once:
            self.client.once("DOM.pseudoElementAdded", fn)
        else:
            self.client.on("DOM.pseudoElementAdded", fn)

    def pseudoElementRemoved(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Called when a pseudo element is removed from an element.
        """
        if once:
            self.client.once("DOM.pseudoElementRemoved", fn)
        else:
            self.client.on("DOM.pseudoElementRemoved", fn)

    def setChildNodes(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when backend wants to provide client with the missing DOM structure. This happens upon
        most of the calls requesting node ids.
        """
        if once:
            self.client.once("DOM.setChildNodes", fn)
        else:
            self.client.on("DOM.setChildNodes", fn)

    def shadowRootPopped(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Called when shadow root is popped from the element.
        """
        if once:
            self.client.once("DOM.shadowRootPopped", fn)
        else:
            self.client.on("DOM.shadowRootPopped", fn)

    def shadowRootPushed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Called when shadow root is pushed into the element.
        """
        if once:
            self.client.once("DOM.shadowRootPushed", fn)
        else:
            self.client.on("DOM.shadowRootPushed", fn)

    def __repr__(self):
        return f"DOM()"
