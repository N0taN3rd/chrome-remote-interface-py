"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOM"]


@attr.dataclass(slots=True, cmp=False)
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

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def collectClassNamesFromSubtree(self, nodeId: int) -> Awaitable[Dict]:
        """
        Collects class names for the node with given id and all of it's child nodes.

        :param nodeId: Id of the node to collect class names.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("DOM.collectClassNamesFromSubtree", msg_dict)

    def copyTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.copyTo", msg_dict)

    def describeNode(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        depth: Optional[int] = None,
        pierce: Optional[bool] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.describeNode", msg_dict)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables DOM agent for the given page.
        """
        return self.client.send("DOM.disable")

    def discardSearchResults(self, searchId: str) -> Awaitable[Dict]:
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer
be called for that search.

        :param searchId: Unique search session identifier.
        :type searchId: str
        """
        msg_dict = dict()
        if searchId is not None:
            msg_dict["searchId"] = searchId
        return self.client.send("DOM.discardSearchResults", msg_dict)

    def enable(self) -> Awaitable[Dict]:
        """
        Enables DOM agent for the given page.
        """
        return self.client.send("DOM.enable")

    def focus(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.focus", msg_dict)

    def getAttributes(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns attributes for the specified node.

        :param nodeId: Id of the node to retrieve attibutes for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("DOM.getAttributes", msg_dict)

    def getBoxModel(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getBoxModel", msg_dict)

    def getContentQuads(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getContentQuads", msg_dict)

    def getDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getDocument", msg_dict)

    def getFlattenedDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getFlattenedDocument", msg_dict)

    def getNodeForLocation(
        self, x: int, y: int, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
either returned or not.

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
        return self.client.send("DOM.getNodeForLocation", msg_dict)

    def getOuterHTML(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getOuterHTML", msg_dict)

    def getRelayoutBoundary(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the id of the nearest ancestor that is a relayout boundary.

        :param nodeId: Id of the node.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("DOM.getRelayoutBoundary", msg_dict)

    def getSearchResults(
        self, searchId: str, fromIndex: int, toIndex: int
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.getSearchResults", msg_dict)

    def hideHighlight(self) -> Awaitable[Dict]:
        """
        Hides any highlight.
        """
        return self.client.send("DOM.hideHighlight")

    def highlightNode(self) -> Awaitable[Dict]:
        """
        Highlights DOM node.
        """
        return self.client.send("DOM.highlightNode")

    def highlightRect(self) -> Awaitable[Dict]:
        """
        Highlights given rectangle.
        """
        return self.client.send("DOM.highlightRect")

    def markUndoableState(self) -> Awaitable[Dict]:
        """
        Marks last undoable state.
        """
        return self.client.send("DOM.markUndoableState")

    def moveTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.moveTo", msg_dict)

    def performSearch(
        self, query: str, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.performSearch", msg_dict)

    def pushNodeByPathToFrontend(self, path: str) -> Awaitable[Dict]:
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath

        :param path: Path to node in the proprietary format.
        :type path: str
        """
        msg_dict = dict()
        if path is not None:
            msg_dict["path"] = path
        return self.client.send("DOM.pushNodeByPathToFrontend", msg_dict)

    def pushNodesByBackendIdsToFrontend(
        self, backendNodeIds: List[int]
    ) -> Awaitable[Dict]:
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.

        :param backendNodeIds: The array of backend node ids.
        :type backendNodeIds: List[int]
        """
        msg_dict = dict()
        if backendNodeIds is not None:
            msg_dict["backendNodeIds"] = backendNodeIds
        return self.client.send("DOM.pushNodesByBackendIdsToFrontend", msg_dict)

    def querySelector(self, nodeId: int, selector: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.querySelector", msg_dict)

    def querySelectorAll(self, nodeId: int, selector: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.querySelectorAll", msg_dict)

    def redo(self) -> Awaitable[Dict]:
        """
        Re-does the last undone action.
        """
        return self.client.send("DOM.redo")

    def removeAttribute(self, nodeId: int, name: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.removeAttribute", msg_dict)

    def removeNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Removes node with given id.

        :param nodeId: Id of the node to remove.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("DOM.removeNode", msg_dict)

    def requestChildNodes(
        self, nodeId: int, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.requestChildNodes", msg_dict)

    def requestNode(self, objectId: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.requestNode", msg_dict)

    def resolveNode(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectGroup: Optional[str] = None,
        executionContextId: Optional[int] = None,
    ) -> Awaitable[Dict]:
        """
        Resolves the JavaScript node object for a given NodeId or BackendNodeId.

        :param nodeId: Id of the node to resolve.
        :type nodeId: Optional[int]
        :param backendNodeId: Backend identifier of the node to resolve.
        :type backendNodeId: Optional[int]
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :type objectGroup: Optional[str]
        :param executionContextId: Execution context in which to resolve the node.
        :type executionContextId: Optional[int]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectGroup is not None:
            msg_dict["objectGroup"] = objectGroup
        if executionContextId is not None:
            msg_dict["executionContextId"] = executionContextId
        return self.client.send("DOM.resolveNode", msg_dict)

    def setAttributeValue(self, nodeId: int, name: str, value: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setAttributeValue", msg_dict)

    def setAttributesAsText(
        self, nodeId: int, text: str, name: Optional[str] = None
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setAttributesAsText", msg_dict)

    def setFileInputFiles(
        self,
        files: List[str],
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setFileInputFiles", msg_dict)

    def getFileInfo(self, objectId: str) -> Awaitable[Dict]:
        """
        Returns file information for the given
File wrapper.

        :param objectId: JavaScript object id of the node wrapper.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        return self.client.send("DOM.getFileInfo", msg_dict)

    def setInspectedNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).

        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("DOM.setInspectedNode", msg_dict)

    def setNodeName(self, nodeId: int, name: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setNodeName", msg_dict)

    def setNodeValue(self, nodeId: int, value: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setNodeValue", msg_dict)

    def setOuterHTML(self, nodeId: int, outerHTML: str) -> Awaitable[Dict]:
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
        return self.client.send("DOM.setOuterHTML", msg_dict)

    def undo(self) -> Awaitable[Dict]:
        """
        Undoes the last performed action.
        """
        return self.client.send("DOM.undo")

    def getFrameOwner(self, frameId: str) -> Awaitable[Dict]:
        """
        Returns iframe node that owns iframe with the given domain.

        :param frameId: The frameId
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        return self.client.send("DOM.getFrameOwner", msg_dict)

    def attributeModified(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when `Element`'s attribute is modified.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.attributeModified", _cb)

            return future

        self.client.on("DOM.attributeModified", cb)
        return lambda: self.client.remove_listener("DOM.attributeModified", cb)

    def attributeRemoved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when `Element`'s attribute is removed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.attributeRemoved", _cb)

            return future

        self.client.on("DOM.attributeRemoved", cb)
        return lambda: self.client.remove_listener("DOM.attributeRemoved", cb)

    def characterDataModified(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Mirrors `DOMCharacterDataModified` event.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.characterDataModified", _cb)

            return future

        self.client.on("DOM.characterDataModified", cb)
        return lambda: self.client.remove_listener("DOM.characterDataModified", cb)

    def childNodeCountUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when `Container`'s child node count has changed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.childNodeCountUpdated", _cb)

            return future

        self.client.on("DOM.childNodeCountUpdated", cb)
        return lambda: self.client.remove_listener("DOM.childNodeCountUpdated", cb)

    def childNodeInserted(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Mirrors `DOMNodeInserted` event.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.childNodeInserted", _cb)

            return future

        self.client.on("DOM.childNodeInserted", cb)
        return lambda: self.client.remove_listener("DOM.childNodeInserted", cb)

    def childNodeRemoved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Mirrors `DOMNodeRemoved` event.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.childNodeRemoved", _cb)

            return future

        self.client.on("DOM.childNodeRemoved", cb)
        return lambda: self.client.remove_listener("DOM.childNodeRemoved", cb)

    def distributedNodesUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Called when distrubution is changed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.distributedNodesUpdated", _cb)

            return future

        self.client.on("DOM.distributedNodesUpdated", cb)
        return lambda: self.client.remove_listener("DOM.distributedNodesUpdated", cb)

    def documentUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when `Document` has been totally updated. Node ids are no longer valid.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.documentUpdated", _cb)

            return future

        self.client.on("DOM.documentUpdated", cb)
        return lambda: self.client.remove_listener("DOM.documentUpdated", cb)

    def inlineStyleInvalidated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when `Element`'s inline style is modified via a CSS property modification.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.inlineStyleInvalidated", _cb)

            return future

        self.client.on("DOM.inlineStyleInvalidated", cb)
        return lambda: self.client.remove_listener("DOM.inlineStyleInvalidated", cb)

    def pseudoElementAdded(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Called when a pseudo element is added to an element.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.pseudoElementAdded", _cb)

            return future

        self.client.on("DOM.pseudoElementAdded", cb)
        return lambda: self.client.remove_listener("DOM.pseudoElementAdded", cb)

    def pseudoElementRemoved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Called when a pseudo element is removed from an element.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.pseudoElementRemoved", _cb)

            return future

        self.client.on("DOM.pseudoElementRemoved", cb)
        return lambda: self.client.remove_listener("DOM.pseudoElementRemoved", cb)

    def setChildNodes(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when backend wants to provide client with the missing DOM structure. This happens upon
        most of the calls requesting node ids.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.setChildNodes", _cb)

            return future

        self.client.on("DOM.setChildNodes", cb)
        return lambda: self.client.remove_listener("DOM.setChildNodes", cb)

    def shadowRootPopped(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Called when shadow root is popped from the element.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.shadowRootPopped", _cb)

            return future

        self.client.on("DOM.shadowRootPopped", cb)
        return lambda: self.client.remove_listener("DOM.shadowRootPopped", cb)

    def shadowRootPushed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Called when shadow root is pushed into the element.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("DOM.shadowRootPushed", _cb)

            return future

        self.client.on("DOM.shadowRootPushed", cb)
        return lambda: self.client.remove_listener("DOM.shadowRootPushed", cb)
