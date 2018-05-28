from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page
from cripy.protocol.domdebugger import types as DOMDebugger


class DOMNode(ChromeTypeBase):
    """A Node in the DOM tree."""
    def __init__(self, nodeType: int, nodeName: str, nodeValue: str, backendNodeId: 'DOM.BackendNodeId', textValue: Optional[str] = None, inputValue: Optional[str] = None, inputChecked: Optional[bool] = None, optionSelected: Optional[bool] = None, childNodeIndexes: Optional[List['int']] = None, attributes: Optional[List['NameValue']] = None, pseudoElementIndexes: Optional[List['int']] = None, layoutNodeIndex: Optional[int] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, contentLanguage: Optional[str] = None, documentEncoding: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, frameId: Optional['Page.FrameId'] = None, contentDocumentIndex: Optional[int] = None, importedDocumentIndex: Optional[int] = None, templateContentIndex: Optional[int] = None, pseudoType: Optional['DOM.PseudoType'] = None, shadowRootType: Optional['DOM.ShadowRootType'] = None, isClickable: Optional[bool] = None, eventListeners: Optional[List['DOMDebugger.EventListener']] = None, currentSourceURL: Optional[str] = None, originURL: Optional[str] = None) -> None:
        """
        :param int nodeType: `Node`'s nodeType.
        :param str nodeName: `Node`'s nodeName.
        :param str nodeValue: `Node`'s nodeValue.
        :param str textValue: Only set for textarea elements, contains the text value.
        :param str inputValue: Only set for input elements, contains the input's associated text value.
        :param bool inputChecked: Only set for radio and checkbox input elements, indicates if the element has been checked
        :param bool optionSelected: Only set for option elements, indicates if the element has been selected
        :param DOM.BackendNodeId backendNodeId: `Node`'s id, corresponds to DOM.Node.backendNodeId.
        :param array childNodeIndexes: The indexes of the node's child nodes in the `domNodes` array returned by `getSnapshot`, if any.
        :param array attributes: Attributes of an `Element` node.
        :param array pseudoElementIndexes: Indexes of pseudo elements associated with this node in the `domNodes` array returned by `getSnapshot`, if any.
        :param int layoutNodeIndex: The index of the node's related layout tree node in the `layoutTreeNodes` array returned by `getSnapshot`, if any.
        :param str documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :param str baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :param str contentLanguage: Only set for documents, contains the document's content language.
        :param str documentEncoding: Only set for documents, contains the document's character set encoding.
        :param str publicId: `DocumentType` node's publicId.
        :param str systemId: `DocumentType` node's systemId.
        :param Page.FrameId frameId: Frame ID for frame owner elements and also for the document node.
        :param int contentDocumentIndex: The index of a frame owner element's content document in the `domNodes` array returned by `getSnapshot`, if any.
        :param int importedDocumentIndex: Index of the imported document's node of a link element in the `domNodes` array returned by `getSnapshot`, if any.
        :param int templateContentIndex: Index of the content node of a template element in the `domNodes` array returned by `getSnapshot`.
        :param DOM.PseudoType pseudoType: Type of a pseudo element node.
        :param DOM.ShadowRootType shadowRootType: Shadow root type.
        :param bool isClickable: Whether this DOM node responds to mouse clicks. This includes nodes that have had click event listeners attached via JavaScript as well as anchor tags that naturally navigate when clicked.
        :param array eventListeners: Details of the node's event listeners, if any.
        :param str currentSourceURL: The selected url for nodes with a srcset attribute.
        :param str originURL: The url of the script (if any) that generates this node.
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


class InlineTextBox(ChromeTypeBase):
    """Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions."""
    def __init__(self, boundingBox: 'DOM.Rect', startCharacterIndex: int, numCharacters: int) -> None:
        """
        :param DOM.Rect boundingBox: The absolute position bounding box.
        :param int startCharacterIndex: The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :param int numCharacters: The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        """
        super().__init__()
        self.boundingBox: DOM.Rect = boundingBox
        self.startCharacterIndex: int = startCharacterIndex
        self.numCharacters: int = numCharacters


class LayoutTreeNode(ChromeTypeBase):
    """Details of an element in the DOM tree with a LayoutObject."""
    def __init__(self, domNodeIndex: int, boundingBox: 'DOM.Rect', layoutText: Optional[str] = None, inlineTextNodes: Optional[List['InlineTextBox']] = None, styleIndex: Optional[int] = None, paintOrder: Optional[int] = None) -> None:
        """
        :param int domNodeIndex: The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.
        :param DOM.Rect boundingBox: The absolute position bounding box.
        :param str layoutText: Contents of the LayoutText, if any.
        :param array inlineTextNodes: The post-layout inline text nodes, if any.
        :param int styleIndex: Index into the `computedStyles` array returned by `getSnapshot`.
        :param int paintOrder: Global paint order index, which is determined by the stacking order of the nodes. Nodes that are painted together will have the same index. Only provided if includePaintOrder in getSnapshot was true.
        """
        super().__init__()
        self.domNodeIndex: int = domNodeIndex
        self.boundingBox: DOM.Rect = boundingBox
        self.layoutText: Optional[str] = layoutText
        self.inlineTextNodes: Optional[List[InlineTextBox]] = inlineTextNodes
        self.styleIndex: Optional[int] = styleIndex
        self.paintOrder: Optional[int] = paintOrder


class ComputedStyle(ChromeTypeBase):
    """A subset of the full ComputedStyle as defined by the request whitelist."""
    def __init__(self, properties: List['NameValue']) -> None:
        """
        :param array properties: Name/value pairs of computed style properties.
        """
        super().__init__()
        self.properties: List[NameValue] = properties


class NameValue(ChromeTypeBase):
    """A name/value pair."""
    def __init__(self, name: str, value: str) -> None:
        """
        :param str name: Attribute/property name.
        :param str value: Attribute/property value.
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


