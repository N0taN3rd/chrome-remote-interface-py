from types import SimpleNamespace
try:
    from cripy.sync.protocol.dom.types import *
except ImportError:
    pass

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
]


class AttributeModifiedEvent(object):
    """
    Fired when `Element`'s attribute is modified.
    """

    event = "DOM.attributeModified"

    def __init__(self, nodeId, name, value):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "AttributeModifiedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = AttributeModifiedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, nodeId, name):
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param name: A ttribute name.
        :type name: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.name = name

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        return "AttributeRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = AttributeRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, nodeId, characterData):
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param characterData: New text value.
        :type characterData: str
        """
        super().__init__()
        self.nodeId = nodeId
        self.characterData = characterData

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.characterData is not None:
            repr_args.append("characterData={!r}".format(self.characterData))
        return "CharacterDataModifiedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = CharacterDataModifiedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, nodeId, childNodeCount):
        """
        :param nodeId: Id of the node that has changed.
        :type nodeId: int
        :param childNodeCount: New node count.
        :type childNodeCount: int
        """
        super().__init__()
        self.nodeId = nodeId
        self.childNodeCount = childNodeCount

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.childNodeCount is not None:
            repr_args.append("childNodeCount={!r}".format(self.childNodeCount))
        return "ChildNodeCountUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ChildNodeCountUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, parentNodeId, previousNodeId, node):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.parentNodeId is not None:
            repr_args.append("parentNodeId={!r}".format(self.parentNodeId))
        if self.previousNodeId is not None:
            repr_args.append("previousNodeId={!r}".format(self.previousNodeId))
        if self.node is not None:
            repr_args.append("node={!r}".format(self.node))
        return "ChildNodeInsertedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ChildNodeInsertedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, parentNodeId, nodeId):
        """
        :param parentNodeId: Parent id.
        :type parentNodeId: int
        :param nodeId: Id of the node that has been removed.
        :type nodeId: int
        """
        super().__init__()
        self.parentNodeId = parentNodeId
        self.nodeId = nodeId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.parentNodeId is not None:
            repr_args.append("parentNodeId={!r}".format(self.parentNodeId))
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        return "ChildNodeRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ChildNodeRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, insertionPointId, distributedNodes):
        """
        :param insertionPointId: Insertion point where distrubuted nodes were updated.
        :type insertionPointId: int
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: List[dict]
        """
        super().__init__()
        self.insertionPointId = insertionPointId
        self.distributedNodes = distributedNodes

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.insertionPointId is not None:
            repr_args.append("insertionPointId={!r}".format(self.insertionPointId))
        if self.distributedNodes is not None:
            repr_args.append("distributedNodes={!r}".format(self.distributedNodes))
        return "DistributedNodesUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DistributedNodesUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "DocumentUpdatedEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DocumentUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, nodeIds):
        """
        :param nodeIds: Ids of the nodes for which the inline styles have been invalidated.
        :type nodeIds: List[int]
        """
        super().__init__()
        self.nodeIds = nodeIds

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.nodeIds is not None:
            repr_args.append("nodeIds={!r}".format(self.nodeIds))
        return "InlineStyleInvalidatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = InlineStyleInvalidatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, parentId, pseudoElement):
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElement: The added pseudo element.
        :type pseudoElement: dict
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElement = Node.safe_create(pseudoElement)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.pseudoElement is not None:
            repr_args.append("pseudoElement={!r}".format(self.pseudoElement))
        return "PseudoElementAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PseudoElementAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, parentId, pseudoElementId):
        """
        :param parentId: Pseudo element's parent element id.
        :type parentId: int
        :param pseudoElementId: The removed pseudo element id.
        :type pseudoElementId: int
        """
        super().__init__()
        self.parentId = parentId
        self.pseudoElementId = pseudoElementId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.pseudoElementId is not None:
            repr_args.append("pseudoElementId={!r}".format(self.pseudoElementId))
        return "PseudoElementRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = PseudoElementRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, parentId, nodes):
        """
        :param parentId: Parent node id to populate with children.
        :type parentId: int
        :param nodes: Child nodes array.
        :type nodes: List[dict]
        """
        super().__init__()
        self.parentId = parentId
        self.nodes = nodes

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.nodes is not None:
            repr_args.append("nodes={!r}".format(self.nodes))
        return "SetChildNodesEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = SetChildNodesEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, hostId, rootId):
        """
        :param hostId: Host element id.
        :type hostId: int
        :param rootId: Shadow root id.
        :type rootId: int
        """
        super().__init__()
        self.hostId = hostId
        self.rootId = rootId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.hostId is not None:
            repr_args.append("hostId={!r}".format(self.hostId))
        if self.rootId is not None:
            repr_args.append("rootId={!r}".format(self.rootId))
        return "ShadowRootPoppedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ShadowRootPoppedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, hostId, root):
        """
        :param hostId: Host element id.
        :type hostId: int
        :param root: Shadow root.
        :type root: dict
        """
        super().__init__()
        self.hostId = hostId
        self.root = Node.safe_create(root)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.hostId is not None:
            repr_args.append("hostId={!r}".format(self.hostId))
        if self.root is not None:
            repr_args.append("root={!r}".format(self.root))
        return "ShadowRootPushedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ShadowRootPushedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShadowRootPushedEvent.safe_create(it))
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

EVENT_NS = SimpleNamespace(
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
