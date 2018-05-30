from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM

AXValueType = TypeVar("AXValueType", str, str) # Enum of possible property types.

AXValueSourceType = TypeVar("AXValueSourceType", str, str) # Enum of possible property sources.

AXValueNativeSourceType = TypeVar("AXValueNativeSourceType", str, str) # Enum of possible native property sources (as a subtype of a particular AXValueSourceType).

AXPropertyName = TypeVar("AXPropertyName", str, str) # Values of AXProperty name: from 'busy' to 'roledescription' - states which apply to every AX node, from 'live' to 'root' - attributes which apply to nodes in live regions, from 'autocomplete' to 'valuetext' - attributes which apply to widgets, from 'checked' to 'selected' - states which apply to widgets, from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.

AXNodeId = TypeVar("AXNodeId", str, str) # Unique accessibility node identifier.


class AXValueSource(ProtocolType):
    """
    A single source for a computed AX property.
    """

    def __init__(self, type: AXValueSourceType, value: Optional[Union['AXValue', dict]] = None, attribute: Optional[str] = None, attributeValue: Optional[Union['AXValue', dict]] = None, superseded: Optional[bool] = None, nativeSource: Optional[AXValueNativeSourceType] = None, nativeSourceValue: Optional[Union['AXValue', dict]] = None, invalid: Optional[bool] = None, invalidReason: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AXValueSource']:
        if init is not None:
            return AXValueSource(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AXValueSource']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXValueSource(**it))
            return list_of_self
        else:
            return init


class AXValue(ProtocolType):
    """
    A single computed AX property.
    """

    def __init__(self, type: AXValueType, value: Optional[Any] = None, relatedNodes: Optional[List[Union['AXRelatedNode', dict]]] = None, sources: Optional[List[Union['AXValueSource', dict]]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AXValue']:
        if init is not None:
            return AXValue(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AXValue']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXValue(**it))
            return list_of_self
        else:
            return init


class AXRelatedNode(ProtocolType):
    def __init__(self, backendDOMNodeId: DOM.BackendNodeId, idref: Optional[str] = None, text: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AXRelatedNode']:
        if init is not None:
            return AXRelatedNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AXRelatedNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXRelatedNode(**it))
            return list_of_self
        else:
            return init


class AXProperty(ProtocolType):
    def __init__(self, name: AXPropertyName, value: Union['AXValue', dict]) -> None:
        """
        :param name: The name of this property.
        :type name: str
        :param value: The value of this property.
        :type value: dict
        """
        super().__init__()
        self.name = name
        self.value = AXValue.safe_create(value)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AXProperty']:
        if init is not None:
            return AXProperty(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AXProperty']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXProperty(**it))
            return list_of_self
        else:
            return init


class AXNode(ProtocolType):
    """
    A node in the accessibility tree.
    """

    def __init__(self, nodeId: AXNodeId, ignored: bool, ignoredReasons: Optional[List[Union['AXProperty', dict]]] = None, role: Optional[Union['AXValue', dict]] = None, name: Optional[Union['AXValue', dict]] = None, description: Optional[Union['AXValue', dict]] = None, value: Optional[Union['AXValue', dict]] = None, properties: Optional[List[Union['AXProperty', dict]]] = None, childIds: Optional[List[AXNodeId]] = None, backendDOMNodeId: Optional[DOM.BackendNodeId] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AXNode']:
        if init is not None:
            return AXNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AXNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AXNode(**it))
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
