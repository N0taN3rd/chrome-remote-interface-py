"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOM"]


class DOM:
    """
    This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object
    that has an `id`. This `id` can be used to get additional information on the Node, resolve it into
    the JavaScript object wrapper, etc. It is important that client receives DOM events only for the
    nodes that are known to the client. Backend keeps track of the nodes that were sent to the client
    and never sends the same node twice. It is client's responsibility to collect information about
    the nodes that were sent to the client.<p>Note that `iframe` owner elements will return
    corresponding document elements as their child nodes.</p>
     
    Domain Dependencies: 
      * Runtime
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/DOM`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of DOM

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def collectClassNamesFromSubtree(self, nodeId: int) -> Awaitable[Dict]:
        """
        Collects class names for the node with given id and all of it's child nodes.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-collectClassNamesFromSubtree`

        :param nodeId: Id of the node to collect class names.
        :return: The results of the command
        """
        return self.client.send("DOM.collectClassNamesFromSubtree", {"nodeId": nodeId})

    def copyTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        Creates a deep copy of the specified node and places it into the target container before the
        given anchor.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-copyTo`

        :param nodeId: Id of the node to copy.
        :param targetNodeId: Id of the element to drop the copy into.
        :param insertBeforeNodeId: Drop the copy before this node (if absent, the copy becomes the last child of
         `targetNodeId`).
        :return: The results of the command
        """
        msg = {"nodeId": nodeId, "targetNodeId": targetNodeId}
        if insertBeforeNodeId is not None:
            msg["insertBeforeNodeId"] = insertBeforeNodeId
        return self.client.send("DOM.copyTo", msg)

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

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-describeNode`

        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
         entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
         (default is false).
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        if depth is not None:
            msg["depth"] = depth
        if pierce is not None:
            msg["pierce"] = pierce
        return self.client.send("DOM.describeNode", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables DOM agent for the given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-disable`

        :return: The results of the command
        """
        return self.client.send("DOM.disable", {})

    def discardSearchResults(self, searchId: str) -> Awaitable[Dict]:
        """
        Discards search results from the session with the given id. `getSearchResults` should no longer
        be called for that search.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-discardSearchResults`

        :param searchId: Unique search session identifier.
        :return: The results of the command
        """
        return self.client.send("DOM.discardSearchResults", {"searchId": searchId})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables DOM agent for the given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-enable`

        :return: The results of the command
        """
        return self.client.send("DOM.enable", {})

    def focus(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Focuses the given element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-focus`

        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        return self.client.send("DOM.focus", msg)

    def getAttributes(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns attributes for the specified node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getAttributes`

        :param nodeId: Id of the node to retrieve attibutes for.
        :return: The results of the command
        """
        return self.client.send("DOM.getAttributes", {"nodeId": nodeId})

    def getBoxModel(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Returns boxes for the given node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getBoxModel`

        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        return self.client.send("DOM.getBoxModel", msg)

    def getContentQuads(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Returns quads that describe node position on the page. This method
        might return multiple quads for inline nodes.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getContentQuads`

        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        return self.client.send("DOM.getContentQuads", msg)

    def getDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getDocument`

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
         entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
         (default is false).
        :return: The results of the command
        """
        msg = {}
        if depth is not None:
            msg["depth"] = depth
        if pierce is not None:
            msg["pierce"] = pierce
        return self.client.send("DOM.getDocument", msg)

    def getFlattenedDocument(
        self, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Returns the root DOM node (and optionally the subtree) to the caller.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getFlattenedDocument`

        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
         entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
         (default is false).
        :return: The results of the command
        """
        msg = {}
        if depth is not None:
            msg["depth"] = depth
        if pierce is not None:
            msg["pierce"] = pierce
        return self.client.send("DOM.getFlattenedDocument", msg)

    def getNodeForLocation(
        self, x: int, y: int, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
        either returned or not.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getNodeForLocation`

        :param x: X coordinate.
        :param y: Y coordinate.
        :param includeUserAgentShadowDOM: False to skip to the nearest non-UA shadow root ancestor (default: false).
        :return: The results of the command
        """
        msg = {"x": x, "y": y}
        if includeUserAgentShadowDOM is not None:
            msg["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        return self.client.send("DOM.getNodeForLocation", msg)

    def getOuterHTML(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Returns node's HTML markup.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getOuterHTML`

        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        return self.client.send("DOM.getOuterHTML", msg)

    def getRelayoutBoundary(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the id of the nearest ancestor that is a relayout boundary.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getRelayoutBoundary`

        :param nodeId: Id of the node.
        :return: The results of the command
        """
        return self.client.send("DOM.getRelayoutBoundary", {"nodeId": nodeId})

    def getSearchResults(
        self, searchId: str, fromIndex: int, toIndex: int
    ) -> Awaitable[Dict]:
        """
        Returns search results from given `fromIndex` to given `toIndex` from the search with the given
        identifier.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getSearchResults`

        :param searchId: Unique search session identifier.
        :param fromIndex: Start index of the search result to be returned.
        :param toIndex: End index of the search result to be returned.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.getSearchResults",
            {"searchId": searchId, "fromIndex": fromIndex, "toIndex": toIndex},
        )

    def hideHighlight(self) -> Awaitable[Dict]:
        """
        Hides any highlight.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-hideHighlight`

        :return: The results of the command
        """
        return self.client.send("DOM.hideHighlight", {})

    def highlightNode(self) -> Awaitable[Dict]:
        """
        Highlights DOM node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-highlightNode`

        :return: The results of the command
        """
        return self.client.send("DOM.highlightNode", {})

    def highlightRect(self) -> Awaitable[Dict]:
        """
        Highlights given rectangle.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-highlightRect`

        :return: The results of the command
        """
        return self.client.send("DOM.highlightRect", {})

    def markUndoableState(self) -> Awaitable[Dict]:
        """
        Marks last undoable state.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-markUndoableState`

        :return: The results of the command
        """
        return self.client.send("DOM.markUndoableState", {})

    def moveTo(
        self, nodeId: int, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        Moves node into the new container, places it before the given anchor.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-moveTo`

        :param nodeId: Id of the node to move.
        :param targetNodeId: Id of the element to drop the moved node into.
        :param insertBeforeNodeId: Drop node before this one (if absent, the moved node becomes the last child of
         `targetNodeId`).
        :return: The results of the command
        """
        msg = {"nodeId": nodeId, "targetNodeId": targetNodeId}
        if insertBeforeNodeId is not None:
            msg["insertBeforeNodeId"] = insertBeforeNodeId
        return self.client.send("DOM.moveTo", msg)

    def performSearch(
        self, query: str, includeUserAgentShadowDOM: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
        `cancelSearch` to end this search session.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-performSearch`

        :param query: Plain text or query selector or XPath search query.
        :param includeUserAgentShadowDOM: True to search in user agent shadow DOM.
        :return: The results of the command
        """
        msg = {"query": query}
        if includeUserAgentShadowDOM is not None:
            msg["includeUserAgentShadowDOM"] = includeUserAgentShadowDOM
        return self.client.send("DOM.performSearch", msg)

    def pushNodeByPathToFrontend(self, path: str) -> Awaitable[Dict]:
        """
        Requests that the node is sent to the caller given its path. // FIXME, use XPath

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-pushNodeByPathToFrontend`

        :param path: Path to node in the proprietary format.
        :return: The results of the command
        """
        return self.client.send("DOM.pushNodeByPathToFrontend", {"path": path})

    def pushNodesByBackendIdsToFrontend(
        self, backendNodeIds: List[int]
    ) -> Awaitable[Dict]:
        """
        Requests that a batch of nodes is sent to the caller given their backend node ids.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-pushNodesByBackendIdsToFrontend`

        :param backendNodeIds: The array of backend node ids.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.pushNodesByBackendIdsToFrontend", {"backendNodeIds": backendNodeIds}
        )

    def querySelector(self, nodeId: int, selector: str) -> Awaitable[Dict]:
        """
        Executes `querySelector` on a given node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelector`

        :param nodeId: Id of the node to query upon.
        :param selector: Selector string.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.querySelector", {"nodeId": nodeId, "selector": selector}
        )

    def querySelectorAll(self, nodeId: int, selector: str) -> Awaitable[Dict]:
        """
        Executes `querySelectorAll` on a given node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelectorAll`

        :param nodeId: Id of the node to query upon.
        :param selector: Selector string.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.querySelectorAll", {"nodeId": nodeId, "selector": selector}
        )

    def redo(self) -> Awaitable[Dict]:
        """
        Re-does the last undone action.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-redo`

        :return: The results of the command
        """
        return self.client.send("DOM.redo", {})

    def removeAttribute(self, nodeId: int, name: str) -> Awaitable[Dict]:
        """
        Removes attribute with given name from an element with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-removeAttribute`

        :param nodeId: Id of the element to remove attribute from.
        :param name: Name of the attribute to remove.
        :return: The results of the command
        """
        return self.client.send("DOM.removeAttribute", {"nodeId": nodeId, "name": name})

    def removeNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Removes node with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-removeNode`

        :param nodeId: Id of the node to remove.
        :return: The results of the command
        """
        return self.client.send("DOM.removeNode", {"nodeId": nodeId})

    def requestChildNodes(
        self, nodeId: int, depth: Optional[int] = None, pierce: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Requests that children of the node with given id are returned to the caller in form of
        `setChildNodes` events where not only immediate children are retrieved, but all children down to
        the specified depth.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-requestChildNodes`

        :param nodeId: Id of the node to get children for.
        :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
         entire subtree or provide an integer larger than 0.
        :param pierce: Whether or not iframes and shadow roots should be traversed when returning the sub-tree
         (default is false).
        :return: The results of the command
        """
        msg = {"nodeId": nodeId}
        if depth is not None:
            msg["depth"] = depth
        if pierce is not None:
            msg["pierce"] = pierce
        return self.client.send("DOM.requestChildNodes", msg)

    def requestNode(self, objectId: str) -> Awaitable[Dict]:
        """
        Requests that the node is sent to the caller given the JavaScript node object reference. All
        nodes that form the path from the node to the root are also sent to the client as a series of
        `setChildNodes` notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-requestNode`

        :param objectId: JavaScript object id to convert into node.
        :return: The results of the command
        """
        return self.client.send("DOM.requestNode", {"objectId": objectId})

    def resolveNode(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectGroup: Optional[str] = None,
        executionContextId: Optional[int] = None,
    ) -> Awaitable[Dict]:
        """
        Resolves the JavaScript node object for a given NodeId or BackendNodeId.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-resolveNode`

        :param nodeId: Id of the node to resolve.
        :param backendNodeId: Backend identifier of the node to resolve.
        :param objectGroup: Symbolic group name that can be used to release multiple objects.
        :param executionContextId: Execution context in which to resolve the node.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectGroup is not None:
            msg["objectGroup"] = objectGroup
        if executionContextId is not None:
            msg["executionContextId"] = executionContextId
        return self.client.send("DOM.resolveNode", msg)

    def setAttributeValue(self, nodeId: int, name: str, value: str) -> Awaitable[Dict]:
        """
        Sets attribute for an element with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setAttributeValue`

        :param nodeId: Id of the element to set attribute for.
        :param name: Attribute name.
        :param value: Attribute value.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.setAttributeValue", {"nodeId": nodeId, "name": name, "value": value}
        )

    def setAttributesAsText(
        self, nodeId: int, text: str, name: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Sets attributes on element with given id. This method is useful when user edits some existing
        attribute value and types in several attribute name/value pairs.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setAttributesAsText`

        :param nodeId: Id of the element to set attributes for.
        :param text: Text with a number of attributes. Will parse this text using HTML parser.
        :param name: Attribute name to replace with new attributes derived from text in case text parsed
         successfully.
        :return: The results of the command
        """
        msg = {"nodeId": nodeId, "text": text}
        if name is not None:
            msg["name"] = name
        return self.client.send("DOM.setAttributesAsText", msg)

    def setFileInputFiles(
        self,
        files: List[str],
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Sets files for the given file input element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setFileInputFiles`

        :param files: Array of file paths to set.
        :param nodeId: Identifier of the node.
        :param backendNodeId: Identifier of the backend node.
        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        msg = {"files": files}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        return self.client.send("DOM.setFileInputFiles", msg)

    def getFileInfo(self, objectId: str) -> Awaitable[Dict]:
        """
        Returns file information for the given
        File wrapper.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getFileInfo`

        :param objectId: JavaScript object id of the node wrapper.
        :return: The results of the command
        """
        return self.client.send("DOM.getFileInfo", {"objectId": objectId})

    def setInspectedNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions).

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setInspectedNode`

        :param nodeId: DOM node id to be accessible by means of $x command line API.
        :return: The results of the command
        """
        return self.client.send("DOM.setInspectedNode", {"nodeId": nodeId})

    def setNodeName(self, nodeId: int, name: str) -> Awaitable[Dict]:
        """
        Sets node name for a node with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setNodeName`

        :param nodeId: Id of the node to set name for.
        :param name: New node's name.
        :return: The results of the command
        """
        return self.client.send("DOM.setNodeName", {"nodeId": nodeId, "name": name})

    def setNodeValue(self, nodeId: int, value: str) -> Awaitable[Dict]:
        """
        Sets node value for a node with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setNodeValue`

        :param nodeId: Id of the node to set value for.
        :param value: New node's value.
        :return: The results of the command
        """
        return self.client.send("DOM.setNodeValue", {"nodeId": nodeId, "value": value})

    def setOuterHTML(self, nodeId: int, outerHTML: str) -> Awaitable[Dict]:
        """
        Sets node HTML markup, returns new node id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setOuterHTML`

        :param nodeId: Id of the node to set markup for.
        :param outerHTML: Outer HTML markup to set.
        :return: The results of the command
        """
        return self.client.send(
            "DOM.setOuterHTML", {"nodeId": nodeId, "outerHTML": outerHTML}
        )

    def undo(self) -> Awaitable[Dict]:
        """
        Undoes the last performed action.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-undo`

        :return: The results of the command
        """
        return self.client.send("DOM.undo", {})

    def getFrameOwner(self, frameId: str) -> Awaitable[Dict]:
        """
        Returns iframe node that owns iframe with the given domain.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getFrameOwner`

        :param frameId: The frameId
        :return: The results of the command
        """
        return self.client.send("DOM.getFrameOwner", {"frameId": frameId})

    def attributeModified(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when `Element`'s attribute is modified.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-attributeModified`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.attributeModified"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def attributeRemoved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when `Element`'s attribute is removed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-attributeRemoved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.attributeRemoved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def characterDataModified(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Mirrors `DOMCharacterDataModified` event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-characterDataModified`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.characterDataModified"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def childNodeCountUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when `Container`'s child node count has changed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-childNodeCountUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.childNodeCountUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def childNodeInserted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Mirrors `DOMNodeInserted` event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-childNodeInserted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.childNodeInserted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def childNodeRemoved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Mirrors `DOMNodeRemoved` event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-childNodeRemoved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.childNodeRemoved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def distributedNodesUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when distrubution is changed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-distributedNodesUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.distributedNodesUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def documentUpdated(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        Fired when `Document` has been totally updated. Node ids are no longer valid.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-documentUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.documentUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def inlineStyleInvalidated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when `Element`'s inline style is modified via a CSS property modification.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-inlineStyleInvalidated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.inlineStyleInvalidated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def pseudoElementAdded(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when a pseudo element is added to an element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-pseudoElementAdded`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.pseudoElementAdded"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def pseudoElementRemoved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when a pseudo element is removed from an element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-pseudoElementRemoved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.pseudoElementRemoved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def setChildNodes(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when backend wants to provide client with the missing DOM structure. This happens upon
        most of the calls requesting node ids.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-setChildNodes`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.setChildNodes"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def shadowRootPopped(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when shadow root is popped from the element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-shadowRootPopped`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.shadowRootPopped"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def shadowRootPushed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when shadow root is pushed into the element.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOM#event-shadowRootPushed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOM.shadowRootPushed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
