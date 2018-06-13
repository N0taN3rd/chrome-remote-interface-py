from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.emulation import types as Emulation
from cripy.sync.protocol.network import types as Network
from cripy.sync.protocol.debugger import types as Debugger
from cripy.sync.protocol.page import events as Events
from cripy.sync.protocol.page import types as Types

__all__ = ["Page"] + Events.__all__ + Types.__all__ 


class Page(object):
    """
    Actions and events related to the inspected page belong to the page domain.
    """

    dependencies = ['Debugger', 'DOM', 'Network']

    def __init__(self, chrome):
        self.chrome = chrome

    def addScriptToEvaluateOnLoad(self, scriptSource, cb=None):
        """
        :param scriptSource: The scriptSource
        :type scriptSource: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if scriptSource is not None:
            msg_dict['scriptSource'] = scriptSource
        self.chrome.send('Page.addScriptToEvaluateOnLoad', params=msg_dict, cb=cb_wrapper)


    def addScriptToEvaluateOnNewDocument(self, source, cb=None):
        """
        :param source: The source
        :type source: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if source is not None:
            msg_dict['source'] = source
        self.chrome.send('Page.addScriptToEvaluateOnNewDocument', params=msg_dict, cb=cb_wrapper)


    def bringToFront(self, cb=None):
        self.chrome.send('Page.bringToFront')


    def captureScreenshot(self, format, quality, clip, fromSurface, cb=None):
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
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if format is not None:
            msg_dict['format'] = format
        if quality is not None:
            msg_dict['quality'] = quality
        if clip is not None:
            msg_dict['clip'] = clip
        if fromSurface is not None:
            msg_dict['fromSurface'] = fromSurface
        self.chrome.send('Page.captureScreenshot', params=msg_dict, cb=cb_wrapper)


    def clearDeviceMetricsOverride(self, cb=None):
        self.chrome.send('Page.clearDeviceMetricsOverride')


    def clearDeviceOrientationOverride(self, cb=None):
        self.chrome.send('Page.clearDeviceOrientationOverride')


    def clearGeolocationOverride(self, cb=None):
        self.chrome.send('Page.clearGeolocationOverride')


    def createIsolatedWorld(self, frameId, worldName, grantUniveralAccess, cb=None):
        """
        :param frameId: Id of the frame in which the isolated world should be created.
        :type frameId: str
        :param worldName: An optional name which is reported in the Execution Context.
        :type worldName: Optional[str]
        :param grantUniveralAccess: Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
        :type grantUniveralAccess: Optional[bool]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        if worldName is not None:
            msg_dict['worldName'] = worldName
        if grantUniveralAccess is not None:
            msg_dict['grantUniveralAccess'] = grantUniveralAccess
        self.chrome.send('Page.createIsolatedWorld', params=msg_dict, cb=cb_wrapper)


    def deleteCookie(self, cookieName, url, cb=None):
        """
        :param cookieName: Name of the cookie to remove.
        :type cookieName: str
        :param url: URL to match cooke domain and path.
        :type url: str
        """
        msg_dict = dict()
        if cookieName is not None:
            msg_dict['cookieName'] = cookieName
        if url is not None:
            msg_dict['url'] = url
        self.chrome.send('Page.deleteCookie', params=msg_dict)


    def disable(self, cb=None):
        self.chrome.send('Page.disable')


    def enable(self, cb=None):
        self.chrome.send('Page.enable')


    def getAppManifest(self, cb=None):
        def cb_wrapper(res):
            res['errors'] = Types.AppManifestError.safe_create_from_list(res['errors'])
            cb(res)
        self.chrome.send('Page.getAppManifest', cb=cb_wrapper)


    def getCookies(self, cb=None):
        def cb_wrapper(res):
            res['cookies'] = Network.Cookie.safe_create_from_list(res['cookies'])
            cb(res)
        self.chrome.send('Page.getCookies', cb=cb_wrapper)


    def getFrameTree(self, cb=None):
        def cb_wrapper(res):
            res['frameTree'] = Types.FrameTree.safe_create(res['frameTree'])
            cb(res)
        self.chrome.send('Page.getFrameTree', cb=cb_wrapper)


    def getLayoutMetrics(self, cb=None):
        def cb_wrapper(res):
            res['layoutViewport'] = Types.LayoutViewport.safe_create(res['layoutViewport'])
            res['visualViewport'] = Types.VisualViewport.safe_create(res['visualViewport'])
            res['contentSize'] = DOM.Rect.safe_create(res['contentSize'])
            cb(res)
        self.chrome.send('Page.getLayoutMetrics', cb=cb_wrapper)


    def getNavigationHistory(self, cb=None):
        def cb_wrapper(res):
            res['entries'] = Types.NavigationEntry.safe_create_from_list(res['entries'])
            cb(res)
        self.chrome.send('Page.getNavigationHistory', cb=cb_wrapper)


    def getResourceContent(self, frameId, url, cb=None):
        """
        :param frameId: Frame id to get resource for.
        :type frameId: str
        :param url: URL of the resource to get content for.
        :type url: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        if url is not None:
            msg_dict['url'] = url
        self.chrome.send('Page.getResourceContent', params=msg_dict, cb=cb_wrapper)


    def getResourceTree(self, cb=None):
        def cb_wrapper(res):
            res['frameTree'] = Types.FrameResourceTree.safe_create(res['frameTree'])
            cb(res)
        self.chrome.send('Page.getResourceTree', cb=cb_wrapper)


    def handleJavaScriptDialog(self, accept, promptText, cb=None):
        """
        :param accept: Whether to accept or dismiss the dialog.
        :type accept: bool
        :param promptText: The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
        :type promptText: Optional[str]
        """
        msg_dict = dict()
        if accept is not None:
            msg_dict['accept'] = accept
        if promptText is not None:
            msg_dict['promptText'] = promptText
        self.chrome.send('Page.handleJavaScriptDialog', params=msg_dict)


    def navigate(self, url, referrer, transitionType, frameId, cb=None):
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
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        if referrer is not None:
            msg_dict['referrer'] = referrer
        if transitionType is not None:
            msg_dict['transitionType'] = transitionType
        if frameId is not None:
            msg_dict['frameId'] = frameId
        self.chrome.send('Page.navigate', params=msg_dict, cb=cb_wrapper)


    def navigateToHistoryEntry(self, entryId, cb=None):
        """
        :param entryId: Unique id of the entry to navigate to.
        :type entryId: int
        """
        msg_dict = dict()
        if entryId is not None:
            msg_dict['entryId'] = entryId
        self.chrome.send('Page.navigateToHistoryEntry', params=msg_dict)


    def printToPDF(self, landscape, displayHeaderFooter, printBackground, scale, paperWidth, paperHeight, marginTop, marginBottom, marginLeft, marginRight, pageRanges, ignoreInvalidPageRanges, headerTemplate, footerTemplate, preferCSSPageSize, cb=None):
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
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if landscape is not None:
            msg_dict['landscape'] = landscape
        if displayHeaderFooter is not None:
            msg_dict['displayHeaderFooter'] = displayHeaderFooter
        if printBackground is not None:
            msg_dict['printBackground'] = printBackground
        if scale is not None:
            msg_dict['scale'] = scale
        if paperWidth is not None:
            msg_dict['paperWidth'] = paperWidth
        if paperHeight is not None:
            msg_dict['paperHeight'] = paperHeight
        if marginTop is not None:
            msg_dict['marginTop'] = marginTop
        if marginBottom is not None:
            msg_dict['marginBottom'] = marginBottom
        if marginLeft is not None:
            msg_dict['marginLeft'] = marginLeft
        if marginRight is not None:
            msg_dict['marginRight'] = marginRight
        if pageRanges is not None:
            msg_dict['pageRanges'] = pageRanges
        if ignoreInvalidPageRanges is not None:
            msg_dict['ignoreInvalidPageRanges'] = ignoreInvalidPageRanges
        if headerTemplate is not None:
            msg_dict['headerTemplate'] = headerTemplate
        if footerTemplate is not None:
            msg_dict['footerTemplate'] = footerTemplate
        if preferCSSPageSize is not None:
            msg_dict['preferCSSPageSize'] = preferCSSPageSize
        self.chrome.send('Page.printToPDF', params=msg_dict, cb=cb_wrapper)


    def reload(self, ignoreCache, scriptToEvaluateOnLoad, cb=None):
        """
        :param ignoreCache: If true, browser cache is ignored (as if the user pressed Shift+refresh).
        :type ignoreCache: Optional[bool]
        :param scriptToEvaluateOnLoad: If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin.
        :type scriptToEvaluateOnLoad: Optional[str]
        """
        msg_dict = dict()
        if ignoreCache is not None:
            msg_dict['ignoreCache'] = ignoreCache
        if scriptToEvaluateOnLoad is not None:
            msg_dict['scriptToEvaluateOnLoad'] = scriptToEvaluateOnLoad
        self.chrome.send('Page.reload', params=msg_dict)


    def removeScriptToEvaluateOnLoad(self, identifier, cb=None):
        """
        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict['identifier'] = identifier
        self.chrome.send('Page.removeScriptToEvaluateOnLoad', params=msg_dict)


    def removeScriptToEvaluateOnNewDocument(self, identifier, cb=None):
        """
        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict['identifier'] = identifier
        self.chrome.send('Page.removeScriptToEvaluateOnNewDocument', params=msg_dict)


    def requestAppBanner(self, cb=None):
        self.chrome.send('Page.requestAppBanner')


    def screencastFrameAck(self, sessionId, cb=None):
        """
        :param sessionId: Frame number.
        :type sessionId: int
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict['sessionId'] = sessionId
        self.chrome.send('Page.screencastFrameAck', params=msg_dict)


    def searchInResource(self, frameId, url, query, caseSensitive, isRegex, cb=None):
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
        def cb_wrapper(res):
            res['result'] = Debugger.SearchMatch.safe_create_from_list(res['result'])
            cb(res)
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        if url is not None:
            msg_dict['url'] = url
        if query is not None:
            msg_dict['query'] = query
        if caseSensitive is not None:
            msg_dict['caseSensitive'] = caseSensitive
        if isRegex is not None:
            msg_dict['isRegex'] = isRegex
        self.chrome.send('Page.searchInResource', params=msg_dict, cb=cb_wrapper)


    def setAdBlockingEnabled(self, enabled, cb=None):
        """
        :param enabled: Whether to block ads.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        self.chrome.send('Page.setAdBlockingEnabled', params=msg_dict)


    def setBypassCSP(self, enabled, cb=None):
        """
        :param enabled: Whether to bypass page CSP.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        self.chrome.send('Page.setBypassCSP', params=msg_dict)


    def setDeviceMetricsOverride(self, width, height, deviceScaleFactor, mobile, scale, screenWidth, screenHeight, positionX, positionY, dontSetVisibleSize, screenOrientation, viewport, cb=None):
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
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if deviceScaleFactor is not None:
            msg_dict['deviceScaleFactor'] = deviceScaleFactor
        if mobile is not None:
            msg_dict['mobile'] = mobile
        if scale is not None:
            msg_dict['scale'] = scale
        if screenWidth is not None:
            msg_dict['screenWidth'] = screenWidth
        if screenHeight is not None:
            msg_dict['screenHeight'] = screenHeight
        if positionX is not None:
            msg_dict['positionX'] = positionX
        if positionY is not None:
            msg_dict['positionY'] = positionY
        if dontSetVisibleSize is not None:
            msg_dict['dontSetVisibleSize'] = dontSetVisibleSize
        if screenOrientation is not None:
            msg_dict['screenOrientation'] = screenOrientation
        if viewport is not None:
            msg_dict['viewport'] = viewport
        self.chrome.send('Page.setDeviceMetricsOverride', params=msg_dict)


    def setDeviceOrientationOverride(self, alpha, beta, gamma, cb=None):
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
            msg_dict['alpha'] = alpha
        if beta is not None:
            msg_dict['beta'] = beta
        if gamma is not None:
            msg_dict['gamma'] = gamma
        self.chrome.send('Page.setDeviceOrientationOverride', params=msg_dict)


    def setFontFamilies(self, fontFamilies, cb=None):
        """
        :param fontFamilies: Specifies font families to set. If a font family is not specified, it won't be changed.
        :type fontFamilies: dict
        """
        msg_dict = dict()
        if fontFamilies is not None:
            msg_dict['fontFamilies'] = fontFamilies
        self.chrome.send('Page.setFontFamilies', params=msg_dict)


    def setFontSizes(self, fontSizes, cb=None):
        """
        :param fontSizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        :type fontSizes: dict
        """
        msg_dict = dict()
        if fontSizes is not None:
            msg_dict['fontSizes'] = fontSizes
        self.chrome.send('Page.setFontSizes', params=msg_dict)


    def setDocumentContent(self, frameId, html, cb=None):
        """
        :param frameId: Frame id to set HTML for.
        :type frameId: str
        :param html: HTML content to set.
        :type html: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict['frameId'] = frameId
        if html is not None:
            msg_dict['html'] = html
        self.chrome.send('Page.setDocumentContent', params=msg_dict)


    def setDownloadBehavior(self, behavior, downloadPath, cb=None):
        """
        :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
        :type behavior: str
        :param downloadPath: The default path to save downloaded files to. This is requred if behavior is set to 'allow'
        :type downloadPath: Optional[str]
        """
        msg_dict = dict()
        if behavior is not None:
            msg_dict['behavior'] = behavior
        if downloadPath is not None:
            msg_dict['downloadPath'] = downloadPath
        self.chrome.send('Page.setDownloadBehavior', params=msg_dict)


    def setGeolocationOverride(self, latitude, longitude, accuracy, cb=None):
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
            msg_dict['latitude'] = latitude
        if longitude is not None:
            msg_dict['longitude'] = longitude
        if accuracy is not None:
            msg_dict['accuracy'] = accuracy
        self.chrome.send('Page.setGeolocationOverride', params=msg_dict)


    def setLifecycleEventsEnabled(self, enabled, cb=None):
        """
        :param enabled: If true, starts emitting lifecycle events.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        self.chrome.send('Page.setLifecycleEventsEnabled', params=msg_dict)


    def setTouchEmulationEnabled(self, enabled, configuration, cb=None):
        """
        :param enabled: Whether the touch event emulation should be enabled.
        :type enabled: bool
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :type configuration: Optional[str]
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        if configuration is not None:
            msg_dict['configuration'] = configuration
        self.chrome.send('Page.setTouchEmulationEnabled', params=msg_dict)


    def startScreencast(self, format, quality, maxWidth, maxHeight, everyNthFrame, cb=None):
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
            msg_dict['format'] = format
        if quality is not None:
            msg_dict['quality'] = quality
        if maxWidth is not None:
            msg_dict['maxWidth'] = maxWidth
        if maxHeight is not None:
            msg_dict['maxHeight'] = maxHeight
        if everyNthFrame is not None:
            msg_dict['everyNthFrame'] = everyNthFrame
        self.chrome.send('Page.startScreencast', params=msg_dict)


    def stopLoading(self, cb=None):
        self.chrome.send('Page.stopLoading')


    def crash(self, cb=None):
        self.chrome.send('Page.crash')


    def close(self, cb=None):
        self.chrome.send('Page.close')


    def setWebLifecycleState(self, state, cb=None):
        """
        :param state: Target lifecycle state
        :type state: str
        """
        msg_dict = dict()
        if state is not None:
            msg_dict['state'] = state
        self.chrome.send('Page.setWebLifecycleState', params=msg_dict)


    def stopScreencast(self, cb=None):
        self.chrome.send('Page.stopScreencast')


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

