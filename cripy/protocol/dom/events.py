from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.dom.types import NodeId, Node


class AttributeModifiedEvent(BaseEvent):
    """Fired when `Element`'s attribute is modified."""

    event: str = "DOM.attributeModified"

    def __init__(self, nodeId: NodeId, name: str, value: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: NodeId
        :param name: Attribute name.
        :type name: str
        :param value: Attribute value.
        :type value: str
        """
        super().__init__()
        self.nodeId: NodeId = nodeId
        self.name: str = name
        self.value: str = value


class AttributeRemovedEvent(BaseEvent):
    """Fired when `Element`'s attribute is removed."""

    event: str = "DOM.attributeRemoved"

    def __init__(self, nodeId: NodeId, name: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: NodeId
        :param name: A ttribute name.
        :type name: str
        """
        super().__init__()
        self.nodeId: NodeId = nodeId
        self.name: str = name


class CharacterDataModifiedEvent(BaseEvent):
    """Mirrors `DOMCharacterDataModified` event."""

    event: str = "DOM.characterDataModified"

    def __init__(self, nodeId: NodeId, characterData: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: NodeId
        :param characterData: New text value.
        :type characterData: str
        """
        super().__init__()
        self.nodeId: NodeId = nodeId
        self.characterData: str = characterData


class ChildNodeCountUpdatedEvent(BaseEvent):
    """Fired when `Container`'s child node count has changed."""

    event: str = "DOM.childNodeCountUpdated"

    def __init__(self, nodeId: NodeId, childNodeCount: int) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: NodeId
        :param childNodeCount: New node count.
        :type childNodeCount: int
        """
        super().__init__()
        self.nodeId: NodeId = nodeId
        self.childNodeCount: int = childNodeCount


class ChildNodeInsertedEvent(BaseEvent):
    """Mirrors `DOMNodeInserted` event."""

    event: str = "DOM.childNodeInserted"

    def __init__(
        self, parentNodeId: NodeId, previousNodeId: NodeId, node: Node
    ) -> None:
        """
        :param parentNodeId: Id of the node that has changed.
        :type parentNodeId: NodeId
        :param previousNodeId: If of the previous siblint.
        :type previousNodeId: NodeId
        :param node: Inserted node data.
        :type node: Node
        """
        super().__init__()
        self.parentNodeId: NodeId = parentNodeId
        self.previousNodeId: NodeId = previousNodeId
        self.node: Node = node


class ChildNodeRemovedEvent(BaseEvent):
    """Mirrors `DOMNodeRemoved` event."""

    event: str = "DOM.childNodeRemoved"

    def __init__(self, parentNodeId: NodeId, nodeId: NodeId) -> None:
        """
        :param parentNodeId: Parent id.
        :type parentNodeId: NodeId
        :param nodeId: Id of the node that has been removed.
        :type nodeId: NodeId
        """
        super().__init__()
        self.parentNodeId: NodeId = parentNodeId
        self.nodeId: NodeId = nodeId


class DistributedNodesUpdatedEvent(BaseEvent):
    """Called when distrubution is changed."""

    event: str = "DOM.distributedNodesUpdated"

    def __init__(
        self, insertionPointId: NodeId, distributedNodes: List[Union[BackendNode, dict]]
    ) -> None:
        """
        :param insertionPointId: Insertion point where distrubuted nodes were updated.
        :type insertionPointId: NodeId
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: array
        """
        super().__init__()
        self.insertionPointId: NodeId = insertionPointId
        self.distributedNodes: List[BackendNode] = distributedNodes


class DocumentUpdatedEvent(BaseEvent):
    """Fired when `Document` has been totally updated.
	Node ids are no longer valid."""

    event: str = "DOM.documentUpdated"

    def __init__(self,) -> None:
        super().__init__()


class InlineStyleInvalidatedEvent(BaseEvent):
    """Fired when `Element`'s inline style is modified via a CSS property modification."""

    event: str = "DOM.inlineStyleInvalidated"

    def __init__(self, nodeIds: List[NodeId]) -> None:
        """
        :param nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        :type nodeIds: array
        """
        super().__init__()
        self.nodeIds: List[NodeId] = nodeIds


class PseudoElementAddedEvent(BaseEvent):
    """Called when a pseudo element is added to an element."""

    event: str = "DOM.pseudoElementAdded"

    def __init__(self, parentId: NodeId, pseudoElement: Node) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: NodeId
        :param pseudoElement: The added pseudo element.
        :type pseudoElement: Node
        """
        super().__init__()
        self.parentId: NodeId = parentId
        self.pseudoElement: Node = pseudoElement


class PseudoElementRemovedEvent(BaseEvent):
    """Called when a pseudo element is removed from an element."""

    event: str = "DOM.pseudoElementRemoved"

    def __init__(self, parentId: NodeId, pseudoElementId: NodeId) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: NodeId
        :param pseudoElementId: The removed pseudo element id.
        :type pseudoElementId: NodeId
        """
        super().__init__()
        self.parentId: NodeId = parentId
        self.pseudoElementId: NodeId = pseudoElementId


class SetChildNodesEvent(BaseEvent):
    """Fired when backend wants to provide client with the missing DOM structure.
	This happens upon most of the calls requesting node ids."""

    event: str = "DOM.setChildNodes"

    def __init__(self, parentId: NodeId, nodes: List[Union[Node, dict]]) -> None:
        """
        :param parentId: Parent node id to populate with children.
        :type parentId: NodeId
        :param nodes: Child nodes array.
        :type nodes: array
        """
        super().__init__()
        self.parentId: NodeId = parentId
        self.nodes: List[Node] = nodes


class ShadowRootPoppedEvent(BaseEvent):
    """Called when shadow root is popped from the element."""

    event: str = "DOM.shadowRootPopped"

    def __init__(self, hostId: NodeId, rootId: NodeId) -> None:
        """
        :param hostId: Host element id.
        :type hostId: NodeId
        :param rootId: Shadow root id.
        :type rootId: NodeId
        """
        super().__init__()
        self.hostId: NodeId = hostId
        self.rootId: NodeId = rootId


class ShadowRootPushedEvent(BaseEvent):
    """Called when shadow root is pushed into the element."""

    event: str = "DOM.shadowRootPushed"

    def __init__(self, hostId: NodeId, root: Node) -> None:
        """
        :param hostId: Host element id.
        :type hostId: NodeId
        :param root: Shadow root.
        :type root: Node
        """
        super().__init__()
        self.hostId: NodeId = hostId
        self.root: Node = root


EVENT_TO_CLASS = {
    "DOM.attributeModified": AttributeModifiedEvent,
    "DOM.attributeRemoved": AttributeRemovedEvent,
    "DOM.characterDataModified": CharacterDataModifiedEvent,
    "DOM.childNodeCountUpdated": ChildNodeCountUpdatedEvent,
    "DOM.childNodeInserted": ChildNodeInsertedEvent,
    "DOM.childNodeRemoved": ChildNodeRemovedEvent,
    "DOM.distributedNodesUpdated": DistributedNodesUpdatedEvent,
    "DOM.documentUpdated": DocumentUpdatedEvent,
    "DOM.inlineStyleInvalidated": InlineStyleInvalidatedEvent,
    "DOM.pseudoElementAdded": PseudoElementAddedEvent,
    "DOM.pseudoElementRemoved": PseudoElementRemovedEvent,
    "DOM.setChildNodes": SetChildNodesEvent,
    "DOM.shadowRootPopped": ShadowRootPoppedEvent,
    "DOM.shadowRootPushed": ShadowRootPushedEvent,
}
