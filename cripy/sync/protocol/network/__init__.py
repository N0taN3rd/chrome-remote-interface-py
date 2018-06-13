from cripy.sync.protocol.io import types as IO
from cripy.sync.protocol.debugger import types as Debugger
from cripy.sync.protocol.network import events as Events
from cripy.sync.protocol.network import types as Types

__all__ = ["Network"] + Events.__all__ + Types.__all__ 


class Network(object):
    """
    Network domain allows tracking network activities of the page. It exposes information about http,
file, data and other requests and responses, their headers, bodies, timing, etc.
    """

    dependencies = ['Debugger', 'Runtime', 'Security']

    def __init__(self, chrome):
        self.chrome = chrome

    def canClearBrowserCache(self):
        def cb(res):
            self.chrome.emit('Network.canClearBrowserCache', res)
        self.chrome.send('Network.canClearBrowserCache', cb=cb)


    def canClearBrowserCookies(self):
        def cb(res):
            self.chrome.emit('Network.canClearBrowserCookies', res)
        self.chrome.send('Network.canClearBrowserCookies', cb=cb)


    def canEmulateNetworkConditions(self):
        def cb(res):
            self.chrome.emit('Network.canEmulateNetworkConditions', res)
        self.chrome.send('Network.canEmulateNetworkConditions', cb=cb)


    def clearBrowserCache(self):
        self.chrome.send('Network.clearBrowserCache')


    def clearBrowserCookies(self):
        self.chrome.send('Network.clearBrowserCookies')


    def continueInterceptedRequest(self, interceptionId, errorReason, rawResponse, url, method, postData, headers, authChallengeResponse):
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
            msg_dict['interceptionId'] = interceptionId
        if errorReason is not None:
            msg_dict['errorReason'] = errorReason
        if rawResponse is not None:
            msg_dict['rawResponse'] = rawResponse
        if url is not None:
            msg_dict['url'] = url
        if method is not None:
            msg_dict['method'] = method
        if postData is not None:
            msg_dict['postData'] = postData
        if headers is not None:
            msg_dict['headers'] = headers
        if authChallengeResponse is not None:
            msg_dict['authChallengeResponse'] = authChallengeResponse
        self.chrome.send('Network.continueInterceptedRequest', params=msg_dict)


    def deleteCookies(self, name, url, domain, path):
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
            msg_dict['name'] = name
        if url is not None:
            msg_dict['url'] = url
        if domain is not None:
            msg_dict['domain'] = domain
        if path is not None:
            msg_dict['path'] = path
        self.chrome.send('Network.deleteCookies', params=msg_dict)


    def disable(self):
        self.chrome.send('Network.disable')


    def emulateNetworkConditions(self, offline, latency, downloadThroughput, uploadThroughput, connectionType):
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
            msg_dict['offline'] = offline
        if latency is not None:
            msg_dict['latency'] = latency
        if downloadThroughput is not None:
            msg_dict['downloadThroughput'] = downloadThroughput
        if uploadThroughput is not None:
            msg_dict['uploadThroughput'] = uploadThroughput
        if connectionType is not None:
            msg_dict['connectionType'] = connectionType
        self.chrome.send('Network.emulateNetworkConditions', params=msg_dict)


    def enable(self, maxTotalBufferSize, maxResourceBufferSize, maxPostDataSize):
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
            msg_dict['maxTotalBufferSize'] = maxTotalBufferSize
        if maxResourceBufferSize is not None:
            msg_dict['maxResourceBufferSize'] = maxResourceBufferSize
        if maxPostDataSize is not None:
            msg_dict['maxPostDataSize'] = maxPostDataSize
        self.chrome.send('Network.enable', params=msg_dict)


    def getAllCookies(self):
        def cb(res):
            res['cookies'] = Types.Cookie.safe_create_from_list(res['cookies'])
            self.chrome.emit('Network.getAllCookies', res)
        self.chrome.send('Network.getAllCookies', cb=cb)


    def getCertificate(self, origin):
        """
        :param origin: Origin to get certificate for.
        :type origin: str
        """
        def cb(res):
            self.chrome.emit('Network.getCertificate', res)
        msg_dict = dict()
        if origin is not None:
            msg_dict['origin'] = origin
        self.chrome.send('Network.getCertificate', params=msg_dict, cb=cb)


    def getCookies(self, urls):
        """
        :param urls: The list of URLs for which applicable cookies will be fetched
        :type urls: Optional[List[str]]
        """
        def cb(res):
            res['cookies'] = Types.Cookie.safe_create_from_list(res['cookies'])
            self.chrome.emit('Network.getCookies', res)
        msg_dict = dict()
        if urls is not None:
            msg_dict['urls'] = urls
        self.chrome.send('Network.getCookies', params=msg_dict, cb=cb)


    def getResponseBody(self, requestId):
        """
        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        def cb(res):
            self.chrome.emit('Network.getResponseBody', res)
        msg_dict = dict()
        if requestId is not None:
            msg_dict['requestId'] = requestId
        self.chrome.send('Network.getResponseBody', params=msg_dict, cb=cb)


    def getRequestPostData(self, requestId):
        """
        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        """
        def cb(res):
            self.chrome.emit('Network.getRequestPostData', res)
        msg_dict = dict()
        if requestId is not None:
            msg_dict['requestId'] = requestId
        self.chrome.send('Network.getRequestPostData', params=msg_dict, cb=cb)


    def getResponseBodyForInterception(self, interceptionId):
        """
        :param interceptionId: Identifier for the intercepted request to get body for.
        :type interceptionId: str
        """
        def cb(res):
            self.chrome.emit('Network.getResponseBodyForInterception', res)
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict['interceptionId'] = interceptionId
        self.chrome.send('Network.getResponseBodyForInterception', params=msg_dict, cb=cb)


    def takeResponseBodyForInterceptionAsStream(self, interceptionId):
        """
        :param interceptionId: The interceptionId
        :type interceptionId: str
        """
        def cb(res):
            self.chrome.emit('Network.takeResponseBodyForInterceptionAsStream', res)
        msg_dict = dict()
        if interceptionId is not None:
            msg_dict['interceptionId'] = interceptionId
        self.chrome.send('Network.takeResponseBodyForInterceptionAsStream', params=msg_dict, cb=cb)


    def replayXHR(self, requestId):
        """
        :param requestId: Identifier of XHR to replay.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict['requestId'] = requestId
        self.chrome.send('Network.replayXHR', params=msg_dict)


    def searchInResponseBody(self, requestId, query, caseSensitive, isRegex):
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
        def cb(res):
            res['result'] = Debugger.SearchMatch.safe_create_from_list(res['result'])
            self.chrome.emit('Network.searchInResponseBody', res)
        msg_dict = dict()
        if requestId is not None:
            msg_dict['requestId'] = requestId
        if query is not None:
            msg_dict['query'] = query
        if caseSensitive is not None:
            msg_dict['caseSensitive'] = caseSensitive
        if isRegex is not None:
            msg_dict['isRegex'] = isRegex
        self.chrome.send('Network.searchInResponseBody', params=msg_dict, cb=cb)


    def setBlockedURLs(self, urls):
        """
        :param urls: URL patterns to block. Wildcards ('*') are allowed.
        :type urls: List[str]
        """
        msg_dict = dict()
        if urls is not None:
            msg_dict['urls'] = urls
        self.chrome.send('Network.setBlockedURLs', params=msg_dict)


    def setBypassServiceWorker(self, bypass):
        """
        :param bypass: Bypass service worker and load from network.
        :type bypass: bool
        """
        msg_dict = dict()
        if bypass is not None:
            msg_dict['bypass'] = bypass
        self.chrome.send('Network.setBypassServiceWorker', params=msg_dict)


    def setCacheDisabled(self, cacheDisabled):
        """
        :param cacheDisabled: Cache disabled state.
        :type cacheDisabled: bool
        """
        msg_dict = dict()
        if cacheDisabled is not None:
            msg_dict['cacheDisabled'] = cacheDisabled
        self.chrome.send('Network.setCacheDisabled', params=msg_dict)


    def setCookie(self, name, value, url, domain, path, secure, httpOnly, sameSite, expires):
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
        def cb(res):
            self.chrome.emit('Network.setCookie', res)
        msg_dict = dict()
        if name is not None:
            msg_dict['name'] = name
        if value is not None:
            msg_dict['value'] = value
        if url is not None:
            msg_dict['url'] = url
        if domain is not None:
            msg_dict['domain'] = domain
        if path is not None:
            msg_dict['path'] = path
        if secure is not None:
            msg_dict['secure'] = secure
        if httpOnly is not None:
            msg_dict['httpOnly'] = httpOnly
        if sameSite is not None:
            msg_dict['sameSite'] = sameSite
        if expires is not None:
            msg_dict['expires'] = expires
        self.chrome.send('Network.setCookie', params=msg_dict, cb=cb)


    def setCookies(self, cookies):
        """
        :param cookies: Cookies to be set.
        :type cookies: List[dict]
        """
        msg_dict = dict()
        if cookies is not None:
            msg_dict['cookies'] = cookies
        self.chrome.send('Network.setCookies', params=msg_dict)


    def setDataSizeLimitsForTest(self, maxTotalSize, maxResourceSize):
        """
        :param maxTotalSize: Maximum total buffer size.
        :type maxTotalSize: int
        :param maxResourceSize: Maximum per-resource size.
        :type maxResourceSize: int
        """
        msg_dict = dict()
        if maxTotalSize is not None:
            msg_dict['maxTotalSize'] = maxTotalSize
        if maxResourceSize is not None:
            msg_dict['maxResourceSize'] = maxResourceSize
        self.chrome.send('Network.setDataSizeLimitsForTest', params=msg_dict)


    def setExtraHTTPHeaders(self, headers):
        """
        :param headers: Map with extra HTTP headers.
        :type headers: dict
        """
        msg_dict = dict()
        if headers is not None:
            msg_dict['headers'] = headers
        self.chrome.send('Network.setExtraHTTPHeaders', params=msg_dict)


    def setRequestInterception(self, patterns):
        """
        :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call.
        :type patterns: List[dict]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict['patterns'] = patterns
        self.chrome.send('Network.setRequestInterception', params=msg_dict)


    def setUserAgentOverride(self, userAgent, acceptLanguage, platform):
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
            msg_dict['userAgent'] = userAgent
        if acceptLanguage is not None:
            msg_dict['acceptLanguage'] = acceptLanguage
        if platform is not None:
            msg_dict['platform'] = platform
        self.chrome.send('Network.setUserAgentOverride', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

