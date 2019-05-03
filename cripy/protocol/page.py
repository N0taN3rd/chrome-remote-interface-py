"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Page"]


class Page:
    """
    Actions and events related to the inspected page belong to the page domain.
     
    Domain Dependencies: 
      * Debugger
      * DOM
      * Network
      * Runtime
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Page`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Page

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def addScriptToEvaluateOnLoad(self, scriptSource: str) -> Awaitable[Dict]:
        """
        Deprecated, please use addScriptToEvaluateOnNewDocument instead.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-addScriptToEvaluateOnLoad`

        :param scriptSource: The scriptSource
        :return: The results of the command
        """
        return self.client.send(
            "Page.addScriptToEvaluateOnLoad", {"scriptSource": scriptSource}
        )

    def addScriptToEvaluateOnNewDocument(
        self, source: str, worldName: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Evaluates given script in every frame upon creation (before loading frame's scripts).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-addScriptToEvaluateOnNewDocument`

        :param source: The source
        :param worldName: If specified, creates an isolated world with the given name and evaluates given script in it.
         This world name will be used as the ExecutionContextDescription::name when the corresponding
         event is emitted.
        :return: The results of the command
        """
        msg = {"source": source}
        if worldName is not None:
            msg["worldName"] = worldName
        return self.client.send("Page.addScriptToEvaluateOnNewDocument", msg)

    def bringToFront(self) -> Awaitable[Dict]:
        """
        Brings page to front (activates tab).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-bringToFront`

        :return: The results of the command
        """
        return self.client.send("Page.bringToFront", {})

    def captureScreenshot(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        clip: Optional[Dict[str, Any]] = None,
        fromSurface: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Capture page screenshot.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-captureScreenshot`

        :param format: Image compression format (defaults to png).
        :param quality: Compression quality from range [0..100] (jpeg only).
        :param clip: Capture the screenshot of a given region only.
        :param fromSurface: Capture the screenshot from the surface, rather than the view. Defaults to true.
        :return: The results of the command
        """
        msg = {}
        if format is not None:
            msg["format"] = format
        if quality is not None:
            msg["quality"] = quality
        if clip is not None:
            msg["clip"] = clip
        if fromSurface is not None:
            msg["fromSurface"] = fromSurface
        return self.client.send("Page.captureScreenshot", msg)

    def captureSnapshot(self, format: Optional[str] = None) -> Awaitable[Dict]:
        """
        Returns a snapshot of the page as a string. For MHTML format, the serialization includes
        iframes, shadow DOM, external resources, and element-inline styles.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-captureSnapshot`

        :param format: Format (defaults to mhtml).
        :return: The results of the command
        """
        msg = {}
        if format is not None:
            msg["format"] = format
        return self.client.send("Page.captureSnapshot", msg)

    def clearDeviceMetricsOverride(self) -> Awaitable[Dict]:
        """
        Clears the overriden device metrics.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-clearDeviceMetricsOverride`

        :return: The results of the command
        """
        return self.client.send("Page.clearDeviceMetricsOverride", {})

    def clearDeviceOrientationOverride(self) -> Awaitable[Dict]:
        """
        Clears the overridden Device Orientation.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-clearDeviceOrientationOverride`

        :return: The results of the command
        """
        return self.client.send("Page.clearDeviceOrientationOverride", {})

    def clearGeolocationOverride(self) -> Awaitable[Dict]:
        """
        Clears the overriden Geolocation Position and Error.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-clearGeolocationOverride`

        :return: The results of the command
        """
        return self.client.send("Page.clearGeolocationOverride", {})

    def createIsolatedWorld(
        self,
        frameId: str,
        worldName: Optional[str] = None,
        grantUniveralAccess: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Creates an isolated world for the given frame.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-createIsolatedWorld`

        :param frameId: Id of the frame in which the isolated world should be created.
        :param worldName: An optional name which is reported in the Execution Context.
        :param grantUniveralAccess: Whether or not universal access should be granted to the isolated world. This is a powerful
         option, use with caution.
        :return: The results of the command
        """
        msg = {"frameId": frameId}
        if worldName is not None:
            msg["worldName"] = worldName
        if grantUniveralAccess is not None:
            msg["grantUniveralAccess"] = grantUniveralAccess
        return self.client.send("Page.createIsolatedWorld", msg)

    def deleteCookie(self, cookieName: str, url: str) -> Awaitable[Dict]:
        """
        Deletes browser cookie with given name, domain and path.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-deleteCookie`

        :param cookieName: Name of the cookie to remove.
        :param url: URL to match cooke domain and path.
        :return: The results of the command
        """
        return self.client.send(
            "Page.deleteCookie", {"cookieName": cookieName, "url": url}
        )

    def disable(self) -> Awaitable[Dict]:
        """
        Disables page domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-disable`

        :return: The results of the command
        """
        return self.client.send("Page.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables page domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-enable`

        :return: The results of the command
        """
        return self.client.send("Page.enable", {})

    def getAppManifest(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getAppManifest`

        :return: The results of the command
        """
        return self.client.send("Page.getAppManifest", {})

    def getInstallabilityErrors(self) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getInstallabilityErrors`

        :return: The results of the command
        """
        return self.client.send("Page.getInstallabilityErrors", {})

    def getCookies(self) -> Awaitable[Dict]:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
        information in the `cookies` field.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getCookies`

        :return: The results of the command
        """
        return self.client.send("Page.getCookies", {})

    def getFrameTree(self) -> Awaitable[Dict]:
        """
        Returns present frame tree structure.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getFrameTree`

        :return: The results of the command
        """
        return self.client.send("Page.getFrameTree", {})

    def getLayoutMetrics(self) -> Awaitable[Dict]:
        """
        Returns metrics relating to the layouting of the page, such as viewport bounds/scale.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getLayoutMetrics`

        :return: The results of the command
        """
        return self.client.send("Page.getLayoutMetrics", {})

    def getNavigationHistory(self) -> Awaitable[Dict]:
        """
        Returns navigation history for the current page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getNavigationHistory`

        :return: The results of the command
        """
        return self.client.send("Page.getNavigationHistory", {})

    def resetNavigationHistory(self) -> Awaitable[Dict]:
        """
        Resets navigation history for the current page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-resetNavigationHistory`

        :return: The results of the command
        """
        return self.client.send("Page.resetNavigationHistory", {})

    def getResourceContent(self, frameId: str, url: str) -> Awaitable[Dict]:
        """
        Returns content of the given resource.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getResourceContent`

        :param frameId: Frame id to get resource for.
        :param url: URL of the resource to get content for.
        :return: The results of the command
        """
        return self.client.send(
            "Page.getResourceContent", {"frameId": frameId, "url": url}
        )

    def getResourceTree(self) -> Awaitable[Dict]:
        """
        Returns present frame / resource tree structure.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-getResourceTree`

        :return: The results of the command
        """
        return self.client.send("Page.getResourceTree", {})

    def handleJavaScriptDialog(
        self, accept: bool, promptText: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-handleJavaScriptDialog`

        :param accept: Whether to accept or dismiss the dialog.
        :param promptText: The text to enter into the dialog prompt before accepting. Used only if this is a prompt
         dialog.
        :return: The results of the command
        """
        msg = {"accept": accept}
        if promptText is not None:
            msg["promptText"] = promptText
        return self.client.send("Page.handleJavaScriptDialog", msg)

    def navigate(
        self,
        url: str,
        referrer: Optional[str] = None,
        transitionType: Optional[str] = None,
        frameId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Navigates current page to the given URL.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-navigate`

        :param url: URL to navigate the page to.
        :param referrer: Referrer URL.
        :param transitionType: Intended transition type.
        :param frameId: Frame id to navigate, if not specified navigates the top frame.
        :return: The results of the command
        """
        msg = {"url": url}
        if referrer is not None:
            msg["referrer"] = referrer
        if transitionType is not None:
            msg["transitionType"] = transitionType
        if frameId is not None:
            msg["frameId"] = frameId
        return self.client.send("Page.navigate", msg)

    def navigateToHistoryEntry(self, entryId: int) -> Awaitable[Dict]:
        """
        Navigates current page to the given history entry.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-navigateToHistoryEntry`

        :param entryId: Unique id of the entry to navigate to.
        :return: The results of the command
        """
        return self.client.send("Page.navigateToHistoryEntry", {"entryId": entryId})

    def printToPDF(
        self,
        landscape: Optional[bool] = None,
        displayHeaderFooter: Optional[bool] = None,
        printBackground: Optional[bool] = None,
        scale: Optional[Union[int, float]] = None,
        paperWidth: Optional[Union[int, float]] = None,
        paperHeight: Optional[Union[int, float]] = None,
        marginTop: Optional[Union[int, float]] = None,
        marginBottom: Optional[Union[int, float]] = None,
        marginLeft: Optional[Union[int, float]] = None,
        marginRight: Optional[Union[int, float]] = None,
        pageRanges: Optional[str] = None,
        ignoreInvalidPageRanges: Optional[bool] = None,
        headerTemplate: Optional[str] = None,
        footerTemplate: Optional[str] = None,
        preferCSSPageSize: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Print page as PDF.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-printToPDF`

        :param landscape: Paper orientation. Defaults to false.
        :param displayHeaderFooter: Display header and footer. Defaults to false.
        :param printBackground: Print background graphics. Defaults to false.
        :param scale: Scale of the webpage rendering. Defaults to 1.
        :param paperWidth: Paper width in inches. Defaults to 8.5 inches.
        :param paperHeight: Paper height in inches. Defaults to 11 inches.
        :param marginTop: Top margin in inches. Defaults to 1cm (~0.4 inches).
        :param marginBottom: Bottom margin in inches. Defaults to 1cm (~0.4 inches).
        :param marginLeft: Left margin in inches. Defaults to 1cm (~0.4 inches).
        :param marginRight: Right margin in inches. Defaults to 1cm (~0.4 inches).
        :param pageRanges: Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means
         print all pages.
        :param ignoreInvalidPageRanges: Whether to silently ignore invalid but successfully parsed page ranges, such as '3-2'.
         Defaults to false.
        :param headerTemplate: HTML template for the print header. Should be valid HTML markup with following
         classes used to inject printing values into them:
         - `date`: formatted print date
         - `title`: document title
         - `url`: document location
         - `pageNumber`: current page number
         - `totalPages`: total pages in the document
         
         For example, `<span class=title></span>` would generate span containing the title.
        :param footerTemplate: HTML template for the print footer. Should use the same format as the `headerTemplate`.
        :param preferCSSPageSize: Whether or not to prefer page size as defined by css. Defaults to false,
         in which case the content will be scaled to fit the paper size.
        :return: The results of the command
        """
        msg = {}
        if landscape is not None:
            msg["landscape"] = landscape
        if displayHeaderFooter is not None:
            msg["displayHeaderFooter"] = displayHeaderFooter
        if printBackground is not None:
            msg["printBackground"] = printBackground
        if scale is not None:
            msg["scale"] = scale
        if paperWidth is not None:
            msg["paperWidth"] = paperWidth
        if paperHeight is not None:
            msg["paperHeight"] = paperHeight
        if marginTop is not None:
            msg["marginTop"] = marginTop
        if marginBottom is not None:
            msg["marginBottom"] = marginBottom
        if marginLeft is not None:
            msg["marginLeft"] = marginLeft
        if marginRight is not None:
            msg["marginRight"] = marginRight
        if pageRanges is not None:
            msg["pageRanges"] = pageRanges
        if ignoreInvalidPageRanges is not None:
            msg["ignoreInvalidPageRanges"] = ignoreInvalidPageRanges
        if headerTemplate is not None:
            msg["headerTemplate"] = headerTemplate
        if footerTemplate is not None:
            msg["footerTemplate"] = footerTemplate
        if preferCSSPageSize is not None:
            msg["preferCSSPageSize"] = preferCSSPageSize
        return self.client.send("Page.printToPDF", msg)

    def reload(
        self,
        ignoreCache: Optional[bool] = None,
        scriptToEvaluateOnLoad: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Reloads given page optionally ignoring the cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-reload`

        :param ignoreCache: If true, browser cache is ignored (as if the user pressed Shift+refresh).
        :param scriptToEvaluateOnLoad: If set, the script will be injected into all frames of the inspected page after reload.
         Argument will be ignored if reloading dataURL origin.
        :return: The results of the command
        """
        msg = {}
        if ignoreCache is not None:
            msg["ignoreCache"] = ignoreCache
        if scriptToEvaluateOnLoad is not None:
            msg["scriptToEvaluateOnLoad"] = scriptToEvaluateOnLoad
        return self.client.send("Page.reload", msg)

    def removeScriptToEvaluateOnLoad(self, identifier: str) -> Awaitable[Dict]:
        """
        Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-removeScriptToEvaluateOnLoad`

        :param identifier: The identifier
        :return: The results of the command
        """
        return self.client.send(
            "Page.removeScriptToEvaluateOnLoad", {"identifier": identifier}
        )

    def removeScriptToEvaluateOnNewDocument(self, identifier: str) -> Awaitable[Dict]:
        """
        Removes given script from the list.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-removeScriptToEvaluateOnNewDocument`

        :param identifier: The identifier
        :return: The results of the command
        """
        return self.client.send(
            "Page.removeScriptToEvaluateOnNewDocument", {"identifier": identifier}
        )

    def screencastFrameAck(self, sessionId: int) -> Awaitable[Dict]:
        """
        Acknowledges that a screencast frame has been received by the frontend.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-screencastFrameAck`

        :param sessionId: Frame number.
        :return: The results of the command
        """
        return self.client.send("Page.screencastFrameAck", {"sessionId": sessionId})

    def searchInResource(
        self,
        frameId: str,
        url: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Searches for given string in resource content.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-searchInResource`

        :param frameId: Frame id for resource to search in.
        :param url: URL of the resource to search in.
        :param query: String to search for.
        :param caseSensitive: If true, search is case sensitive.
        :param isRegex: If true, treats string parameter as regex.
        :return: The results of the command
        """
        msg = {"frameId": frameId, "url": url, "query": query}
        if caseSensitive is not None:
            msg["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg["isRegex"] = isRegex
        return self.client.send("Page.searchInResource", msg)

    def setAdBlockingEnabled(self, enabled: bool) -> Awaitable[Dict]:
        """
        Enable Chrome's experimental ad filter on all sites.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setAdBlockingEnabled`

        :param enabled: Whether to block ads.
        :return: The results of the command
        """
        return self.client.send("Page.setAdBlockingEnabled", {"enabled": enabled})

    def setBypassCSP(self, enabled: bool) -> Awaitable[Dict]:
        """
        Enable page Content Security Policy by-passing.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setBypassCSP`

        :param enabled: Whether to bypass page CSP.
        :return: The results of the command
        """
        return self.client.send("Page.setBypassCSP", {"enabled": enabled})

    def setDeviceMetricsOverride(
        self,
        width: int,
        height: int,
        deviceScaleFactor: Union[int, float],
        mobile: bool,
        scale: Optional[Union[int, float]] = None,
        screenWidth: Optional[int] = None,
        screenHeight: Optional[int] = None,
        positionX: Optional[int] = None,
        positionY: Optional[int] = None,
        dontSetVisibleSize: Optional[bool] = None,
        screenOrientation: Optional[Dict[str, Any]] = None,
        viewport: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
        window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
        query results).

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setDeviceMetricsOverride`

        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
         autosizing and more.
        :param scale: Scale to apply to resulting view image.
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :param dontSetVisibleSize: Do not set visible view size, rely upon explicit setVisibleSize call.
        :param screenOrientation: Screen orientation override.
        :param viewport: The viewport dimensions and scale. If not set, the override is cleared.
        :return: The results of the command
        """
        msg = {
            "width": width,
            "height": height,
            "deviceScaleFactor": deviceScaleFactor,
            "mobile": mobile,
        }
        if scale is not None:
            msg["scale"] = scale
        if screenWidth is not None:
            msg["screenWidth"] = screenWidth
        if screenHeight is not None:
            msg["screenHeight"] = screenHeight
        if positionX is not None:
            msg["positionX"] = positionX
        if positionY is not None:
            msg["positionY"] = positionY
        if dontSetVisibleSize is not None:
            msg["dontSetVisibleSize"] = dontSetVisibleSize
        if screenOrientation is not None:
            msg["screenOrientation"] = screenOrientation
        if viewport is not None:
            msg["viewport"] = viewport
        return self.client.send("Page.setDeviceMetricsOverride", msg)

    def setDeviceOrientationOverride(
        self,
        alpha: Union[int, float],
        beta: Union[int, float],
        gamma: Union[int, float],
    ) -> Awaitable[Dict]:
        """
        Overrides the Device Orientation.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setDeviceOrientationOverride`

        :param alpha: Mock alpha
        :param beta: Mock beta
        :param gamma: Mock gamma
        :return: The results of the command
        """
        return self.client.send(
            "Page.setDeviceOrientationOverride",
            {"alpha": alpha, "beta": beta, "gamma": gamma},
        )

    def setFontFamilies(self, fontFamilies: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Set generic font families.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setFontFamilies`

        :param fontFamilies: Specifies font families to set. If a font family is not specified, it won't be changed.
        :return: The results of the command
        """
        return self.client.send("Page.setFontFamilies", {"fontFamilies": fontFamilies})

    def setFontSizes(self, fontSizes: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Set default font sizes.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setFontSizes`

        :param fontSizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        :return: The results of the command
        """
        return self.client.send("Page.setFontSizes", {"fontSizes": fontSizes})

    def setDocumentContent(self, frameId: str, html: str) -> Awaitable[Dict]:
        """
        Sets given markup as the document's HTML.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setDocumentContent`

        :param frameId: Frame id to set HTML for.
        :param html: HTML content to set.
        :return: The results of the command
        """
        return self.client.send(
            "Page.setDocumentContent", {"frameId": frameId, "html": html}
        )

    def setDownloadBehavior(
        self, behavior: str, downloadPath: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Set the behavior when downloading a file.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setDownloadBehavior`

        :param behavior: Whether to allow all or deny all download requests, or use default Chrome behavior if
         available (otherwise deny).
        :param downloadPath: The default path to save downloaded files to. This is requred if behavior is set to 'allow'
        :return: The results of the command
        """
        msg = {"behavior": behavior}
        if downloadPath is not None:
            msg["downloadPath"] = downloadPath
        return self.client.send("Page.setDownloadBehavior", msg)

    def setGeolocationOverride(
        self,
        latitude: Optional[Union[int, float]] = None,
        longitude: Optional[Union[int, float]] = None,
        accuracy: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
        unavailable.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setGeolocationOverride`

        :param latitude: Mock latitude
        :param longitude: Mock longitude
        :param accuracy: Mock accuracy
        :return: The results of the command
        """
        msg = {}
        if latitude is not None:
            msg["latitude"] = latitude
        if longitude is not None:
            msg["longitude"] = longitude
        if accuracy is not None:
            msg["accuracy"] = accuracy
        return self.client.send("Page.setGeolocationOverride", msg)

    def setLifecycleEventsEnabled(self, enabled: bool) -> Awaitable[Dict]:
        """
        Controls whether page will emit lifecycle events.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setLifecycleEventsEnabled`

        :param enabled: If true, starts emitting lifecycle events.
        :return: The results of the command
        """
        return self.client.send("Page.setLifecycleEventsEnabled", {"enabled": enabled})

    def setTouchEmulationEnabled(
        self, enabled: bool, configuration: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Toggles mouse event-based touch event emulation.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setTouchEmulationEnabled`

        :param enabled: Whether the touch event emulation should be enabled.
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :return: The results of the command
        """
        msg = {"enabled": enabled}
        if configuration is not None:
            msg["configuration"] = configuration
        return self.client.send("Page.setTouchEmulationEnabled", msg)

    def startScreencast(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        maxWidth: Optional[int] = None,
        maxHeight: Optional[int] = None,
        everyNthFrame: Optional[int] = None,
    ) -> Awaitable[Dict]:
        """
        Starts sending each frame using the `screencastFrame` event.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-startScreencast`

        :param format: Image compression format.
        :param quality: Compression quality from range [0..100].
        :param maxWidth: Maximum screenshot width.
        :param maxHeight: Maximum screenshot height.
        :param everyNthFrame: Send every n-th frame.
        :return: The results of the command
        """
        msg = {}
        if format is not None:
            msg["format"] = format
        if quality is not None:
            msg["quality"] = quality
        if maxWidth is not None:
            msg["maxWidth"] = maxWidth
        if maxHeight is not None:
            msg["maxHeight"] = maxHeight
        if everyNthFrame is not None:
            msg["everyNthFrame"] = everyNthFrame
        return self.client.send("Page.startScreencast", msg)

    def stopLoading(self) -> Awaitable[Dict]:
        """
        Force the page stop all navigations and pending resource fetches.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-stopLoading`

        :return: The results of the command
        """
        return self.client.send("Page.stopLoading", {})

    def crash(self) -> Awaitable[Dict]:
        """
        Crashes renderer on the IO thread, generates minidumps.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-crash`

        :return: The results of the command
        """
        return self.client.send("Page.crash", {})

    def close(self) -> Awaitable[Dict]:
        """
        Tries to close page, running its beforeunload hooks, if any.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-close`

        :return: The results of the command
        """
        return self.client.send("Page.close", {})

    def setWebLifecycleState(self, state: str) -> Awaitable[Dict]:
        """
        Tries to update the web lifecycle state of the page.
        It will transition the page to the given state according to:
        https://github.com/WICG/web-lifecycle/

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setWebLifecycleState`

        :param state: Target lifecycle state
        :return: The results of the command
        """
        return self.client.send("Page.setWebLifecycleState", {"state": state})

    def stopScreencast(self) -> Awaitable[Dict]:
        """
        Stops sending each frame in the `screencastFrame`.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-stopScreencast`

        :return: The results of the command
        """
        return self.client.send("Page.stopScreencast", {})

    def setProduceCompilationCache(self, enabled: bool) -> Awaitable[Dict]:
        """
        Forces compilation cache to be generated for every subresource script.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-setProduceCompilationCache`

        :param enabled: The enabled
        :return: The results of the command
        """
        return self.client.send("Page.setProduceCompilationCache", {"enabled": enabled})

    def addCompilationCache(self, url: str, data: str) -> Awaitable[Dict]:
        """
        Seeds compilation cache for given url. Compilation cache does not survive
        cross-process navigation.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-addCompilationCache`

        :param url: The url
        :param data: Base64-encoded data
        :return: The results of the command
        """
        return self.client.send("Page.addCompilationCache", {"url": url, "data": data})

    def clearCompilationCache(self) -> Awaitable[Dict]:
        """
        Clears seeded compilation cache.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-clearCompilationCache`

        :return: The results of the command
        """
        return self.client.send("Page.clearCompilationCache", {})

    def generateTestReport(
        self, message: str, group: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Generates a report for testing.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-generateTestReport`

        :param message: Message to be displayed in the report.
        :param group: Specifies the endpoint group to deliver the report to.
        :return: The results of the command
        """
        msg = {"message": message}
        if group is not None:
            msg["group"] = group
        return self.client.send("Page.generateTestReport", msg)

    def waitForDebugger(self) -> Awaitable[Dict]:
        """
        Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#method-waitForDebugger`

        :return: The results of the command
        """
        return self.client.send("Page.waitForDebugger", {})

    def domContentEventFired(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-domContentEventFired`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.domContentEventFired"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameAttached(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame has been attached to its parent.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameAttached`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameAttached"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameClearedScheduledNavigation(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame no longer has a scheduled navigation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameClearedScheduledNavigation`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameClearedScheduledNavigation"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameDetached(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame has been detached from its parent.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameDetached`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameDetached"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameNavigated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired once navigation of the frame has completed. Frame is now associated with the new loader.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameNavigated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameNavigated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameResized(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameResized`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameResized"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameRequestedNavigation(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when a renderer-initiated navigation is requested.
        Navigation may still be cancelled after the event is issued.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameRequestedNavigation`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameRequestedNavigation"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameScheduledNavigation(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame schedules a potential navigation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameScheduledNavigation`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameScheduledNavigation"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameStartedLoading(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame has started loading.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameStartedLoading`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameStartedLoading"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def frameStoppedLoading(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when frame has stopped loading.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-frameStoppedLoading`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.frameStoppedLoading"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def interstitialHidden(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Fired when interstitial page was hidden

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-interstitialHidden`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.interstitialHidden"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def interstitialShown(self, listener: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        Fired when interstitial page was shown

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-interstitialShown`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.interstitialShown"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def javascriptDialogClosed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
        closed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-javascriptDialogClosed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.javascriptDialogClosed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def javascriptDialogOpening(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
        open.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-javascriptDialogOpening`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.javascriptDialogOpening"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def lifecycleEvent(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired for top level page lifecycle events such as navigation, load, paint, etc.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-lifecycleEvent`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.lifecycleEvent"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def loadEventFired(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-loadEventFired`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.loadEventFired"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def navigatedWithinDocument(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-navigatedWithinDocument`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.navigatedWithinDocument"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def screencastFrame(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Compressed image data requested by the `startScreencast`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-screencastFrame`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.screencastFrame"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def screencastVisibilityChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when the page with currently enabled screencast was shown or hidden `.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-screencastVisibilityChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.screencastVisibilityChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def windowOpen(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when a new window is going to be opened, via window.open(), link click, form submission,
        etc.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-windowOpen`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.windowOpen"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def compilationCacheProduced(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued for every compilation cache generated. Is only available
        if Page.setGenerateCompilationCache is enabled.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Page#event-compilationCacheProduced`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Page.compilationCacheProduced"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
