from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM
from cripy.protocol.domdebugger import types as DOMDebugger
from cripy.protocol.page import types as Page


class NameValue(ProtocolType):
    """A name/value pair."""

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: Attribute/property name.
        :type name: str
        :param value: Attribute/property value.
        :type value: str
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


class LayoutTreeNode(ProtocolType):
    """Details of an element in the DOM tree with a LayoutObject."""

    def __init__(
        self,
        domNodeIndex: int,
        boundingBox: "DOM.Rect",
        layoutText: Optional[str] = None,
        inlineTextNodes: Optional[List[Union["InlineTextBox", dict]]] = None,
        styleIndex: Optional[int] = None,
        paintOrder: Optional[int] = None,
    ) -> None:
        """
        :param domNodeIndex: The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.
        :type domNodeIndex: int
        :param boundingBox: The absolute position bounding box.
        :type boundingBox: DOM.Rect
        :param layoutText: Contents of the LayoutText, if any.
        :type layoutText: str
        :param inlineTextNodes: The post-layout inline text nodes, if any.
        :type inlineTextNodes: array
        :param styleIndex: Index into the `computedStyles` array returned by `getSnapshot`.
        :type styleIndex: int
        :param paintOrder: Global paint order index, which is determined by the stacking order of the nodes. Nodes that are painted together will have the same index. Only provided if includePaintOrder in getSnapshot was true.
        :type paintOrder: int
        """
        super().__init__()
        self.domNodeIndex: int = domNodeIndex
        self.boundingBox: DOM.Rect = boundingBox
        self.layoutText: Optional[str] = layoutText
        self.inlineTextNodes: Optional[List[InlineTextBox]] = inlineTextNodes
        self.styleIndex: Optional[int] = styleIndex
        self.paintOrder: Optional[int] = paintOrder


class InlineTextBox(ProtocolType):
    """Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions."""

    def __init__(
        self, boundingBox: "DOM.Rect", startCharacterIndex: int, numCharacters: int
    ) -> None:
        """
        :param boundingBox: The absolute position bounding box.
        :type boundingBox: DOM.Rect
        :param startCharacterIndex: The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type startCharacterIndex: int
        :param numCharacters: The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type numCharacters: int
        """
        super().__init__()
        self.boundingBox: DOM.Rect = boundingBox
        self.startCharacterIndex: int = startCharacterIndex
        self.numCharacters: int = numCharacters


