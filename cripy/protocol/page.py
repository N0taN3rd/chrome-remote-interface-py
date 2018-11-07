# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import (
    Awaitable,
    Any,
    Callable,
    ClassVar,
    List,
    Optional,
    Union,
    TYPE_CHECKING,
)

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Page"]


@attr.dataclass(slots=True)
class Page(object):
    """
    Actions and events related to the inspected page belong to the page domain.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["Debugger", "DOM", "Network", "Runtime"]

    def addScriptToEvaluateOnLoad(self, scriptSource: str) -> Awaitable[Optional[dict]]:
        """
        Deprecated, please use addScriptToEvaluateOnNewDocument instead.

        :param scriptSource: The scriptSource
        :type scriptSource: str
        """
        msg_dict = dict()
        if scriptSource is not None:
            msg_dict["scriptSource"] = scriptSource
        return self.client.send("Page.addScriptToEvaluateOnLoad", msg_dict)

    def addScriptToEvaluateOnNewDocument(
        self, source: str, worldName: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Evaluates given script in every frame upon creation (before loading frame's scripts).

        :param source: The source
        :type source: str
        :param worldName: If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted.
        :type worldName: Optional[str]
        """
        msg_dict = dict()
        if source is not None:
            msg_dict["source"] = source
        if worldName is not None:
            msg_dict["worldName"] = worldName
        return self.client.send("Page.addScriptToEvaluateOnNewDocument", msg_dict)

    def bringToFront(self) -> Awaitable[Optional[dict]]:
        """
        Brings page to front (activates tab).
        """
        return self.client.send("Page.bringToFront")

    def captureScreenshot(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        clip: Optional[dict] = None,
        fromSurface: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.captureScreenshot", msg_dict)

    def clearDeviceMetricsOverride(self) -> Awaitable[Optional[dict]]:
        """
        Clears the overriden device metrics.
        """
        return self.client.send("Page.clearDeviceMetricsOverride")

    def clearDeviceOrientationOverride(self) -> Awaitable[Optional[dict]]:
        """
        Clears the overridden Device Orientation.
        """
        return self.client.send("Page.clearDeviceOrientationOverride")

    def clearGeolocationOverride(self) -> Awaitable[Optional[dict]]:
        """
        Clears the overriden Geolocation Position and Error.
        """
        return self.client.send("Page.clearGeolocationOverride")

    def createIsolatedWorld(
        self,
        frameId: str,
        worldName: Optional[str] = None,
        grantUniveralAccess: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.createIsolatedWorld", msg_dict)

    def deleteCookie(self, cookieName: str, url: str) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.deleteCookie", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables page domain notifications.
        """
        return self.client.send("Page.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables page domain notifications.
        """
        return self.client.send("Page.enable")

    def getAppManifest(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Page.getAppManifest")

    def getCookies(self) -> Awaitable[Optional[dict]]:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
        """
        return self.client.send("Page.getCookies")

    def getFrameTree(self) -> Awaitable[Optional[dict]]:
        """
        Returns present frame tree structure.
        """
        return self.client.send("Page.getFrameTree")

    def getLayoutMetrics(self) -> Awaitable[Optional[dict]]:
        """
        Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
        """
        return self.client.send("Page.getLayoutMetrics")

    def getNavigationHistory(self) -> Awaitable[Optional[dict]]:
        """
        Returns navigation history for the current page.
        """
        return self.client.send("Page.getNavigationHistory")

    def getResourceContent(self, frameId: str, url: str) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.getResourceContent", msg_dict)

    def getResourceTree(self) -> Awaitable[Optional[dict]]:
        """
        Returns present frame / resource tree structure.
        """
        return self.client.send("Page.getResourceTree")

    def handleJavaScriptDialog(
        self, accept: bool, promptText: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.handleJavaScriptDialog", msg_dict)

    def navigate(
        self,
        url: str,
        referrer: Optional[str] = None,
        transitionType: Optional[str] = None,
        frameId: Optional[str] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.navigate", msg_dict)

    def navigateToHistoryEntry(self, entryId: int) -> Awaitable[Optional[dict]]:
        """
        Navigates current page to the given history entry.

        :param entryId: Unique id of the entry to navigate to.
        :type entryId: int
        """
        msg_dict = dict()
        if entryId is not None:
            msg_dict["entryId"] = entryId
        return self.client.send("Page.navigateToHistoryEntry", msg_dict)

    def printToPDF(
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
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.printToPDF", msg_dict)

    def reload(
        self,
        ignoreCache: Optional[bool] = None,
        scriptToEvaluateOnLoad: Optional[str] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.reload", msg_dict)

    def removeScriptToEvaluateOnLoad(
        self, identifier: str
    ) -> Awaitable[Optional[dict]]:
        """
        Deprecated, please use removeScriptToEvaluateOnNewDocument instead.

        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        return self.client.send("Page.removeScriptToEvaluateOnLoad", msg_dict)

    def removeScriptToEvaluateOnNewDocument(
        self, identifier: str
    ) -> Awaitable[Optional[dict]]:
        """
        Removes given script from the list.

        :param identifier: The identifier
        :type identifier: str
        """
        msg_dict = dict()
        if identifier is not None:
            msg_dict["identifier"] = identifier
        return self.client.send("Page.removeScriptToEvaluateOnNewDocument", msg_dict)

    def requestAppBanner(self) -> Awaitable[Optional[dict]]:
        return self.client.send("Page.requestAppBanner")

    def screencastFrameAck(self, sessionId: int) -> Awaitable[Optional[dict]]:
        """
        Acknowledges that a screencast frame has been received by the frontend.

        :param sessionId: Frame number.
        :type sessionId: int
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict["sessionId"] = sessionId
        return self.client.send("Page.screencastFrameAck", msg_dict)

    def searchInResource(
        self,
        frameId: str,
        url: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.searchInResource", msg_dict)

    def setAdBlockingEnabled(self, enabled: bool) -> Awaitable[Optional[dict]]:
        """
        Enable Chrome's experimental ad filter on all sites.

        :param enabled: Whether to block ads.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        return self.client.send("Page.setAdBlockingEnabled", msg_dict)

    def setBypassCSP(self, enabled: bool) -> Awaitable[Optional[dict]]:
        """
        Enable page Content Security Policy by-passing.

        :param enabled: Whether to bypass page CSP.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        return self.client.send("Page.setBypassCSP", msg_dict)

    def setDeviceMetricsOverride(
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
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setDeviceMetricsOverride", msg_dict)

    def setDeviceOrientationOverride(
        self, alpha: float, beta: float, gamma: float
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setDeviceOrientationOverride", msg_dict)

    def setFontFamilies(self, fontFamilies: dict) -> Awaitable[Optional[dict]]:
        """
        Set generic font families.

        :param fontFamilies: Specifies font families to set. If a font family is not specified, it won't be changed.
        :type fontFamilies: dict
        """
        msg_dict = dict()
        if fontFamilies is not None:
            msg_dict["fontFamilies"] = fontFamilies
        return self.client.send("Page.setFontFamilies", msg_dict)

    def setFontSizes(self, fontSizes: dict) -> Awaitable[Optional[dict]]:
        """
        Set default font sizes.

        :param fontSizes: Specifies font sizes to set. If a font size is not specified, it won't be changed.
        :type fontSizes: dict
        """
        msg_dict = dict()
        if fontSizes is not None:
            msg_dict["fontSizes"] = fontSizes
        return self.client.send("Page.setFontSizes", msg_dict)

    def setDocumentContent(self, frameId: str, html: str) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setDocumentContent", msg_dict)

    def setDownloadBehavior(
        self, behavior: str, downloadPath: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setDownloadBehavior", msg_dict)

    def setGeolocationOverride(
        self,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        accuracy: Optional[float] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setGeolocationOverride", msg_dict)

    def setLifecycleEventsEnabled(self, enabled: bool) -> Awaitable[Optional[dict]]:
        """
        Controls whether page will emit lifecycle events.

        :param enabled: If true, starts emitting lifecycle events.
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        return self.client.send("Page.setLifecycleEventsEnabled", msg_dict)

    def setTouchEmulationEnabled(
        self, enabled: bool, configuration: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setTouchEmulationEnabled", msg_dict)

    def startScreencast(
        self,
        format: Optional[str] = None,
        quality: Optional[int] = None,
        maxWidth: Optional[int] = None,
        maxHeight: Optional[int] = None,
        everyNthFrame: Optional[int] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.startScreencast", msg_dict)

    def stopLoading(self) -> Awaitable[Optional[dict]]:
        """
        Force the page stop all navigations and pending resource fetches.
        """
        return self.client.send("Page.stopLoading")

    def crash(self) -> Awaitable[Optional[dict]]:
        """
        Crashes renderer on the IO thread, generates minidumps.
        """
        return self.client.send("Page.crash")

    def close(self) -> Awaitable[Optional[dict]]:
        """
        Tries to close page, running its beforeunload hooks, if any.
        """
        return self.client.send("Page.close")

    def setWebLifecycleState(self, state: str) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.setWebLifecycleState", msg_dict)

    def stopScreencast(self) -> Awaitable[Optional[dict]]:
        """
        Stops sending each frame in the `screencastFrame`.
        """
        return self.client.send("Page.stopScreencast")

    def setProduceCompilationCache(self, enabled: bool) -> Awaitable[Optional[dict]]:
        """
        Forces compilation cache to be generated for every subresource script.

        :param enabled: The enabled
        :type enabled: bool
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict["enabled"] = enabled
        return self.client.send("Page.setProduceCompilationCache", msg_dict)

    def addCompilationCache(self, url: str, data: str) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Page.addCompilationCache", msg_dict)

    def clearCompilationCache(self) -> Awaitable[Optional[dict]]:
        """
        Clears seeded compilation cache.
        """
        return self.client.send("Page.clearCompilationCache")

    def generateTestReport(
        self, message: str, group: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Generates a report for testing.

        :param message: Message to be displayed in the report.
        :type message: str
        :param group: Specifies the endpoint group to deliver the report to.
        :type group: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict["message"] = message
        if group is not None:
            msg_dict["group"] = group
        return self.client.send("Page.generateTestReport", msg_dict)

    def domContentEventFired(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.domContentEventFired", _cb)

            return future

        self.client.on("Page.domContentEventFired", cb)

    def frameAttached(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when frame has been attached to its parent.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameAttached", _cb)

            return future

        self.client.on("Page.frameAttached", cb)

    def frameClearedScheduledNavigation(
        self, cb: Optional[Callable[..., Any]] = None
    ) -> Any:
        """
        Fired when frame no longer has a scheduled navigation.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameClearedScheduledNavigation", _cb)

            return future

        self.client.on("Page.frameClearedScheduledNavigation", cb)

    def frameDetached(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when frame has been detached from its parent.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameDetached", _cb)

            return future

        self.client.on("Page.frameDetached", cb)

    def frameNavigated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired once navigation of the frame has completed. Frame is now associated with the new loader.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameNavigated", _cb)

            return future

        self.client.on("Page.frameNavigated", cb)

    def frameResized(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameResized", _cb)

            return future

        self.client.on("Page.frameResized", cb)

    def frameScheduledNavigation(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when frame schedules a potential navigation.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameScheduledNavigation", _cb)

            return future

        self.client.on("Page.frameScheduledNavigation", cb)

    def frameStartedLoading(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when frame has started loading.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameStartedLoading", _cb)

            return future

        self.client.on("Page.frameStartedLoading", cb)

    def frameStoppedLoading(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when frame has stopped loading.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.frameStoppedLoading", _cb)

            return future

        self.client.on("Page.frameStoppedLoading", cb)

    def interstitialHidden(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when interstitial page was hidden
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.interstitialHidden", _cb)

            return future

        self.client.on("Page.interstitialHidden", cb)

    def interstitialShown(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when interstitial page was shown
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.interstitialShown", _cb)

            return future

        self.client.on("Page.interstitialShown", cb)

    def javascriptDialogClosed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been
        closed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.javascriptDialogClosed", _cb)

            return future

        self.client.on("Page.javascriptDialogClosed", cb)

    def javascriptDialogOpening(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to
        open.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.javascriptDialogOpening", _cb)

            return future

        self.client.on("Page.javascriptDialogOpening", cb)

    def lifecycleEvent(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired for top level page lifecycle events such as navigation, load, paint, etc.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.lifecycleEvent", _cb)

            return future

        self.client.on("Page.lifecycleEvent", cb)

    def loadEventFired(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.loadEventFired", _cb)

            return future

        self.client.on("Page.loadEventFired", cb)

    def navigatedWithinDocument(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when same-document navigation happens, e.g. due to history API usage or anchor navigation.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.navigatedWithinDocument", _cb)

            return future

        self.client.on("Page.navigatedWithinDocument", cb)

    def screencastFrame(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Compressed image data requested by the `startScreencast`.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.screencastFrame", _cb)

            return future

        self.client.on("Page.screencastFrame", cb)

    def screencastVisibilityChanged(
        self, cb: Optional[Callable[..., Any]] = None
    ) -> Any:
        """
        Fired when the page with currently enabled screencast was shown or hidden `.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.screencastVisibilityChanged", _cb)

            return future

        self.client.on("Page.screencastVisibilityChanged", cb)

    def windowOpen(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when a new window is going to be opened, via window.open(), link click, form submission,
        etc.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.windowOpen", _cb)

            return future

        self.client.on("Page.windowOpen", cb)

    def compilationCacheProduced(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued for every compilation cache generated. Is only available
        if Page.setGenerateCompilationCache is enabled.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Page.compilationCacheProduced", _cb)

            return future

        self.client.on("Page.compilationCacheProduced", cb)
