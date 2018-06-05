from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM


class AXValueSource(object):
    """
    A single source for a computed AX property.
    """

    def __init__(
        self,
        type: str,
        value: Optional[Union["AXValue", dict]] = None,
        attribute: Optional[str] = None,
        attributeValue: Optional[Union["AXValue", dict]] = None,
        superseded: Optional[bool] = None,
        nativeSource: Optional[str] = None,
        nativeSourceValue: Optional[Union["AXValue", dict]] = None,
        invalid: Optional[bool] = None,
        invalidReason: Optional[str] = None,
    ) -> None:
        """
        :param type: What type of source this is.
        :type type: str
        :param value: The value of this property source.
        :type value: Optional[dict]
        :param attribute: The name of the relevant attribute, if any.
        :type attribute: Optional[str]
        :param attributeValue: The value of the relevant attribute, if any.
        :type attributeValue: Optional[dict]
        :param superseded: Whether this source is superseded by a higher priority source.
        :type superseded: Optional[bool]
        :param nativeSource: The native markup source for this value, e.g. a <label> element.
        :type nativeSource: Optional[str]
        :param nativeSourceValue: The value, such as a node or node list, of the native source.
        :type nativeSourceValue: Optional[dict]
        :param invalid: Whether the value for this property is invalid.
        :type invalid: Optional[bool]
        :param invalidReason: Reason for the value being invalid, if it is.
        :type invalidReason: Optional[str]
        """
        super().__init__()
        self.type = type
        self.value = AXValue.safe_create(value)
        self.attribute = attribute
        self.attributeValue = AXValue.safe_create(attributeValue)
        self.superseded = superseded
        self.nativeSource = nativeSource
        self.nativeSourceValue = AXValue.safe_create(nativeSourceValue)
        self.invalid = invalid
        self.invalidReason = invalidReason

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.attribute is not None:
            repr_args.append("attribute={!r}".format(self.attribute))
        if self.attributeValue is not None:
            repr_args.append("attributeValue={!r}".format(self.attributeValue))
        if self.superseded is not None:
            repr_args.append("superseded={!r}".format(self.superseded))
        if self.nativeSource is not None:
            repr_args.append("nativeSource={!r}".format(self.nativeSource))
        if self.nativeSourceValue is not None:
            repr_args.append("nativeSourceValue={!r}".format(self.nativeSourceValue))
        if self.invalid is not None:
            repr_args.append("invalid={!r}".format(self.invalid))
        if self.invalidReason is not None:
            repr_args.append("invalidReason={!r}".format(self.invalidReason))
        return "AXValueSource(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AXValueSource", dict]]:
        if init is not None:
            try:
                ourselves = AXValueSource(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AXValueSource", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXValueSource.safe_create(it))
            return list_of_self
        else:
            return init


class AXValue(object):
    """
    A single computed AX property.
    """

    def __init__(
        self,
        type: str,
        value: Optional[Any] = None,
        relatedNodes: Optional[List[Union["AXRelatedNode", dict]]] = None,
        sources: Optional[List[Union["AXValueSource", dict]]] = None,
    ) -> None:
        """
        :param type: The type of this value.
        :type type: str
        :param value: The computed value of this property.
        :type value: Optional[Any]
        :param relatedNodes: One or more related nodes, if applicable.
        :type relatedNodes: Optional[List[dict]]
        :param sources: The sources which contributed to the computation of this property.
        :type sources: Optional[List[dict]]
        """
        super().__init__()
        self.type = type
        self.value = value
        self.relatedNodes = AXRelatedNode.safe_create_from_list(relatedNodes)
        self.sources = AXValueSource.safe_create_from_list(sources)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.relatedNodes is not None:
            repr_args.append("relatedNodes={!r}".format(self.relatedNodes))
        if self.sources is not None:
            repr_args.append("sources={!r}".format(self.sources))
        return "AXValue(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AXValue", dict]]:
        if init is not None:
            try:
                ourselves = AXValue(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AXValue", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXValue.safe_create(it))
            return list_of_self
        else:
            return init


class AXRelatedNode(object):

    def __init__(
        self,
        backendDOMNodeId: int,
        idref: Optional[str] = None,
        text: Optional[str] = None,
    ) -> None:
        """
        :param backendDOMNodeId: The BackendNodeId of the related DOM node.
        :type backendDOMNodeId: int
        :param idref: The IDRef value provided, if any.
        :type idref: Optional[str]
        :param text: The text alternative of this node in the current context.
        :type text: Optional[str]
        """
        super().__init__()
        self.backendDOMNodeId = backendDOMNodeId
        self.idref = idref
        self.text = text

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.backendDOMNodeId is not None:
            repr_args.append("backendDOMNodeId={!r}".format(self.backendDOMNodeId))
        if self.idref is not None:
            repr_args.append("idref={!r}".format(self.idref))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        return "AXRelatedNode(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AXRelatedNode", dict]]:
        if init is not None:
            try:
                ourselves = AXRelatedNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AXRelatedNode", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXRelatedNode.safe_create(it))
            return list_of_self
        else:
            return init


