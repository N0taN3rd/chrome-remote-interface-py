from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

# Unique accessibility node identifier.
AXNodeId = str

# Enum of possible property types.
AXValueType = str

# Enum of possible property sources.
AXValueSourceType = str

# Enum of possible native property sources (as a subtype of a particular AXValueSourceType).
AXValueNativeSourceType = str

# Values of AXProperty name: from 'busy' to 'roledescription' - states which apply to every AX node, from 'live' to 'root' - attributes which apply to nodes in live regions, from 'autocomplete' to 'valuetext' - attributes which apply to widgets, from 'checked' to 'selected' - states which apply to widgets, from 'activedescendant' to 'owns' - relationships between elements other than parent/child/sibling.
AXPropertyName = str


class AXValueSource(ChromeTypeBase):
    """A single source for a computed AX property."""

    def __init__(self, type: 'AXValueSourceType', value: Optional['AXValue'] = None, attribute: Optional[str] = None, attributeValue: Optional['AXValue'] = None, superseded: Optional[bool] = None, nativeSource: Optional['AXValueNativeSourceType'] = None, nativeSourceValue: Optional['AXValue'] = None, invalid: Optional[bool] = None, invalidReason: Optional[str] = None) -> None:
        """
        :param type: What type of source this is.
        :type AXValueSourceType:
        :param value: The value of this property source.
        :type AXValue:
        :param attribute: The name of the relevant attribute, if any.
        :type str:
        :param attributeValue: The value of the relevant attribute, if any.
        :type AXValue:
        :param superseded: Whether this source is superseded by a higher priority source.
        :type bool:
        :param nativeSource: The native markup source for this value, e.g. a <label> element.
        :type AXValueNativeSourceType:
        :param nativeSourceValue: The value, such as a node or node list, of the native source.
        :type AXValue:
        :param invalid: Whether the value for this property is invalid.
        :type bool:
        :param invalidReason: Reason for the value being invalid, if it is.
        :type str:
        """
        super().__init__()
        self.type: AXValueSourceType = type
        self.value: Optional[AXValue] = value
        self.attribute: Optional[str] = attribute
        self.attributeValue: Optional[AXValue] = attributeValue
        self.superseded: Optional[bool] = superseded
        self.nativeSource: Optional[AXValueNativeSourceType] = nativeSource
        self.nativeSourceValue: Optional[AXValue] = nativeSourceValue
        self.invalid: Optional[bool] = invalid
        self.invalidReason: Optional[str] = invalidReason


class AXRelatedNode(ChromeTypeBase):

    def __init__(self, backendDOMNodeId: 'DOM.BackendNodeId', idref: Optional[str] = None, text: Optional[str] = None) -> None:
        """
        :param backendDOMNodeId: The BackendNodeId of the related DOM node.
        :type DOM.BackendNodeId:
        :param idref: The IDRef value provided, if any.
        :type str:
        :param text: The text alternative of this node in the current context.
        :type str:
        """
        super().__init__()
        self.backendDOMNodeId: DOM.BackendNodeId = backendDOMNodeId
        self.idref: Optional[str] = idref
        self.text: Optional[str] = text


class AXProperty(ChromeTypeBase):

    def __init__(self, name: 'AXPropertyName', value: 'AXValue') -> None:
        """
        :param name: The name of this property.
        :type AXPropertyName:
        :param value: The value of this property.
        :type AXValue:
        """
        super().__init__()
        self.name: AXPropertyName = name
        self.value: AXValue = value


class AXValue(ChromeTypeBase):
    """A single computed AX property."""

    def __init__(self, type: 'AXValueType', value: Optional[Any] = None, relatedNodes: Optional[List['AXRelatedNode']] = None, sources: Optional[List['AXValueSource']] = None) -> None:
        """
        :param type: The type of this value.
        :type AXValueType:
        :param value: The computed value of this property.
        :type Any:
        :param relatedNodes: One or more related nodes, if applicable.
        :type array:
        :param sources: The sources which contributed to the computation of this property.
        :type array:
        """
        super().__init__()
        self.type: AXValueType = type
        self.value: Optional[Any] = value
        self.relatedNodes: Optional[List[AXRelatedNode]] = relatedNodes
        self.sources: Optional[List[AXValueSource]] = sources


class AXNode(ChromeTypeBase):
    """A node in the accessibility tree."""

    def __init__(self, nodeId: 'AXNodeId', ignored: bool, ignoredReasons: Optional[List['AXProperty']] = None, role: Optional['AXValue'] = None, name: Optional['AXValue'] = None, description: Optional['AXValue'] = None, value: Optional['AXValue'] = None, properties: Optional[List['AXProperty']] = None, childIds: Optional[List['AXNodeId']] = None, backendDOMNodeId: Optional['DOM.BackendNodeId'] = None) -> None:
        """
        :param nodeId: Unique identifier for this node.
        :type AXNodeId:
        :param ignored: Whether this node is ignored for accessibility
        :type bool:
        :param ignoredReasons: Collection of reasons why this node is hidden.
        :type array:
        :param role: This `Node`'s role, whether explicit or implicit.
        :type AXValue:
        :param name: The accessible name for this `Node`.
        :type AXValue:
        :param description: The accessible description for this `Node`.
        :type AXValue:
        :param value: The value for this `Node`.
        :type AXValue:
        :param properties: All other properties
        :type array:
        :param childIds: IDs for each of this node's child nodes.
        :type array:
        :param backendDOMNodeId: The backend ID for the associated DOM node, if any.
        :type DOM.BackendNodeId:
        """
        super().__init__()
        self.nodeId: AXNodeId = nodeId
        self.ignored: bool = ignored
        self.ignoredReasons: Optional[List[AXProperty]] = ignoredReasons
        self.role: Optional[AXValue] = role
        self.name: Optional[AXValue] = name
        self.description: Optional[AXValue] = description
        self.value: Optional[AXValue] = value
        self.properties: Optional[List[AXProperty]] = properties
        self.childIds: Optional[List[AXNodeId]] = childIds
        self.backendDOMNodeId: Optional[DOM.BackendNodeId] = backendDOMNodeId


