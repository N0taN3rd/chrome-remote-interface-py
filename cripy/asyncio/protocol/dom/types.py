from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.page import types as Page

__all__ = [
    "ShapeOutsideInfo",
    "Rect",
    "RGBA",
    "Node",
    "BoxModel",
    "BackendNode",
    "DOM_TYPES_TO_OBJECT"
]


class ShapeOutsideInfo(object):
    """
    CSS Shape Outside details.
    """

    __slots__ = ["bounds", "shape", "marginShape"]

    def __init__(self, bounds: list, shape: List[Any], marginShape: List[Any]) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.bounds is not None:
            repr_args.append("bounds={!r}".format(self.bounds))
        if self.shape is not None:
            repr_args.append("shape={!r}".format(self.shape))
        if self.marginShape is not None:
            repr_args.append("marginShape={!r}".format(self.marginShape))
        return "ShapeOutsideInfo(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ShapeOutsideInfo', dict]]:
        """
        Safely create ShapeOutsideInfo from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ShapeOutsideInfo
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ShapeOutsideInfo if creation did not fail
        :rtype: Optional[Union[dict, ShapeOutsideInfo]]
        """
        if init is not None:
            try:
                ourselves = ShapeOutsideInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ShapeOutsideInfo', dict]]]:
        """
        Safely create a new list ShapeOutsideInfos from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ShapeOutsideInfo instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ShapeOutsideInfo instances if creation did not fail
        :rtype: Optional[List[Union[dict, ShapeOutsideInfo]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ShapeOutsideInfo.safe_create(it))
            return list_of_self
        else:
            return init


class Rect(object):
    """
    Rectangle.
    """

    __slots__ = ["x", "y", "width", "height"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.x is not None:
            repr_args.append("x={!r}".format(self.x))
        if self.y is not None:
            repr_args.append("y={!r}".format(self.y))
        if self.width is not None:
            repr_args.append("width={!r}".format(self.width))
        if self.height is not None:
            repr_args.append("height={!r}".format(self.height))
        return "Rect(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Rect', dict]]:
        """
        Safely create Rect from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Rect
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Rect if creation did not fail
        :rtype: Optional[Union[dict, Rect]]
        """
        if init is not None:
            try:
                ourselves = Rect(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Rect', dict]]]:
        """
        Safely create a new list Rects from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Rect instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Rect instances if creation did not fail
        :rtype: Optional[List[Union[dict, Rect]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Rect.safe_create(it))
            return list_of_self
        else:
            return init


class RGBA(object):
    """
    A structure holding an RGBA color.
    """

    __slots__ = ["r", "g", "b", "a"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.r is not None:
            repr_args.append("r={!r}".format(self.r))
        if self.g is not None:
            repr_args.append("g={!r}".format(self.g))
        if self.b is not None:
            repr_args.append("b={!r}".format(self.b))
        if self.a is not None:
            repr_args.append("a={!r}".format(self.a))
        return "RGBA(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RGBA', dict]]:
        """
        Safely create RGBA from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RGBA
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RGBA if creation did not fail
        :rtype: Optional[Union[dict, RGBA]]
        """
        if init is not None:
            try:
                ourselves = RGBA(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['RGBA', dict]]]:
        """
        Safely create a new list RGBAs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RGBA instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RGBA instances if creation did not fail
        :rtype: Optional[List[Union[dict, RGBA]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RGBA.safe_create(it))
            return list_of_self
        else:
            return init


class Node(object):
    """
    DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
DOMNode is a base node mirror type.
    """

    __slots__ = ["nodeId", "parentId", "backendNodeId", "nodeType", "nodeName", "localName", "nodeValue", "childNodeCount", "children", "attributes", "documentURL", "baseURL", "publicId", "systemId", "internalSubset", "xmlVersion", "name", "value", "pseudoType", "shadowRootType", "frameId", "contentDocument", "shadowRoots", "templateContent", "pseudoElements", "importedDocument", "distributedNodes", "isSVG"]

    def __init__(self, nodeId: int, backendNodeId: int, nodeType: int, nodeName: str, localName: str, nodeValue: str, parentId: Optional[int] = None, childNodeCount: Optional[int] = None, children: Optional[List[Union['Node', dict]]] = None, attributes: Optional[List[str]] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, internalSubset: Optional[str] = None, xmlVersion: Optional[str] = None, name: Optional[str] = None, value: Optional[str] = None, pseudoType: Optional[str] = None, shadowRootType: Optional[str] = None, frameId: Optional[str] = None, contentDocument: Optional[Union['Node', dict]] = None, shadowRoots: Optional[List[Union['Node', dict]]] = None, templateContent: Optional[Union['Node', dict]] = None, pseudoElements: Optional[List[Union['Node', dict]]] = None, importedDocument: Optional[Union['Node', dict]] = None, distributedNodes: Optional[List[Union['BackendNode', dict]]] = None, isSVG: Optional[bool] = None) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeId is not None:
            repr_args.append("nodeId={!r}".format(self.nodeId))
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        if self.nodeType is not None:
            repr_args.append("nodeType={!r}".format(self.nodeType))
        if self.nodeName is not None:
            repr_args.append("nodeName={!r}".format(self.nodeName))
        if self.localName is not None:
            repr_args.append("localName={!r}".format(self.localName))
        if self.nodeValue is not None:
            repr_args.append("nodeValue={!r}".format(self.nodeValue))
        if self.childNodeCount is not None:
            repr_args.append("childNodeCount={!r}".format(self.childNodeCount))
        if self.children is not None:
            repr_args.append("children={!r}".format(self.children))
        if self.attributes is not None:
            repr_args.append("attributes={!r}".format(self.attributes))
        if self.documentURL is not None:
            repr_args.append("documentURL={!r}".format(self.documentURL))
        if self.baseURL is not None:
            repr_args.append("baseURL={!r}".format(self.baseURL))
        if self.publicId is not None:
            repr_args.append("publicId={!r}".format(self.publicId))
        if self.systemId is not None:
            repr_args.append("systemId={!r}".format(self.systemId))
        if self.internalSubset is not None:
            repr_args.append("internalSubset={!r}".format(self.internalSubset))
        if self.xmlVersion is not None:
            repr_args.append("xmlVersion={!r}".format(self.xmlVersion))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.pseudoType is not None:
            repr_args.append("pseudoType={!r}".format(self.pseudoType))
        if self.shadowRootType is not None:
            repr_args.append("shadowRootType={!r}".format(self.shadowRootType))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.contentDocument is not None:
            repr_args.append("contentDocument={!r}".format(self.contentDocument))
        if self.shadowRoots is not None:
            repr_args.append("shadowRoots={!r}".format(self.shadowRoots))
        if self.templateContent is not None:
            repr_args.append("templateContent={!r}".format(self.templateContent))
        if self.pseudoElements is not None:
            repr_args.append("pseudoElements={!r}".format(self.pseudoElements))
        if self.importedDocument is not None:
            repr_args.append("importedDocument={!r}".format(self.importedDocument))
        if self.distributedNodes is not None:
            repr_args.append("distributedNodes={!r}".format(self.distributedNodes))
        if self.isSVG is not None:
            repr_args.append("isSVG={!r}".format(self.isSVG))
        return "Node(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Node', dict]]:
        """
        Safely create Node from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Node
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Node if creation did not fail
        :rtype: Optional[Union[dict, Node]]
        """
        if init is not None:
            try:
                ourselves = Node(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Node', dict]]]:
        """
        Safely create a new list Nodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Node instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Node instances if creation did not fail
        :rtype: Optional[List[Union[dict, Node]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Node.safe_create(it))
            return list_of_self
        else:
            return init


class BoxModel(object):
    """
    Box model.
    """

    __slots__ = ["content", "padding", "border", "margin", "width", "height", "shapeOutside"]

    def __init__(self, content: list, padding: list, border: list, margin: list, width: int, height: int, shapeOutside: Optional[Union['ShapeOutsideInfo', dict]] = None) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.content is not None:
            repr_args.append("content={!r}".format(self.content))
        if self.padding is not None:
            repr_args.append("padding={!r}".format(self.padding))
        if self.border is not None:
            repr_args.append("border={!r}".format(self.border))
        if self.margin is not None:
            repr_args.append("margin={!r}".format(self.margin))
        if self.width is not None:
            repr_args.append("width={!r}".format(self.width))
        if self.height is not None:
            repr_args.append("height={!r}".format(self.height))
        if self.shapeOutside is not None:
            repr_args.append("shapeOutside={!r}".format(self.shapeOutside))
        return "BoxModel(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['BoxModel', dict]]:
        """
        Safely create BoxModel from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of BoxModel
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of BoxModel if creation did not fail
        :rtype: Optional[Union[dict, BoxModel]]
        """
        if init is not None:
            try:
                ourselves = BoxModel(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['BoxModel', dict]]]:
        """
        Safely create a new list BoxModels from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list BoxModel instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of BoxModel instances if creation did not fail
        :rtype: Optional[List[Union[dict, BoxModel]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BoxModel.safe_create(it))
            return list_of_self
        else:
            return init


class BackendNode(object):
    """
    Backend node with a friendly name.
    """

    __slots__ = ["nodeType", "nodeName", "backendNodeId"]

    def __init__(self, nodeType: int, nodeName: str, backendNodeId: int) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.nodeType is not None:
            repr_args.append("nodeType={!r}".format(self.nodeType))
        if self.nodeName is not None:
            repr_args.append("nodeName={!r}".format(self.nodeName))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        return "BackendNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['BackendNode', dict]]:
        """
        Safely create BackendNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of BackendNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of BackendNode if creation did not fail
        :rtype: Optional[Union[dict, BackendNode]]
        """
        if init is not None:
            try:
                ourselves = BackendNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['BackendNode', dict]]]:
        """
        Safely create a new list BackendNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list BackendNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of BackendNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, BackendNode]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BackendNode.safe_create(it))
            return list_of_self
        else:
            return init


DOM_TYPES_TO_OBJECT = {
    "ShapeOutsideInfo": ShapeOutsideInfo,
    "Rect": Rect,
    "RGBA": RGBA,
    "Node": Node,
    "BoxModel": BoxModel,
    "BackendNode": BackendNode,
}