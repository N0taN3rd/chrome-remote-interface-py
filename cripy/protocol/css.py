"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["CSS"]


@attr.dataclass(slots=True, cmp=False)
class CSS(object):
    """
    This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
have an associated `id` used in subsequent operations on the related object. Each object type has
a specific `id` structure, and those are not interchangeable between objects of different kinds.
CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def addRule(
        self, styleSheetId: str, ruleText: str, location: dict
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.addRule", msg_dict)

    def collectClassNames(self, styleSheetId: str) -> Awaitable[Dict]:
        """
        Returns all class names from specified stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        return self.client.send("CSS.collectClassNames", msg_dict)

    def createStyleSheet(self, frameId: str) -> Awaitable[Dict]:
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        return self.client.send("CSS.createStyleSheet", msg_dict)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the CSS agent for the given page.
        """
        return self.client.send("CSS.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.
        """
        return self.client.send("CSS.enable")

    def forcePseudoState(
        self, nodeId: int, forcedPseudoClasses: List[str]
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.forcePseudoState", msg_dict)

    def getBackgroundColors(self, nodeId: int) -> Awaitable[Dict]:
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("CSS.getBackgroundColors", msg_dict)

    def getComputedStyleForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the computed style for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("CSS.getComputedStyleForNode", msg_dict)

    def getInlineStylesForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("CSS.getInlineStylesForNode", msg_dict)

    def getMatchedStylesForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns requested styles for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("CSS.getMatchedStylesForNode", msg_dict)

    def getMediaQueries(self) -> Awaitable[Dict]:
        """
        Returns all media queries parsed by the rendering engine.
        """
        return self.client.send("CSS.getMediaQueries")

    def getPlatformFontsForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Requests information about platform fonts which we used to render child TextNodes in the given
node.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        return self.client.send("CSS.getPlatformFontsForNode", msg_dict)

    def getStyleSheetText(self, styleSheetId: str) -> Awaitable[Dict]:
        """
        Returns the current textual content for a stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        return self.client.send("CSS.getStyleSheetText", msg_dict)

    def setEffectivePropertyValueForNode(
        self, nodeId: int, propertyName: str, value: str
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.setEffectivePropertyValueForNode", msg_dict)

    def setKeyframeKey(
        self, styleSheetId: str, range: dict, keyText: str
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.setKeyframeKey", msg_dict)

    def setMediaText(
        self, styleSheetId: str, range: dict, text: str
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.setMediaText", msg_dict)

    def setRuleSelector(
        self, styleSheetId: str, range: dict, selector: str
    ) -> Awaitable[Dict]:
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
        return self.client.send("CSS.setRuleSelector", msg_dict)

    def setStyleSheetText(self, styleSheetId: str, text: str) -> Awaitable[Dict]:
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
        return self.client.send("CSS.setStyleSheetText", msg_dict)

    def setStyleTexts(self, edits: List[dict]) -> Awaitable[Dict]:
        """
        Applies specified style edits one after another in the given order.

        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict["edits"] = edits
        return self.client.send("CSS.setStyleTexts", msg_dict)

    def startRuleUsageTracking(self) -> Awaitable[Dict]:
        """
        Enables the selector recording.
        """
        return self.client.send("CSS.startRuleUsageTracking")

    def stopRuleUsageTracking(self) -> Awaitable[Dict]:
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation)
        """
        return self.client.send("CSS.stopRuleUsageTracking")

    def takeCoverageDelta(self) -> Awaitable[Dict]:
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation)
        """
        return self.client.send("CSS.takeCoverageDelta")

    def fontsUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
        web font
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("CSS.fontsUpdated", _cb)

            return future

        self.client.on("CSS.fontsUpdated", cb)
        return lambda: self.client.remove_listener("CSS.fontsUpdated", cb)

    def mediaQueryResultChanged(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fires whenever a MediaQuery result changes (for example, after a browser window has been
        resized.) The current implementation considers only viewport-dependent media features.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("CSS.mediaQueryResultChanged", _cb)

            return future

        self.client.on("CSS.mediaQueryResultChanged", cb)
        return lambda: self.client.remove_listener("CSS.mediaQueryResultChanged", cb)

    def styleSheetAdded(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired whenever an active document stylesheet is added.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("CSS.styleSheetAdded", _cb)

            return future

        self.client.on("CSS.styleSheetAdded", cb)
        return lambda: self.client.remove_listener("CSS.styleSheetAdded", cb)

    def styleSheetChanged(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired whenever a stylesheet is changed as a result of the client operation.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("CSS.styleSheetChanged", _cb)

            return future

        self.client.on("CSS.styleSheetChanged", cb)
        return lambda: self.client.remove_listener("CSS.styleSheetChanged", cb)

    def styleSheetRemoved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired whenever an active document stylesheet is removed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("CSS.styleSheetRemoved", _cb)

            return future

        self.client.on("CSS.styleSheetRemoved", cb)
        return lambda: self.client.remove_listener("CSS.styleSheetRemoved", cb)
