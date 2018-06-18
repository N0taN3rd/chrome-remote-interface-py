from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.emulation import types as Emulation
from cripy.gevent.protocol.network import types as Network
from cripy.gevent.protocol.debugger import types as Debugger
from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.page import events as Events
from cripy.gevent.protocol.page import types as Types

__all__ = ["Page"] + Events.__all__ + Types.__all__


class Page(object):
    """
    Actions and events related to the inspected page belong to the page domain.
    """

    dependencies = ["Debugger", "DOM", "Network"]

    def __init__(self, chrome):
        self.chrome = chrome

    def addScriptToEvaluateOnLoad(self, scriptSource):
        """
        :param scriptSource: The scriptSource
        :type scriptSource: str
        """
        msg_dict = dict()
        if scriptSource is not None:
            msg_dict["scriptSource"] = scriptSource
        wres = self.chrome.send("Page.addScriptToEvaluateOnLoad", msg_dict)
        res = wres.get()
        return res

    def addScriptToEvaluateOnNewDocument(self, source):
        """
        :param source: The source
        :type source: str
        """
        msg_dict = dict()
        if source is not None:
            msg_dict["source"] = source
        wres = self.chrome.send("Page.addScriptToEvaluateOnNewDocument", msg_dict)
        res = wres.get()
        return res

    def bringToFront(self):
        wres = self.chrome.send("Page.bringToFront")
        return wres.get()

    def captureScreenshot(self, format=None, quality=None, clip=None, fromSurface=None):
        """
        :param format: Image compression format (defaults to png).
        :type format: Optional[str]
        :param quality: Compression quality from range [0..100] (jpeg only).
        :type quality: Optional[int]
        :param clip: Capture the screenshot of a given region only.
        :type clip: Optional[dict]
        :param fromSurface: Capture the screenshot from the surface, rather than the view. Defaults to true.
        :type fromSurface: Optional[bool]
        """
        msg_dict = dict()
        if format is not None:
            msg_dict["format"] = format
        if quality is not None:
            msg_dict["quality"] = quality
        if clip is not None:
            msg_dict["clip"] = clip
        if fromSurface is not None:
            msg_dict["fromSurface"] = fromSurface
        wres = self.chrome.send("Page.captureScreenshot", msg_dict)
        res = wres.get()
        return res

    def clearDeviceMetricsOverride(self):
        wres = self.chrome.send("Page.clearDeviceMetricsOverride")
        return wres.get()

    def clearDeviceOrientationOverride(self):
        wres = self.chrome.send("Page.clearDeviceOrientationOverride")
        return wres.get()

    def clearGeolocationOverride(self):
        wres = self.chrome.send("Page.clearGeolocationOverride")
        return wres.get()

    def createIsolatedWorld(self, frameId, worldName=None, grantUniveralAccess=None):
        """
        :param frameId: Id of the frame in which the isolated world should be created.
        :type frameId: str
        :param worldName: An optional name which is reported in the Execution Context.
        :type worldName: Optional[str]
        :param grantUniveralAccess: Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
        :type grantUniveralAccess: Optional[bool]
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        if worldName is not None:
            msg_dict["worldName"] = worldName
        if grantUniveralAccess is not None:
            msg_dict["grantUniveralAccess"] = grantUniveralAccess
        wres = self.chrome.send("Page.createIsolatedWorld", msg_dict)
        res = wres.get()
        return res

    def deleteCookie(self, cookieName, url):
        """
        :param cookieName: Name of the cookie to remove.
        :type cookieName: str
        :param url: URL to match cooke domain and path.
        :type url: str
        """
        msg_dict = dict()
        if cookieName is not None:
            msg_dict["cookieName"] = cookieName
        if url is not None:
            msg_dict["url"] = url
        wres = self.chrome.send("Page.deleteCookie", msg_dict)
        return wres.get()

    def disable(self):
        wres = self.chrome.send("Page.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Page.enable")
        return wres.get()

    def getAppManifest(self):
        wres = self.chrome.send("Page.getAppManifest")
        res = wres.get()
        res["errors"] = Types.AppManifestError.safe_create_from_list(res["errors"])
        return res

    def getCookies(self):
        wres = self.chrome.send("Page.getCookies")
        res = wres.get()
        res["cookies"] = Network.Cookie.safe_create_from_list(res["cookies"])
        return res

    def getFrameTree(self):
        wres = self.chrome.send("Page.getFrameTree")
        res = wres.get()
        res["frameTree"] = Types.FrameTree.safe_create(res["frameTree"])
        return res

    def getLayoutMetrics(self):
        wres = self.chrome.send("Page.getLayoutMetrics")
        res = wres.get()
        res["layoutViewport"] = Types.LayoutViewport.safe_create(res["layoutViewport"])
        res["visualViewport"] = Types.VisualViewport.safe_create(res["visualViewport"])
        res["contentSize"] = DOM.Rect.safe_create(res["contentSize"])
        return res

    def getNavigationHistory(self):
        wres = self.chrome.send("Page.getNavigationHistory")
        res = wres.get()
        res["entries"] = Types.NavigationEntry.safe_create_from_list(res["entries"])
        return res

    def getResourceContent(self, frameId, url):
        """
        :param frameId: Frame id to get resource for.
        :type frameId: str
        :param url: URL of the resource to get content for.
        :type url: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        if url is not None:
            msg_dict["url"] = url
        wres = self.chrome.send("Page.getResourceContent", msg_dict)
        res = wres.get()
        return res

    def getResourceTree(self):
        wres = self.chrome.send("Page.getResourceTree")
        res = wres.get()
        res["frameTree"] = Types.FrameResourceTree.safe_create(res["frameTree"])
        return res

    def handleJavaScriptDialog(self, accept, promptText=None):
        """
        :param accept: Whether to accept or dismiss the dialog.
        :type accept: bool
        :param promptText: The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
        :type promptText: Optional[str]
        """
        msg_dict = dict()
        if accept is not None:
            msg_dict["accept"] = accept
        if promptText is not None:
            msg_dict["promptText"] = promptText
        wres = self.chrome.send("Page.handleJavaScriptDialog", msg_dict)
        return wres.get()

    def navigate(self, url, referrer=None, transitionType=None, frameId=None):
        """
        :param url: URL to navigate the page to.
        :type url: str
        :param referrer: Referrer URL.
        :type referrer: Optional[str]
        :param transitionType: Intended transition type.
        :type transitionType: Optional[str]
        :param frameId: Frame id to navigate, if not specified navigates the top frame.
        :type frameId: Optional[str]
        """
        msg_dict = dict()
        if url is not None:
            msg_dict["url"] = url
        if referrer is not None:
            msg_dict["referrer"] = referrer
        if transitionType is not None:
            msg_dict["transitionType"] = transitionType
        if frameId is not None:
            msg_dict["frameId"] = frameId
        wres = self.chrome.send("Page.navigate", msg_dict)
        res = wres.get()
        return res

    def navigateToHistoryEntry(self, entryId):
        """
        :param entryId: Unique id of the entry to navigate to.
        :type entryId: int
        """
        msg_dict = dict()
        if entryId is not None:
            msg_dict["entryId"] = entryId
        wres = self.chrome.send("Page.navigateToHistoryEntry", msg_dict)
        return wres.get()

    def printToPDF(
        self,
        landscape=None,
        displayHeaderFooter=None,
        printBackground=None,
        scale=None,
        paperWidth=None,
        paperHeight=None,
        marginTop=None,
        marginBottom=None,
        marginLeft=None,
        marginRight=None,
        pageRanges=None,
        ignoreInvalidPageRanges=None,
        headerTemplate=None,
        footerTemplate=None,
        preferCSSPageSize=None,
    ):
        """
        :param landscape: Paper orientation. Defaults to false.
        :type landscape: Optional[bool]
        :param displayHeaderFooter: Display header and footer. Defaults to false.
        :type displayHeaderFooter: Optional[bool]
        :param printBackground: Print background graphics. Defaults to false.
        :type printBackground: Optional[bool]
        :param scale: Scale of the webpage rendering. Defaults to 1.
        :type scale: Optional[float]
        :param paperWidth: Paper width in inches. Defaults to 8.5 inches.
        :type paperWidth: Optional[float]
        :param paperHeight: Paper height in inches. Defaults to 11 inches.
        :type paperHeight: Optional[float]
        :param marginTop: Top margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginTop: Optional[float]
        :param marginBottom: Bottom margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginBottom: Optional[float]
        :param marginLeft: Left margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginLeft: Optional[float]
        :param marginRight: Right margin in inches. Defaults to 1cm (~0.4 inches).
        :type marginRight: Optional[float]
        :param pageRanges: Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
        :type pageRanges: Optional[str]
        :param ignoreInvalidPageRanges: Whether to silently ignore invalid but successfully parsed page ranges, such as '3-2'. Defaults to false.
        :type ignoreInvalidPageRanges: Optional[bool]
        :param headerTemplate: HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - `date`: formatted print date - `title`: document title - `url`: document location - `pageNumber`: current page number - `totalPages`: total pages in the document  For example, `<span class=title></span>` would generate span containing the title.
        :type headerTemplate: Optional[str]
        :param footerTemplate: HTML template for the print footer. Should use the same format as the `headerTemplate`.
        :type footerTemplate: Optional[str]
        :param preferCSSPageSize: Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size.
        :type preferCSSPageSize: Optional[bool]
        """
        msg_dict = dict()
        if landscape is not None:
            msg_dict["landscape"] = landscape
        if displayHeaderFooter is not None:
            msg_dict["displayHeaderFooter"] = displayHeaderFooter
        if printBackground is not None:
            msg_dict["printBackground"] = printBackground
        if scale is not None:
            msg_dict["scale"] = scale
        if paperWidth is not None:
            msg_dict["paperWidth"] = paperWidth
        if paperHeight is not None:
            msg_dict["paperHeight"] = paperHeight
        if marginTop is not None:
            msg_dict["marginTop"] = marginTop
        if marginBottom is not None:
            msg_dict["marginBottom"] = marginBottom
        if marginLeft is not None:
            msg_dict["marginLeft"] = marginLeft
        if marginRight is not None:
            msg_dict["marginRight"] = marginRight
        if pageRanges is not None:
            msg_dict["pageRanges"] = pageRanges
        if ignoreInvalidPageRanges is not None:
            msg_dict["ignoreInvalidPageRanges"] = ignoreInvalidPageRanges
        if headerTemplate is not None:
            msg_dict["headerTemplate"] = headerTemplate
        if footerTemplate is not None:
            msg_dict["footerTemplate"] = footerTemplate
        if preferCSSPageSize is not None:
            msg_dict["preferCSSPageSize"] = preferCSSPageSize
        wres = self.chrome.send("Page.printToPDF", msg_dict)
        res = wres.get()
        return res

    def reload(self, ignoreCache=None, scriptToEvaluateOnLoad=None):
        """
        :param ignoreCache: If true, browser cache is ignored (as if the user pressed Shift+refresh).
        :type ignoreCache: Optional[bool]
        :param scriptToEvaluateOnLoad: If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin.
        :type scriptToEvaluateOnLoad: Optional[str]
        """
        msg_dict = dict()
        if ignoreCache is not None:
            msg_dict["ignoreCache"] = ignoreCache
        if scriptToEvaluateOnLoad is not None:
            msg_dict["scriptToEvaluateOnLoad"] = scriptToEvaluateOnLoad
        wres = self.chrome.send("Page.reload", msg_dict)
        return wres.get()

    def removeScriptToEvaluateOnLoad(self, identifier):
        """
        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        wres = self.chrome.send("Page.removeScriptToEvaluateOnLoad", msg_dict)
        return wres.get()

    def removeScriptToEvaluateOnNewDocument(self, identifier):
        """
        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        wres = self.chrome.send("Page.removeScriptToEvaluateOnNewDocument", msg_dict)
        return wres.get()

    def requestAppBanner(self):
        wres = self.chrome.send("Page.requestAppBanner")
        return wres.get()

    def screencastFrameAck(self, sessionId):
        """
        :param sessionId: Frame number.
        :type sessionId: int
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict["sessionId"] = sessionId
        wres = self.chrome.send("Page.screencastFrameAck", msg_dict)
        return wres.get()

    def searchInResource(self, frameId, url, query, caseSensitive=None, isRegex=None):
        """
        :param frameId: Frame id for resource to search in.
        :type frameId: str
        :param url: URL of the resource to search in.
        :type url: str
        :param query: String to search for.
        :type query: str
        :param caseSensitive: If true, search is case sensitive.
        :type caseSensitive: Optional[bool]
        :param isRegex: If true, treats string parameter as regex.
        :type isRegex: Optional[bool]
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        if url is not None:
            msg_dict["url"] = url
        if query is not None:
            msg_dict["query"] = query
        if caseSensitive is not None:
            msg_dict["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg_dict["isRegex"] = isRegex
        wres = self.chrome.send("Page.searchInResource", msg_dict)
        res = wres.get()
        res["result"] = Debugger.SearchMatch.safe_create_from_list(res["result"])
        return res

    def setAdBlockingEnabled(self, enabled):
        """
        :param enabled: Whether to block ads.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        wres = self.chrome.send("Page.setAdBlockingEnabled", msg_dict)
        return wres.get()

    def setBypassCSP(self, enabled):
        """
        :param enabled: Whether to bypass page CSP.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        wres = self.chrome.send("Page.setBypassCSP", msg_dict)
        return wres.get()

    def setDeviceMetricsOverride(
        self,
        width,
        height,
        deviceScaleFactor,
        mobile,
        scale=None,
        screenWidth=None,
        screenHeight=None,
        positionX=None,
        positionY=None,
        dontSetVisibleSize=None,
        screenOrientation=None,
        viewport=None,
    ):
        """
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type width: int
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type height: int
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :type deviceScaleFactor: float
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
        :type mobile: bool
        :param scale: Scale to apply to resulting view image.
        :type scale: Optional[float]
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :type screenWidth: Optional[int]
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :type screenHeight: Optional[int]
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :type positionX: Optional[int]
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :type positionY: Optional[int]
        :param dontSetVisibleSize: Do not set visible view size, rely upon explicit setVisibleSize call.
        :type dontSetVisibleSize: Optional[bool]
        :param screenOrientation: Screen orientation override.
        :type screenOrientation: Optional[dict]
        :param viewport: The viewport dimensions and scale. If not set, the override is cleared.
        :type viewport: Optional[dict]
        """
        msg_dict = dict()
        if width is not None:
            msg_dict["width"] = width
        if height is not None:
            msg_dict["height"] = height
        if deviceScaleFactor is not None:
            msg_dict["deviceScaleFactor"] = deviceScaleFactor
        if mobile is not None:
            msg_dict["mobile"] = mobile
        if scale is not None:
            msg_dict["scale"] = scale
        if screenWidth is not None:
            msg_dict["screenWidth"] = screenWidth
        if screenHeight is not None:
            msg_dict["screenHeight"] = screenHeight
        if positionX is not None:
            msg_dict["positionX"] = positionX
        if positionY is not None:
            msg_dict["positionY"] = positionY
        if dontSetVisibleSize is not None:
            msg_dict["dontSetVisibleSize"] = dontSetVisibleSize
        if screenOrientation is not None:
            msg_dict["screenOrientation"] = screenOrientation
        if viewport is not None:
            msg_dict["viewport"] = viewport
        wres = self.chrome.send("Page.setDeviceMetricsOverride", msg_dict)
        return wres.get()

    def setDeviceOrientationOverride(self, alpha, beta, gamma):
        """
        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        msg_dict = dict()
        if alpha is not None:
            msg_dict["alpha"] = alpha
        if beta is not None:
            msg_dict["beta"] = beta
        if gamma is not None:
            msg_dict["gamma"] = gamma
        wres = self.chrome.send("Page.setDeviceOrientationOverride", msg_dict)
        return wres.get()

    def setFontFamilies(self, fontFamilies):
        """
        :param fontFamilies: Specifies font families to set. If a font family is not specified, it won't be changed.
        :type fontFamilies: dict
        """
        msg_dict = dict()
        if fontFamilies is not None:
            msg_dict["fontFamilies"] = fontFamilies
        wres = self.chrome.send("Page.setFontFamilies", msg_dict)
        return wres.get()

    def setFontSizes(self, fontSizes):
        """
        :param fontSizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        :type fontSizes: dict
        """
        msg_dict = dict()
        if fontSizes is not None:
            msg_dict["fontSizes"] = fontSizes
        wres = self.chrome.send("Page.setFontSizes", msg_dict)
        return wres.get()

    def setDocumentContent(self, frameId, html):
        """
        :param frameId: Frame id to set HTML for.
        :type frameId: str
        :param html: HTML content to set.
        :type html: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        if html is not None:
            msg_dict["html"] = html
        wres = self.chrome.send("Page.setDocumentContent", msg_dict)
        return wres.get()

    def setDownloadBehavior(self, behavior, downloadPath=None):
        """
        :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
        :type behavior: str
        :param downloadPath: The default path to save downloaded files to. This is requred if behavior is set to 'allow'
        :type downloadPath: Optional[str]
        """
        msg_dict = dict()
        if behavior is not None:
            msg_dict["behavior"] = behavior
        if downloadPath is not None:
            msg_dict["downloadPath"] = downloadPath
        wres = self.chrome.send("Page.setDownloadBehavior", msg_dict)
        return wres.get()

    def setGeolocationOverride(self, latitude=None, longitude=None, accuracy=None):
        """
        :param latitude: Mock latitude
        :type latitude: Optional[float]
        :param longitude: Mock longitude
        :type longitude: Optional[float]
        :param accuracy: Mock accuracy
        :type accuracy: Optional[float]
        """
        msg_dict = dict()
        if latitude is not None:
            msg_dict["latitude"] = latitude
        if longitude is not None:
            msg_dict["longitude"] = longitude
        if accuracy is not None:
            msg_dict["accuracy"] = accuracy
        wres = self.chrome.send("Page.setGeolocationOverride", msg_dict)
        return wres.get()

    def setLifecycleEventsEnabled(self, enabled):
        """
        :param enabled: If true, starts emitting lifecycle events.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        wres = self.chrome.send("Page.setLifecycleEventsEnabled", msg_dict)
        return wres.get()

    def setTouchEmulationEnabled(self, enabled, configuration=None):
        """
        :param enabled: Whether the touch event emulation should be enabled.
        :type enabled: bool
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :type configuration: Optional[str]
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        if configuration is not None:
            msg_dict["configuration"] = configuration
        wres = self.chrome.send("Page.setTouchEmulationEnabled", msg_dict)
        return wres.get()

    def startScreencast(
        self,
        format=None,
        quality=None,
        maxWidth=None,
        maxHeight=None,
        everyNthFrame=None,
    ):
        """
        :param format: Image compression format.
        :type format: Optional[str]
        :param quality: Compression quality from range [0..100].
        :type quality: Optional[int]
        :param maxWidth: Maximum screenshot width.
        :type maxWidth: Optional[int]
        :param maxHeight: Maximum screenshot height.
        :type maxHeight: Optional[int]
        :param everyNthFrame: Send every n-th frame.
        :type everyNthFrame: Optional[int]
        """
        msg_dict = dict()
        if format is not None:
            msg_dict["format"] = format
        if quality is not None:
            msg_dict["quality"] = quality
        if maxWidth is not None:
            msg_dict["maxWidth"] = maxWidth
        if maxHeight is not None:
            msg_dict["maxHeight"] = maxHeight
        if everyNthFrame is not None:
            msg_dict["everyNthFrame"] = everyNthFrame
        wres = self.chrome.send("Page.startScreencast", msg_dict)
        return wres.get()

    def stopLoading(self):
        wres = self.chrome.send("Page.stopLoading")
        return wres.get()

    def crash(self):
        wres = self.chrome.send("Page.crash")
        return wres.get()

    def close(self):
        wres = self.chrome.send("Page.close")
        return wres.get()

    def setWebLifecycleState(self, state):
        """
        :param state: Target lifecycle state
        :type state: str
        """
        msg_dict = dict()
        if state is not None:
            msg_dict["state"] = state
        wres = self.chrome.send("Page.setWebLifecycleState", msg_dict)
        return wres.get()

    def stopScreencast(self):
        wres = self.chrome.send("Page.stopScreencast")
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
