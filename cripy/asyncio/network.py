from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Network"]


@attr.dataclass(slots=True)
class Network(object):
    """
    Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.
    """

    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["Debugger", "Runtime", "Security"]

    async def canClearBrowserCache(self) -> Optional[dict]:
        """
        Tells whether clearing browser cache is supported.
        """
        res = await self.client.send("Network.canClearBrowserCache")
        return res

    async def canClearBrowserCookies(self) -> Optional[dict]:
        """
        Tells whether clearing browser cookies is supported.
        """
        res = await self.client.send("Network.canClearBrowserCookies")
        return res

    async def canEmulateNetworkConditions(self) -> Optional[dict]:
        """
        Tells whether emulation of network conditions is supported.
        """
        res = await self.client.send("Network.canEmulateNetworkConditions")
        return res

    async def clearBrowserCache(self) -> Optional[dict]:
        """
        Clears browser cache.
        """
        res = await self.client.send("Network.clearBrowserCache")
        return res

    async def clearBrowserCookies(self) -> Optional[dict]:
        """
        Clears browser cookies.
        """
        res = await self.client.send("Network.clearBrowserCookies")
        return res

    async def continueInterceptedRequest(
        self,
        interceptionId: str,
        errorReason: Optional[str] = None,
        rawResponse: Optional[str] = None,
        url: Optional[str] = None,
        method: Optional[str] = None,
        postData: Optional[str] = None,
        headers: Optional[dict] = None,
        authChallengeResponse: Optional[dict] = None,
    ) -> Optional[dict]:
        """
        Response to Network.requestIntercepted which either modifies the request to continue with any
modifications, or blocks it, or completes it with the provided response bytes. If a network
fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
event will be sent with the same InterceptionId.

        :param interceptionId: The interceptionId
        :type interceptionId: str
        :param errorReason: If set this causes the request to fail with the given reason. Passing `Aborted` for requests marked with `isNavigationRequest` also cancels the navigation. Must not be set in response to an authChallenge.
        :type errorReason: Optional[str]
        :param rawResponse: If set the requests completes using with the provided base64 encoded raw response, including HTTP status line and headers etc... Must not be set in response to an authChallenge.
        :type rawResponse: Optional[str]
        :param url: If set the request url will be modified in a way that's not observable by page. Must not be set in response to an authChallenge.
        :type url: Optional[str]
        :param method: If set this allows the request method to be overridden. Must not be set in response to an authChallenge.
        :type method: Optional[str]
        :param postData: If set this allows postData to be set. Must not be set in response to an authChallenge.
        :type postData: Optional[str]
        :param headers: If set this allows the request headers to be changed. Must not be set in response to an authChallenge.
        :type headers: Optional[dict]
        :param authChallengeResponse: Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
        :type authChallengeResponse: Optional[dict]
        """
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict["interceptionId"] = interceptionId
        if errorReason is not None:
            msg_dict["errorReason"] = errorReason
        if rawResponse is not None:
            msg_dict["rawResponse"] = rawResponse
        if url is not None:
            msg_dict["url"] = url
        if method is not None:
            msg_dict["method"] = method
        if postData is not None:
            msg_dict["postData"] = postData
        if headers is not None:
            msg_dict["headers"] = headers
        if authChallengeResponse is not None:
            msg_dict["authChallengeResponse"] = authChallengeResponse
        res = await self.client.send("Network.continueInterceptedRequest", msg_dict)
        return res

    async def deleteCookies(
        self,
        name: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Deletes browser cookies with matching name and url or domain/path pair.

        :param name: Name of the cookies to remove.
        :type name: str
        :param url: If specified, deletes all the cookies with the given name where domain and path match provided URL.
        :type url: Optional[str]
        :param domain: If specified, deletes only cookies with the exact domain.
        :type domain: Optional[str]
        :param path: If specified, deletes only cookies with the exact path.
        :type path: Optional[str]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        if url is not None:
            msg_dict["url"] = url
        if domain is not None:
            msg_dict["domain"] = domain
        if path is not None:
            msg_dict["path"] = path
        res = await self.client.send("Network.deleteCookies", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables network tracking, prevents network events from being sent to the client.
        """
        res = await self.client.send("Network.disable")
        return res

    async def emulateNetworkConditions(
        self,
        offline: bool,
        latency: float,
        downloadThroughput: float,
        uploadThroughput: float,
        connectionType: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Activates emulation of network conditions.

        :param offline: True to emulate internet disconnection.
        :type offline: bool
        :param latency: Minimum latency from request sent to response headers received (ms).
        :type latency: float
        :param downloadThroughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        :type downloadThroughput: float
        :param uploadThroughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        :type uploadThroughput: float
        :param connectionType: Connection type if known.
        :type connectionType: Optional[str]
        """
        msg_dict = dict()
        if offline is not None:
            msg_dict["offline"] = offline
        if latency is not None:
            msg_dict["latency"] = latency
        if downloadThroughput is not None:
            msg_dict["downloadThroughput"] = downloadThroughput
        if uploadThroughput is not None:
            msg_dict["uploadThroughput"] = uploadThroughput
        if connectionType is not None:
            msg_dict["connectionType"] = connectionType
        res = await self.client.send("Network.emulateNetworkConditions", msg_dict)
        return res

    async def enable(
        self,
        maxTotalBufferSize: Optional[int] = None,
        maxResourceBufferSize: Optional[int] = None,
        maxPostDataSize: Optional[int] = None,
    ) -> Optional[dict]:
        """
        Enables network tracking, network events will now be delivered to the client.

        :param maxTotalBufferSize: Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :type maxTotalBufferSize: Optional[int]
        :param maxResourceBufferSize: Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :type maxResourceBufferSize: Optional[int]
        :param maxPostDataSize: Longest post body size (in bytes) that would be included in requestWillBeSent notification
        :type maxPostDataSize: Optional[int]
        """
        msg_dict = dict()
        if maxTotalBufferSize is not None:
            msg_dict["maxTotalBufferSize"] = maxTotalBufferSize
        if maxResourceBufferSize is not None:
            msg_dict["maxResourceBufferSize"] = maxResourceBufferSize
        if maxPostDataSize is not None:
            msg_dict["maxPostDataSize"] = maxPostDataSize
        res = await self.client.send("Network.enable", msg_dict)
        return res

    async def getAllCookies(self) -> Optional[dict]:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
        """
        res = await self.client.send("Network.getAllCookies")
        return res

    async def getCertificate(self, origin: str) -> Optional[dict]:
        """
        Returns the DER-encoded certificate.

        :param origin: Origin to get certificate for.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        res = await self.client.send("Network.getCertificate", msg_dict)
        return res

    async def getCookies(self, urls: Optional[List[str]] = None) -> Optional[dict]:
        """
        Returns all browser cookies for the current URL. Depending on the backend support, will return
detailed cookie information in the `cookies` field.

        :param urls: The list of URLs for which applicable cookies will be fetched
        :type urls: Optional[List[str]]
        """
        msg_dict = dict()
        if urls is not None:
            msg_dict["urls"] = urls
        res = await self.client.send("Network.getCookies", msg_dict)
        return res

    async def getResponseBody(self, requestId: str) -> Optional[dict]:
        """
        Returns content served for the given request.

        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        res = await self.client.send("Network.getResponseBody", msg_dict)
        return res

    async def getRequestPostData(self, requestId: str) -> Optional[dict]:
        """
        Returns post data sent with the request. Returns an error when no data was sent with the request.

        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        res = await self.client.send("Network.getRequestPostData", msg_dict)
        return res

    async def getResponseBodyForInterception(
        self, interceptionId: str
    ) -> Optional[dict]:
        """
        Returns content served for the given currently intercepted request.

        :param interceptionId: Identifier for the intercepted request to get body for.
        :type interceptionId: str
        """
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict["interceptionId"] = interceptionId
        res = await self.client.send("Network.getResponseBodyForInterception", msg_dict)
        return res

    async def takeResponseBodyForInterceptionAsStream(
        self, interceptionId: str
    ) -> Optional[dict]:
        """
        Returns a handle to the stream representing the response body. Note that after this command,
the intercepted request can't be continued as is -- you either need to cancel it or to provide
the response body. The stream only supports sequential read, IO.read will fail if the position
is specified.

        :param interceptionId: The interceptionId
        :type interceptionId: str
        """
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict["interceptionId"] = interceptionId
        res = await self.client.send(
            "Network.takeResponseBodyForInterceptionAsStream", msg_dict
        )
        return res

    async def replayXHR(self, requestId: str) -> Optional[dict]:
        """
        This method sends a new XMLHttpRequest which is identical to the original one. The following
parameters should be identical: method, url, async, request body, extra headers, withCredentials
attribute, user, password.

        :param requestId: Identifier of XHR to replay.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        res = await self.client.send("Network.replayXHR", msg_dict)
        return res

    async def searchInResponseBody(
        self,
        requestId: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Searches for given string in response content.

        :param requestId: Identifier of the network response to search.
        :type requestId: str
        :param query: String to search for.
        :type query: str
        :param caseSensitive: If true, search is case sensitive.
        :type caseSensitive: Optional[bool]
        :param isRegex: If true, treats string parameter as regex.
        :type isRegex: Optional[bool]
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if query is not None:
            msg_dict["query"] = query
        if caseSensitive is not None:
            msg_dict["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg_dict["isRegex"] = isRegex
        res = await self.client.send("Network.searchInResponseBody", msg_dict)
        return res

    async def setBlockedURLs(self, urls: List[str]) -> Optional[dict]:
        """
        Blocks URLs from loading.

        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        :type urls: List[str]
        """
        msg_dict = dict()
        if urls is not None:
            msg_dict["urls"] = urls
        res = await self.client.send("Network.setBlockedURLs", msg_dict)
        return res

    async def setBypassServiceWorker(self, bypass: bool) -> Optional[dict]:
        """
        Toggles ignoring of service worker for each request.

        :param bypass: Bypass service worker and load from network.
        :type bypass: bool
        """
        msg_dict = dict()
        if bypass is not None:
            msg_dict["bypass"] = bypass
        res = await self.client.send("Network.setBypassServiceWorker", msg_dict)
        return res

    async def setCacheDisabled(self, cacheDisabled: bool) -> Optional[dict]:
        """
        Toggles ignoring cache for each request. If `true`, cache will not be used.

        :param cacheDisabled: Cache disabled state.
        :type cacheDisabled: bool
        """
        msg_dict = dict()
        if cacheDisabled is not None:
            msg_dict["cacheDisabled"] = cacheDisabled
        res = await self.client.send("Network.setCacheDisabled", msg_dict)
        return res

    async def setCookie(
        self,
        name: str,
        value: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
        secure: Optional[bool] = None,
        httpOnly: Optional[bool] = None,
        sameSite: Optional[str] = None,
        expires: Optional[float] = None,
    ) -> Optional[dict]:
        """
        Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

        :param name: Cookie name.
        :type name: str
        :param value: Cookie value.
        :type value: str
        :param url: The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
        :type url: Optional[str]
        :param domain: Cookie domain.
        :type domain: Optional[str]
        :param path: Cookie path.
        :type path: Optional[str]
        :param secure: True if cookie is secure.
        :type secure: Optional[bool]
        :param httpOnly: True if cookie is http-only.
        :type httpOnly: Optional[bool]
        :param sameSite: Cookie SameSite type.
        :type sameSite: Optional[str]
        :param expires: Cookie expiration date, session cookie if not set
        :type expires: Optional[float]
        """
        msg_dict = dict()
        if name is not None:
            msg_dict["name"] = name
        if value is not None:
            msg_dict["value"] = value
        if url is not None:
            msg_dict["url"] = url
        if domain is not None:
            msg_dict["domain"] = domain
        if path is not None:
            msg_dict["path"] = path
        if secure is not None:
            msg_dict["secure"] = secure
        if httpOnly is not None:
            msg_dict["httpOnly"] = httpOnly
        if sameSite is not None:
            msg_dict["sameSite"] = sameSite
        if expires is not None:
            msg_dict["expires"] = expires
        res = await self.client.send("Network.setCookie", msg_dict)
        return res

    async def setCookies(self, cookies: List[dict]) -> Optional[dict]:
        """
        Sets given cookies.

        :param cookies: Cookies to be set.
        :type cookies: List[dict]
        """
        msg_dict = dict()
        if cookies is not None:
            msg_dict["cookies"] = cookies
        res = await self.client.send("Network.setCookies", msg_dict)
        return res

    async def setDataSizeLimitsForTest(
        self, maxTotalSize: int, maxResourceSize: int
    ) -> Optional[dict]:
        """
        For testing.

        :param maxTotalSize: Maximum total buffer size.
        :type maxTotalSize: int
        :param maxResourceSize: Maximum per-resource size.
        :type maxResourceSize: int
        """
        msg_dict = dict()
        if maxTotalSize is not None:
            msg_dict["maxTotalSize"] = maxTotalSize
        if maxResourceSize is not None:
            msg_dict["maxResourceSize"] = maxResourceSize
        res = await self.client.send("Network.setDataSizeLimitsForTest", msg_dict)
        return res

    async def setExtraHTTPHeaders(self, headers: dict) -> Optional[dict]:
        """
        Specifies whether to always send extra HTTP headers with the requests from this page.

        :param headers: Map with extra HTTP headers.
        :type headers: dict
        """
        msg_dict = dict()
        if headers is not None:
            msg_dict["headers"] = headers
        res = await self.client.send("Network.setExtraHTTPHeaders", msg_dict)
        return res

    async def setRequestInterception(self, patterns: List[dict]) -> Optional[dict]:
        """
        Sets the requests to intercept that match a the provided patterns and optionally resource types.

        :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call.
        :type patterns: List[dict]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict["patterns"] = patterns
        res = await self.client.send("Network.setRequestInterception", msg_dict)
        return res

    async def setUserAgentOverride(
        self,
        userAgent: str,
        acceptLanguage: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Allows overriding user agent with the given string.

        :param userAgent: User agent to use.
        :type userAgent: str
        :param acceptLanguage: Browser langugage to emulate.
        :type acceptLanguage: Optional[str]
        :param platform: The platform navigator.platform should return.
        :type platform: Optional[str]
        """
        msg_dict = dict()
        if userAgent is not None:
            msg_dict["userAgent"] = userAgent
        if acceptLanguage is not None:
            msg_dict["acceptLanguage"] = acceptLanguage
        if platform is not None:
            msg_dict["platform"] = platform
        res = await self.client.send("Network.setUserAgentOverride", msg_dict)
        return res

    def dataReceived(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when data chunk was received over the network.
        """
        if once:
            self.client.once("Network.dataReceived", fn)
        else:
            self.client.on("Network.dataReceived", fn)

    def eventSourceMessageReceived(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when EventSource message is received.
        """
        if once:
            self.client.once("Network.eventSourceMessageReceived", fn)
        else:
            self.client.on("Network.eventSourceMessageReceived", fn)

    def loadingFailed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when HTTP request has failed to load.
        """
        if once:
            self.client.once("Network.loadingFailed", fn)
        else:
            self.client.on("Network.loadingFailed", fn)

    def loadingFinished(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when HTTP request has finished loading.
        """
        if once:
            self.client.once("Network.loadingFinished", fn)
        else:
            self.client.on("Network.loadingFinished", fn)

    def requestIntercepted(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
        mocked.
        """
        if once:
            self.client.once("Network.requestIntercepted", fn)
        else:
            self.client.on("Network.requestIntercepted", fn)

    def requestServedFromCache(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired if request ended up loading from cache.
        """
        if once:
            self.client.once("Network.requestServedFromCache", fn)
        else:
            self.client.on("Network.requestServedFromCache", fn)

    def requestWillBeSent(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when page is about to send HTTP request.
        """
        if once:
            self.client.once("Network.requestWillBeSent", fn)
        else:
            self.client.on("Network.requestWillBeSent", fn)

    def resourceChangedPriority(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when resource loading priority is changed
        """
        if once:
            self.client.once("Network.resourceChangedPriority", fn)
        else:
            self.client.on("Network.resourceChangedPriority", fn)

    def signedExchangeReceived(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when a signed exchange was received over the network
        """
        if once:
            self.client.once("Network.signedExchangeReceived", fn)
        else:
            self.client.on("Network.signedExchangeReceived", fn)

    def responseReceived(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when HTTP response is available.
        """
        if once:
            self.client.once("Network.responseReceived", fn)
        else:
            self.client.on("Network.responseReceived", fn)

    def webSocketClosed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when WebSocket is closed.
        """
        if once:
            self.client.once("Network.webSocketClosed", fn)
        else:
            self.client.on("Network.webSocketClosed", fn)

    def webSocketCreated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired upon WebSocket creation.
        """
        if once:
            self.client.once("Network.webSocketCreated", fn)
        else:
            self.client.on("Network.webSocketCreated", fn)

    def webSocketFrameError(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when WebSocket frame error occurs.
        """
        if once:
            self.client.once("Network.webSocketFrameError", fn)
        else:
            self.client.on("Network.webSocketFrameError", fn)

    def webSocketFrameReceived(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when WebSocket frame is received.
        """
        if once:
            self.client.once("Network.webSocketFrameReceived", fn)
        else:
            self.client.on("Network.webSocketFrameReceived", fn)

    def webSocketFrameSent(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Fired when WebSocket frame is sent.
        """
        if once:
            self.client.once("Network.webSocketFrameSent", fn)
        else:
            self.client.on("Network.webSocketFrameSent", fn)

    def webSocketHandshakeResponseReceived(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when WebSocket handshake response becomes available.
        """
        if once:
            self.client.once("Network.webSocketHandshakeResponseReceived", fn)
        else:
            self.client.on("Network.webSocketHandshakeResponseReceived", fn)

    def webSocketWillSendHandshakeRequest(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Fired when WebSocket is about to initiate handshake.
        """
        if once:
            self.client.once("Network.webSocketWillSendHandshakeRequest", fn)
        else:
            self.client.on("Network.webSocketWillSendHandshakeRequest", fn)
