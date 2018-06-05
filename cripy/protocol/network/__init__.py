from typing import Any, List, Optional, Union
from cripy.protocol.io import types as IO
from cripy.protocol.debugger import types as Debugger
from cripy.protocol.network import events as Events
from cripy.protocol.network import types as Types


class Network(object):
    """
    Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.
    """

    dependencies = ["Debugger", "Runtime", "Security"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def canClearBrowserCache(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.canClearBrowserCache")
        res = await mayberes
        return res

    async def canClearBrowserCookies(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.canClearBrowserCookies")
        res = await mayberes
        return res

    async def canEmulateNetworkConditions(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.canEmulateNetworkConditions")
        res = await mayberes
        return res

    async def clearBrowserCache(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.clearBrowserCache")
        return mayberes

    async def clearBrowserCookies(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.clearBrowserCookies")
        return mayberes

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
        mayberes = await self.chrome.send(
            "Network.continueInterceptedRequest", msg_dict
        )
        return mayberes

    async def deleteCookies(
        self,
        name: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.deleteCookies", msg_dict)
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.disable")
        return mayberes

    async def emulateNetworkConditions(
        self,
        offline: bool,
        latency: float,
        downloadThroughput: float,
        uploadThroughput: float,
        connectionType: Optional[str] = None,
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.emulateNetworkConditions", msg_dict)
        return mayberes

    async def enable(
        self,
        maxTotalBufferSize: Optional[int] = None,
        maxResourceBufferSize: Optional[int] = None,
        maxPostDataSize: Optional[int] = None,
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.enable", msg_dict)
        return mayberes

    async def getAllCookies(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Network.getAllCookies")
        res = await mayberes
        res["cookies"] = Types.Cookie.safe_create_from_list(res["cookies"])
        return res

    async def getCertificate(self, origin: str) -> Optional[dict]:
        """
        :param origin: Origin to get certificate for.
        :type origin: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        mayberes = await self.chrome.send("Network.getCertificate", msg_dict)
        res = await mayberes
        return res

    async def getCookies(self, urls: Optional[List[str]] = None) -> Optional[dict]:
        """
        :param urls: The list of URLs for which applicable cookies will be fetched
        :type urls: Optional[List[str]]
        """
        msg_dict = dict()
        if urls is not None:
            msg_dict["urls"] = urls
        mayberes = await self.chrome.send("Network.getCookies", msg_dict)
        res = await mayberes
        res["cookies"] = Types.Cookie.safe_create_from_list(res["cookies"])
        return res

    async def getResponseBody(self, requestId: str) -> Optional[dict]:
        """
        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        mayberes = await self.chrome.send("Network.getResponseBody", msg_dict)
        res = await mayberes
        return res

    async def getRequestPostData(self, requestId: str) -> Optional[dict]:
        """
        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        mayberes = await self.chrome.send("Network.getRequestPostData", msg_dict)
        res = await mayberes
        return res

    async def getResponseBodyForInterception(
        self, interceptionId: str
    ) -> Optional[dict]:
        """
        :param interceptionId: Identifier for the intercepted request to get body for.
        :type interceptionId: str
        """
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict["interceptionId"] = interceptionId
        mayberes = await self.chrome.send(
            "Network.getResponseBodyForInterception", msg_dict
        )
        res = await mayberes
        return res

    async def takeResponseBodyForInterceptionAsStream(
        self, interceptionId: str
    ) -> Optional[dict]:
        """
        :param interceptionId: The interceptionId
        :type interceptionId: str
        """
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict["interceptionId"] = interceptionId
        mayberes = await self.chrome.send(
            "Network.takeResponseBodyForInterceptionAsStream", msg_dict
        )
        res = await mayberes
        return res

    async def replayXHR(self, requestId: str) -> Optional[dict]:
        """
        :param requestId: Identifier of XHR to replay.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        mayberes = await self.chrome.send("Network.replayXHR", msg_dict)
        return mayberes

    async def searchInResponseBody(
        self,
        requestId: str,
        query: str,
        caseSensitive: Optional[bool] = None,
        isRegex: Optional[bool] = None,
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.searchInResponseBody", msg_dict)
        res = await mayberes
        res["result"] = Debugger.SearchMatch.safe_create_from_list(res["result"])
        return res

    async def setBlockedURLs(self, urls: List[str]) -> Optional[dict]:
        """
        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        :type urls: List[str]
        """
        msg_dict = dict()
        if urls is not None:
            msg_dict["urls"] = urls
        mayberes = await self.chrome.send("Network.setBlockedURLs", msg_dict)
        return mayberes

    async def setBypassServiceWorker(self, bypass: bool) -> Optional[dict]:
        """
        :param bypass: Bypass service worker and load from network.
        :type bypass: bool
        """
        msg_dict = dict()
        if bypass is not None:
            msg_dict["bypass"] = bypass
        mayberes = await self.chrome.send("Network.setBypassServiceWorker", msg_dict)
        return mayberes

    async def setCacheDisabled(self, cacheDisabled: bool) -> Optional[dict]:
        """
        :param cacheDisabled: Cache disabled state.
        :type cacheDisabled: bool
        """
        msg_dict = dict()
        if cacheDisabled is not None:
            msg_dict["cacheDisabled"] = cacheDisabled
        mayberes = await self.chrome.send("Network.setCacheDisabled", msg_dict)
        return mayberes

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
        mayberes = await self.chrome.send("Network.setCookie", msg_dict)
        res = await mayberes
        return res

    async def setCookies(self, cookies: List[dict]) -> Optional[dict]:
        """
        :param cookies: Cookies to be set.
        :type cookies: List[dict]
        """
        msg_dict = dict()
        if cookies is not None:
            msg_dict["cookies"] = cookies
        mayberes = await self.chrome.send("Network.setCookies", msg_dict)
        return mayberes

    async def setDataSizeLimitsForTest(
        self, maxTotalSize: int, maxResourceSize: int
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.setDataSizeLimitsForTest", msg_dict)
        return mayberes

    async def setExtraHTTPHeaders(self, headers: dict) -> Optional[dict]:
        """
        :param headers: Map with extra HTTP headers.
        :type headers: dict
        """
        msg_dict = dict()
        if headers is not None:
            msg_dict["headers"] = headers
        mayberes = await self.chrome.send("Network.setExtraHTTPHeaders", msg_dict)
        return mayberes

    async def setRequestInterception(self, patterns: List[dict]) -> Optional[dict]:
        """
        :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call.
        :type patterns: List[dict]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict["patterns"] = patterns
        mayberes = await self.chrome.send("Network.setRequestInterception", msg_dict)
        return mayberes

    async def setUserAgentOverride(
        self,
        userAgent: str,
        acceptLanguage: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Optional[dict]:
        """
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
        mayberes = await self.chrome.send("Network.setUserAgentOverride", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
