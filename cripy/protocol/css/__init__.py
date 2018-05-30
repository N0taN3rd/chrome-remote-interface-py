from typing import Any, List, Optional, Union
from cripy.protocol.page import types as Page
from cripy.protocol.dom import types as DOM
from cripy.protocol.css import events as Events
from cripy.protocol.css import types as Types


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

    async def addRule(self, styleSheetId: str, ruleText: str, location: dict) -> Optional[dict]:
        """
        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :type styleSheetId: str
        :param ruleText: The text of a new rule.
        :type ruleText: str
        :param location: Text position of a new rule in the target style sheet.
        :type location: dict
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if ruleText is not None:
            msg_dict['ruleText'] = ruleText
        if location is not None:
            msg_dict['location'] = location
        res = await self.chrome.send('CSS.addRule', msg_dict)
        res['rule'] = Types.CSSRule.safe_create(res['rule'])
        return res

    async def collectClassNames(self, styleSheetId: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        res = await self.chrome.send('CSS.collectClassNames', msg_dict)
        return res

    async def createStyleSheet(self, frameId: str) -> Optional[dict]:
        """
        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        res = await self.chrome.send('CSS.createStyleSheet', msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.enable')
        return res

    async def forcePseudoState(self, nodeId: int, forcedPseudoClasses: List[str]) -> Optional[dict]:
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
        res = await self.chrome.send('CSS.forcePseudoState', msg_dict)
        return res

    async def getBackgroundColors(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('CSS.getBackgroundColors', msg_dict)
        return res

    async def getComputedStyleForNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('CSS.getComputedStyleForNode', msg_dict)
        res['computedStyle'] = Types.TypesComputedStyleProperty.safe_create_from_list(res['computedStyle'])
        return res

    async def getInlineStylesForNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('CSS.getInlineStylesForNode', msg_dict)
        res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
        res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
        return res

    async def getMatchedStylesForNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('CSS.getMatchedStylesForNode', msg_dict)
        res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
        res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
        res['matchedCSSRules'] = Types.RuleMatch.safe_create_from_list(res['matchedCSSRules'])
        res['pseudoElements'] = Types.PseudoElementMatches.safe_create_from_list(res['pseudoElements'])
        res['inherited'] = Types.InheritedStyleEntry.safe_create_from_list(res['inherited'])
        res['cssKeyframesRules'] = Types.TypesKeyframesRule.safe_create_from_list(res['cssKeyframesRules'])
        return res

    async def getMediaQueries(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.getMediaQueries')
        res['medias'] = Types.TypesMedia.safe_create_from_list(res['medias'])
        return res

    async def getPlatformFontsForNode(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        res = await self.chrome.send('CSS.getPlatformFontsForNode', msg_dict)
        res['fonts'] = Types.PlatformFontUsage.safe_create_from_list(res['fonts'])
        return res

    async def getStyleSheetText(self, styleSheetId: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        res = await self.chrome.send('CSS.getStyleSheetText', msg_dict)
        return res

    async def setEffectivePropertyValueForNode(self, nodeId: int, propertyName: str, value: str) -> Optional[dict]:
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
        res = await self.chrome.send('CSS.setEffectivePropertyValueForNode', msg_dict)
        return res

    async def setKeyframeKey(self, styleSheetId: str, range: dict, keyText: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param keyText: The keyText
        :type keyText: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if keyText is not None:
            msg_dict['keyText'] = keyText
        res = await self.chrome.send('CSS.setKeyframeKey', msg_dict)
        res['keyText'] = Types.Value.safe_create(res['keyText'])
        return res

    async def setMediaText(self, styleSheetId: str, range: dict, text: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param text: The text
        :type text: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if text is not None:
            msg_dict['text'] = text
        res = await self.chrome.send('CSS.setMediaText', msg_dict)
        res['media'] = Types.CSSMedia.safe_create(res['media'])
        return res

    async def setRuleSelector(self, styleSheetId: str, range: dict, selector: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param selector: The selector
        :type selector: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if range is not None:
            msg_dict['range'] = range
        if selector is not None:
            msg_dict['selector'] = selector
        res = await self.chrome.send('CSS.setRuleSelector', msg_dict)
        res['selectorList'] = Types.SelectorList.safe_create(res['selectorList'])
        return res

    async def setStyleSheetText(self, styleSheetId: str, text: str) -> Optional[dict]:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param text: The text
        :type text: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        if text is not None:
            msg_dict['text'] = text
        res = await self.chrome.send('CSS.setStyleSheetText', msg_dict)
        return res

    async def setStyleTexts(self, edits: List[dict]) -> Optional[dict]:
        """
        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict['edits'] = edits
        res = await self.chrome.send('CSS.setStyleTexts', msg_dict)
        res['styles'] = Types.TypesStyle.safe_create_from_list(res['styles'])
        return res

    async def startRuleUsageTracking(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.startRuleUsageTracking')
        return res

    async def stopRuleUsageTracking(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.stopRuleUsageTracking')
        res['ruleUsage'] = Types.RuleUsage.safe_create_from_list(res['ruleUsage'])
        return res

    async def takeCoverageDelta(self) -> Optional[dict]:
        res = await self.chrome.send('CSS.takeCoverageDelta')
        res['coverage'] = Types.RuleUsage.safe_create_from_list(res['coverage'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

