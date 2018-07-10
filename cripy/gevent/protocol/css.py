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

    def __init__(self, chrome):
        """
        Construct a new CSS object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def addRule(self, styleSheetId, ruleText, location):
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
        wres = self.chrome.send('CSS.addRule', msg_dict)
        return wres.get()

    def collectClassNames(self, styleSheetId):
        """
        Returns all class names from specified stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        wres = self.chrome.send('CSS.collectClassNames', msg_dict)
        return wres.get()

    def createStyleSheet(self, frameId):
        """
        Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        wres = self.chrome.send('CSS.createStyleSheet', msg_dict)
        return wres.get()

    def disable(self):
        """
        Disables the CSS agent for the given page.
        """
        wres = self.chrome.send('CSS.disable')
        return wres.get()

    def enable(self):
        """
        Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.
        """
        wres = self.chrome.send('CSS.enable')
        return wres.get()

    def forcePseudoState(self, nodeId, forcedPseudoClasses):
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
        wres = self.chrome.send('CSS.forcePseudoState', msg_dict)
        return wres.get()

    def getBackgroundColors(self, nodeId):
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('CSS.getBackgroundColors', msg_dict)
        return wres.get()

    def getComputedStyleForNode(self, nodeId):
        """
        Returns the computed style for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('CSS.getComputedStyleForNode', msg_dict)
        return wres.get()

    def getInlineStylesForNode(self, nodeId):
        """
        Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('CSS.getInlineStylesForNode', msg_dict)
        return wres.get()

    def getMatchedStylesForNode(self, nodeId):
        """
        Returns requested styles for a DOM node identified by `nodeId`.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('CSS.getMatchedStylesForNode', msg_dict)
        return wres.get()

    def getMediaQueries(self):
        """
        Returns all media queries parsed by the rendering engine.
        """
        wres = self.chrome.send('CSS.getMediaQueries')
        return wres.get()

    def getPlatformFontsForNode(self, nodeId):
        """
        Requests information about platform fonts which we used to render child TextNodes in the given
node.

        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict['nodeId'] = nodeId
        wres = self.chrome.send('CSS.getPlatformFontsForNode', msg_dict)
        return wres.get()

    def getStyleSheetText(self, styleSheetId):
        """
        Returns the current textual content for a stylesheet.

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict['styleSheetId'] = styleSheetId
        wres = self.chrome.send('CSS.getStyleSheetText', msg_dict)
        return wres.get()

    def setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
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
        wres = self.chrome.send('CSS.setEffectivePropertyValueForNode', msg_dict)
        return wres.get()

    def setKeyframeKey(self, styleSheetId, range, keyText):
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
        wres = self.chrome.send('CSS.setKeyframeKey', msg_dict)
        return wres.get()

    def setMediaText(self, styleSheetId, range, text):
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
        wres = self.chrome.send('CSS.setMediaText', msg_dict)
        return wres.get()

    def setRuleSelector(self, styleSheetId, range, selector):
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
        wres = self.chrome.send('CSS.setRuleSelector', msg_dict)
        return wres.get()

    def setStyleSheetText(self, styleSheetId, text):
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
        wres = self.chrome.send('CSS.setStyleSheetText', msg_dict)
        return wres.get()

    def setStyleTexts(self, edits):
        """
        Applies specified style edits one after another in the given order.

        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict['edits'] = edits
        wres = self.chrome.send('CSS.setStyleTexts', msg_dict)
        return wres.get()

    def startRuleUsageTracking(self):
        """
        Enables the selector recording.
        """
        wres = self.chrome.send('CSS.startRuleUsageTracking')
        return wres.get()

    def stopRuleUsageTracking(self):
        """
        Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation)
        """
        wres = self.chrome.send('CSS.stopRuleUsageTracking')
        return wres.get()

    def takeCoverageDelta(self):
        """
        Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation)
        """
        wres = self.chrome.send('CSS.takeCoverageDelta')
        return wres.get()

    def fontsUpdated(self, fn, once=False):
        """
        Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
        web font
        """
        self.chrome.on("CSS.fontsUpdated", fn, once=once)

    def mediaQueryResultChanged(self, fn, once=False):
        """
        Fires whenever a MediaQuery result changes (for example, after a browser window has been
        resized.) The current implementation considers only viewport-dependent media features.
        """
        self.chrome.on("CSS.mediaQueryResultChanged", fn, once=once)

    def styleSheetAdded(self, fn, once=False):
        """
        Fired whenever an active document stylesheet is added.
        """
        self.chrome.on("CSS.styleSheetAdded", fn, once=once)

    def styleSheetChanged(self, fn, once=False):
        """
        Fired whenever a stylesheet is changed as a result of the client operation.
        """
        self.chrome.on("CSS.styleSheetChanged", fn, once=once)

    def styleSheetRemoved(self, fn, once=False):
        """
        Fired whenever an active document stylesheet is removed.
        """
        self.chrome.on("CSS.styleSheetRemoved", fn, once=once)


