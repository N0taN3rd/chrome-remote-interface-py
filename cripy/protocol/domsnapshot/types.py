from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.page import types as Page
from cripy.protocol.dom import types as DOM
from cripy.protocol.domdebugger import types as DOMDebugger


class DOMNode(ChromeTypeBase):
    """A Node in the DOM tree."""

    def __init__(self, nodeType: int, nodeName: str, nodeValue: str, backendNodeId: 'DOM.BackendNodeId', textValue: Optional[str] = None, inputValue: Optional[str] = None, inputChecked: Optional[bool] = None, optionSelected: Optional[bool] = None, childNodeIndexes: Optional[List['int']] = None, attributes: Optional[List['NameValue']] = None, pseudoElementIndexes: Optional[List['int']] = None, layoutNodeIndex: Optional[int] = None, documentURL: Optional[str] = None, baseURL: Optional[str] = None, contentLanguage: Optional[str] = None, documentEncoding: Optional[str] = None, publicId: Optional[str] = None, systemId: Optional[str] = None, frameId: Optional['Page.FrameId'] = None, contentDocumentIndex: Optional[int] = None, importedDocumentIndex: Optional[int] = None, templateContentIndex: Optional[int] = None, pseudoType: Optional['DOM.PseudoType'] = None, shadowRootType: Optional['DOM.ShadowRootType'] = None, isClickable: Optional[bool] = None, eventListeners: Optional[List['DOMDebugger.EventListener']] = None, currentSourceURL: Optional[str] = None, originURL: Optional[str] = None) -> None:
        """
        :param nodeType: `Node`'s nodeType.
        :type int:
        :param nodeName: `Node`'s nodeName.
        :type str:
        :param nodeValue: `Node`'s nodeValue.
        :type str:
        :param textValue: Only set for textarea elements, contains the text value.
        :type str:
        :param inputValue: Only set for input elements, contains the input's associated text value.
        :type str:
        :param inputChecked: Only set for radio and checkbox input elements, indicates if the element has been
        checked
        :type bool:
        :param optionSelected: Only set for option elements, indicates if the element has been selected
        :type bool:
        :param backendNodeId: `Node`'s id, corresponds to DOM.Node.backendNodeId.
        :type DOM.BackendNodeId:
        :param childNodeIndexes: The indexes of the node's child nodes in the `domNodes` array returned by
        `getSnapshot`, if any.
        :type array:
        :param attributes: Attributes of an `Element` node.
        :type array:
        :param pseudoElementIndexes: Indexes of pseudo elements associated with this node in the `domNodes` array returned
        by `getSnapshot`, if any.
        :type array:
        :param layoutNodeIndex: The index of the node's related layout tree node in the `layoutTreeNodes` array
        returned by `getSnapshot`, if any.
        :type int:
        :param documentURL: Document URL that `Document` or `FrameOwner` node points to.
        :type str:
        :param baseURL: Base URL that `Document` or `FrameOwner` node uses for URL completion.
        :type str:
        :param contentLanguage: Only set for documents, contains the document's content language.
        :type str:
        :param documentEncoding: Only set for documents, contains the document's character set encoding.
        :type str:
        :param publicId: `DocumentType` node's publicId.
        :type str:
        :param systemId: `DocumentType` node's systemId.
        :type str:
        :param frameId: Frame ID for frame owner elements and also for the document node.
        :type Page.FrameId:
        :param contentDocumentIndex: The index of a frame owner element's content document in the `domNodes` array
        returned by `getSnapshot`, if any.
        :type int:
        :param importedDocumentIndex: Index of the imported document's node of a link element in the `domNodes` array
        returned by `getSnapshot`, if any.
        :type int:
        :param templateContentIndex: Index of the content node of a template element in the `domNodes` array returned by
        `getSnapshot`.
        :type int:
        :param pseudoType: Type of a pseudo element node.
        :type DOM.PseudoType:
        :param shadowRootType: Shadow root type.
        :type DOM.ShadowRootType:
        :param isClickable: Whether this DOM node responds to mouse clicks. This includes nodes that have had
        click event listeners attached via JavaScript as well as anchor tags that naturally
        navigate when clicked.
        :type bool:
        :param eventListeners: Details of the node's event listeners, if any.
        :type array:
        :param currentSourceURL: The selected url for nodes with a srcset attribute.
        :type str:
        :param originURL: The url of the script (if any) that generates this node.
        :type str:
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
        :param boundingBox: The absolute position bounding box.
        :type DOM.Rect:
        :param startCharacterIndex: The starting index in characters, for this post layout textbox substring. Characters
        that would be represented as a surrogate pair in UTF-16 have length 2.
        :type int:
        :param numCharacters: The number of characters in this post layout textbox substring. Characters that would
        be represented as a surrogate pair in UTF-16 have length 2.
        :type int:
        """
        super().__init__()
        self.boundingBox: DOM.Rect = boundingBox
        self.startCharacterIndex: int = startCharacterIndex
        self.numCharacters: int = numCharacters


class LayoutTreeNode(ChromeTypeBase):
    """Details of an element in the DOM tree with a LayoutObject."""

    def __init__(self, domNodeIndex: int, boundingBox: 'DOM.Rect', layoutText: Optional[str] = None, inlineTextNodes: Optional[List['InlineTextBox']] = None, styleIndex: Optional[int] = None, paintOrder: Optional[int] = None) -> None:
        """
        :param domNodeIndex: The index of the related DOM node in the `domNodes` array returned by `getSnapshot`.
        :type int:
        :param boundingBox: The absolute position bounding box.
        :type DOM.Rect:
        :param layoutText: Contents of the LayoutText, if any.
        :type str:
        :param inlineTextNodes: The post-layout inline text nodes, if any.
        :type array:
        :param styleIndex: Index into the `computedStyles` array returned by `getSnapshot`.
        :type int:
        :param paintOrder: Global paint order index, which is determined by the stacking order of the nodes.
        Nodes that are painted together will have the same index. Only provided if
        includePaintOrder in getSnapshot was true.
        :type int:
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
        :param properties: Name/value pairs of computed style properties.
        :type array:
        """
        super().__init__()
        self.properties: List[NameValue] = properties


class NameValue(ChromeTypeBase):
    """A name/value pair."""

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: Attribute/property name.
        :type str:
        :param value: Attribute/property value.
        :type str:
        """
        super().__init__()
        self.name: str = name
        self.value: str = value


