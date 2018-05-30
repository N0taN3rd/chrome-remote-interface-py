from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.page import types as Page
from cripy.protocol.dom import types as DOM
from cripy.protocol.domdebugger import types as DOMDebugger


class NameValue(ProtocolType):
    """
    A name/value pair.
    """

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: Attribute/property name.
        :type name: str
        :param value: Attribute/property value.
        :type value: str
        """
        super().__init__()
        self.name = name
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['NameValue']:
        if init is not None:
            return NameValue(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['NameValue']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NameValue(**it))
            return list_of_self
        else:
            return init


class LayoutTreeNode(ProtocolType):
    """
    Details of an element in the DOM tree with a LayoutObject.
    """

    def __init__(self, domNodeIndex: int, boundingBox: Union['DOM.Rect', dict], layoutText: Optional[str] = None, inlineTextNodes: Optional[List[Union['InlineTextBox', dict]]] = None, styleIndex: Optional[int] = None, paintOrder: Optional[int] = None) -> None:
        """
        :param domNodeIndex: The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.
        :type domNodeIndex: int
        :param boundingBox: The absolute position bounding box.
        :type boundingBox: dict
        :param layoutText: Contents of the LayoutText, if any.
        :type layoutText: Optional[str]
        :param inlineTextNodes: The post-layout inline text nodes, if any.
        :type inlineTextNodes: Optional[List[dict]]
        :param styleIndex: Index into the `computedStyles` array returned by `getSnapshot`.
        :type styleIndex: Optional[int]
        :param paintOrder: Global paint order index, which is determined by the stacking order of the nodes. Nodes that are painted together will have the same index. Only provided if includePaintOrder in getSnapshot was true.
        :type paintOrder: Optional[int]
        """
        super().__init__()
        self.domNodeIndex = domNodeIndex
        self.boundingBox = DOM.Rect.safe_create(boundingBox)
        self.layoutText = layoutText
        self.inlineTextNodes = InlineTextBox.safe_create_from_list(inlineTextNodes)
        self.styleIndex = styleIndex
        self.paintOrder = paintOrder

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LayoutTreeNode']:
        if init is not None:
            return LayoutTreeNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LayoutTreeNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayoutTreeNode(**it))
            return list_of_self
        else:
            return init


class InlineTextBox(ProtocolType):
    """
    Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.
    """

    def __init__(self, boundingBox: Union['DOM.Rect', dict], startCharacterIndex: int, numCharacters: int) -> None:
        """
        :param boundingBox: The absolute position bounding box.
        :type boundingBox: dict
        :param startCharacterIndex: The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type startCharacterIndex: int
        :param numCharacters: The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type numCharacters: int
        """
        super().__init__()
        self.boundingBox = DOM.Rect.safe_create(boundingBox)
        self.startCharacterIndex = startCharacterIndex
        self.numCharacters = numCharacters

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InlineTextBox']:
        if init is not None:
            return InlineTextBox(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InlineTextBox']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InlineTextBox(**it))
            return list_of_self
        else:
            return init


class DOMNode(ProtocolType):
    """
    A Node in the DOM tree.
    """

    def __init__(self, nodeType: int, nodeName: str, nodeValue: str, backendNodeId: DOM.BackendNodeId, textValue: Optional[str] = None, inputValue: Optional[str] = None, inputChecked: Optional[bool] = None, optionSelected: Optional[bool] = None, childNodeIndexes: Optional[List[int]] = None, attributes: Optional[List[Union['NameValue', dict]]] = None, pseudoElementIndexes: Optional[List[int]] = None, layoutNodeIndex: Optional[int] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, contentLanguage: Optional[str] = None, documentEncoding: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, frameId: Optional[Page.FrameId] = None, contentDocumentIndex: Optional[int] = None, importedDocumentIndex: Optional[int] = None, templateContentIndex: Optional[int] = None, pseudoType: Optional[DOM.PseudoType] = None, shadowRootType: Optional[DOM.ShadowRootType] = None, isClickable: Optional[bool] = None, eventListeners: Optional[List[Union['DOMDebugger.EventListener', dict]]] = None, currentSourceURL: Optional[str] = None, originURL: Optional[str] = None) -> None:
        """
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param nodeValue: `Node`'s nodeValue.
        :type nodeValue: str
        :param textValue: Only set for textarea elements, contains the text value.
        :type textValue: Optional[str]
        :param inputValue: Only set for input elements, contains the input's associated text value.
        :type inputValue: Optional[str]
        :param inputChecked: Only set for radio and checkbox input elements, indicates if the element has been checked
        :type inputChecked: Optional[bool]
        :param optionSelected: Only set for option elements, indicates if the element has been selected
        :type optionSelected: Optional[bool]
        :param backendNodeId: `Node`'s id, corresponds to DOM.Node.backendNodeId.
        :type backendNodeId: int
        :param childNodeIndexes: The indexes of the node's child nodes in the `domNodes` array returned by `getSnapshot`, if any.
        :type childNodeIndexes: Optional[List[int]]
        :param attributes: Attributes of an `Element` node.
        :type attributes: Optional[List[dict]]
        :param pseudoElementIndexes: Indexes of pseudo elements associated with this node in the `domNodes` array returned by `getSnapshot`, if any.
        :type pseudoElementIndexes: Optional[List[int]]
        :param layoutNodeIndex: The index of the node's related layout tree node in the `layoutTreeNodes` array returned by `getSnapshot`, if any.
        :type layoutNodeIndex: Optional[int]
        :param documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :type documentURL: Optional[str]
        :param baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :type baseURL: Optional[str]
        :param contentLanguage: Only set for documents, contains the document's content language.
        :type contentLanguage: Optional[str]
        :param documentEncoding: Only set for documents, contains the document's character set encoding.
        :type documentEncoding: Optional[str]
        :param publicId: `DocumentType` node's publicId.
        :type publicId: Optional[str]
        :param systemId: `DocumentType` node's systemId.
        :type systemId: Optional[str]
        :param frameId: Frame ID for frame owner elements and also for the document node.
        :type frameId: Optional[str]
        :param contentDocumentIndex: The index of a frame owner element's content document in the `domNodes` array returned by `getSnapshot`, if any.
        :type contentDocumentIndex: Optional[int]
        :param importedDocumentIndex: Index of the imported document's node of a link element in the `domNodes` array returned by `getSnapshot`, if any.
        :type importedDocumentIndex: Optional[int]
        :param templateContentIndex: Index of the content node of a template element in the `domNodes` array returned by `getSnapshot`.
        :type templateContentIndex: Optional[int]
        :param pseudoType: Type of a pseudo element node.
        :type pseudoType: Optional[str]
        :param shadowRootType: Shadow root type.
        :type shadowRootType: Optional[str]
        :param isClickable: Whether this DOM node responds to mouse clicks. This includes nodes that have had click event listeners attached via JavaScript as well as anchor tags that naturally navigate when clicked.
        :type isClickable: Optional[bool]
        :param eventListeners: Details of the node's event listeners, if any.
        :type eventListeners: Optional[List[dict]]
        :param currentSourceURL: The selected url for nodes with a srcset attribute.
        :type currentSourceURL: Optional[str]
        :param originURL: The url of the script (if any) that generates this node.
        :type originURL: Optional[str]
        """
        super().__init__()
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.textValue = textValue
        self.inputValue = inputValue
        self.inputChecked = inputChecked
        self.optionSelected = optionSelected
        self.backendNodeId = backendNodeId
        self.childNodeIndexes = childNodeIndexes
        self.attributes = NameValue.safe_create_from_list(attributes)
        self.pseudoElementIndexes = pseudoElementIndexes
        self.layoutNodeIndex = layoutNodeIndex
        self.documentURL = documentURL
        self.baseURL = baseURL
        self.contentLanguage = contentLanguage
        self.documentEncoding = documentEncoding
        self.publicId = publicId
        self.systemId = systemId
        self.frameId = frameId
        self.contentDocumentIndex = contentDocumentIndex
        self.importedDocumentIndex = importedDocumentIndex
        self.templateContentIndex = templateContentIndex
        self.pseudoType = pseudoType
        self.shadowRootType = shadowRootType
        self.isClickable = isClickable
        self.eventListeners = DOMDebugger.EventListener.safe_create_from_list(eventListeners)
        self.currentSourceURL = currentSourceURL
        self.originURL = originURL

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DOMNode']:
        if init is not None:
            return DOMNode(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DOMNode']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DOMNode(**it))
            return list_of_self
        else:
            return init


class ComputedStyle(ProtocolType):
    """
    A subset of the full ComputedStyle as defined by the request whitelist.
    """

    def __init__(self, properties: List[Union['NameValue', dict]]) -> None:
        """
        :param properties: Name/value pairs of computed style properties.
        :type properties: List[dict]
        """
        super().__init__()
        self.properties = NameValue.safe_create_from_list(properties)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ComputedStyle']:
        if init is not None:
            return ComputedStyle(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ComputedStyle']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ComputedStyle(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "NameValue": NameValue,
    "LayoutTreeNode": LayoutTreeNode,
    "InlineTextBox": InlineTextBox,
    "DOMNode": DOMNode,
    "ComputedStyle": ComputedStyle,
}
