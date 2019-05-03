"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["CSS"]


class CSS:
    """
    This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
    have an associated `id` used in subsequent operations on the related object. Each object type has
    a specific `id` structure, and those are not interchangeable between objects of different kinds.
    CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
    can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
    subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.
     
    Domain Dependencies: 
      * DOM
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/CSS`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of CSS

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def addRule(
        self, styleSheetId: str, ruleText: str, location: Dict[str, Any]
    ) -> Awaitable[Dict]:
        """
        Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
        position specified by `location`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-addRule`

        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :param ruleText: The text of a new rule.
        :param location: Text position of a new rule in the target style sheet.
        :return: The results of the command
        """
        return self.client.send(
            "CSS.addRule",
            {"styleSheetId": styleSheetId, "ruleText": ruleText, "location": location},
        )

    def collectClassNames(self, styleSheetId: str) -> Awaitable[Dict]:
        """
        Returns all class names from specified stylesheet.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-collectClassNames`

        :param styleSheetId: The styleSheetId
        :return: The results of the command
        """
        return self.client.send("CSS.collectClassNames", {"styleSheetId": styleSheetId})

    def createStyleSheet(self, frameId: str) -> Awaitable[Dict]:
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-createStyleSheet`

        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :return: The results of the command
        """
        return self.client.send("CSS.createStyleSheet", {"frameId": frameId})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the CSS agent for the given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-disable`

        :return: The results of the command
        """
        return self.client.send("CSS.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
        enabled until the result of this command is received.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-enable`

        :return: The results of the command
        """
        return self.client.send("CSS.enable", {})

    def forcePseudoState(
        self, nodeId: int, forcedPseudoClasses: List[str]
    ) -> Awaitable[Dict]:
        """
        Ensures that the given node will have specified pseudo-classes whenever its style is computed by
        the browser.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-forcePseudoState`

        :param nodeId: The element id for which to force the pseudo state.
        :param forcedPseudoClasses: Element pseudo classes to force when computing the element's style.
        :return: The results of the command
        """
        return self.client.send(
            "CSS.forcePseudoState",
            {"nodeId": nodeId, "forcedPseudoClasses": forcedPseudoClasses},
        )

    def getBackgroundColors(self, nodeId: int) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getBackgroundColors`

        :param nodeId: Id of the node to get background colors for.
        :return: The results of the command
        """
        return self.client.send("CSS.getBackgroundColors", {"nodeId": nodeId})

    def getComputedStyleForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the computed style for a DOM node identified by `nodeId`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getComputedStyleForNode`

        :param nodeId: The nodeId
        :return: The results of the command
        """
        return self.client.send("CSS.getComputedStyleForNode", {"nodeId": nodeId})

    def getInlineStylesForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
        attributes) for a DOM node identified by `nodeId`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getInlineStylesForNode`

        :param nodeId: The nodeId
        :return: The results of the command
        """
        return self.client.send("CSS.getInlineStylesForNode", {"nodeId": nodeId})

    def getMatchedStylesForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Returns requested styles for a DOM node identified by `nodeId`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getMatchedStylesForNode`

        :param nodeId: The nodeId
        :return: The results of the command
        """
        return self.client.send("CSS.getMatchedStylesForNode", {"nodeId": nodeId})

    def getMediaQueries(self) -> Awaitable[Dict]:
        """
        Returns all media queries parsed by the rendering engine.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getMediaQueries`

        :return: The results of the command
        """
        return self.client.send("CSS.getMediaQueries", {})

    def getPlatformFontsForNode(self, nodeId: int) -> Awaitable[Dict]:
        """
        Requests information about platform fonts which we used to render child TextNodes in the given
        node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getPlatformFontsForNode`

        :param nodeId: The nodeId
        :return: The results of the command
        """
        return self.client.send("CSS.getPlatformFontsForNode", {"nodeId": nodeId})

    def getStyleSheetText(self, styleSheetId: str) -> Awaitable[Dict]:
        """
        Returns the current textual content for a stylesheet.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-getStyleSheetText`

        :param styleSheetId: The styleSheetId
        :return: The results of the command
        """
        return self.client.send("CSS.getStyleSheetText", {"styleSheetId": styleSheetId})

    def setEffectivePropertyValueForNode(
        self, nodeId: int, propertyName: str, value: str
    ) -> Awaitable[Dict]:
        """
        Find a rule with the given active property for the given node and set the new value for this
        property

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setEffectivePropertyValueForNode`

        :param nodeId: The element id for which to set property.
        :param propertyName: The propertyName
        :param value: The value
        :return: The results of the command
        """
        return self.client.send(
            "CSS.setEffectivePropertyValueForNode",
            {"nodeId": nodeId, "propertyName": propertyName, "value": value},
        )

    def setKeyframeKey(
        self, styleSheetId: str, range: Dict[str, Any], keyText: str
    ) -> Awaitable[Dict]:
        """
        Modifies the keyframe rule key text.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setKeyframeKey`

        :param styleSheetId: The styleSheetId
        :param range: The range
        :param keyText: The keyText
        :return: The results of the command
        """
        return self.client.send(
            "CSS.setKeyframeKey",
            {"styleSheetId": styleSheetId, "range": range, "keyText": keyText},
        )

    def setMediaText(
        self, styleSheetId: str, range: Dict[str, Any], text: str
    ) -> Awaitable[Dict]:
        """
        Modifies the rule selector.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setMediaText`

        :param styleSheetId: The styleSheetId
        :param range: The range
        :param text: The text
        :return: The results of the command
        """
        return self.client.send(
            "CSS.setMediaText",
            {"styleSheetId": styleSheetId, "range": range, "text": text},
        )

    def setRuleSelector(
        self, styleSheetId: str, range: Dict[str, Any], selector: str
    ) -> Awaitable[Dict]:
        """
        Modifies the rule selector.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setRuleSelector`

        :param styleSheetId: The styleSheetId
        :param range: The range
        :param selector: The selector
        :return: The results of the command
        """
        return self.client.send(
            "CSS.setRuleSelector",
            {"styleSheetId": styleSheetId, "range": range, "selector": selector},
        )

    def setStyleSheetText(self, styleSheetId: str, text: str) -> Awaitable[Dict]:
        """
        Sets the new stylesheet text.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setStyleSheetText`

        :param styleSheetId: The styleSheetId
        :param text: The text
        :return: The results of the command
        """
        return self.client.send(
            "CSS.setStyleSheetText", {"styleSheetId": styleSheetId, "text": text}
        )

    def setStyleTexts(self, edits: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        Applies specified style edits one after another in the given order.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-setStyleTexts`

        :param edits: The edits
        :return: The results of the command
        """
        return self.client.send("CSS.setStyleTexts", {"edits": edits})

    def startRuleUsageTracking(self) -> Awaitable[Dict]:
        """
        Enables the selector recording.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-startRuleUsageTracking`

        :return: The results of the command
        """
        return self.client.send("CSS.startRuleUsageTracking", {})

    def stopRuleUsageTracking(self) -> Awaitable[Dict]:
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
        `takeCoverageDelta` (or since start of coverage instrumentation)

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-stopRuleUsageTracking`

        :return: The results of the command
        """
        return self.client.send("CSS.stopRuleUsageTracking", {})

    def takeCoverageDelta(self) -> Awaitable[Dict]:
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
        instrumentation)

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#method-takeCoverageDelta`

        :return: The results of the command
        """
        return self.client.send("CSS.takeCoverageDelta", {})

    def fontsUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
        web font

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#event-fontsUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "CSS.fontsUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def mediaQueryResultChanged(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Fires whenever a MediaQuery result changes (for example, after a browser window has been
        resized.) The current implementation considers only viewport-dependent media features.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#event-mediaQueryResultChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "CSS.mediaQueryResultChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def styleSheetAdded(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired whenever an active document stylesheet is added.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#event-styleSheetAdded`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "CSS.styleSheetAdded"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def styleSheetChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired whenever a stylesheet is changed as a result of the client operation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#event-styleSheetChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "CSS.styleSheetChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def styleSheetRemoved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired whenever an active document stylesheet is removed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/CSS#event-styleSheetRemoved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "CSS.styleSheetRemoved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
