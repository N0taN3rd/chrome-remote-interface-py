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

    def addRule(self, styleSheetId, ruleText, location, cb=None):
        """
        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :type styleSheetId: str
        :param ruleText: The text of a new rule.
        :type ruleText: str
        :param location: Text position of a new rule in the target style sheet.
        :type location: dict
        """
        def cb_wrapper(res):
            res['rule'] = Types.CSSRule.safe_create(res['rule'])
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if ruleText is not None:
            msg_dict['ruleText'] = ruleText
        if location is not None:
            msg_dict['location'] = location
        self.chrome.send('CSS.addRule', params=msg_dict, cb=cb_wrapper)


    def collectClassNames(self, styleSheetId, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        self.chrome.send('CSS.collectClassNames', params=msg_dict, cb=cb_wrapper)


    def createStyleSheet(self, frameId, cb=None):
        """
        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('CSS.createStyleSheet', params=msg_dict, cb=cb_wrapper)


    def disable(self, cb=None):
        self.chrome.send('CSS.disable')


    def enable(self, cb=None):
        self.chrome.send('CSS.enable')


    def forcePseudoState(self, nodeId, forcedPseudoClasses, cb=None):
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


    def getBackgroundColors(self, nodeId, cb=None):
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getBackgroundColors', params=msg_dict, cb=cb_wrapper)


    def getComputedStyleForNode(self, nodeId, cb=None):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb_wrapper(res):
            res['computedStyle'] = Types.CSSComputedStyleProperty.safe_create_from_list(res['computedStyle'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getComputedStyleForNode', params=msg_dict, cb=cb_wrapper)


    def getInlineStylesForNode(self, nodeId, cb=None):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb_wrapper(res):
            res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
            res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getInlineStylesForNode', params=msg_dict, cb=cb_wrapper)


    def getMatchedStylesForNode(self, nodeId, cb=None):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb_wrapper(res):
            res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
            res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
            res['matchedCSSRules'] = Types.RuleMatch.safe_create_from_list(res['matchedCSSRules'])
            res['pseudoElements'] = Types.PseudoElementMatches.safe_create_from_list(res['pseudoElements'])
            res['inherited'] = Types.InheritedStyleEntry.safe_create_from_list(res['inherited'])
            res['cssKeyframesRules'] = Types.CSSKeyframesRule.safe_create_from_list(res['cssKeyframesRules'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getMatchedStylesForNode', params=msg_dict, cb=cb_wrapper)


    def getMediaQueries(self, cb=None):
        def cb_wrapper(res):
            res['medias'] = Types.CSSMedia.safe_create_from_list(res['medias'])
            cb(res)
        self.chrome.send('CSS.getMediaQueries', cb=cb_wrapper)


    def getPlatformFontsForNode(self, nodeId, cb=None):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        def cb_wrapper(res):
            res['fonts'] = Types.PlatformFontUsage.safe_create_from_list(res['fonts'])
            cb(res)
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        self.chrome.send('CSS.getPlatformFontsForNode', params=msg_dict, cb=cb_wrapper)


    def getStyleSheetText(self, styleSheetId, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        self.chrome.send('CSS.getStyleSheetText', params=msg_dict, cb=cb_wrapper)


    def setEffectivePropertyValueForNode(self, nodeId, propertyName, value, cb=None):
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


    def setKeyframeKey(self, styleSheetId, range, keyText, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param keyText: The keyText
        :type keyText: str
        """
        def cb_wrapper(res):
            res['keyText'] = Types.Value.safe_create(res['keyText'])
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if keyText is not None:
            msg_dict['keyText'] = keyText
        self.chrome.send('CSS.setKeyframeKey', params=msg_dict, cb=cb_wrapper)


    def setMediaText(self, styleSheetId, range, text, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param text: The text
        :type text: str
        """
        def cb_wrapper(res):
            res['media'] = Types.CSSMedia.safe_create(res['media'])
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if text is not None:
            msg_dict['text'] = text
        self.chrome.send('CSS.setMediaText', params=msg_dict, cb=cb_wrapper)


    def setRuleSelector(self, styleSheetId, range, selector, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param selector: The selector
        :type selector: str
        """
        def cb_wrapper(res):
            res['selectorList'] = Types.SelectorList.safe_create(res['selectorList'])
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if selector is not None:
            msg_dict['selector'] = selector
        self.chrome.send('CSS.setRuleSelector', params=msg_dict, cb=cb_wrapper)


    def setStyleSheetText(self, styleSheetId, text, cb=None):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param text: The text
        :type text: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if text is not None:
            msg_dict['text'] = text
        self.chrome.send('CSS.setStyleSheetText', params=msg_dict, cb=cb_wrapper)


    def setStyleTexts(self, edits, cb=None):
        """
        :param edits: The edits
        :type edits: List[dict]
        """
        def cb_wrapper(res):
            res['styles'] = Types.CSSStyle.safe_create_from_list(res['styles'])
            cb(res)
        msg_dict = dict()
        if edits is not None:
            msg_dict['edits'] = edits
        self.chrome.send('CSS.setStyleTexts', params=msg_dict, cb=cb_wrapper)


    def startRuleUsageTracking(self, cb=None):
        self.chrome.send('CSS.startRuleUsageTracking')


    def stopRuleUsageTracking(self, cb=None):
        def cb_wrapper(res):
            res['ruleUsage'] = Types.RuleUsage.safe_create_from_list(res['ruleUsage'])
            cb(res)
        self.chrome.send('CSS.stopRuleUsageTracking', cb=cb_wrapper)


    def takeCoverageDelta(self, cb=None):
        def cb_wrapper(res):
            res['coverage'] = Types.RuleUsage.safe_create_from_list(res['coverage'])
            cb(res)
        self.chrome.send('CSS.takeCoverageDelta', cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

