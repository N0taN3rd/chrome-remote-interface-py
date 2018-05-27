from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page

NodeId = int

BackendNodeId = int

PseudoType = str

ShadowRootType = str

Quad = list


class BackendNode(ChromeTypeBase):

    def __init__(
        self, nodeType: int, nodeName: str, backendNodeId: "BackendNodeId"
    ) -> None:
        super().__init__()
        self.nodeType: int = nodeType
        self.nodeName: str = nodeName
        self.backendNodeId: BackendNodeId = backendNodeId


class Node(ChromeTypeBase):

    def __init__(
        self,
        nodeId: "NodeId",
        backendNodeId: "BackendNodeId",
        nodeType: int,
        nodeName: str,
        localName: str,
        nodeValue: str,
        parentId: Optional["NodeId"] = None,
        childNodeCount: Optional[int] = None,
        children: Optional[List["Node"]] = None,
        attributes: Optional[List["str"]] = None,
        documentURL: Optional[str] = None,
        baseURL: Optional[str] = None,
        publicId: Optional[str] = None,
        systemId: Optional[str] = None,
        internalSubset: Optional[str] = None,
        xmlVersion: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        pseudoType: Optional["PseudoType"] = None,
        shadowRootType: Optional["ShadowRootType"] = None,
        frameId: Optional["Page.FrameId"] = None,
        contentDocument: Optional["Node"] = None,
        shadowRoots: Optional[List["Node"]] = None,
        templateContent: Optional["Node"] = None,
        pseudoElements: Optional[List["Node"]] = None,
        importedDocument: Optional["Node"] = None,
        distributedNodes: Optional[List["BackendNode"]] = None,
        isSVG: Optional[bool] = None,
    ) -> None:
        super().__init__()
        self.nodeId: NodeId = nodeId
        self.parentId: Optional[NodeId] = parentId
        self.backendNodeId: BackendNodeId = backendNodeId
        self.nodeType: int = nodeType
        self.nodeName: str = nodeName
        self.localName: str = localName
        self.nodeValue: str = nodeValue
        self.childNodeCount: Optional[int] = childNodeCount
        self.children: Optional[List[Node]] = children
        self.attributes: Optional[List[str]] = attributes
        self.documentURL: Optional[str] = documentURL
        self.baseURL: Optional[str] = baseURL
        self.publicId: Optional[str] = publicId
        self.systemId: Optional[str] = systemId
        self.internalSubset: Optional[str] = internalSubset
        self.xmlVersion: Optional[str] = xmlVersion
        self.name: Optional[str] = name
        self.value: Optional[str] = value
        self.pseudoType: Optional[PseudoType] = pseudoType
        self.shadowRootType: Optional[ShadowRootType] = shadowRootType
        self.frameId: Optional[Page.FrameId] = frameId
        self.contentDocument: Optional[Node] = contentDocument
        self.shadowRoots: Optional[List[Node]] = shadowRoots
        self.templateContent: Optional[Node] = templateContent
        self.pseudoElements: Optional[List[Node]] = pseudoElements
        self.importedDocument: Optional[Node] = importedDocument
        self.distributedNodes: Optional[List[BackendNode]] = distributedNodes
        self.isSVG: Optional[bool] = isSVG


class RGBA(ChromeTypeBase):

    def __init__(self, r: int, g: int, b: int, a: Optional[float] = None) -> None:
        super().__init__()
        self.r: int = r
        self.g: int = g
        self.b: int = b
        self.a: Optional[float] = a


class BoxModel(ChromeTypeBase):

    def __init__(
        self,
        content: "Quad",
        padding: "Quad",
        border: "Quad",
        margin: "Quad",
        width: int,
        height: int,
        shapeOutside: Optional["ShapeOutsideInfo"] = None,
    ) -> None:
        super().__init__()
        self.content: Quad = content
        self.padding: Quad = padding
        self.border: Quad = border
        self.margin: Quad = margin
        self.width: int = width
        self.height: int = height
        self.shapeOutside: Optional[ShapeOutsideInfo] = shapeOutside


class ShapeOutsideInfo(ChromeTypeBase):

    def __init__(
        self, bounds: "Quad", shape: List[Any], marginShape: List[Any]
    ) -> None:
        super().__init__()
        self.bounds: Quad = bounds
        self.shape: List[Any] = shape
        self.marginShape: List[Any] = marginShape


class Rect(ChromeTypeBase):

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