class AXProperty(object):

    def __init__(self, name: str, value: Union["AXValue", dict]) -> None:
        """
        :param name: The name of this property.
        :type name: str
        :param value: The value of this property.
        :type value: dict
        """
        super().__init__()
        self.name = name
        self.value = AXValue.safe_create(value)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "AXProperty(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AXProperty", dict]]:
        if init is not None:
            try:
                ourselves = AXProperty(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AXProperty", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXProperty.safe_create(it))
            return list_of_self
        else:
            return init


class AXNode(object):
    """
    A node in the accessibility tree.
    """

    def __init__(
        self,
        nodeId: str,
        ignored: bool,
        ignoredReasons: Optional[List[Union["AXProperty", dict]]] = None,
        role: Optional[Union["AXValue", dict]] = None,
        name: Optional[Union["AXValue", dict]] = None,
        description: Optional[Union["AXValue", dict]] = None,
        value: Optional[Union["AXValue", dict]] = None,
        properties: Optional[List[Union["AXProperty", dict]]] = None,
        childIds: Optional[List[str]] = None,
        backendDOMNodeId: Optional[int] = None,
    ) -> None:
        """
        :param nodeId: Unique identifier for this node.
        :type nodeId: str
        :param ignored: Whether this node is ignored for accessibility
        :type ignored: bool
        :param ignoredReasons: Collection of reasons why this node is hidden.
        :type ignoredReasons: Optional[List[dict]]
        :param role: This `Node`'s role, whether explicit or implicit.
        :type role: Optional[dict]
        :param name: The accessible name for this `Node`.
        :type name: Optional[dict]
        :param description: The accessible description for this `Node`.
        :type description: Optional[dict]
        :param value: The value for this `Node`.
        :type value: Optional[dict]
        :param properties: All other properties
        :type properties: Optional[List[dict]]
        :param childIds: IDs for each of this node's child nodes.
        :type childIds: Optional[List[str]]
        :param backendDOMNodeId: The backend ID for the associated DOM node, if any.
        :type backendDOMNodeId: Optional[int]
        """
        super().__init__()
        self.nodeId = nodeId
        self.ignored = ignored
        self.ignoredReasons = AXProperty.safe_create_from_list(ignoredReasons)
        self.role = AXValue.safe_create(role)
        self.name = AXValue.safe_create(name)
        self.description = AXValue.safe_create(description)
        self.value = AXValue.safe_create(value)
        self.properties = AXProperty.safe_create_from_list(properties)
        self.childIds = childIds
        self.backendDOMNodeId = backendDOMNodeId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.ignored is not None:
            repr_args.append("ignored={!r}".format(self.ignored))
        if self.ignoredReasons is not None:
            repr_args.append("ignoredReasons={!r}".format(self.ignoredReasons))
        if self.role is not None:
            repr_args.append("role={!r}".format(self.role))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.description is not None:
            repr_args.append("description={!r}".format(self.description))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.properties is not None:
            repr_args.append("properties={!r}".format(self.properties))
        if self.childIds is not None:
            repr_args.append("childIds={!r}".format(self.childIds))
        if self.backendDOMNodeId is not None:
            repr_args.append("backendDOMNodeId={!r}".format(self.backendDOMNodeId))
        return "AXNode(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AXNode", dict]]:
        if init is not None:
            try:
                ourselves = AXNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AXNode", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXNode.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "AXValueSource": AXValueSource,
    "AXValue": AXValue,
    "AXRelatedNode": AXRelatedNode,
    "AXProperty": AXProperty,
    "AXNode": AXNode,
}
