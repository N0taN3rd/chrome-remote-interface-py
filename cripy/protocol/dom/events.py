from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AttributeModifiedEvent(BaseEvent):
    """Fired when `Element`'s attribute is modified."""

    event: str = "DOM.attributeModified"

    def __init__(self) -> None:
        """
        :param NodeId nodeId: Id of the node that has changed.
        :param str name: Attribute name.
        :param str value: Attribute value.
        """
        super().__init__()


class AttributeRemovedEvent(BaseEvent):
    """Fired when `Element`'s attribute is removed."""

    event: str = "DOM.attributeRemoved"

    def __init__(self) -> None:
        """
        :param NodeId nodeId: Id of the node that has changed.
        :param str name: A ttribute name.
        """
        super().__init__()


class CharacterDataModifiedEvent(BaseEvent):
    """Mirrors `DOMCharacterDataModified` event."""

    event: str = "DOM.characterDataModified"

    def __init__(self) -> None:
        """
        :param NodeId nodeId: Id of the node that has changed.
        :param str characterData: New text value.
        """
        super().__init__()


class ChildNodeCountUpdatedEvent(BaseEvent):
    """Fired when `Container`'s child node count has changed."""

    event: str = "DOM.childNodeCountUpdated"

    def __init__(self) -> None:
        """
        :param NodeId nodeId: Id of the node that has changed.
        :param int childNodeCount: New node count.
        """
        super().__init__()


class ChildNodeInsertedEvent(BaseEvent):
    """Mirrors `DOMNodeInserted` event."""

    event: str = "DOM.childNodeInserted"

    def __init__(self) -> None:
        """
        :param NodeId parentNodeId: Id of the node that has changed.
        :param NodeId previousNodeId: If of the previous siblint.
        :param Node node: Inserted node data.
        """
        super().__init__()


class ChildNodeRemovedEvent(BaseEvent):
    """Mirrors `DOMNodeRemoved` event."""

    event: str = "DOM.childNodeRemoved"

    def __init__(self) -> None:
        """
        :param NodeId parentNodeId: Parent id.
        :param NodeId nodeId: Id of the node that has been removed.
        """
        super().__init__()


class DistributedNodesUpdatedEvent(BaseEvent):
    """Called when distrubution is changed."""

    event: str = "DOM.distributedNodesUpdated"

    def __init__(self) -> None:
        """
        :param NodeId insertionPointId: Insertion point where distrubuted nodes were updated.
        :param array distributedNodes: Distributed nodes for given insertion point.
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
        :param array nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        """
        super().__init__()


class PseudoElementAddedEvent(BaseEvent):
    """Called when a pseudo element is added to an element."""

    event: str = "DOM.pseudoElementAdded"

    def __init__(self) -> None:
        """
        :param NodeId parentId: Pseudo element's parent element id.
        :param Node pseudoElement: The added pseudo element.
        """
        super().__init__()


class PseudoElementRemovedEvent(BaseEvent):
    """Called when a pseudo element is removed from an element."""

    event: str = "DOM.pseudoElementRemoved"

    def __init__(self) -> None:
        """
        :param NodeId parentId: Pseudo element's parent element id.
        :param NodeId pseudoElementId: The removed pseudo element id.
        """
        super().__init__()


class SetChildNodesEvent(BaseEvent):
    """Fired when backend wants to provide client with the missing DOM structure.
	This happens upon most of the calls requesting node ids."""

    event: str = "DOM.setChildNodes"

    def __init__(self) -> None:
        """
        :param NodeId parentId: Parent node id to populate with children.
        :param array nodes: Child nodes array.
        """
        super().__init__()


class ShadowRootPoppedEvent(BaseEvent):
    """Called when shadow root is popped from the element."""

    event: str = "DOM.shadowRootPopped"

    def __init__(self) -> None:
        """
        :param NodeId hostId: Host element id.
        :param NodeId rootId: Shadow root id.
        """
        super().__init__()


class ShadowRootPushedEvent(BaseEvent):
    """Called when shadow root is pushed into the element."""

    event: str = "DOM.shadowRootPushed"

    def __init__(self) -> None:
        """
        :param NodeId hostId: Host element id.
        :param Node root: Shadow root.
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

