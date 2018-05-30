from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.dom.types import *
except ImportError:
    pass


class AttributeModifiedEvent(BaseEvent):
    """
    Fired when `Element`'s attribute is modified.
    """

    event = "DOM.attributeModified"

    def __init__(self, nodeId: NodeId, name: str, value: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param name: Attribute name.
        :type name: str
        :param value: Attribute value.
        :type value: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.name = name
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AttributeModifiedEvent']:
        if init is not None:
            return AttributeModifiedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AttributeModifiedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttributeModifiedEvent(**it))
            return list_of_self
        else:
            return init


class AttributeRemovedEvent(BaseEvent):
    """
    Fired when `Element`'s attribute is removed.
    """

    event = "DOM.attributeRemoved"

    def __init__(self, nodeId: NodeId, name: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param name: A ttribute name.
        :type name: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.name = name

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AttributeRemovedEvent']:
        if init is not None:
            return AttributeRemovedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AttributeRemovedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttributeRemovedEvent(**it))
            return list_of_self
        else:
            return init


class CharacterDataModifiedEvent(BaseEvent):
    """
    Mirrors `DOMCharacterDataModified` event.
    """

    event = "DOM.characterDataModified"

    def __init__(self, nodeId: NodeId, characterData: str) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param characterData: New text value.
        :type characterData: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.characterData = characterData

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CharacterDataModifiedEvent']:
        if init is not None:
            return CharacterDataModifiedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CharacterDataModifiedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CharacterDataModifiedEvent(**it))
            return list_of_self
        else:
            return init


