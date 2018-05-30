from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.page import types as Page

ShadowRootType = TypeVar("ShadowRootType", str, str) # Shadow root type.

Quad = TypeVar("Quad", list, list) # An array of quad vertices, x immediately followed by y for each point, points clock-wise.

PseudoType = TypeVar("PseudoType", str, str) # Pseudo element type.

NodeId = TypeVar("NodeId", int, int) # Unique DOM node identifier.

BackendNodeId = TypeVar("BackendNodeId", int, int) # Unique DOM node identifier used to reference a node that may not have been pushed to the front-end.


class ShapeOutsideInfo(ProtocolType):
    """
    CSS Shape Outside details.
    """

    def __init__(self, bounds: Quad, shape: List[Any], marginShape: List[Any]) -> None:
        """
        :param bounds: Shape bounds
        :type bounds: Any
        :param shape: Shape coordinate details
        :type shape: List[Any]
        :param marginShape: Margin shape bounds
        :type marginShape: List[Any]
        """
        super().__init__()
        self.bounds = bounds
        self.shape = shape
        self.marginShape = marginShape

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ShapeOutsideInfo']:
        if init is not None:
            return ShapeOutsideInfo(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ShapeOutsideInfo']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShapeOutsideInfo(**it))
            return list_of_self
        else:
            return init


class Rect(ProtocolType):
    """
    Rectangle.
    """

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
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Rect']:
        if init is not None:
            return Rect(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Rect']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Rect(**it))
            return list_of_self
        else:
            return init


class RGBA(ProtocolType):
    """
    A structure holding an RGBA color.
    """

    def __init__(self, r: int, g: int, b: int, a: Optional[float] = None) -> None:
        """
        :param r: The red component, in the [0-255] range.
        :type r: int
        :param g: The green component, in the [0-255] range.
        :type g: int
        :param b: The blue component, in the [0-255] range.
        :type b: int
        :param a: The alpha component, in the [0-1] range (default: 1).
        :type a: Optional[float]
        """
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RGBA']:
        if init is not None:
            return RGBA(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RGBA']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RGBA(**it))
            return list_of_self
        else:
            return init


class Node(ProtocolType):
    """
    DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type.
    """

    def __init__(self, nodeId: NodeId, backendNodeId: BackendNodeId, nodeType: int, nodeName: str, localName: str, nodeValue: str, parentId: Optional[NodeId] = None, childNodeCount: Optional[int] = None, children: Optional[List[Union['Node', dict]]] = None, attributes: Optional[List[str]] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, internalSubset: Optional[str] = None, xmlVersion: Optional[str] = None, name: Optional[str] = None, value: Optional[str] = None, pseudoType: Optional[PseudoType] = None, shadowRootType: Optional[ShadowRootType] = None, frameId: Optional[Page.FrameId] = None, contentDocument: Optional[Union['Node', dict]] = None, shadowRoots: Optional[List[Union['Node', dict]]] = None, templateContent: Optional[Union['Node', dict]] = None, pseudoElements: Optional[List[Union['Node', dict]]] = None, importedDocument: Optional[Union['Node', dict]] = None, distributedNodes: Optional[List[Union['BackendNode', dict]]] = None, isSVG: Optional[bool] = None) -> None:
        """
        :param nodeId: Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend will only push node with given `id` once. It is aware of all requested nodes and will only fire DOM events for nodes known to the client.
        :type nodeId: int
        :param parentId: The id of the parent node if any.
        :type parentId: Optional[int]
        :param backendNodeId: The BackendNodeId for this node.
        :type backendNodeId: int
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param localName: `Node`'s localName.
        :type localName: str
        :param nodeValue: `Node`'s nodeValue.
        :type nodeValue: str
        :param childNodeCount: Child count for `Container` nodes.
        :type childNodeCount: Optional[int]
        :param children: Child nodes of this node when requested with children.
        :type children: Optional[List[dict]]
        :param attributes: Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`.
        :type attributes: Optional[List[str]]
        :param documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :type documentURL: Optional[str]
        :param baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :type baseURL: Optional[str]
        :param publicId: `DocumentType`'s publicId.
        :type publicId: Optional[str]
        :param systemId: `DocumentType`'s systemId.
        :type systemId: Optional[str]
        :param internalSubset: `DocumentType`'s internalSubset.
        :type internalSubset: Optional[str]
        :param xmlVersion: `Document`'s XML version in case of XML documents.
        :type xmlVersion: Optional[str]
        :param name: `Attr`'s name.
        :type name: Optional[str]
        :param value: `Attr`'s value.
        :type value: Optional[str]
        :param pseudoType: Pseudo element type for this node.
        :type pseudoType: Optional[str]
        :param shadowRootType: Shadow root type.
        :type shadowRootType: Optional[str]
        :param frameId: Frame ID for frame owner elements.
        :type frameId: Optional[str]
        :param contentDocument: Content document for frame owner elements.
        :type contentDocument: Optional[dict]
        :param shadowRoots: Shadow root list for given element host.
        :type shadowRoots: Optional[List[dict]]
        :param templateContent: Content document fragment for template elements.
        :type templateContent: Optional[dict]
        :param pseudoElements: Pseudo elements associated with this node.
        :type pseudoElements: Optional[List[dict]]
        :param importedDocument: Import document for the HTMLImport links.
        :type importedDocument: Optional[dict]
        :param distributedNodes: Distributed nodes for given insertion point.
        :type distributedNodes: Optional[List[dict]]
        :param isSVG: Whether the node is SVG.
        :type isSVG: Optional[bool]
        """
        super().__init__()
        self.nodeId = nodeId
        self.parentId = parentId
        self.backendNodeId = backendNodeId
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.localName = localName
        self.nodeValue = nodeValue
        self.childNodeCount = childNodeCount
        self.children = Node.safe_create_from_list(children)
        self.attributes = attributes
        self.documentURL = documentURL
        self.baseURL = baseURL
        self.publicId = publicId
        self.systemId = systemId
        self.internalSubset = internalSubset
        self.xmlVersion = xmlVersion
        self.name = name
        self.value = value
        self.pseudoType = pseudoType
        self.shadowRootType = shadowRootType
        self.frameId = frameId
        self.contentDocument = Node.safe_create(contentDocument)
        self.shadowRoots = Node.safe_create_from_list(shadowRoots)
        self.templateContent = Node.safe_create(templateContent)
        self.pseudoElements = Node.safe_create_from_list(pseudoElements)
        self.importedDocument = Node.safe_create(importedDocument)
        self.distributedNodes = BackendNode.safe_create_from_list(distributedNodes)
        self.isSVG = isSVG

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Node']:
        if init is not None:
            return Node(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Node']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Node(**it))
            return list_of_self
        else:
            return init


class BoxModel(ProtocolType):
    """
    Box model.
    """

    def __init__(self, content: Quad, padding: Quad, border: Quad, margin: Quad, width: int, height: int, shapeOutside: Optional[Union['ShapeOutsideInfo', dict]] = None) -> None:
        """
        :param content: Content box
        :type content: Any
        :param padding: Padding box
        :type padding: Any
        :param border: Border box
        :type border: Any
        :param margin: Margin box
        :type margin: Any
        :param width: Node width
        :type width: int
        :param height: Node height
        :type height: int
        :param shapeOutside: Shape outside coordinates
        :type shapeOutside: Optional[dict]
        """
        super().__init__()
        self.content = content
        self.padding = padding
        self.border = border
        self.margin = margin
        self.width = width
        self.height = height
        self.shapeOutside = ShapeOutsideInfo.safe_create(shapeOutside)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['BoxModel']:
        if init is not None:
            return BoxModel(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['BoxModel']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BoxModel(**it))
            return list_of_self
        else:
            return init


class BackendNode(ProtocolType):
    """
    Backend node with a friendly name.
    """

    def __init__(self, nodeType: int, nodeName: str, backendNodeId: BackendNodeId) -> None:
        """
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param backendNodeId: The backendNodeId
        :type backendNodeId: int
        """
        super().__init__()
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.backendNodeId = backendNodeId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['BackendNode']:
        if init is not None:
            return BackendNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['BackendNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BackendNode(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ShapeOutsideInfo": ShapeOutsideInfo,
    "Rect": Rect,
    "RGBA": RGBA,
    "Node": Node,
    "BoxModel": BoxModel,
    "BackendNode": BackendNode,
}
