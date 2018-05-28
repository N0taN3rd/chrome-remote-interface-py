from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page

# Unique DOM node identifier.
NodeId = int

# Unique DOM node identifier used to reference a node that may not have been pushed to the front-end.
BackendNodeId = int

# Pseudo element type.
PseudoType = str

# Shadow root type.
ShadowRootType = str

# An array of quad vertices, x immediately followed by y for each point, points clock-wise.
Quad = list


class BackendNode(ChromeTypeBase):
    """Backend node with a friendly name."""
    def __init__(self, nodeType: int, nodeName: str, backendNodeId: 'BackendNodeId') -> None:
        """
        :param int nodeType: `Node`'s nodeType.
        :param str nodeName: `Node`'s nodeName.
        :param BackendNodeId backendNodeId: The backendNodeId
        """
        super().__init__()
        self.nodeType: int = nodeType
        self.nodeName: str = nodeName
        self.backendNodeId: BackendNodeId = backendNodeId


class Node(ChromeTypeBase):
    """DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type."""
    def __init__(self, nodeId: 'NodeId', backendNodeId: 'BackendNodeId', nodeType: int, nodeName: str, localName: str, nodeValue: str, parentId: Optional['NodeId'] = None, childNodeCount: Optional[int] = None, children: Optional[List['Node']] = None, attributes: Optional[List['str']] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, internalSubset: Optional[str] = None, xmlVersion: Optional[str] = None, name: Optional[str] = None, value: Optional[str] = None, pseudoType: Optional['PseudoType'] = None, shadowRootType: Optional['ShadowRootType'] = None, frameId: Optional['Page.FrameId'] = None, contentDocument: Optional['Node'] = None, shadowRoots: Optional[List['Node']] = None, templateContent: Optional['Node'] = None, pseudoElements: Optional[List['Node']] = None, importedDocument: Optional['Node'] = None, distributedNodes: Optional[List['BackendNode']] = None, isSVG: Optional[bool] = None) -> None:
        """
        :param NodeId nodeId: Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend will only push node with given `id` once. It is aware of all requested nodes and will only fire DOM events for nodes known to the client.
        :param NodeId parentId: The id of the parent node if any.
        :param BackendNodeId backendNodeId: The BackendNodeId for this node.
        :param int nodeType: `Node`'s nodeType.
        :param str nodeName: `Node`'s nodeName.
        :param str localName: `Node`'s localName.
        :param str nodeValue: `Node`'s nodeValue.
        :param int childNodeCount: Child count for `Container` nodes.
        :param array children: Child nodes of this node when requested with children.
        :param array attributes: Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`.
        :param str documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :param str baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :param str publicId: `DocumentType`'s publicId.
        :param str systemId: `DocumentType`'s systemId.
        :param str internalSubset: `DocumentType`'s internalSubset.
        :param str xmlVersion: `Document`'s XML version in case of XML documents.
        :param str name: `Attr`'s name.
        :param str value: `Attr`'s value.
        :param PseudoType pseudoType: Pseudo element type for this node.
        :param ShadowRootType shadowRootType: Shadow root type.
        :param Page.FrameId frameId: Frame ID for frame owner elements.
        :param Node contentDocument: Content document for frame owner elements.
        :param array shadowRoots: Shadow root list for given element host.
        :param Node templateContent: Content document fragment for template elements.
        :param array pseudoElements: Pseudo elements associated with this node.
        :param Node importedDocument: Import document for the HTMLImport links.
        :param array distributedNodes: Distributed nodes for given insertion point.
        :param bool isSVG: Whether the node is SVG.
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


class RGBA(ChromeTypeBase):
    """A structure holding an RGBA color."""
    def __init__(self, r: int, g: int, b: int, a: Optional[float] = None) -> None:
        """
        :param int r: The red component, in the [0-255] range.
        :param int g: The green component, in the [0-255] range.
        :param int b: The blue component, in the [0-255] range.
        :param float a: The alpha component, in the [0-1] range (default: 1).
        """
        super().__init__()
        self.r: int = r
        self.g: int = g
        self.b: int = b
        self.a: Optional[float] = a


class BoxModel(ChromeTypeBase):
    """Box model."""
    def __init__(self, content: 'Quad', padding: 'Quad', border: 'Quad', margin: 'Quad', width: int, height: int, shapeOutside: Optional['ShapeOutsideInfo'] = None) -> None:
        """
        :param Quad content: Content box
        :param Quad padding: Padding box
        :param Quad border: Border box
        :param Quad margin: Margin box
        :param int width: Node width
        :param int height: Node height
        :param ShapeOutsideInfo shapeOutside: Shape outside coordinates
        """
        super().__init__()
        self.content: Quad = content
        self.padding: Quad = padding
        self.border: Quad = border
        self.margin: Quad = margin
        self.width: int = width
        self.height: int = height
        self.shapeOutside: Optional[ShapeOutsideInfo] = shapeOutside


class ShapeOutsideInfo(ChromeTypeBase):
    """CSS Shape Outside details."""
    def __init__(self, bounds: 'Quad', shape: List[Any], marginShape: List[Any]) -> None:
        """
        :param Quad bounds: Shape bounds
        :param array shape: Shape coordinate details
        :param array marginShape: Margin shape bounds
        """
        super().__init__()
        self.bounds: Quad = bounds
        self.shape: List[Any] = shape
        self.marginShape: List[Any] = marginShape


class Rect(ChromeTypeBase):
    """Rectangle."""
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        :param float x: X coordinate
        :param float y: Y coordinate
        :param float width: Rectangle width
        :param float height: Rectangle height
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height


