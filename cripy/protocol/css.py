# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

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

    dependencies: ClassVar[List[str]] = ["DOM"]

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def addRule(
        self, styleSheetId: str, ruleText: str, location: dict
    ) -> Optional[dict]:
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
            msg_dict["styleSheetId"] = styleSheetId
        if ruleText is not None:
            msg_dict["ruleText"] = ruleText
        if location is not None:
            msg_dict["location"] = location
        res = await self.client.send("CSS.addRule", msg_dict)
        return res

    async def collectClassNames(self, styleSheetId: str) -> Optional[dict]:
        """
        Returns all class names from specified stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        res = await self.client.send("CSS.collectClassNames", msg_dict)
        return res

    async def createStyleSheet(self, frameId: str) -> Optional[dict]:
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        res = await self.client.send("CSS.createStyleSheet", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables the CSS agent for the given page.
        """
        res = await self.client.send("CSS.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.
        """
        res = await self.client.send("CSS.enable")
        return res

    async def forcePseudoState(
        self, nodeId: int, forcedPseudoClasses: List[str]
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if forcedPseudoClasses is not None:
            msg_dict["forcedPseudoClasses"] = forcedPseudoClasses
        res = await self.client.send("CSS.forcePseudoState", msg_dict)
        return res

    async def getBackgroundColors(self, nodeId: int) -> Optional[dict]:
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("CSS.getBackgroundColors", msg_dict)
        return res

    async def getComputedStyleForNode(self, nodeId: int) -> Optional[dict]:
        """
        Returns the computed style for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("CSS.getComputedStyleForNode", msg_dict)
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
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("CSS.getInlineStylesForNode", msg_dict)
        return res

    async def getMatchedStylesForNode(self, nodeId: int) -> Optional[dict]:
        """
        Returns requested styles for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("CSS.getMatchedStylesForNode", msg_dict)
        return res

    async def getMediaQueries(self) -> Optional[dict]:
        """
        Returns all media queries parsed by the rendering engine.
        """
        res = await self.client.send("CSS.getMediaQueries")
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
            msg_dict["nodeId"] = nodeId
        res = await self.client.send("CSS.getPlatformFontsForNode", msg_dict)
        return res

    async def getStyleSheetText(self, styleSheetId: str) -> Optional[dict]:
        """
        Returns the current textual content for a stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        res = await self.client.send("CSS.getStyleSheetText", msg_dict)
        return res

    async def setEffectivePropertyValueForNode(
        self, nodeId: int, propertyName: str, value: str
    ) -> Optional[dict]:
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
            msg_dict["nodeId"] = nodeId
        if propertyName is not None:
            msg_dict["propertyName"] = propertyName
        if value is not None:
            msg_dict["value"] = value
        res = await self.client.send("CSS.setEffectivePropertyValueForNode", msg_dict)
        return res

    async def setKeyframeKey(
        self, styleSheetId: str, range: dict, keyText: str
    ) -> Optional[dict]:
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
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if keyText is not None:
            msg_dict["keyText"] = keyText
        res = await self.client.send("CSS.setKeyframeKey", msg_dict)
        return res

    async def setMediaText(
        self, styleSheetId: str, range: dict, text: str
    ) -> Optional[dict]:
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
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if text is not None:
            msg_dict["text"] = text
        res = await self.client.send("CSS.setMediaText", msg_dict)
        return res

    async def setRuleSelector(
        self, styleSheetId: str, range: dict, selector: str
    ) -> Optional[dict]:
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
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if selector is not None:
            msg_dict["selector"] = selector
        res = await self.client.send("CSS.setRuleSelector", msg_dict)
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
            msg_dict["styleSheetId"] = styleSheetId
        if text is not None:
            msg_dict["text"] = text
        res = await self.client.send("CSS.setStyleSheetText", msg_dict)
        return res

    async def setStyleTexts(self, edits: List[dict]) -> Optional[dict]:
        """
        Applies specified style edits one after another in the given order.

        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict["edits"] = edits
        res = await self.client.send("CSS.setStyleTexts", msg_dict)
        return res

    async def startRuleUsageTracking(self) -> Optional[dict]:
        """
        Enables the selector recording.
        """
        res = await self.client.send("CSS.startRuleUsageTracking")
        return res

    async def stopRuleUsageTracking(self) -> Optional[dict]:
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation)
        """
        res = await self.client.send("CSS.stopRuleUsageTracking")
        return res

    async def takeCoverageDelta(self) -> Optional[dict]:
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation)
        """
        res = await self.client.send("CSS.takeCoverageDelta")
        return res

    def fontsUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
        web font
        """
        if once:
            self.client.once("CSS.fontsUpdated", fn)
        else:
            self.client.on("CSS.fontsUpdated", fn)

    def mediaQueryResultChanged(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fires whenever a MediaQuery result changes (for example, after a browser window has been
        resized.) The current implementation considers only viewport-dependent media features.
        """
        if once:
            self.client.once("CSS.mediaQueryResultChanged", fn)
        else:
            self.client.on("CSS.mediaQueryResultChanged", fn)

    def styleSheetAdded(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired whenever an active document stylesheet is added.
        """
        if once:
            self.client.once("CSS.styleSheetAdded", fn)
        else:
            self.client.on("CSS.styleSheetAdded", fn)

    def styleSheetChanged(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired whenever a stylesheet is changed as a result of the client operation.
        """
        if once:
            self.client.once("CSS.styleSheetChanged", fn)
        else:
            self.client.on("CSS.styleSheetChanged", fn)

    def styleSheetRemoved(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired whenever an active document stylesheet is removed.
        """
        if once:
            self.client.once("CSS.styleSheetRemoved", fn)
        else:
            self.client.on("CSS.styleSheetRemoved", fn)

    def __repr__(self):
        return f"CSS()"
