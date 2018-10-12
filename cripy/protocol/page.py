# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Page"]


class Page(object):
    """
    Actions and events related to the inspected page belong to the page domain.
    """

    dependencies: ClassVar[List[str]] = ["Debugger", "DOM", "Network"]

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def addScriptToEvaluateOnLoad(self, scriptSource: str) -> Optional[dict]:
        """
        Deprecated, please use addScriptToEvaluateOnNewDocument instead.

        :param scriptSource: The scriptSource
        :type scriptSource: str
        """
        msg_dict = dict()
        if scriptSource is not None:
            msg_dict["scriptSource"] = scriptSource
        res = await self.client.send("Page.addScriptToEvaluateOnLoad", msg_dict)
        return res

    async def addScriptToEvaluateOnNewDocument(self, source: str) -> Optional[dict]:
        """
        Evaluates given script in every frame upon creation (before loading frame's scripts).

        :param source: The source
        :type source: str
        """
        msg_dict = dict()
        if source is not None:
            msg_dict["source"] = source
        res = await self.client.send("Page.addScriptToEvaluateOnNewDocument", msg_dict)
        return res

    async def bringToFront(self) -> Optional[dict]:
        """
        Brings page to front (activates tab).
        """
        res = await self.client.send("Page.bringToFront")
        return res

    async def captureScreenshot(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        clip: Optional[dict] = None,
        fromSurface: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Capture page screenshot.

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
        res = await self.client.send("Page.captureScreenshot", msg_dict)
        return res

    async def clearDeviceMetricsOverride(self) -> Optional[dict]:
        """
        Clears the overriden device metrics.
        """
        res = await self.client.send("Page.clearDeviceMetricsOverride")
        return res

    async def clearDeviceOrientationOverride(self) -> Optional[dict]:
        """
        Clears the overridden Device Orientation.
        """
        res = await self.client.send("Page.clearDeviceOrientationOverride")
        return res

    async def clearGeolocationOverride(self) -> Optional[dict]:
        """
        Clears the overriden Geolocation Position and Error.
        """
        res = await self.client.send("Page.clearGeolocationOverride")
        return res

    async def createIsolatedWorld(
        self,
        frameId: str,
        worldName: Optional[str] = None,
        grantUniveralAccess: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Creates an isolated world for the given frame.

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
        res = await self.client.send("Page.createIsolatedWorld", msg_dict)
        return res

    async def deleteCookie(self, cookieName: str, url: str) -> Optional[dict]:
        """
        Deletes browser cookie with given name, domain and path.

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
        res = await self.client.send("Page.deleteCookie", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables page domain notifications.
        """
        res = await self.client.send("Page.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables page domain notifications.
        """
        res = await self.client.send("Page.enable")
        return res

    async def getAppManifest(self) -> Optional[dict]:
        res = await self.client.send("Page.getAppManifest")
        return res

    async def getCookies(self) -> Optional[dict]:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
        """
        res = await self.client.send("Page.getCookies")
        return res

    async def getFrameTree(self) -> Optional[dict]:
        """
        Returns present frame tree structure.
        """
        res = await self.client.send("Page.getFrameTree")
        return res

    async def getLayoutMetrics(self) -> Optional[dict]:
        """
        Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
        """
        res = await self.client.send("Page.getLayoutMetrics")
        return res

    async def getNavigationHistory(self) -> Optional[dict]:
        """
        Returns navigation history for the current page.
        """
        res = await self.client.send("Page.getNavigationHistory")
        return res

    async def getResourceContent(self, frameId: str, url: str) -> Optional[dict]:
        """
        Returns content of the given resource.

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
        res = await self.client.send("Page.getResourceContent", msg_dict)
        return res

    async def getResourceTree(self) -> Optional[dict]:
        """
        Returns present frame / resource tree structure.
        """
        res = await self.client.send("Page.getResourceTree")
        return res

    async def handleJavaScriptDialog(
        self, accept: bool, promptText: Optional[str] = None
    ) -> Optional[dict]:
        """
        Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).

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
        res = await self.client.send("Page.handleJavaScriptDialog", msg_dict)
        return res

    async def navigate(
        self,
        url: str,
        referrer: Optional[str] = None,
        transitionType: Optional[str] = None,
        frameId: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Navigates current page to the given URL.

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
        res = await self.client.send("Page.navigate", msg_dict)
        return res

    async def navigateToHistoryEntry(self, entryId: int) -> Optional[dict]:
        """
        Navigates current page to the given history entry.

        :param entryId: Unique id of the entry to navigate to.
        :type entryId: int
        """
        msg_dict = dict()
        if entryId is not None:
            msg_dict["entryId"] = entryId
        res = await self.client.send("Page.navigateToHistoryEntry", msg_dict)
        return res

    async def printToPDF(
        self,
        landscape: Optional[bool] = None,
        displayHeaderFooter: Optional[bool] = None,
        printBackground: Optional[bool] = None,
        scale: Optional[float] = None,
        paperWidth: Optional[float] = None,
        paperHeight: Optional[float] = None,
        marginTop: Optional[float] = None,
        marginBottom: Optional[float] = None,
        marginLeft: Optional[float] = None,
        marginRight: Optional[float] = None,
        pageRanges: Optional[str] = None,
        ignoreInvalidPageRanges: Optional[bool] = None,
        headerTemplate: Optional[str] = None,
        footerTemplate: Optional[str] = None,
        preferCSSPageSize: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Print page as PDF.

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
        res = await self.client.send("Page.printToPDF", msg_dict)
        return res

    async def reload(
        self,
        ignoreCache: Optional[bool] = None,
        scriptToEvaluateOnLoad: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Reloads given page optionally ignoring the cache.

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
        res = await self.client.send("Page.reload", msg_dict)
        return res

    async def removeScriptToEvaluateOnLoad(self, identifier: str) -> Optional[dict]:
        """
        Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        res = await self.client.send("Page.removeScriptToEvaluateOnLoad", msg_dict)
        return res

    async def removeScriptToEvaluateOnNewDocument(
        self, identifier: str
    ) -> Optional[dict]:
        """
        Removes given script from the list.

        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        res = await self.client.send(
            "Page.removeScriptToEvaluateOnNewDocument", msg_dict
        )
        return res

    async def requestAppBanner(self) -> Optional[dict]:
        res = await self.client.send("Page.requestAppBanner")
        return res

    async def screencastFrameAck(self, sessionId: int) -> Optional[dict]:
        """
        Acknowledges that a screencast frame has been received by the frontend.

        :param sessionId: Frame number.
        :type sessionId: int
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict["sessionId"] = sessionId
        res = await self.client.send("Page.screencastFrameAck", msg_dict)
        return res

    async def searchInResource(
        self,
        frameId: str,
        url: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Searches for given string in resource content.

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
        res = await self.client.send("Page.searchInResource", msg_dict)
        return res

    async def setAdBlockingEnabled(self, enabled: bool) -> Optional[dict]:
        """
        Enable Chrome's experimental ad filter on all sites.

        :param enabled: Whether to block ads.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        res = await self.client.send("Page.setAdBlockingEnabled", msg_dict)
        return res

    async def setBypassCSP(self, enabled: bool) -> Optional[dict]:
        """
        Enable page Content Security Policy by-passing.

        :param enabled: Whether to bypass page CSP.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        res = await self.client.send("Page.setBypassCSP", msg_dict)
        return res

    async def setDeviceMetricsOverride(
        self,
        width: int,
        height: int,
        deviceScaleFactor: float,
        mobile: bool,
        scale: Optional[float] = None,
        screenWidth: Optional[int] = None,
        screenHeight: Optional[int] = None,
        positionX: Optional[int] = None,
        positionY: Optional[int] = None,
        dontSetVisibleSize: Optional[bool] = None,
        screenOrientation: Optional[dict] = None,
        viewport: Optional[dict] = None,
    ) -> Optional[dict]:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).

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
        res = await self.client.send("Page.setDeviceMetricsOverride", msg_dict)
        return res

    async def setDeviceOrientationOverride(
        self, alpha: float, beta: float, gamma: float
    ) -> Optional[dict]:
        """
        Overrides the Device Orientation.

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
        res = await self.client.send("Page.setDeviceOrientationOverride", msg_dict)
        return res

    async def setFontFamilies(self, fontFamilies: dict) -> Optional[dict]:
        """
        Set generic font families.

        :param fontFamilies: Specifies font families to set. If a font family is not specified, it won't be changed.
        :type fontFamilies: dict
        """
        msg_dict = dict()
        if fontFamilies is not None:
            msg_dict["fontFamilies"] = fontFamilies
        res = await self.client.send("Page.setFontFamilies", msg_dict)
        return res

    async def setFontSizes(self, fontSizes: dict) -> Optional[dict]:
        """
        Set default font sizes.

        :param fontSizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        :type fontSizes: dict
        """
        msg_dict = dict()
        if fontSizes is not None:
            msg_dict["fontSizes"] = fontSizes
        res = await self.client.send("Page.setFontSizes", msg_dict)
        return res

    async def setDocumentContent(self, frameId: str, html: str) -> Optional[dict]:
        """
        Sets given markup as the document's HTML.

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
        res = await self.client.send("Page.setDocumentContent", msg_dict)
        return res

    async def setDownloadBehavior(
        self, behavior: str, downloadPath: Optional[str] = None
    ) -> Optional[dict]:
        """
        Set the behavior when downloading a file.

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
        res = await self.client.send("Page.setDownloadBehavior", msg_dict)
        return res

    async def setGeolocationOverride(
        self,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        accuracy: Optional[float] = None,
    ) -> Optional[dict]:
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.

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
        res = await self.client.send("Page.setGeolocationOverride", msg_dict)
        return res

    async def setLifecycleEventsEnabled(self, enabled: bool) -> Optional[dict]:
        """
        Controls whether page will emit lifecycle events.

        :param enabled: If true, starts emitting lifecycle events.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        res = await self.client.send("Page.setLifecycleEventsEnabled", msg_dict)
        return res

    async def setTouchEmulationEnabled(
        self, enabled: bool, configuration: Optional[str] = None
    ) -> Optional[dict]:
        """
        Toggles mouse event-based touch event emulation.

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
        res = await self.client.send("Page.setTouchEmulationEnabled", msg_dict)
        return res

    async def startScreencast(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        maxWidth: Optional[int] = None,
        maxHeight: Optional[int] = None,
        everyNthFrame: Optional[int] = None,
    ) -> Optional[dict]:
        """
        Starts sending each frame using the `screencastFrame` event.

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
        res = await self.client.send("Page.startScreencast", msg_dict)
        return res

    async def stopLoading(self) -> Optional[dict]:
        """
        Force the page stop all navigations and pending resource fetches.
        """
        res = await self.client.send("Page.stopLoading")
        return res

    async def crash(self) -> Optional[dict]:
        """
        Crashes renderer on the IO thread, generates minidumps.
        """
        res = await self.client.send("Page.crash")
        return res

    async def close(self) -> Optional[dict]:
        """
        Tries to close page, running its beforeunload hooks, if any.
        """
        res = await self.client.send("Page.close")
        return res

    async def setWebLifecycleState(self, state: str) -> Optional[dict]:
        """
        Tries to update the web lifecycle state of the page.
It will transition the page to the given state according to:
https://github.com/WICG/web-lifecycle/

        :param state: Target lifecycle state
        :type state: str
        """
        msg_dict = dict()
        if state is not None:
            msg_dict["state"] = state
        res = await self.client.send("Page.setWebLifecycleState", msg_dict)
        return res

    async def stopScreencast(self) -> Optional[dict]:
        """
        Stops sending each frame in the `screencastFrame`.
        """
        res = await self.client.send("Page.stopScreencast")
        return res

    async def setProduceCompilationCache(self, enabled: bool) -> Optional[dict]:
        """
        Forces compilation cache to be generated for every subresource script.

        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        res = await self.client.send("Page.setProduceCompilationCache", msg_dict)
        return res

    async def addCompilationCache(self, url: str, data: str) -> Optional[dict]:
        """
        Seeds compilation cache for given url. Compilation cache does not survive
cross-process navigation.

        :param url: The url
        :type url: str
        :param data: Base64-encoded data
        :type data: str
        """
        msg_dict = dict()
        if url is not None:
            msg_dict["url"] = url
        if data is not None:
            msg_dict["data"] = data
        res = await self.client.send("Page.addCompilationCache", msg_dict)
        return res

    async def clearCompilationCache(self) -> Optional[dict]:
        """
        Clears seeded compilation cache.
        """
        res = await self.client.send("Page.clearCompilationCache")
        return res

    def domContentEventFired(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("Page.domContentEventFired", fn)
        else:
            self.client.on("Page.domContentEventFired", fn)

    def frameAttached(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when frame has been attached to its parent.
        """
        if once:
            self.client.once("Page.frameAttached", fn)
        else:
            self.client.on("Page.frameAttached", fn)

    def frameClearedScheduledNavigation(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when frame no longer has a scheduled navigation.
        """
        if once:
            self.client.once("Page.frameClearedScheduledNavigation", fn)
        else:
            self.client.on("Page.frameClearedScheduledNavigation", fn)

    def frameDetached(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when frame has been detached from its parent.
        """
        if once:
            self.client.once("Page.frameDetached", fn)
        else:
            self.client.on("Page.frameDetached", fn)

    def frameNavigated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired once navigation of the frame has completed. Frame is now associated with the new loader.
        """
        if once:
            self.client.once("Page.frameNavigated", fn)
        else:
            self.client.on("Page.frameNavigated", fn)

    def frameResized(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("Page.frameResized", fn)
        else:
            self.client.on("Page.frameResized", fn)

    def frameScheduledNavigation(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when frame schedules a potential navigation.
        """
        if once:
            self.client.once("Page.frameScheduledNavigation", fn)
        else:
            self.client.on("Page.frameScheduledNavigation", fn)

    def frameStartedLoading(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when frame has started loading.
        """
        if once:
            self.client.once("Page.frameStartedLoading", fn)
        else:
            self.client.on("Page.frameStartedLoading", fn)

    def frameStoppedLoading(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when frame has stopped loading.
        """
        if once:
            self.client.once("Page.frameStoppedLoading", fn)
        else:
            self.client.on("Page.frameStoppedLoading", fn)

    def interstitialHidden(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when interstitial page was hidden
        """
        if once:
            self.client.once("Page.interstitialHidden", fn)
        else:
            self.client.on("Page.interstitialHidden", fn)

    def interstitialShown(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when interstitial page was shown
        """
        if once:
            self.client.once("Page.interstitialShown", fn)
        else:
            self.client.on("Page.interstitialShown", fn)

    def javascriptDialogClosed(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
        closed.
        """
        if once:
            self.client.once("Page.javascriptDialogClosed", fn)
        else:
            self.client.on("Page.javascriptDialogClosed", fn)

    def javascriptDialogOpening(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
        open.
        """
        if once:
            self.client.once("Page.javascriptDialogOpening", fn)
        else:
            self.client.on("Page.javascriptDialogOpening", fn)

    def lifecycleEvent(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired for top level page lifecycle events such as navigation, load, paint, etc.
        """
        if once:
            self.client.once("Page.lifecycleEvent", fn)
        else:
            self.client.on("Page.lifecycleEvent", fn)

    def loadEventFired(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("Page.loadEventFired", fn)
        else:
            self.client.on("Page.loadEventFired", fn)

    def navigatedWithinDocument(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.
        """
        if once:
            self.client.once("Page.navigatedWithinDocument", fn)
        else:
            self.client.on("Page.navigatedWithinDocument", fn)

    def screencastFrame(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Compressed image data requested by the `startScreencast`.
        """
        if once:
            self.client.once("Page.screencastFrame", fn)
        else:
            self.client.on("Page.screencastFrame", fn)

    def screencastVisibilityChanged(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when the page with currently enabled screencast was shown or hidden `.
        """
        if once:
            self.client.once("Page.screencastVisibilityChanged", fn)
        else:
            self.client.on("Page.screencastVisibilityChanged", fn)

    def windowOpen(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when a new window is going to be opened, via window.open(), link click, form submission,
        etc.
        """
        if once:
            self.client.once("Page.windowOpen", fn)
        else:
            self.client.on("Page.windowOpen", fn)

    def compilationCacheProduced(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Issued for every compilation cache generated. Is only available
        if Page.setGenerateCompilationCache is enabled.
        """
        if once:
            self.client.once("Page.compilationCacheProduced", fn)
        else:
            self.client.on("Page.compilationCacheProduced", fn)

    def __repr__(self):
        return f"Page()"
