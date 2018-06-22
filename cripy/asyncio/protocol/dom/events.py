from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.dom.types import *

__all__ = [
    "AttributeModifiedEvent",
    "AttributeRemovedEvent",
    "CharacterDataModifiedEvent",
    "ChildNodeCountUpdatedEvent",
    "ChildNodeInsertedEvent",
    "ChildNodeRemovedEvent",
    "DistributedNodesUpdatedEvent",
    "DocumentUpdatedEvent",
    "InlineStyleInvalidatedEvent",
    "PseudoElementAddedEvent",
    "PseudoElementRemovedEvent",
    "SetChildNodesEvent",
    "ShadowRootPoppedEvent",
    "ShadowRootPushedEvent",
    "DOM_EVENTS_TO_CLASS",
    "DOM_EVENTS_NS"
]

class AttributeModifiedEvent(object):
    """
    Fired when `Element`'s attribute is modified.
    """

    event = "DOM.attributeModified"

    __slots__ = ["nodeId", "name", "value"]

    def __init__(self, nodeId: int, name: str, value: str) -> None:
        """
        Create a new instance of AttributeModifiedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "AttributeModifiedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AttributeModifiedEvent', dict]]:
        """
        Safely create AttributeModifiedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AttributeModifiedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AttributeModifiedEvent if creation did not fail
        :rtype: Optional[Union[dict, AttributeModifiedEvent]]
        """
        if init is not None:
            try:
                ourselves = AttributeModifiedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AttributeModifiedEvent', dict]]]:
        """
        Safely create a new list AttributeModifiedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AttributeModifiedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AttributeModifiedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AttributeModifiedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttributeModifiedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class AttributeRemovedEvent(object):
    """
    Fired when `Element`'s attribute is removed.
    """

    event = "DOM.attributeRemoved"

    __slots__ = ["nodeId", "name"]

    def __init__(self, nodeId: int, name: str) -> None:
        """
        Create a new instance of AttributeRemovedEvent

        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param name: A ttribute name.
        :type name: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.name = name

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        return "AttributeRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AttributeRemovedEvent', dict]]:
        """
        Safely create AttributeRemovedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AttributeRemovedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AttributeRemovedEvent if creation did not fail
        :rtype: Optional[Union[dict, AttributeRemovedEvent]]
        """
        if init is not None:
            try:
                ourselves = AttributeRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AttributeRemovedEvent', dict]]]:
        """
        Safely create a new list AttributeRemovedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AttributeRemovedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AttributeRemovedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AttributeRemovedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AttributeRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class CharacterDataModifiedEvent(object):
    """
    Mirrors `DOMCharacterDataModified` event.
    """

    event = "DOM.characterDataModified"

    __slots__ = ["nodeId", "characterData"]

    def __init__(self, nodeId: int, characterData: str) -> None:
        """
        Create a new instance of CharacterDataModifiedEvent

        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param characterData: New text value.
        :type characterData: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.characterData = characterData

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.characterData is not None:
            repr_args.append("characterData={!r}".format(self.characterData))
        return "CharacterDataModifiedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CharacterDataModifiedEvent', dict]]:
        """
        Safely create CharacterDataModifiedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CharacterDataModifiedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CharacterDataModifiedEvent if creation did not fail
        :rtype: Optional[Union[dict, CharacterDataModifiedEvent]]
        """
        if init is not None:
            try:
                ourselves = CharacterDataModifiedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CharacterDataModifiedEvent', dict]]]:
        """
        Safely create a new list CharacterDataModifiedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CharacterDataModifiedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CharacterDataModifiedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, CharacterDataModifiedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CharacterDataModifiedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ChildNodeCountUpdatedEvent(object):
    """
    Fired when `Container`'s child node count has changed.
    """

    event = "DOM.childNodeCountUpdated"

    __slots__ = ["nodeId", "childNodeCount"]

    def __init__(self, nodeId: int, childNodeCount: int) -> None:
        """
        Create a new instance of ChildNodeCountUpdatedEvent

        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param childNodeCount: New node count.
        :type childNodeCount: int
        """
        super().__init__()
        self.nodeId = nodeId
        self.childNodeCount = childNodeCount

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.childNodeCount is not None:
            repr_args.append("childNodeCount={!r}".format(self.childNodeCount))
        return "ChildNodeCountUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ChildNodeCountUpdatedEvent', dict]]:
        """
        Safely create ChildNodeCountUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ChildNodeCountUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ChildNodeCountUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, ChildNodeCountUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = ChildNodeCountUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ChildNodeCountUpdatedEvent', dict]]]:
        """
        Safely create a new list ChildNodeCountUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ChildNodeCountUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ChildNodeCountUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ChildNodeCountUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeCountUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ChildNodeInsertedEvent(object):
    """
    Mirrors `DOMNodeInserted` event.
    """

    event = "DOM.childNodeInserted"

    __slots__ = ["parentNodeId", "previousNodeId", "node"]

    def __init__(self, parentNodeId: int, previousNodeId: int, node: Union[Node, dict]) -> None:
        """
        Create a new instance of ChildNodeInsertedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.parentNodeId is not None:
            repr_args.append("parentNodeId={!r}".format(self.parentNodeId))
        if self.previousNodeId is not None:
            repr_args.append("previousNodeId={!r}".format(self.previousNodeId))
        if self.node is not None:
            repr_args.append("node={!r}".format(self.node))
        return "ChildNodeInsertedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ChildNodeInsertedEvent', dict]]:
        """
        Safely create ChildNodeInsertedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ChildNodeInsertedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ChildNodeInsertedEvent if creation did not fail
        :rtype: Optional[Union[dict, ChildNodeInsertedEvent]]
        """
        if init is not None:
            try:
                ourselves = ChildNodeInsertedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ChildNodeInsertedEvent', dict]]]:
        """
        Safely create a new list ChildNodeInsertedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ChildNodeInsertedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ChildNodeInsertedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ChildNodeInsertedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeInsertedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ChildNodeRemovedEvent(object):
    """
    Mirrors `DOMNodeRemoved` event.
    """

    event = "DOM.childNodeRemoved"

    __slots__ = ["parentNodeId", "nodeId"]

    def __init__(self, parentNodeId: int, nodeId: int) -> None:
        """
        Create a new instance of ChildNodeRemovedEvent

        :param parentNodeId: Parent id.
        :type parentNodeId: int
        :param nodeId: Id of the node that has been removed.
        :type nodeId: int
        """
        super().__init__()
        self.parentNodeId = parentNodeId
        self.nodeId = nodeId

    def __repr__(self) -> str:
        repr_args = []
        if self.parentNodeId is not None:
            repr_args.append("parentNodeId={!r}".format(self.parentNodeId))
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        return "ChildNodeRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ChildNodeRemovedEvent', dict]]:
        """
        Safely create ChildNodeRemovedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ChildNodeRemovedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ChildNodeRemovedEvent if creation did not fail
        :rtype: Optional[Union[dict, ChildNodeRemovedEvent]]
        """
        if init is not None:
            try:
                ourselves = ChildNodeRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ChildNodeRemovedEvent', dict]]]:
        """
        Safely create a new list ChildNodeRemovedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ChildNodeRemovedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ChildNodeRemovedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ChildNodeRemovedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ChildNodeRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DistributedNodesUpdatedEvent(object):
    """
    Called when distrubution is changed.
    """

    event = "DOM.distributedNodesUpdated"

    __slots__ = ["insertionPointId", "distributedNodes"]

    def __init__(self, insertionPointId: int, distributedNodes: List[Union[BackendNode, dict]]) -> None:
        """
        Create a new instance of DistributedNodesUpdatedEvent

        :param insertionPointId: Insertion point where distrubuted nodes were updated.
        :type insertionPointId: int
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: List[dict]
        """
        super().__init__()
        self.insertionPointId = insertionPointId
        self.distributedNodes = BackendNode.safe_create_from_list(distributedNodes)

    def __repr__(self) -> str:
        repr_args = []
        if self.insertionPointId is not None:
            repr_args.append("insertionPointId={!r}".format(self.insertionPointId))
        if self.distributedNodes is not None:
            repr_args.append("distributedNodes={!r}".format(self.distributedNodes))
        return "DistributedNodesUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DistributedNodesUpdatedEvent', dict]]:
        """
        Safely create DistributedNodesUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DistributedNodesUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DistributedNodesUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, DistributedNodesUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = DistributedNodesUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DistributedNodesUpdatedEvent', dict]]]:
        """
        Safely create a new list DistributedNodesUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DistributedNodesUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DistributedNodesUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DistributedNodesUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DistributedNodesUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class DocumentUpdatedEvent(dict):
    """
    Fired when `Document` has been totally updated.
	Node ids are no longer valid.
    """

    event = "DOM.documentUpdated"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "DocumentUpdatedEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DocumentUpdatedEvent', dict]]:
        """
        Safely create DocumentUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DocumentUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DocumentUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, DocumentUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = DocumentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DocumentUpdatedEvent', dict]]]:
        """
        Safely create a new list DocumentUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DocumentUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DocumentUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DocumentUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DocumentUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class InlineStyleInvalidatedEvent(object):
    """
    Fired when `Element`'s inline style is modified via a CSS property modification.
    """

    event = "DOM.inlineStyleInvalidated"

    __slots__ = ["nodeIds"]

    def __init__(self, nodeIds: List[int]) -> None:
        """
        Create a new instance of InlineStyleInvalidatedEvent

        :param nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        :type nodeIds: List[int]
        """
        super().__init__()
        self.nodeIds = nodeIds

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeIds is not None:
            repr_args.append("nodeIds={!r}".format(self.nodeIds))
        return "InlineStyleInvalidatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['InlineStyleInvalidatedEvent', dict]]:
        """
        Safely create InlineStyleInvalidatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InlineStyleInvalidatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InlineStyleInvalidatedEvent if creation did not fail
        :rtype: Optional[Union[dict, InlineStyleInvalidatedEvent]]
        """
        if init is not None:
            try:
                ourselves = InlineStyleInvalidatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['InlineStyleInvalidatedEvent', dict]]]:
        """
        Safely create a new list InlineStyleInvalidatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InlineStyleInvalidatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InlineStyleInvalidatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, InlineStyleInvalidatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InlineStyleInvalidatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class PseudoElementAddedEvent(object):
    """
    Called when a pseudo element is added to an element.
    """

    event = "DOM.pseudoElementAdded"

    __slots__ = ["parentId", "pseudoElement"]

    def __init__(self, parentId: int, pseudoElement: Union[Node, dict]) -> None:
        """
        Create a new instance of PseudoElementAddedEvent

        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElement: The added pseudo element.
        :type pseudoElement: dict
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElement = Node.safe_create(pseudoElement)

    def __repr__(self) -> str:
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.pseudoElement is not None:
            repr_args.append("pseudoElement={!r}".format(self.pseudoElement))
        return "PseudoElementAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PseudoElementAddedEvent', dict]]:
        """
        Safely create PseudoElementAddedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of PseudoElementAddedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of PseudoElementAddedEvent if creation did not fail
        :rtype: Optional[Union[dict, PseudoElementAddedEvent]]
        """
        if init is not None:
            try:
                ourselves = PseudoElementAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['PseudoElementAddedEvent', dict]]]:
        """
        Safely create a new list PseudoElementAddedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list PseudoElementAddedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of PseudoElementAddedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, PseudoElementAddedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class PseudoElementRemovedEvent(object):
    """
    Called when a pseudo element is removed from an element.
    """

    event = "DOM.pseudoElementRemoved"

    __slots__ = ["parentId", "pseudoElementId"]

    def __init__(self, parentId: int, pseudoElementId: int) -> None:
        """
        Create a new instance of PseudoElementRemovedEvent

        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElementId: The removed pseudo element id.
        :type pseudoElementId: int
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElementId = pseudoElementId

    def __repr__(self) -> str:
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.pseudoElementId is not None:
            repr_args.append("pseudoElementId={!r}".format(self.pseudoElementId))
        return "PseudoElementRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['PseudoElementRemovedEvent', dict]]:
        """
        Safely create PseudoElementRemovedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of PseudoElementRemovedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of PseudoElementRemovedEvent if creation did not fail
        :rtype: Optional[Union[dict, PseudoElementRemovedEvent]]
        """
        if init is not None:
            try:
                ourselves = PseudoElementRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['PseudoElementRemovedEvent', dict]]]:
        """
        Safely create a new list PseudoElementRemovedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list PseudoElementRemovedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of PseudoElementRemovedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, PseudoElementRemovedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(PseudoElementRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class SetChildNodesEvent(object):
    """
    Fired when backend wants to provide client with the missing DOM structure.
	This happens upon most of the calls requesting node ids.
    """

    event = "DOM.setChildNodes"

    __slots__ = ["parentId", "nodes"]

    def __init__(self, parentId: int, nodes: List[Union[Node, dict]]) -> None:
        """
        Create a new instance of SetChildNodesEvent

        :param parentId: Parent node id to populate with children.
        :type parentId: int
        :param nodes: Child nodes array.
        :type nodes: List[dict]
        """
        super().__init__()
        self.parentId = parentId
        self.nodes = Node.safe_create_from_list(nodes)

    def __repr__(self) -> str:
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.nodes is not None:
            repr_args.append("nodes={!r}".format(self.nodes))
        return "SetChildNodesEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SetChildNodesEvent', dict]]:
        """
        Safely create SetChildNodesEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SetChildNodesEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SetChildNodesEvent if creation did not fail
        :rtype: Optional[Union[dict, SetChildNodesEvent]]
        """
        if init is not None:
            try:
                ourselves = SetChildNodesEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SetChildNodesEvent', dict]]]:
        """
        Safely create a new list SetChildNodesEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SetChildNodesEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SetChildNodesEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, SetChildNodesEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SetChildNodesEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ShadowRootPoppedEvent(object):
    """
    Called when shadow root is popped from the element.
    """

    event = "DOM.shadowRootPopped"

    __slots__ = ["hostId", "rootId"]

    def __init__(self, hostId: int, rootId: int) -> None:
        """
        Create a new instance of ShadowRootPoppedEvent

        :param hostId: Host element id.
        :type hostId: int
        :param rootId: Shadow root id.
        :type rootId: int
        """
        super().__init__()
        self.hostId = hostId
        self.rootId = rootId

    def __repr__(self) -> str:
        repr_args = []
        if self.hostId is not None:
            repr_args.append("hostId={!r}".format(self.hostId))
        if self.rootId is not None:
            repr_args.append("rootId={!r}".format(self.rootId))
        return "ShadowRootPoppedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ShadowRootPoppedEvent', dict]]:
        """
        Safely create ShadowRootPoppedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ShadowRootPoppedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ShadowRootPoppedEvent if creation did not fail
        :rtype: Optional[Union[dict, ShadowRootPoppedEvent]]
        """
        if init is not None:
            try:
                ourselves = ShadowRootPoppedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ShadowRootPoppedEvent', dict]]]:
        """
        Safely create a new list ShadowRootPoppedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ShadowRootPoppedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ShadowRootPoppedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ShadowRootPoppedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShadowRootPoppedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ShadowRootPushedEvent(object):
    """
    Called when shadow root is pushed into the element.
    """

    event = "DOM.shadowRootPushed"

    __slots__ = ["hostId", "root"]

    def __init__(self, hostId: int, root: Union[Node, dict]) -> None:
        """
        Create a new instance of ShadowRootPushedEvent

        :param hostId: Host element id.
        :type hostId: int
        :param root: Shadow root.
        :type root: dict
        """
        super().__init__()
        self.hostId = hostId
        self.root = Node.safe_create(root)

    def __repr__(self) -> str:
        repr_args = []
        if self.hostId is not None:
            repr_args.append("hostId={!r}".format(self.hostId))
        if self.root is not None:
            repr_args.append("root={!r}".format(self.root))
        return "ShadowRootPushedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ShadowRootPushedEvent', dict]]:
        """
        Safely create ShadowRootPushedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ShadowRootPushedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ShadowRootPushedEvent if creation did not fail
        :rtype: Optional[Union[dict, ShadowRootPushedEvent]]
        """
        if init is not None:
            try:
                ourselves = ShadowRootPushedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ShadowRootPushedEvent', dict]]]:
        """
        Safely create a new list ShadowRootPushedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ShadowRootPushedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ShadowRootPushedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ShadowRootPushedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShadowRootPushedEvent.safe_create(it))
            return list_of_self
        else:
            return init


DOM_EVENTS_TO_CLASS = {
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

DOMNS = namedtuple("DOMNS", ["AttributeModified", "AttributeRemoved", "CharacterDataModified", "ChildNodeCountUpdated", "ChildNodeInserted", "ChildNodeRemoved", "DistributedNodesUpdated", "DocumentUpdated", "InlineStyleInvalidated", "PseudoElementAdded", "PseudoElementRemoved", "SetChildNodes", "ShadowRootPopped", "ShadowRootPushed"])

DOM_EVENTS_NS = DOMNS(
  AttributeModified="DOM.attributeModified",
  AttributeRemoved="DOM.attributeRemoved",
  CharacterDataModified="DOM.characterDataModified",
  ChildNodeCountUpdated="DOM.childNodeCountUpdated",
  ChildNodeInserted="DOM.childNodeInserted",
  ChildNodeRemoved="DOM.childNodeRemoved",
  DistributedNodesUpdated="DOM.distributedNodesUpdated",
  DocumentUpdated="DOM.documentUpdated",
  InlineStyleInvalidated="DOM.inlineStyleInvalidated",
  PseudoElementAdded="DOM.pseudoElementAdded",
  PseudoElementRemoved="DOM.pseudoElementRemoved",
  SetChildNodes="DOM.setChildNodes",
  ShadowRootPopped="DOM.shadowRootPopped",
  ShadowRootPushed="DOM.shadowRootPushed",
)
