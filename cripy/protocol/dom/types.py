from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.page import types as Page

ShadowRootType = TypeVar("ShadowRootType", str, str)
"""Shadow root type."""

Quad = TypeVar("Quad", list, list)
"""An array of quad vertices, x immediately followed by y for each point, points clock-wise."""

PseudoType = TypeVar("PseudoType", str, str)
"""Pseudo element type."""

NodeId = TypeVar("NodeId", int, int)
"""Unique DOM node identifier."""

BackendNodeId = TypeVar("BackendNodeId", int, int)
"""Unique DOM node identifier used to reference a node that may not have been pushed to the front-end."""


class ShapeOutsideInfo(ProtocolType):
    """CSS Shape Outside details."""

    def __init__(
        self, bounds: "Quad", shape: List[Any], marginShape: List[Any]
    ) -> None:
        """
        :param bounds: Shape bounds
        :type bounds: Quad
        :param shape: Shape coordinate details
        :type shape: array
        :param marginShape: Margin shape bounds
        :type marginShape: array
        """
        super().__init__()
        self.bounds: Quad = bounds
        self.shape: List[Any] = shape
        self.marginShape: List[Any] = marginShape


class Rect(ProtocolType):
    """Rectangle."""

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        :param x: X coordinate
        :type x: float
        :param y: Y coordinate
        :type y: float
        :param width: Rectangle width
        :type width: float
        :param height: Rectangle height
        :type height: float
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height


class RGBA(ProtocolType):
    """A structure holding an RGBA color."""

    def __init__(self, r: int, g: int, b: int, a: Optional[float] = None) -> None:
        """
        :param r: The red component, in the [0-255] range.
        :type r: int
        :param g: The green component, in the [0-255] range.
        :type g: int
        :param b: The blue component, in the [0-255] range.
        :type b: int
        :param a: The alpha component, in the [0-1] range (default: 1).
        :type a: float
        """
        super().__init__()
        self.r: int = r
        self.g: int = g
        self.b: int = b
        self.a: Optional[float] = a


class Node(ProtocolType):
    """DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type."""

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
        children: Optional[List[Union["Node", dict]]] = None,
        attributes: Optional[List[str]] = None,
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
        shadowRoots: Optional[List[Union["Node", dict]]] = None,
        templateContent: Optional["Node"] = None,
        pseudoElements: Optional[List[Union["Node", dict]]] = None,
        importedDocument: Optional["Node"] = None,
        distributedNodes: Optional[List[Union["BackendNode", dict]]] = None,
        isSVG: Optional[bool] = None,
    ) -> None:
        """
        :param nodeId: Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend will only push node with given `id` once. It is aware of all requested nodes and will only fire DOM events for nodes known to the client.
        :type nodeId: NodeId
        :param parentId: The id of the parent node if any.
        :type parentId: NodeId
        :param backendNodeId: The BackendNodeId for this node.
        :type backendNodeId: BackendNodeId
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param localName: `Node`'s localName.
        :type localName: str
        :param nodeValue: `Node`'s nodeValue.
        :type nodeValue: str
        :param childNodeCount: Child count for `Container` nodes.
        :type childNodeCount: int
        :param children: Child nodes of this node when requested with children.
        :type children: array
        :param attributes: Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`.
        :type attributes: array
        :param documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :type documentURL: str
        :param baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :type baseURL: str
        :param publicId: `DocumentType`'s publicId.
        :type publicId: str
        :param systemId: `DocumentType`'s systemId.
        :type systemId: str
        :param internalSubset: `DocumentType`'s internalSubset.
        :type internalSubset: str
        :param xmlVersion: `Document`'s XML version in case of XML documents.
        :type xmlVersion: str
        :param name: `Attr`'s name.
        :type name: str
        :param value: `Attr`'s value.
        :type value: str
        :param pseudoType: Pseudo element type for this node.
        :type pseudoType: PseudoType
        :param shadowRootType: Shadow root type.
        :type shadowRootType: ShadowRootType
        :param frameId: Frame ID for frame owner elements.
        :type frameId: Page.FrameId
        :param contentDocument: Content document for frame owner elements.
        :type contentDocument: Node
        :param shadowRoots: Shadow root list for given element host.
        :type shadowRoots: array
        :param templateContent: Content document fragment for template elements.
        :type templateContent: Node
        :param pseudoElements: Pseudo elements associated with this node.
        :type pseudoElements: array
        :param importedDocument: Import document for the HTMLImport links.
        :type importedDocument: Node
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: array
        :param isSVG: Whether the node is SVG.
        :type isSVG: bool
        """
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


class BoxModel(ProtocolType):
    """Box model."""

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
        """
        :param content: Content box
        :type content: Quad
        :param padding: Padding box
        :type padding: Quad
        :param border: Border box
        :type border: Quad
        :param margin: Margin box
        :type margin: Quad
        :param width: Node width
        :type width: int
        :param height: Node height
        :type height: int
        :param shapeOutside: Shape outside coordinates
        :type shapeOutside: ShapeOutsideInfo
        """
        super().__init__()
        self.content: Quad = content
        self.padding: Quad = padding
        self.border: Quad = border
        self.margin: Quad = margin
        self.width: int = width
        self.height: int = height
        self.shapeOutside: Optional[ShapeOutsideInfo] = shapeOutside


class BackendNode(ProtocolType):
    """Backend node with a friendly name."""

    def __init__(
        self, nodeType: int, nodeName: str, backendNodeId: "BackendNodeId"
    ) -> None:
        """
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param backendNodeId: The backendNodeId
        :type backendNodeId: BackendNodeId
        """
        super().__init__()
        self.nodeType: int = nodeType
        self.nodeName: str = nodeName
        self.backendNodeId: BackendNodeId = backendNodeId


OBJECT_LIST = {
    "ShapeOutsideInfo": ShapeOutsideInfo,
    "Rect": Rect,
    "RGBA": RGBA,
    "Node": Node,
    "BoxModel": BoxModel,
    "BackendNode": BackendNode,
}
