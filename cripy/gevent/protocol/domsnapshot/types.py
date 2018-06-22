from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.domdebugger import types as DOMDebugger

__all__ = [
    "NameValue",
    "LayoutTreeNode",
    "InlineTextBox",
    "DOMNode",
    "ComputedStyle",
    "DOMSNAPSHOT_TYPE_TO_OBJECT"
]


class NameValue(object):
    """
    A name/value pair.
    """

    __slots__ = ["name", "value"]

    def __init__(self, name, value):
        """
        :param name: Attribute/property name.
        :type name: str
        :param value: Attribute/property value.
        :type value: str
        """
        super(NameValue, self).__init__()
        self.name = name
        self.value = value

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "NameValue(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create NameValue from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NameValue
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NameValue if creation did not fail
        :rtype: Optional[Union[dict, NameValue]]
        """
        if init is not None:
            try:
                ourselves = NameValue(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list NameValues from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NameValue instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NameValue instances if creation did not fail
        :rtype: Optional[List[Union[dict, NameValue]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NameValue.safe_create(it))
            return list_of_self
        else:
            return init


class LayoutTreeNode(object):
    """
    Details of an element in the DOM tree with a LayoutObject.
    """

    __slots__ = ["domNodeIndex", "boundingBox", "layoutText", "inlineTextNodes", "styleIndex", "paintOrder"]

    def __init__(self, domNodeIndex, boundingBox, layoutText=None, inlineTextNodes=None, styleIndex=None, paintOrder=None):
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
        super(LayoutTreeNode, self).__init__()
        self.domNodeIndex = domNodeIndex
        self.boundingBox = DOM.Rect.safe_create(boundingBox)
        self.layoutText = layoutText
        self.inlineTextNodes = InlineTextBox.safe_create_from_list(inlineTextNodes)
        self.styleIndex = styleIndex
        self.paintOrder = paintOrder

    def __repr__(self):
        repr_args = []
        if self.domNodeIndex is not None:
            repr_args.append("domNodeIndex={!r}".format(self.domNodeIndex))
        if self.boundingBox is not None:
            repr_args.append("boundingBox={!r}".format(self.boundingBox))
        if self.layoutText is not None:
            repr_args.append("layoutText={!r}".format(self.layoutText))
        if self.inlineTextNodes is not None:
            repr_args.append("inlineTextNodes={!r}".format(self.inlineTextNodes))
        if self.styleIndex is not None:
            repr_args.append("styleIndex={!r}".format(self.styleIndex))
        if self.paintOrder is not None:
            repr_args.append("paintOrder={!r}".format(self.paintOrder))
        return "LayoutTreeNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LayoutTreeNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LayoutTreeNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LayoutTreeNode if creation did not fail
        :rtype: Optional[Union[dict, LayoutTreeNode]]
        """
        if init is not None:
            try:
                ourselves = LayoutTreeNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list LayoutTreeNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LayoutTreeNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LayoutTreeNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, LayoutTreeNode]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayoutTreeNode.safe_create(it))
            return list_of_self
        else:
            return init


