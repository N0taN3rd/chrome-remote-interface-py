from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AttributeModifiedEvent(BaseEvent):
    """Fired when `Element`'s attribute is modified."""

    event: str = "DOM.attributeModified"

    def __init__(self) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type NodeId:
        :param name: Attribute name.
        :type str:
        :param value: Attribute value.
        :type str:
        """
        super().__init__()


class AttributeRemovedEvent(BaseEvent):
    """Fired when `Element`'s attribute is removed."""

    event: str = "DOM.attributeRemoved"

    def __init__(self) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type NodeId:
        :param name: A ttribute name.
        :type str:
        """
        super().__init__()


class CharacterDataModifiedEvent(BaseEvent):
    """Mirrors `DOMCharacterDataModified` event."""

    event: str = "DOM.characterDataModified"

    def __init__(self) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type NodeId:
        :param characterData: New text value.
        :type str:
        """
        super().__init__()


class ChildNodeCountUpdatedEvent(BaseEvent):
    """Fired when `Container`'s child node count has changed."""

    event: str = "DOM.childNodeCountUpdated"

    def __init__(self) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type NodeId:
        :param childNodeCount: New node count.
        :type int:
        """
        super().__init__()


class ChildNodeInsertedEvent(BaseEvent):
    """Mirrors `DOMNodeInserted` event."""

    event: str = "DOM.childNodeInserted"

    def __init__(self) -> None:
        """
        :param parentNodeId: Id of the node that has changed.
        :type NodeId:
        :param previousNodeId: If of the previous siblint.
        :type NodeId:
        :param node: Inserted node data.
        :type Node:
        """
        super().__init__()


class ChildNodeRemovedEvent(BaseEvent):
    """Mirrors `DOMNodeRemoved` event."""

    event: str = "DOM.childNodeRemoved"

    def __init__(self) -> None:
        """
        :param parentNodeId: Parent id.
        :type NodeId:
        :param nodeId: Id of the node that has been removed.
        :type NodeId:
        """
        super().__init__()


class DistributedNodesUpdatedEvent(BaseEvent):
    """Called when distrubution is changed."""

    event: str = "DOM.distributedNodesUpdated"

    def __init__(self) -> None:
        """
        :param insertionPointId: Insertion point where distrubuted nodes were updated.
        :type NodeId:
        :param distributedNodes: Distributed nodes for given insertion point.
        :type array:
        """
        super().__init__()


class DocumentUpdatedEvent(BaseEvent):
    """Fired when `Document` has been totally updated.
	Node ids are no longer valid."""

    event: str = "DOM.documentUpdated"

    def __init__(self) -> None:
        super().__init__()


class InlineStyleInvalidatedEvent(BaseEvent):
    """Fired when `Element`'s inline style is modified via a CSS property modification."""

    event: str = "DOM.inlineStyleInvalidated"

    def __init__(self) -> None:
        """
        :param nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        :type array:
        """
        super().__init__()


class PseudoElementAddedEvent(BaseEvent):
    """Called when a pseudo element is added to an element."""

    event: str = "DOM.pseudoElementAdded"

    def __init__(self) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type NodeId:
        :param pseudoElement: The added pseudo element.
        :type Node:
        """
        super().__init__()


class PseudoElementRemovedEvent(BaseEvent):
    """Called when a pseudo element is removed from an element."""

    event: str = "DOM.pseudoElementRemoved"

    def __init__(self) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type NodeId:
        :param pseudoElementId: The removed pseudo element id.
        :type NodeId:
        """
        super().__init__()


class SetChildNodesEvent(BaseEvent):
    """Fired when backend wants to provide client with the missing DOM structure.
	This happens upon most of the calls requesting node ids."""

    event: str = "DOM.setChildNodes"

    def __init__(self) -> None:
        """
        :param parentId: Parent node id to populate with children.
        :type NodeId:
        :param nodes: Child nodes array.
        :type array:
        """
        super().__init__()


class ShadowRootPoppedEvent(BaseEvent):
    """Called when shadow root is popped from the element."""

    event: str = "DOM.shadowRootPopped"

    def __init__(self) -> None:
        """
        :param hostId: Host element id.
        :type NodeId:
        :param rootId: Shadow root id.
        :type NodeId:
        """
        super().__init__()


class ShadowRootPushedEvent(BaseEvent):
    """Called when shadow root is pushed into the element."""

    event: str = "DOM.shadowRootPushed"

    def __init__(self) -> None:
        """
        :param hostId: Host element id.
        :type NodeId:
        :param root: Shadow root.
        :type Node:
        """
        super().__init__()


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

