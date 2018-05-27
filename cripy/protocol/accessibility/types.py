from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

AXNodeId = str

AXValueType = str

AXValueSourceType = str

AXValueNativeSourceType = str

AXPropertyName = str


class AXValueSource(ChromeTypeBase):

    def __init__(
        self,
        type: "AXValueSourceType",
        value: Optional["AXValue"] = None,
        attribute: Optional[str] = None,
        attributeValue: Optional["AXValue"] = None,
        superseded: Optional[bool] = None,
        nativeSource: Optional["AXValueNativeSourceType"] = None,
        nativeSourceValue: Optional["AXValue"] = None,
        invalid: Optional[bool] = None,
        invalidReason: Optional[str] = None,
    ) -> None:
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

    def __init__(
        self,
        backendDOMNodeId: "DOM.BackendNodeId",
        idref: Optional[str] = None,
        text: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.backendDOMNodeId: DOM.BackendNodeId = backendDOMNodeId
        self.idref: Optional[str] = idref
        self.text: Optional[str] = text


class AXProperty(ChromeTypeBase):

    def __init__(self, name: "AXPropertyName", value: "AXValue") -> None:
        super().__init__()
        self.name: AXPropertyName = name
        self.value: AXValue = value


class AXValue(ChromeTypeBase):

    def __init__(
        self,
        type: "AXValueType",
        value: Optional[Any] = None,
        relatedNodes: Optional[List["AXRelatedNode"]] = None,
        sources: Optional[List["AXValueSource"]] = None,
    ) -> None:
        super().__init__()
        self.type: AXValueType = type
        self.value: Optional[Any] = value
        self.relatedNodes: Optional[List[AXRelatedNode]] = relatedNodes
        self.sources: Optional[List[AXValueSource]] = sources


class AXNode(ChromeTypeBase):

    def __init__(
        self,
        nodeId: "AXNodeId",
        ignored: bool,
        ignoredReasons: Optional[List["AXProperty"]] = None,
        role: Optional["AXValue"] = None,
        name: Optional["AXValue"] = None,
        description: Optional["AXValue"] = None,
        value: Optional["AXValue"] = None,
        properties: Optional[List["AXProperty"]] = None,
        childIds: Optional[List["AXNodeId"]] = None,
        backendDOMNodeId: Optional["DOM.BackendNodeId"] = None,
    ) -> None:
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
