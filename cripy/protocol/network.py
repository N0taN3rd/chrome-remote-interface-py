"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Network"]


class Network:
    """
    Network domain allows tracking network activities of the page. It exposes information about http,
    file, data and other requests and responses, their headers, bodies, timing, etc.
     
    Domain Dependencies: 
      * Debugger
      * Runtime
      * Security
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Network`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Network

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def canClearBrowserCache(self) -> Awaitable[Dict]:
        """
        Tells whether clearing browser cache is supported.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-canClearBrowserCache`

        :return: The results of the command
        """
        return self.client.send("Network.canClearBrowserCache", {})

    def canClearBrowserCookies(self) -> Awaitable[Dict]:
        """
        Tells whether clearing browser cookies is supported.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-canClearBrowserCookies`

        :return: The results of the command
        """
        return self.client.send("Network.canClearBrowserCookies", {})

    def canEmulateNetworkConditions(self) -> Awaitable[Dict]:
        """
        Tells whether emulation of network conditions is supported.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-canEmulateNetworkConditions`

        :return: The results of the command
        """
        return self.client.send("Network.canEmulateNetworkConditions", {})

    def clearBrowserCache(self) -> Awaitable[Dict]:
        """
        Clears browser cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-clearBrowserCache`

        :return: The results of the command
        """
        return self.client.send("Network.clearBrowserCache", {})

    def clearBrowserCookies(self) -> Awaitable[Dict]:
        """
        Clears browser cookies.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-clearBrowserCookies`

        :return: The results of the command
        """
        return self.client.send("Network.clearBrowserCookies", {})

    def continueInterceptedRequest(
        self,
        interceptionId: str,
        errorReason: Optional[str] = None,
        rawResponse: Optional[str] = None,
        url: Optional[str] = None,
        method: Optional[str] = None,
        postData: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
        authChallengeResponse: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Response to Network.requestIntercepted which either modifies the request to continue with any
        modifications, or blocks it, or completes it with the provided response bytes. If a network
        fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
        event will be sent with the same InterceptionId.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-continueInterceptedRequest`

        :param interceptionId: The interceptionId
        :param errorReason: If set this causes the request to fail with the given reason. Passing `Aborted` for requests
         marked with `isNavigationRequest` also cancels the navigation. Must not be set in response
         to an authChallenge.
        :param rawResponse: If set the requests completes using with the provided base64 encoded raw response, including
         HTTP status line and headers etc... Must not be set in response to an authChallenge.
        :param url: If set the request url will be modified in a way that's not observable by page. Must not be
         set in response to an authChallenge.
        :param method: If set this allows the request method to be overridden. Must not be set in response to an
         authChallenge.
        :param postData: If set this allows postData to be set. Must not be set in response to an authChallenge.
        :param headers: If set this allows the request headers to be changed. Must not be set in response to an
         authChallenge.
        :param authChallengeResponse: Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
        :return: The results of the command
        """
        msg = {"interceptionId": interceptionId}
        if errorReason is not None:
            msg["errorReason"] = errorReason
        if rawResponse is not None:
            msg["rawResponse"] = rawResponse
        if url is not None:
            msg["url"] = url
        if method is not None:
            msg["method"] = method
        if postData is not None:
            msg["postData"] = postData
        if headers is not None:
            msg["headers"] = headers
        if authChallengeResponse is not None:
            msg["authChallengeResponse"] = authChallengeResponse
        return self.client.send("Network.continueInterceptedRequest", msg)

    def deleteCookies(
        self,
        name: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Deletes browser cookies with matching name and url or domain/path pair.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-deleteCookies`

        :param name: Name of the cookies to remove.
        :param url: If specified, deletes all the cookies with the given name where domain and path match
         provided URL.
        :param domain: If specified, deletes only cookies with the exact domain.
        :param path: If specified, deletes only cookies with the exact path.
        :return: The results of the command
        """
        msg = {"name": name}
        if url is not None:
            msg["url"] = url
        if domain is not None:
            msg["domain"] = domain
        if path is not None:
            msg["path"] = path
        return self.client.send("Network.deleteCookies", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables network tracking, prevents network events from being sent to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-disable`

        :return: The results of the command
        """
        return self.client.send("Network.disable", {})

    def emulateNetworkConditions(
        self,
        offline: bool,
        latency: Union[int, float],
        downloadThroughput: Union[int, float],
        uploadThroughput: Union[int, float],
        connectionType: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Activates emulation of network conditions.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-emulateNetworkConditions`

        :param offline: True to emulate internet disconnection.
        :param latency: Minimum latency from request sent to response headers received (ms).
        :param downloadThroughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
        :param uploadThroughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
        :param connectionType: Connection type if known.
        :return: The results of the command
        """
        msg = {
            "offline": offline,
            "latency": latency,
            "downloadThroughput": downloadThroughput,
            "uploadThroughput": uploadThroughput,
        }
        if connectionType is not None:
            msg["connectionType"] = connectionType
        return self.client.send("Network.emulateNetworkConditions", msg)

    def enable(
        self,
        maxTotalBufferSize: Optional[int] = None,
        maxResourceBufferSize: Optional[int] = None,
        maxPostDataSize: Optional[int] = None,
    ) -> Awaitable[Dict]:
        """
        Enables network tracking, network events will now be delivered to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-enable`

        :param maxTotalBufferSize: Buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :param maxResourceBufferSize: Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
        :param maxPostDataSize: Longest post body size (in bytes) that would be included in requestWillBeSent notification
        :return: The results of the command
        """
        msg = {}
        if maxTotalBufferSize is not None:
            msg["maxTotalBufferSize"] = maxTotalBufferSize
        if maxResourceBufferSize is not None:
            msg["maxResourceBufferSize"] = maxResourceBufferSize
        if maxPostDataSize is not None:
            msg["maxPostDataSize"] = maxPostDataSize
        return self.client.send("Network.enable", msg)

    def getAllCookies(self) -> Awaitable[Dict]:
        """
        Returns all browser cookies. Depending on the backend support, will return detailed cookie
        information in the `cookies` field.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getAllCookies`

        :return: The results of the command
        """
        return self.client.send("Network.getAllCookies", {})

    def getCertificate(self, origin: str) -> Awaitable[Dict]:
        """
        Returns the DER-encoded certificate.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getCertificate`

        :param origin: Origin to get certificate for.
        :return: The results of the command
        """
        return self.client.send("Network.getCertificate", {"origin": origin})

    def getCookies(self, urls: Optional[List[str]] = None) -> Awaitable[Dict]:
        """
        Returns all browser cookies for the current URL. Depending on the backend support, will return
        detailed cookie information in the `cookies` field.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getCookies`

        :param urls: The list of URLs for which applicable cookies will be fetched
        :return: The results of the command
        """
        msg = {}
        if urls is not None:
            msg["urls"] = urls
        return self.client.send("Network.getCookies", msg)

    def getResponseBody(self, requestId: str) -> Awaitable[Dict]:
        """
        Returns content served for the given request.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getResponseBody`

        :param requestId: Identifier of the network request to get content for.
        :return: The results of the command
        """
        return self.client.send("Network.getResponseBody", {"requestId": requestId})

    def getRequestPostData(self, requestId: str) -> Awaitable[Dict]:
        """
        Returns post data sent with the request. Returns an error when no data was sent with the request.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getRequestPostData`

        :param requestId: Identifier of the network request to get content for.
        :return: The results of the command
        """
        return self.client.send("Network.getRequestPostData", {"requestId": requestId})

    def getResponseBodyForInterception(self, interceptionId: str) -> Awaitable[Dict]:
        """
        Returns content served for the given currently intercepted request.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-getResponseBodyForInterception`

        :param interceptionId: Identifier for the intercepted request to get body for.
        :return: The results of the command
        """
        return self.client.send(
            "Network.getResponseBodyForInterception", {"interceptionId": interceptionId}
        )

    def takeResponseBodyForInterceptionAsStream(
        self, interceptionId: str
    ) -> Awaitable[Dict]:
        """
        Returns a handle to the stream representing the response body. Note that after this command,
        the intercepted request can't be continued as is -- you either need to cancel it or to provide
        the response body. The stream only supports sequential read, IO.read will fail if the position
        is specified.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-takeResponseBodyForInterceptionAsStream`

        :param interceptionId: The interceptionId
        :return: The results of the command
        """
        return self.client.send(
            "Network.takeResponseBodyForInterceptionAsStream",
            {"interceptionId": interceptionId},
        )

    def replayXHR(self, requestId: str) -> Awaitable[Dict]:
        """
        This method sends a new XMLHttpRequest which is identical to the original one. The following
        parameters should be identical: method, url, async, request body, extra headers, withCredentials
        attribute, user, password.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-replayXHR`

        :param requestId: Identifier of XHR to replay.
        :return: The results of the command
        """
        return self.client.send("Network.replayXHR", {"requestId": requestId})

    def searchInResponseBody(
        self,
        requestId: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Searches for given string in response content.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-searchInResponseBody`

        :param requestId: Identifier of the network response to search.
        :param query: String to search for.
        :param caseSensitive: If true, search is case sensitive.
        :param isRegex: If true, treats string parameter as regex.
        :return: The results of the command
        """
        msg = {"requestId": requestId, "query": query}
        if caseSensitive is not None:
            msg["caseSensitive"] = caseSensitive
        if isRegex is not None:
            msg["isRegex"] = isRegex
        return self.client.send("Network.searchInResponseBody", msg)

    def setBlockedURLs(self, urls: List[str]) -> Awaitable[Dict]:
        """
        Blocks URLs from loading.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setBlockedURLs`

        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        :return: The results of the command
        """
        return self.client.send("Network.setBlockedURLs", {"urls": urls})

    def setBypassServiceWorker(self, bypass: bool) -> Awaitable[Dict]:
        """
        Toggles ignoring of service worker for each request.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setBypassServiceWorker`

        :param bypass: Bypass service worker and load from network.
        :return: The results of the command
        """
        return self.client.send("Network.setBypassServiceWorker", {"bypass": bypass})

    def setCacheDisabled(self, cacheDisabled: bool) -> Awaitable[Dict]:
        """
        Toggles ignoring cache for each request. If `true`, cache will not be used.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setCacheDisabled`

        :param cacheDisabled: Cache disabled state.
        :return: The results of the command
        """
        return self.client.send(
            "Network.setCacheDisabled", {"cacheDisabled": cacheDisabled}
        )

    def setCookie(
        self,
        name: str,
        value: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
        secure: Optional[bool] = None,
        httpOnly: Optional[bool] = None,
        sameSite: Optional[str] = None,
        expires: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setCookie`

        :param name: Cookie name.
        :param value: Cookie value.
        :param url: The request-URI to associate with the setting of the cookie. This value can affect the
         default domain and path values of the created cookie.
        :param domain: Cookie domain.
        :param path: Cookie path.
        :param secure: True if cookie is secure.
        :param httpOnly: True if cookie is http-only.
        :param sameSite: Cookie SameSite type.
        :param expires: Cookie expiration date, session cookie if not set
        :return: The results of the command
        """
        msg = {"name": name, "value": value}
        if url is not None:
            msg["url"] = url
        if domain is not None:
            msg["domain"] = domain
        if path is not None:
            msg["path"] = path
        if secure is not None:
            msg["secure"] = secure
        if httpOnly is not None:
            msg["httpOnly"] = httpOnly
        if sameSite is not None:
            msg["sameSite"] = sameSite
        if expires is not None:
            msg["expires"] = expires
        return self.client.send("Network.setCookie", msg)

    def setCookies(self, cookies: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        Sets given cookies.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setCookies`

        :param cookies: Cookies to be set.
        :return: The results of the command
        """
        return self.client.send("Network.setCookies", {"cookies": cookies})

    def setDataSizeLimitsForTest(
        self, maxTotalSize: int, maxResourceSize: int
    ) -> Awaitable[Dict]:
        """
        For testing.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setDataSizeLimitsForTest`

        :param maxTotalSize: Maximum total buffer size.
        :param maxResourceSize: Maximum per-resource size.
        :return: The results of the command
        """
        return self.client.send(
            "Network.setDataSizeLimitsForTest",
            {"maxTotalSize": maxTotalSize, "maxResourceSize": maxResourceSize},
        )

    def setExtraHTTPHeaders(self, headers: Dict[str, Any]) -> Awaitable[Dict]:
        """
        Specifies whether to always send extra HTTP headers with the requests from this page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setExtraHTTPHeaders`

        :param headers: Map with extra HTTP headers.
        :return: The results of the command
        """
        return self.client.send("Network.setExtraHTTPHeaders", {"headers": headers})

    def setRequestInterception(self, patterns: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        Sets the requests to intercept that match the provided patterns and optionally resource types.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setRequestInterception`

        :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding
         continueInterceptedRequest call.
        :return: The results of the command
        """
        return self.client.send(
            "Network.setRequestInterception", {"patterns": patterns}
        )

    def setUserAgentOverride(
        self,
        userAgent: str,
        acceptLanguage: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Allows overriding user agent with the given string.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#method-setUserAgentOverride`

        :param userAgent: User agent to use.
        :param acceptLanguage: Browser langugage to emulate.
        :param platform: The platform navigator.platform should return.
        :return: The results of the command
        """
        msg = {"userAgent": userAgent}
        if acceptLanguage is not None:
            msg["acceptLanguage"] = acceptLanguage
        if platform is not None:
            msg["platform"] = platform
        return self.client.send("Network.setUserAgentOverride", msg)

    def dataReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when data chunk was received over the network.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-dataReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.dataReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def eventSourceMessageReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when EventSource message is received.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-eventSourceMessageReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.eventSourceMessageReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def loadingFailed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when HTTP request has failed to load.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-loadingFailed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.loadingFailed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def loadingFinished(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when HTTP request has finished loading.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-loadingFinished`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.loadingFinished"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def requestIntercepted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Details of an intercepted HTTP request, which must be either allowed, blocked, modified or
        mocked.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-requestIntercepted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.requestIntercepted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def requestServedFromCache(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired if request ended up loading from cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-requestServedFromCache`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.requestServedFromCache"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def requestWillBeSent(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when page is about to send HTTP request.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-requestWillBeSent`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.requestWillBeSent"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def resourceChangedPriority(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when resource loading priority is changed

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-resourceChangedPriority`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.resourceChangedPriority"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def signedExchangeReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when a signed exchange was received over the network

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-signedExchangeReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.signedExchangeReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def responseReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when HTTP response is available.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-responseReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.responseReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketClosed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket is closed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketClosed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketClosed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketCreated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired upon WebSocket creation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketCreated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketCreated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketFrameError(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket message error occurs.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketFrameError`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketFrameError"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketFrameReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket message is received.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketFrameReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketFrameReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketFrameSent(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket message is sent.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketFrameSent`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketFrameSent"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketHandshakeResponseReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket handshake response becomes available.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketHandshakeResponseReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketHandshakeResponseReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def webSocketWillSendHandshakeRequest(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Fired when WebSocket is about to initiate handshake.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Network#event-webSocketWillSendHandshakeRequest`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Network.webSocketWillSendHandshakeRequest"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
