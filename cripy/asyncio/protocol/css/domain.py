from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.dom import types as DOM
from cripy.asyncio.protocol.css import events as Events
from cripy.asyncio.protocol.css import types as Types

__all__ = ["CSS"]


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

    events = Events.CSS_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new CSS object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def addRule(self, styleSheetId: str, ruleText: str, location: dict) -> Optional[dict]:
        """
        Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
position specified by `location`.

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
        mayberes = await self.chrome.send('CSS.addRule', msg_dict)
        res = await mayberes
        res['rule'] = Types.CSSRule.safe_create(res['rule'])
        return res

    async def collectClassNames(self, styleSheetId: str) -> Optional[dict]:
        """
        Returns all class names from specified stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        mayberes = await self.chrome.send('CSS.collectClassNames', msg_dict)
        res = await mayberes
        return res

    async def createStyleSheet(self, frameId: str) -> Optional[dict]:
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        mayberes = await self.chrome.send('CSS.createStyleSheet', msg_dict)
        res = await mayberes
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables the CSS agent for the given page.
        """
        mayberes = await self.chrome.send('CSS.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.
        """
        mayberes = await self.chrome.send('CSS.enable')
        return mayberes

    async def forcePseudoState(self, nodeId: int, forcedPseudoClasses: List[str]) -> Optional[dict]:
        """
        Ensures that the given node will have specified pseudo-classes whenever its style is computed by
the browser.

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
        mayberes = await self.chrome.send('CSS.forcePseudoState', msg_dict)
        return mayberes

    async def getBackgroundColors(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        mayberes = await self.chrome.send('CSS.getBackgroundColors', msg_dict)
        res = await mayberes
        return res

    async def getComputedStyleForNode(self, nodeId: int) -> Optional[dict]:
        """
        Returns the computed style for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        mayberes = await self.chrome.send('CSS.getComputedStyleForNode', msg_dict)
        res = await mayberes
        res['computedStyle'] = Types.CSSComputedStyleProperty.safe_create_from_list(res['computedStyle'])
        return res

    async def getInlineStylesForNode(self, nodeId: int) -> Optional[dict]:
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        mayberes = await self.chrome.send('CSS.getInlineStylesForNode', msg_dict)
        res = await mayberes
        res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
        res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
        return res

    async def getMatchedStylesForNode(self, nodeId: int) -> Optional[dict]:
        """
        Returns requested styles for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        mayberes = await self.chrome.send('CSS.getMatchedStylesForNode', msg_dict)
        res = await mayberes
        res['inlineStyle'] = Types.CSSStyle.safe_create(res['inlineStyle'])
        res['attributesStyle'] = Types.CSSStyle.safe_create(res['attributesStyle'])
        res['matchedCSSRules'] = Types.RuleMatch.safe_create_from_list(res['matchedCSSRules'])
        res['pseudoElements'] = Types.PseudoElementMatches.safe_create_from_list(res['pseudoElements'])
        res['inherited'] = Types.InheritedStyleEntry.safe_create_from_list(res['inherited'])
        res['cssKeyframesRules'] = Types.CSSKeyframesRule.safe_create_from_list(res['cssKeyframesRules'])
        return res

    async def getMediaQueries(self) -> Optional[dict]:
        """
        Returns all media queries parsed by the rendering engine.
        """
        mayberes = await self.chrome.send('CSS.getMediaQueries')
        res = await mayberes
        res['medias'] = Types.CSSMedia.safe_create_from_list(res['medias'])
        return res

    async def getPlatformFontsForNode(self, nodeId: int) -> Optional[dict]:
        """
        Requests information about platform fonts which we used to render child TextNodes in the given
node.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        mayberes = await self.chrome.send('CSS.getPlatformFontsForNode', msg_dict)
        res = await mayberes
        res['fonts'] = Types.PlatformFontUsage.safe_create_from_list(res['fonts'])
        return res

    async def getStyleSheetText(self, styleSheetId: str) -> Optional[dict]:
        """
        Returns the current textual content for a stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        mayberes = await self.chrome.send('CSS.getStyleSheetText', msg_dict)
        res = await mayberes
        return res

    async def setEffectivePropertyValueForNode(self, nodeId: int, propertyName: str, value: str) -> Optional[dict]:
        """
        Find a rule with the given active property for the given node and set the new value for this
property

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
        mayberes = await self.chrome.send('CSS.setEffectivePropertyValueForNode', msg_dict)
        return mayberes

    async def setKeyframeKey(self, styleSheetId: str, range: dict, keyText: str) -> Optional[dict]:
        """
        Modifies the keyframe rule key text.

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
        mayberes = await self.chrome.send('CSS.setKeyframeKey', msg_dict)
        res = await mayberes
        res['keyText'] = Types.Value.safe_create(res['keyText'])
        return res

    async def setMediaText(self, styleSheetId: str, range: dict, text: str) -> Optional[dict]:
        """
        Modifies the rule selector.

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
        mayberes = await self.chrome.send('CSS.setMediaText', msg_dict)
        res = await mayberes
        res['media'] = Types.CSSMedia.safe_create(res['media'])
        return res

    async def setRuleSelector(self, styleSheetId: str, range: dict, selector: str) -> Optional[dict]:
        """
        Modifies the rule selector.

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
        mayberes = await self.chrome.send('CSS.setRuleSelector', msg_dict)
        res = await mayberes
        res['selectorList'] = Types.SelectorList.safe_create(res['selectorList'])
        return res

    async def setStyleSheetText(self, styleSheetId: str, text: str) -> Optional[dict]:
        """
        Sets the new stylesheet text.

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
        mayberes = await self.chrome.send('CSS.setStyleSheetText', msg_dict)
        res = await mayberes
        return res

    async def setStyleTexts(self, edits: List[dict]) -> Optional[dict]:
        """
        Applies specified style edits one after another in the given order.

        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict['edits'] = edits
        mayberes = await self.chrome.send('CSS.setStyleTexts', msg_dict)
        res = await mayberes
        res['styles'] = Types.CSSStyle.safe_create_from_list(res['styles'])
        return res

    async def startRuleUsageTracking(self) -> Optional[dict]:
        """
        Enables the selector recording.
        """
        mayberes = await self.chrome.send('CSS.startRuleUsageTracking')
        return mayberes

    async def stopRuleUsageTracking(self) -> Optional[dict]:
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation)
        """
        mayberes = await self.chrome.send('CSS.stopRuleUsageTracking')
        res = await mayberes
        res['ruleUsage'] = Types.RuleUsage.safe_create_from_list(res['ruleUsage'])
        return res

    async def takeCoverageDelta(self) -> Optional[dict]:
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation)
        """
        mayberes = await self.chrome.send('CSS.takeCoverageDelta')
        res = await mayberes
        res['coverage'] = Types.RuleUsage.safe_create_from_list(res['coverage'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.CSS_EVENTS_TO_CLASS