class InlineTextBox(object):
    """
    Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.
    """

    __slots__ = ["boundingBox", "startCharacterIndex", "numCharacters"]

    def __init__(self, boundingBox, startCharacterIndex, numCharacters):
        """
        :param boundingBox: The absolute position bounding box.
        :type boundingBox: dict
        :param startCharacterIndex: The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type startCharacterIndex: int
        :param numCharacters: The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2.
        :type numCharacters: int
        """
        super(InlineTextBox, self).__init__()
        self.boundingBox = DOM.Rect.safe_create(boundingBox)
        self.startCharacterIndex = startCharacterIndex
        self.numCharacters = numCharacters

    def __repr__(self):
        repr_args = []
        if self.boundingBox is not None:
            repr_args.append("boundingBox={!r}".format(self.boundingBox))
        if self.startCharacterIndex is not None:
            repr_args.append("startCharacterIndex={!r}".format(self.startCharacterIndex))
        if self.numCharacters is not None:
            repr_args.append("numCharacters={!r}".format(self.numCharacters))
        return "InlineTextBox(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create InlineTextBox from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InlineTextBox
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InlineTextBox if creation did not fail
        :rtype: Optional[Union[dict, InlineTextBox]]
        """
        if init is not None:
            try:
                ourselves = InlineTextBox(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list InlineTextBoxs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InlineTextBox instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InlineTextBox instances if creation did not fail
        :rtype: Optional[List[Union[dict, InlineTextBox]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InlineTextBox.safe_create(it))
            return list_of_self
        else:
            return init


class DOMNode(object):
    """
    A Node in the DOM tree.
    """

    __slots__ = ["nodeType", "nodeName", "nodeValue", "textValue", "inputValue", "inputChecked", "optionSelected", "backendNodeId", "childNodeIndexes", "attributes", "pseudoElementIndexes", "layoutNodeIndex", "documentURL", "baseURL", "contentLanguage", "documentEncoding", "publicId", "systemId", "frameId", "contentDocumentIndex", "importedDocumentIndex", "templateContentIndex", "pseudoType", "shadowRootType", "isClickable", "eventListeners", "currentSourceURL", "originURL"]

    def __init__(self, nodeType, nodeName, nodeValue, backendNodeId, textValue=None, inputValue=None, inputChecked=None, optionSelected=None, childNodeIndexes=None, attributes=None, pseudoElementIndexes=None, layoutNodeIndex=None, documentURL=None, baseURL=None, contentLanguage=None, documentEncoding=None, publicId=None, systemId=None, frameId=None, contentDocumentIndex=None, importedDocumentIndex=None, templateContentIndex=None, pseudoType=None, shadowRootType=None, isClickable=None, eventListeners=None, currentSourceURL=None, originURL=None):
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
        super(DOMNode, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.nodeType is not None:
            repr_args.append("nodeType={!r}".format(self.nodeType))
        if self.nodeName is not None:
            repr_args.append("nodeName={!r}".format(self.nodeName))
        if self.nodeValue is not None:
            repr_args.append("nodeValue={!r}".format(self.nodeValue))
        if self.textValue is not None:
            repr_args.append("textValue={!r}".format(self.textValue))
        if self.inputValue is not None:
            repr_args.append("inputValue={!r}".format(self.inputValue))
        if self.inputChecked is not None:
            repr_args.append("inputChecked={!r}".format(self.inputChecked))
        if self.optionSelected is not None:
            repr_args.append("optionSelected={!r}".format(self.optionSelected))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        if self.childNodeIndexes is not None:
            repr_args.append("childNodeIndexes={!r}".format(self.childNodeIndexes))
        if self.attributes is not None:
            repr_args.append("attributes={!r}".format(self.attributes))
        if self.pseudoElementIndexes is not None:
            repr_args.append("pseudoElementIndexes={!r}".format(self.pseudoElementIndexes))
        if self.layoutNodeIndex is not None:
            repr_args.append("layoutNodeIndex={!r}".format(self.layoutNodeIndex))
        if self.documentURL is not None:
            repr_args.append("documentURL={!r}".format(self.documentURL))
        if self.baseURL is not None:
            repr_args.append("baseURL={!r}".format(self.baseURL))
        if self.contentLanguage is not None:
            repr_args.append("contentLanguage={!r}".format(self.contentLanguage))
        if self.documentEncoding is not None:
            repr_args.append("documentEncoding={!r}".format(self.documentEncoding))
        if self.publicId is not None:
            repr_args.append("publicId={!r}".format(self.publicId))
        if self.systemId is not None:
            repr_args.append("systemId={!r}".format(self.systemId))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.contentDocumentIndex is not None:
            repr_args.append("contentDocumentIndex={!r}".format(self.contentDocumentIndex))
        if self.importedDocumentIndex is not None:
            repr_args.append("importedDocumentIndex={!r}".format(self.importedDocumentIndex))
        if self.templateContentIndex is not None:
            repr_args.append("templateContentIndex={!r}".format(self.templateContentIndex))
        if self.pseudoType is not None:
            repr_args.append("pseudoType={!r}".format(self.pseudoType))
        if self.shadowRootType is not None:
            repr_args.append("shadowRootType={!r}".format(self.shadowRootType))
        if self.isClickable is not None:
            repr_args.append("isClickable={!r}".format(self.isClickable))
        if self.eventListeners is not None:
            repr_args.append("eventListeners={!r}".format(self.eventListeners))
        if self.currentSourceURL is not None:
            repr_args.append("currentSourceURL={!r}".format(self.currentSourceURL))
        if self.originURL is not None:
            repr_args.append("originURL={!r}".format(self.originURL))
        return "DOMNode(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create DOMNode from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DOMNode
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DOMNode if creation did not fail
        :rtype: Optional[Union[dict, DOMNode]]
        """
        if init is not None:
            try:
                ourselves = DOMNode(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list DOMNodes from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DOMNode instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DOMNode instances if creation did not fail
        :rtype: Optional[List[Union[dict, DOMNode]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DOMNode.safe_create(it))
            return list_of_self
        else:
            return init


class ComputedStyle(object):
    """
    A subset of the full ComputedStyle as defined by the request whitelist.
    """

    __slots__ = ["properties"]

    def __init__(self, properties):
        """
        :param properties: Name/value pairs of computed style properties.
        :type properties: List[dict]
        """
        super(ComputedStyle, self).__init__()
        self.properties = NameValue.safe_create_from_list(properties)

    def __repr__(self):
        repr_args = []
        if self.properties is not None:
            repr_args.append("properties={!r}".format(self.properties))
        return "ComputedStyle(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ComputedStyle from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ComputedStyle
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ComputedStyle if creation did not fail
        :rtype: Optional[Union[dict, ComputedStyle]]
        """
        if init is not None:
            try:
                ourselves = ComputedStyle(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ComputedStyles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ComputedStyle instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ComputedStyle instances if creation did not fail
        :rtype: Optional[List[Union[dict, ComputedStyle]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ComputedStyle.safe_create(it))
            return list_of_self
        else:
            return init


DOMSNAPSHOT_TYPE_TO_OBJECT = {
    "NameValue": NameValue,
    "LayoutTreeNode": LayoutTreeNode,
    "InlineTextBox": InlineTextBox,
    "DOMNode": DOMNode,
    "ComputedStyle": ComputedStyle,
}