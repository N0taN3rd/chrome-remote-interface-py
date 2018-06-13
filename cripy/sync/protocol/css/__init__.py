from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.page import types as Page
from cripy.sync.protocol.css import events as Events
from cripy.sync.protocol.css import types as Types

__all__ = ["CSS"] + Events.__all__ + Types.__all__ 


class CSS(object):
    """
    This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
have an associated `id` used in subsequent operations on the related object. Each object type has
a specific `id` structure, and those are not interchangeable between objects of different kinds.
CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.
    """

    dependencies = ['DOM']

    def __init__(self, chrome):
        self.chrome = chrome

    def addRule(self, styleSheetId, ruleText, location):
        """
        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :type styleSheetId: str
        :param ruleText: The text of a new rule.
        :type ruleText: str
        :param location: Text position of a new rule in the target style sheet.
        :type location: dict
        """
        def cb(res):
            res['rule'] = Types.CSSRule.safe_create(res['rule'])
            self.chrome.emit('CSS.addRule', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if ruleText is not None:
            msg_dict['ruleText'] = ruleText
        if location is not None:
            msg_dict['location'] = location
        self.chrome.send('CSS.addRule', params=msg_dict, cb=cb)


    def collectClassNames(self, styleSheetId):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        def cb(res):
            self.chrome.emit('CSS.collectClassNames', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        self.chrome.send('CSS.collectClassNames', params=msg_dict, cb=cb)


    def createStyleSheet(self, frameId):
        """
        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        def cb(res):
            self.chrome.emit('CSS.createStyleSheet', res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('CSS.createStyleSheet', params=msg_dict, cb=cb)


    def disable(self):
        self.chrome.send('CSS.disable')


    def enable(self):
        self.chrome.send('CSS.enable')


    def forcePseudoState(self, nodeId, forcedPseudoClasses):
        """
        :param nodeId: The element id for which to force the pseudo state.
        :type nodeId: int
        :param forcedPseudoClasses: Element pseudo classes to force when computing the element's style.
        :type forcedPseudoClasses: List[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if forcedPseudoClasses is not None:
            msg_dict['forcedPseudoClasses'] = forcedPseudoClasses
        self.chrome.send('CSS.forcePseudoState', params=msg_dict)


    def getBackgroundColors(self, nodeId):
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        def cb(res):
            self.chrome.emit('CSS.getBackgroundColors', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getBackgroundColors', params=msg_dict, cb=cb)


    def getComputedStyleForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb(res):
            res['computedStyle'] = Types.CSSComputedStyleProperty.safe_create_from_list(res['computedStyle'])
            self.chrome.emit('CSS.getComputedStyleForNode', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getComputedStyleForNode', params=msg_dict, cb=cb)


    def getInlineStylesForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb(res):
            res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
            res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
            self.chrome.emit('CSS.getInlineStylesForNode', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getInlineStylesForNode', params=msg_dict, cb=cb)


    def getMatchedStylesForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb(res):
            res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
            res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
            res['matchedCSSRules'] = Types.RuleMatch.safe_create_from_list(res['matchedCSSRules'])
            res['pseudoElements'] = Types.PseudoElementMatches.safe_create_from_list(res['pseudoElements'])
            res['inherited'] = Types.InheritedStyleEntry.safe_create_from_list(res['inherited'])
            res['cssKeyframesRules'] = Types.CSSKeyframesRule.safe_create_from_list(res['cssKeyframesRules'])
            self.chrome.emit('CSS.getMatchedStylesForNode', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getMatchedStylesForNode', params=msg_dict, cb=cb)


    def getMediaQueries(self):
        def cb(res):
            res['medias'] = Types.CSSMedia.safe_create_from_list(res['medias'])
            self.chrome.emit('CSS.getMediaQueries', res)
        self.chrome.send('CSS.getMediaQueries', cb=cb)


    def getPlatformFontsForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb(res):
            res['fonts'] = Types.PlatformFontUsage.safe_create_from_list(res['fonts'])
            self.chrome.emit('CSS.getPlatformFontsForNode', res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getPlatformFontsForNode', params=msg_dict, cb=cb)


    def getStyleSheetText(self, styleSheetId):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        def cb(res):
            self.chrome.emit('CSS.getStyleSheetText', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        self.chrome.send('CSS.getStyleSheetText', params=msg_dict, cb=cb)


    def setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
        """
        :param nodeId: The element id for which to set property.
        :type nodeId: int
        :param propertyName: The propertyName
        :type propertyName: str
        :param value: The value
        :type value: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        if propertyName is not None:
            msg_dict['propertyName'] = propertyName
        if value is not None:
            msg_dict['value'] = value
        self.chrome.send('CSS.setEffectivePropertyValueForNode', params=msg_dict)


    def setKeyframeKey(self, styleSheetId, range, keyText):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param keyText: The keyText
        :type keyText: str
        """
        def cb(res):
            res['keyText'] = Types.Value.safe_create(res['keyText'])
            self.chrome.emit('CSS.setKeyframeKey', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if keyText is not None:
            msg_dict['keyText'] = keyText
        self.chrome.send('CSS.setKeyframeKey', params=msg_dict, cb=cb)


    def setMediaText(self, styleSheetId, range, text):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param text: The text
        :type text: str
        """
        def cb(res):
            res['media'] = Types.CSSMedia.safe_create(res['media'])
            self.chrome.emit('CSS.setMediaText', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if text is not None:
            msg_dict['text'] = text
        self.chrome.send('CSS.setMediaText', params=msg_dict, cb=cb)


    def setRuleSelector(self, styleSheetId, range, selector):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param selector: The selector
        :type selector: str
        """
        def cb(res):
            res['selectorList'] = Types.SelectorList.safe_create(res['selectorList'])
            self.chrome.emit('CSS.setRuleSelector', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('CSS.setRuleSelector', params=msg_dict, cb=cb)


    def setStyleSheetText(self, styleSheetId, text):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param text: The text
        :type text: str
        """
        def cb(res):
            self.chrome.emit('CSS.setStyleSheetText', res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if text is not None:
            msg_dict['text'] = text
        self.chrome.send('CSS.setStyleSheetText', params=msg_dict, cb=cb)


    def setStyleTexts(self, edits):
        """
        :param edits: The edits
        :type edits: List[dict]
        """
        def cb(res):
            res['styles'] = Types.CSSStyle.safe_create_from_list(res['styles'])
            self.chrome.emit('CSS.setStyleTexts', res)
        msg_dict = dict()
        if edits is not None:
            msg_dict['edits'] = edits
        self.chrome.send('CSS.setStyleTexts', params=msg_dict, cb=cb)


    def startRuleUsageTracking(self):
        self.chrome.send('CSS.startRuleUsageTracking')


    def stopRuleUsageTracking(self):
        def cb(res):
            res['ruleUsage'] = Types.RuleUsage.safe_create_from_list(res['ruleUsage'])
            self.chrome.emit('CSS.stopRuleUsageTracking', res)
        self.chrome.send('CSS.stopRuleUsageTracking', cb=cb)


    def takeCoverageDelta(self):
        def cb(res):
            res['coverage'] = Types.RuleUsage.safe_create_from_list(res['coverage'])
            self.chrome.emit('CSS.takeCoverageDelta', res)
        self.chrome.send('CSS.takeCoverageDelta', cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