class ChildNodeCountUpdatedEvent(BaseEvent):
    """
    Fired when `Container`'s child node count has changed.
    """

    event = "DOM.childNodeCountUpdated"

    def __init__(self, nodeId: NodeId, childNodeCount: int) -> None:
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param childNodeCount: New node count.
        :type childNodeCount: int
        """
        super().__init__()
        self.nodeId = nodeId
        self.childNodeCount = childNodeCount

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ChildNodeCountUpdatedEvent']:
        if init is not None:
            return ChildNodeCountUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ChildNodeCountUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeCountUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class ChildNodeInsertedEvent(BaseEvent):
    """
    Mirrors `DOMNodeInserted` event.
    """

    event = "DOM.childNodeInserted"

    def __init__(self, parentNodeId: NodeId, previousNodeId: NodeId, node: Union[Node, dict]) -> None:
        """
        :param parentNodeId: Id of the node that has changed.
        :type parentNodeId: int
        :param previousNodeId: If of the previous siblint.
        :type previousNodeId: int
        :param node: Inserted node data.
        :type node: dict
        """
        super().__init__()
        self.parentNodeId = parentNodeId
        self.previousNodeId = previousNodeId
        self.node = Node.safe_create(node)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ChildNodeInsertedEvent']:
        if init is not None:
            return ChildNodeInsertedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ChildNodeInsertedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeInsertedEvent(**it))
            return list_of_self
        else:
            return init


class ChildNodeRemovedEvent(BaseEvent):
    """
    Mirrors `DOMNodeRemoved` event.
    """

    event = "DOM.childNodeRemoved"

    def __init__(self, parentNodeId: NodeId, nodeId: NodeId) -> None:
        """
        :param parentNodeId: Parent id.
        :type parentNodeId: int
        :param nodeId: Id of the node that has been removed.
        :type nodeId: int
        """
        super().__init__()
        self.parentNodeId = parentNodeId
        self.nodeId = nodeId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ChildNodeRemovedEvent']:
        if init is not None:
            return ChildNodeRemovedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ChildNodeRemovedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeRemovedEvent(**it))
            return list_of_self
        else:
            return init


class DistributedNodesUpdatedEvent(BaseEvent):
    """
    Called when distrubution is changed.
    """

    event = "DOM.distributedNodesUpdated"

    def __init__(self, insertionPointId: NodeId, distributedNodes: List[Union[BackendNode, dict]]) -> None:
        """
        :param insertionPointId: Insertion point where distrubuted nodes were updated.
        :type insertionPointId: int
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: List[dict]
        """
        super().__init__()
        self.insertionPointId = insertionPointId
        self.distributedNodes = BackendNode.safe_create_from_list(distributedNodes)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DistributedNodesUpdatedEvent']:
        if init is not None:
            return DistributedNodesUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DistributedNodesUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DistributedNodesUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class DocumentUpdatedEvent(BaseEvent, dict):
    """
    Fired when `Document` has been totally updated.
	Node ids are no longer valid.
    """

    event = "DOM.documentUpdated"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DocumentUpdatedEvent']:
        if init is not None:
            return DocumentUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DocumentUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DocumentUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class InlineStyleInvalidatedEvent(BaseEvent):
    """
    Fired when `Element`'s inline style is modified via a CSS property modification.
    """

    event = "DOM.inlineStyleInvalidated"

    def __init__(self, nodeIds: List[NodeId]) -> None:
        """
        :param nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        :type nodeIds: List[int]
        """
        super().__init__()
        self.nodeIds = nodeIds

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InlineStyleInvalidatedEvent']:
        if init is not None:
            return InlineStyleInvalidatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InlineStyleInvalidatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InlineStyleInvalidatedEvent(**it))
            return list_of_self
        else:
            return init


class PseudoElementAddedEvent(BaseEvent):
    """
    Called when a pseudo element is added to an element.
    """

    event = "DOM.pseudoElementAdded"

    def __init__(self, parentId: NodeId, pseudoElement: Union[Node, dict]) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElement: The added pseudo element.
        :type pseudoElement: dict
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElement = Node.safe_create(pseudoElement)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PseudoElementAddedEvent']:
        if init is not None:
            return PseudoElementAddedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PseudoElementAddedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementAddedEvent(**it))
            return list_of_self
        else:
            return init


class PseudoElementRemovedEvent(BaseEvent):
    """
    Called when a pseudo element is removed from an element.
    """

    event = "DOM.pseudoElementRemoved"

    def __init__(self, parentId: NodeId, pseudoElementId: NodeId) -> None:
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElementId: The removed pseudo element id.
        :type pseudoElementId: int
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElementId = pseudoElementId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['PseudoElementRemovedEvent']:
        if init is not None:
            return PseudoElementRemovedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['PseudoElementRemovedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementRemovedEvent(**it))
            return list_of_self
        else:
            return init


class SetChildNodesEvent(BaseEvent):
    """
    Fired when backend wants to provide client with the missing DOM structure.
	This happens upon most of the calls requesting node ids.
    """

    event = "DOM.setChildNodes"

    def __init__(self, parentId: NodeId, nodes: List[Union[Node, dict]]) -> None:
        """
        :param parentId: Parent node id to populate with children.
        :type parentId: int
        :param nodes: Child nodes array.
        :type nodes: List[dict]
        """
        super().__init__()
        self.parentId = parentId
        self.nodes = Node.safe_create_from_list(nodes)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SetChildNodesEvent']:
        if init is not None:
            return SetChildNodesEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SetChildNodesEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SetChildNodesEvent(**it))
            return list_of_self
        else:
            return init


class ShadowRootPoppedEvent(BaseEvent):
    """
    Called when shadow root is popped from the element.
    """

    event = "DOM.shadowRootPopped"

    def __init__(self, hostId: NodeId, rootId: NodeId) -> None:
        """
        :param hostId: Host element id.
        :type hostId: int
        :param rootId: Shadow root id.
        :type rootId: int
        """
        super().__init__()
        self.hostId = hostId
        self.rootId = rootId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ShadowRootPoppedEvent']:
        if init is not None:
            return ShadowRootPoppedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ShadowRootPoppedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShadowRootPoppedEvent(**it))
            return list_of_self
        else:
            return init


class ShadowRootPushedEvent(BaseEvent):
    """
    Called when shadow root is pushed into the element.
    """

    event = "DOM.shadowRootPushed"

    def __init__(self, hostId: NodeId, root: Union[Node, dict]) -> None:
        """
        :param hostId: Host element id.
        :type hostId: int
        :param root: Shadow root.
        :type root: dict
        """
        super().__init__()
        self.hostId = hostId
        self.root = Node.safe_create(root)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ShadowRootPushedEvent']:
        if init is not None:
            return ShadowRootPushedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ShadowRootPushedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShadowRootPushedEvent(**it))
            return list_of_self
        else:
            return init


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