class DOMNode(ProtocolType):
    """A Node in the DOM tree."""

    def __init__(
        self,
        nodeType: int,
        nodeName: str,
        nodeValue: str,
        backendNodeId: "DOM.BackendNodeId",
        textValue: Optional[str] = None,
        inputValue: Optional[str] = None,
        inputChecked: Optional[bool] = None,
        optionSelected: Optional[bool] = None,
        childNodeIndexes: Optional[List[int]] = None,
        attributes: Optional[List[Union["NameValue", dict]]] = None,
        pseudoElementIndexes: Optional[List[int]] = None,
        layoutNodeIndex: Optional[int] = None,
        documentURL: Optional[str] = None,
        baseURL: Optional[str] = None,
        contentLanguage: Optional[str] = None,
        documentEncoding: Optional[str] = None,
        publicId: Optional[str] = None,
        systemId: Optional[str] = None,
        frameId: Optional["Page.FrameId"] = None,
        contentDocumentIndex: Optional[int] = None,
        importedDocumentIndex: Optional[int] = None,
        templateContentIndex: Optional[int] = None,
        pseudoType: Optional["DOM.PseudoType"] = None,
        shadowRootType: Optional["DOM.ShadowRootType"] = None,
        isClickable: Optional[bool] = None,
        eventListeners: Optional[List[Union["DOMDebugger.EventListener", dict]]] = None,
        currentSourceURL: Optional[str] = None,
        originURL: Optional[str] = None,
    ) -> None:
        """
        :param nodeType: `Node`'s nodeType.
        :type nodeType: int
        :param nodeName: `Node`'s nodeName.
        :type nodeName: str
        :param nodeValue: `Node`'s nodeValue.
        :type nodeValue: str
        :param textValue: Only set for textarea elements, contains the text value.
        :type textValue: str
        :param inputValue: Only set for input elements, contains the input's associated text value.
        :type inputValue: str
        :param inputChecked: Only set for radio and checkbox input elements, indicates if the element has been checked
        :type inputChecked: bool
        :param optionSelected: Only set for option elements, indicates if the element has been selected
        :type optionSelected: bool
        :param backendNodeId: `Node`'s id, corresponds to DOM.Node.backendNodeId.
        :type backendNodeId: DOM.BackendNodeId
        :param childNodeIndexes: The indexes of the node's child nodes in the `domNodes` array returned by `getSnapshot`, if any.
        :type childNodeIndexes: array
        :param attributes: Attributes of an `Element` node.
        :type attributes: array
        :param pseudoElementIndexes: Indexes of pseudo elements associated with this node in the `domNodes` array returned by `getSnapshot`, if any.
        :type pseudoElementIndexes: array
        :param layoutNodeIndex: The index of the node's related layout tree node in the `layoutTreeNodes` array returned by `getSnapshot`, if any.
        :type layoutNodeIndex: int
        :param documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :type documentURL: str
        :param baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :type baseURL: str
        :param contentLanguage: Only set for documents, contains the document's content language.
        :type contentLanguage: str
        :param documentEncoding: Only set for documents, contains the document's character set encoding.
        :type documentEncoding: str
        :param publicId: `DocumentType` node's publicId.
        :type publicId: str
        :param systemId: `DocumentType` node's systemId.
        :type systemId: str
        :param frameId: Frame ID for frame owner elements and also for the document node.
        :type frameId: Page.FrameId
        :param contentDocumentIndex: The index of a frame owner element's content document in the `domNodes` array returned by `getSnapshot`, if any.
        :type contentDocumentIndex: int
        :param importedDocumentIndex: Index of the imported document's node of a link element in the `domNodes` array returned by `getSnapshot`, if any.
        :type importedDocumentIndex: int
        :param templateContentIndex: Index of the content node of a template element in the `domNodes` array returned by `getSnapshot`.
        :type templateContentIndex: int
        :param pseudoType: Type of a pseudo element node.
        :type pseudoType: DOM.PseudoType
        :param shadowRootType: Shadow root type.
        :type shadowRootType: DOM.ShadowRootType
        :param isClickable: Whether this DOM node responds to mouse clicks. This includes nodes that have had click event listeners attached via JavaScript as well as anchor tags that naturally navigate when clicked.
        :type isClickable: bool
        :param eventListeners: Details of the node's event listeners, if any.
        :type eventListeners: array
        :param currentSourceURL: The selected url for nodes with a srcset attribute.
        :type currentSourceURL: str
        :param originURL: The url of the script (if any) that generates this node.
        :type originURL: str
        """
        super().__init__()
        self.nodeType: int = nodeType
        self.nodeName: str = nodeName
        self.nodeValue: str = nodeValue
        self.textValue: Optional[str] = textValue
        self.inputValue: Optional[str] = inputValue
        self.inputChecked: Optional[bool] = inputChecked
        self.optionSelected: Optional[bool] = optionSelected
        self.backendNodeId: DOM.BackendNodeId = backendNodeId
        self.childNodeIndexes: Optional[List[int]] = childNodeIndexes
        self.attributes: Optional[List[NameValue]] = attributes
        self.pseudoElementIndexes: Optional[List[int]] = pseudoElementIndexes
        self.layoutNodeIndex: Optional[int] = layoutNodeIndex
        self.documentURL: Optional[str] = documentURL
        self.baseURL: Optional[str] = baseURL
        self.contentLanguage: Optional[str] = contentLanguage
        self.documentEncoding: Optional[str] = documentEncoding
        self.publicId: Optional[str] = publicId
        self.systemId: Optional[str] = systemId
        self.frameId: Optional[Page.FrameId] = frameId
        self.contentDocumentIndex: Optional[int] = contentDocumentIndex
        self.importedDocumentIndex: Optional[int] = importedDocumentIndex
        self.templateContentIndex: Optional[int] = templateContentIndex
        self.pseudoType: Optional[DOM.PseudoType] = pseudoType
        self.shadowRootType: Optional[DOM.ShadowRootType] = shadowRootType
        self.isClickable: Optional[bool] = isClickable
        self.eventListeners: Optional[List[DOMDebugger.EventListener]] = eventListeners
        self.currentSourceURL: Optional[str] = currentSourceURL
        self.originURL: Optional[str] = originURL


class ComputedStyle(ProtocolType):
    """A subset of the full ComputedStyle as defined by the request whitelist."""

    def __init__(self, properties: List[Union["NameValue", dict]]) -> None:
        """
        :param properties: Name/value pairs of computed style properties.
        :type properties: array
        """
        super().__init__()
        self.properties: List[NameValue] = properties


OBJECT_LIST = {
    "NameValue": NameValue,
    "LayoutTreeNode": LayoutTreeNode,
    "InlineTextBox": InlineTextBox,
    "DOMNode": DOMNode,
    "ComputedStyle": ComputedStyle,
}
