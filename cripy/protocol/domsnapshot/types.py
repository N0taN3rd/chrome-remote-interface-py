from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.domdebugger import types as DOMDebugger
from cripy.protocol.dom import types as DOM
from cripy.protocol.page import types as Page


class DOMNode(ChromeTypeBase):

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
        childNodeIndexes: Optional[List["int"]] = None,
        attributes: Optional[List["NameValue"]] = None,
        pseudoElementIndexes: Optional[List["int"]] = None,
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
        eventListeners: Optional[List["DOMDebugger.EventListener"]] = None,
        currentSourceURL: Optional[str] = None,
        originURL: Optional[str] = None,
    ) -> None:
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

    def __init__(
        self, boundingBox: "DOM.Rect", startCharacterIndex: int, numCharacters: int
    ) -> None:
        super().__init__()
        self.boundingBox: DOM.Rect = boundingBox
        self.startCharacterIndex: int = startCharacterIndex
        self.numCharacters: int = numCharacters


class LayoutTreeNode(ChromeTypeBase):

    def __init__(
        self,
        domNodeIndex: int,
        boundingBox: "DOM.Rect",
        layoutText: Optional[str] = None,
        inlineTextNodes: Optional[List["InlineTextBox"]] = None,
        styleIndex: Optional[int] = None,
        paintOrder: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.domNodeIndex: int = domNodeIndex
        self.boundingBox: DOM.Rect = boundingBox
        self.layoutText: Optional[str] = layoutText
        self.inlineTextNodes: Optional[List[InlineTextBox]] = inlineTextNodes
        self.styleIndex: Optional[int] = styleIndex
        self.paintOrder: Optional[int] = paintOrder


class ComputedStyle(ChromeTypeBase):

    def __init__(self, properties: List["NameValue"]) -> None:
        super().__init__()
        self.properties: List[NameValue] = properties


class NameValue(ChromeTypeBase):

    def __init__(self, name: str, value: str) -> None:
        super().__init__()
        self.name: str = name
        self.value: str = value
