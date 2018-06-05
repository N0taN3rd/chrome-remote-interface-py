

"""Network Manager module."""

import asyncio
import base64
from collections import OrderedDict
import json
from urllib.parse import unquote
from types import SimpleNamespace
from typing import Awaitable, Dict, Optional, Union, TYPE_CHECKING

from pyee import EventEmitter

from cripy.chrome.connection import CDPSession
from cripy.chrome.errors import NetworkError
from cripy.chrome.frame_manager import FrameManager, Frame
from cripy.chrome.multimap import Multimap
from cripy.protocol.network.types import Request as PRequest, Response as PResponse

if TYPE_CHECKING:
    from typing import Set  # noqa: F401


class NetworkManager(EventEmitter):
    """NetworkManager class."""

    Events = SimpleNamespace(
        Request="request",
        Response="response",
        RequestFailed="requestfailed",
        RequestFinished="requestfinished",
    )

    def __init__(self, client: CDPSession, frameManager: FrameManager) -> None:
        """Make new NetworkManager."""
        super().__init__()
        self._client: CDPSession = client
        self._frameManager = frameManager
        self._requestIdToRequest: Dict[Optional[str], Request] = dict()
        self._interceptionIdToRequest: Dict[Optional[str], Request] = dict()
        self._extraHTTPHeaders: OrderedDict[str, str] = OrderedDict()
        self._offline: bool = False
        self._credentials: Optional[Dict[str, str]] = None
        self._attemptedAuthentications: Set[str] = set()
        self._userRequestInterceptionEnabled = False
        self._protocolRequestInterceptionEnabled = False
        self._requestHashToRequestIds = Multimap()
        self._requestHashToInterceptionIds = Multimap()

        self._client.on("Network.requestWillBeSent", self._onRequestWillBeSent)
        self._client.on(
            "Network.requestIntercepted", self._onRequestIntercepted
        )  # noqa: E501
        self._client.on(
            "Network.requestServedFromCache", self._onRequestServedFromCache
        )  # noqa: #501
        self._client.on("Network.responseReceived", self._onResponseReceived)
        self._client.on("Network.loadingFinished", self._onLoadingFinished)
        self._client.on("Network.loadingFailed", self._onLoadingFailed)

    async def authenticate(self, credentials: Dict[str, str]) -> None:
        """Provide credentials for http auth."""
        self._credentials = credentials
        await self._updateProtocolRequestInterception()

    async def setExtraHTTPHeaders(self, extraHTTPHeaders: Dict[str, str]) -> None:
        """Set extra http headers."""
        self._extraHTTPHeaders = OrderedDict()
        for k, v in extraHTTPHeaders.items():
            if not isinstance(v, str):
                raise TypeError(
                    f'Expected value of header "{k}" to be string, {type(v)}'
                )
            self._extraHTTPHeaders[k.lower()] = v
        await self._client.send(
            "Network.setExtraHTTPHeaders", {"headers": self._extraHTTPHeaders}
        )

    def extraHTTPHeaders(self) -> Dict[str, str]:
        """Get extra http headers."""
        return dict(**self._extraHTTPHeaders)

    async def setOfflineMode(self, value: bool) -> None:
        """Change offline mode enable/disable."""
        if self._offline == value:
            return
        self._offline = value
        await self._client.send(
            "Network.emulateNetworkConditions",
            {
                "offline": self._offline,
                "latency": 0,
                "downloadThroughput": -1,
                "uploadThroughput": -1,
            },
        )

    async def setUserAgent(self, userAgent: str) -> None:
        """Set user agent."""
        await self._client.send(
            "Network.setUserAgentOverride", {"userAgent": userAgent}
        )

    async def setRequestInterception(self, value: bool) -> None:
        """Enable request intercetion."""
        self._userRequestInterceptionEnabled = value
        await self._updateProtocolRequestInterception()

    async def _updateProtocolRequestInterception(self) -> None:
        enabled = self._userRequestInterceptionEnabled or bool(self._credentials)
        if enabled == self._protocolRequestInterceptionEnabled:
            return
        self._protocolRequestInterceptionEnabled = enabled
        patterns = [{"urlPattern": "*"}] if enabled else []
        await asyncio.gather(
            self._client.send("Network.setCacheDisabled", {"cacheDisabled": enabled}),
            self._client.send("Network.setRequestInterception", {"patterns": patterns}),
        )

    def _onRequestIntercepted(self, event: dict) -> None:  # noqa: C901
        if event.get("authChallenge"):
            response = "Default"
            if event["interceptionId"] in self._attemptedAuthentications:
                response = "CancelAuth"
            elif self._credentials:
                response = "ProvideCredentials"
                self._attemptedAuthentications.add(event["interceptionId"])
            username = getattr(self, "_credentials", {}).get("username")
            password = getattr(self, "_credentials", {}).get("password")
            asyncio.ensure_future(
                self._client.send(
                    "Network.continueInterceptedRequest",
                    {
                        "interceptionId": event["interceptionId"],
                        "authChallengeResponse": {
                            "response": response,
                            "username": username,
                            "password": password,
                        },
                    },
                )
            )
            return

        if (
            not self._userRequestInterceptionEnabled
            and self._protocolRequestInterceptionEnabled
        ):
            asyncio.ensure_future(
                self._client.send(
                    "Network.continueInterceptedRequest",
                    {"interceptionId": event["interceptionId"]},
                )
            )

        if "redirectURL" in event:
            request = self._interceptionIdToRequest.get(event.get("interceptionId", ""))
            if request:
                self._handleRequestRedirect(
                    request,
                    event.get("redirectStatusCode", 0),
                    event.get("redirectHeaders", {}),
                    False,
                    False,
                    None,
                )
                self._handleRequestStart(
                    request.requestId,
                    event.get("interceptionId", ""),
                    event.get("redirectUrl", ""),
                    event.get("resourceType", ""),
                    event.get("postData", ""),
                    event.get("frameId"),
                    event.get("request", {}),
                )
            return

        requestHash = generateRequestHash(event["request"])
        requestId = self._requestHashToRequestIds.firstValue(requestHash)
        if requestId:
            self._requestHashToRequestIds.delete(requestHash, requestId)
            self._handleRequestStart(
                requestId,
                event["interceptionId"],
                event["request"]["url"],
                event["resourceType"],
                event["request"],
                event["frameId"],
                event["request"],
            )
        else:
            self._requestHashToInterceptionIds.set(requestHash, event["interceptionId"])
            self._handleRequestStart(
                None,
                event["interceptionId"],
                event["request"]["url"],
                event["resourceType"],
                event["request"],
                event["frameId"],
                event["request"],
            )

    def _onRequestServedFromCache(self, event: Dict) -> None:
        request = self._requestIdToRequest.get(event.get("requestId"))
        if request:
            request.fromMemoryCache = True

    def _handleRequestRedirect(
        self,
        request: "Request",
        redirectStatus: int,
        redirectHeaders: Dict,
        fromDiskCache: bool,
        fromServiceWorker: bool,
        securityDetails: Dict = None,
        redirectResponse: Optional[Union[dict, PResponse]] = None,
    ) -> None:
        response = Response(
            self._client,
            request,
            redirectStatus,
            redirectHeaders,
            fromDiskCache,
            fromServiceWorker,
            securityDetails,
            redirectResponse,
        )
        request.response = response
        self._requestIdToRequest.pop(request.requestId, None)
        self._interceptionIdToRequest.pop(request._interceptionId, None)
        self._attemptedAuthentications.discard(request._interceptionId)
        self.emit(NetworkManager.Events.Response, response)
        self.emit(NetworkManager.Events.RequestFinished, request)

    def _handleRequestStart(
        self,
        requestId: Optional[str],
        interceptionId: str,
        url: str,
        resourceType: str,
        requestPayload: Dict,
        frameId: Optional[str],
        rreq: Optional[Union[dict, PRequest]] = None,
    ) -> None:
        frame = None
        if frameId and self._frameManager is not None:
            frame = self._frameManager.frame(frameId)

        request = Request(
            self._client,
            requestId,
            interceptionId,
            self._userRequestInterceptionEnabled,
            url,
            resourceType,
            requestPayload,
            frame,
            rreq,
        )
        if requestId:
            self._requestIdToRequest[requestId] = request
        if interceptionId:
            self._interceptionIdToRequest[interceptionId] = request
        self.emit(NetworkManager.Events.Request, request)

    def _onRequestWillBeSent(self, event: dict) -> None:
        if self._protocolRequestInterceptionEnabled:
            if event.get("redirectResponse"):
                return
            requestHash = generateRequestHash(event["request"])
            interceptionId = self._requestHashToInterceptionIds.firstValue(requestHash)
            request = self._interceptionIdToRequest.get(interceptionId)
            if request:
                request.requestId = event["requestId"]
                self._requestIdToRequest[event["requestId"]] = request
                self._requestHashToInterceptionIds.delete(requestHash, interceptionId)
            else:
                self._requestHashToRequestIds.set(requestHash, event["requestId"])
            return
        if event.get("redirectResponse"):
            request = self._requestIdToRequest[event["requestId"]]
            if request:
                redirectResponse = event.get("redirectResponse", {})
                self._handleRequestRedirect(
                    request,
                    redirectResponse.get("status"),
                    redirectResponse.get("headers"),
                    redirectResponse.get("fromDiskCache"),
                    redirectResponse.get("fromServiceWorker"),
                    redirectResponse.get("securityDetails"),
                    redirectResponse,
                )
        r = event.get("request", {})
        self._handleRequestStart(
            event.get("requestId", ""),
            "",
            r.get("url", ""),
            event.get("type", ""),
            event.get("request", {}),
            event.get("frameId"),
            r,
        )

    def _onResponseReceived(self, event: dict) -> None:
        request = self._requestIdToRequest.get(event["requestId"])
        # FileUpload sends a response without a matching request.
        if not request:
            return
        _resp = event.get("response", {})
        response = Response(
            self._client,
            request,
            _resp.get("status", 0),
            _resp.get("headers", {}),
            _resp.get("fromDiskCache"),
            _resp.get("fromServiceWorker"),
            _resp.get("securityDetails"),
            _resp,
        )
        request.response = response
        self.emit(NetworkManager.Events.Response, response)

    def _onLoadingFinished(self, event: dict) -> None:
        request = self._requestIdToRequest.get(event.get("requestId", ""))
        # For certain requestIds we never receive requestWillBeSent event.
        # @see https://crbug.com/750469
        if not request:
            return
        request._completePromiseFulfill()
        self._requestIdToRequest.pop(request.requestId, None)
        self._interceptionIdToRequest.pop(request._interceptionId, None)
        self._attemptedAuthentications.discard(request._interceptionId)
        self.emit(NetworkManager.Events.RequestFinished, request)

    def _onLoadingFailed(self, event: dict) -> None:
        request = self._requestIdToRequest.get(event["requestId"])
        # For certain requestIds we never receive requestWillBeSent event.
        # @see https://crbug.com/750469
        if not request:
            return
        request.failureText = event.get("errorText")
        request._completePromiseFulfill()
        self._requestIdToRequest.pop(request.requestId, None)
        self._interceptionIdToRequest.pop(request._interceptionId, None)
        self._attemptedAuthentications.discard(request._interceptionId)
        self.emit(NetworkManager.Events.RequestFailed, request)


class Request(object):
    """Request class."""

    def __init__(
        self,
        client: CDPSession,
        requestId: Optional[str],
        interceptionId: str,
        allowInterception: bool,
        url: str,
        resourceType: str,
        payload: dict,
        frame: Optional[Frame],
        rreq: Optional[Union[dict, PRequest]] = None,
    ) -> None:
        self._client = client
        self.requestId = requestId
        self._interceptionId = interceptionId
        self._allowInterception = allowInterception
        self._interceptionHandled = False
        self.response: Optional[Response] = None
        self.failureText: Optional[str] = None
        self._completePromise = asyncio.get_event_loop().create_future()

        self.url = url
        self.resourceType = resourceType.lower()
        self.method = payload.get("method")
        self.postData = payload.get("postData")
        headers = payload.get("headers", {})
        self.headers = {k.lower(): v for k, v in headers.items()}
        self.frame = frame

        self.fromMemoryCache = False
        self.preq: Optional[Union[dict, PRequest]] = rreq

    def _completePromiseFulfill(self) -> None:
        self._completePromise.set_result(None)

    def failure(self) -> Optional[Dict]:
        """Return error text.

        Return ``None`` unless this request was failed, as reported by
        ``requestfailed`` event.

        When request failed, this method return dictionary which has a
        ``errorText`` field, which contains human-readable error message, e.g.
        ``'net::ERR_RAILED'``.
        """
        if not self.failureText:
            return None
        return {"errorText": self.failureText}

    async def continue_(self, overrides: Dict = None) -> None:
        """Continue request with optional request overrides.

        To use this method, request interception should be enabled by
        :meth:`pyppeteer.page.Page.setRequestInterception`. If request
        interception is not enabled, raise ``NetworkError``.

        ``overrides`` can have the following fields:

        * ``url`` (str): If set, the request url will be changed.
        * ``method`` (str): If set, change the request method (e.g. ``GET``).
        * ``postData`` (str): If set, change the post data or request.
        * ``headers`` (dict): If set, change the request HTTP header.
        """
        if overrides is None:
            overrides = {}

        if not self._allowInterception:
            raise NetworkError("Request interception is not enabled.")
        if self._interceptionHandled:
            raise NetworkError("Request is already handled.")

        self._interceptionHandled = True
        opt = {"interceptionId": self._interceptionId}
        opt.update(overrides)
        await self._client.send("Network.continueInterceptedRequest", opt)

    async def respond(self, response: Dict) -> None:  # noqa: C901
        """Fulfills request with given response.

        To use this, request interception shuold by enabled by
        :meth:`pyppeteer.page.Page.setRequestInterception`. Requst interception
        is not enabled, raise ``NetworkError``.

        ``response`` is a dictinary which can have the following fields:

        * ``status`` (int): Response status code, defaults to 200.
        * ``headers`` (dict): Optional response headers.
        * ``contentType`` (str): If set, euqals to setting ``Content-Type``
          response header.
        * ``body`` (str|bytes): Optional response body.
        """
        if self.url.startswith("data:"):
            return
        if not self._allowInterception:
            raise NetworkError("Request interception is not enabled.")
        if self._interceptionHandled:
            raise NetworkError("Request is already handled.")
        self._interceptionHandled = True

        if response.get("body") and isinstance(response["body"], str):
            responseBody: Optional[bytes] = response["body"].encode("utf-8")
        else:
            responseBody = response.get("body")

        responseHeaders = {}
        if response.get("headers"):
            for header in response["headers"]:
                responseHeaders[header.lower()] = response["headers"][header]
        if response.get("contentType"):
            responseHeaders["content-type"] = response["contentType"]
        if responseBody and "content-length" not in responseHeaders:
            responseHeaders["content-length"] = len(responseBody)

        statusCode = response.get("status", 200)
        statusText = statusTexts.get(statusCode, "")
        statusLine = f"HTTP/1.1 {statusCode} {statusText}"

        CRLF = "\r\n"
        text = statusLine + CRLF
        for header in responseHeaders:
            text = f"{text}{header}: {responseHeaders[header]}{CRLF}"
        text = text + CRLF
        responseBuffer = text.encode("utf-8")
        if responseBody:
            responseBuffer = responseBuffer + responseBody

        rawResponse = base64.b64encode(responseBuffer).decode("ascii")
        await self._client.send(
            "Network.continueInterceptedRequest",
            {"interceptionId": self._interceptionId, "rawResponse": rawResponse},
        )

    async def abort(self, errorCode: str = "failed") -> None:
        """Abort request.

        To use this, request interception should be enabled by
        :meth:`pyppeteer.page.Page.setRequestInterception`.
        If request interception is not enabled, raise ``NetworkError``.

        ``errorCode`` is an optional error code string. Defaults to ``failed``,
        could be one of the following: ``aborted``, ``accesdenied``,
        ``addressunreachable``, ``connectionaborted``, ``connectionclosed``,
        ``connectionfailed``, ``connnectionrefused``, ``connectionreset``,
        ``internetdisconnected``, ``namenotresolved``, ``timedout``, ``failed``
        """
        errorReason = errorReasons[errorCode]
        if not errorReason:
            raise NetworkError("Unknown error code: {}".format(errorCode))
        if not self._allowInterception:
            raise NetworkError("Request interception is not enabled.")
        if self._interceptionHandled:
            raise NetworkError("Request is already handled.")
        self._interceptionHandled = True
        await self._client.send(
            "Network.continueInterceptedRequest",
            dict(interceptionId=self._interceptionId, errorReason=errorReason),
        )


errorReasons = {
    "aborted": "Aborted",
    "accessdenied": "AccessDenied",
    "addressunreachable": "AddressUnreachable",
    "connectionaborted": "ConnectionAborted",
    "connectionclosed": "ConnectionClosed",
    "connectionfailed": "ConnectionFailed",
    "connectionrefused": "ConnectionRefused",
    "connectionreset": "ConnectionReset",
    "internetdisconnected": "InternetDisconnected",
    "namenotresolved": "NameNotResolved",
    "timedout": "TimedOut",
    "failed": "Failed",
}


class Response(object):
    """Response class represents responses which are recieved by ``Page``."""

    def __init__(
        self,
        client: CDPSession,
        request: Request,
        status: int,
        headers: Dict[str, str],
        fromDiskCache: bool,
        fromServiceWorker: bool,
        securityDetails: Dict = None,
        rresp: Optional[Union[dict, PResponse]] = None,
    ) -> None:
        self._client = client
        self.request = request
        self.status = status
        self._contentPromise = asyncio.get_event_loop().create_future()
        self.url = request.url
        self.fromDiskCache = fromDiskCache
        self.fromServiceWorker = fromServiceWorker
        self.headers = {k.lower(): v for k, v in headers.items()}
        self.securityDetails: Union[Dict, SecurityDetails] = {}
        if securityDetails:
            self.securityDetails = SecurityDetails(
                securityDetails["subjectName"],
                securityDetails["issuer"],
                securityDetails["validFrom"],
                securityDetails["validTo"],
                securityDetails["protocol"],
            )
        self.pres = rresp

    async def _bufread(self) -> bytes:
        response = await self._client.send(
            "Network.getResponseBody", {"requestId": self.request.requestId}
        )
        body = response.get("body", b"")
        if response.get("base64Encoded"):
            return base64.b64decode(body)
        return body

    def buffer(self) -> Awaitable[bytes]:
        """Retrun awaitable which resolves to bytes with response body."""
        if not self._contentPromise.done():
            return asyncio.ensure_future(self._bufread())
        return self._contentPromise

    async def text(self) -> str:
        """Get text representation of response body."""
        content = await self.buffer()
        if isinstance(content, str):
            return content
        else:
            return content.decode("utf-8")

    async def json(self) -> dict:
        """Get JSON representation of response body."""
        content = await self.text()
        return json.loads(content)


def generateRequestHash(request: dict) -> str:
    """Generate request hash."""
    normalizedURL = request.get("url", "")
    try:
        normalizedURL = unquote(normalizedURL)
    except Exception:
        pass

    _hash = {
        "url": normalizedURL,
        "method": request.get("method"),
        "postData": request.get("postData"),
        "headers": {},
    }

    if not normalizedURL.startswith("data:"):
        headers = list(request["headers"].keys())
        headers.sort()
        for header in headers:
            headerValue = request["headers"][header]
            header = header.lower()
            if (
                header == "accept"
                or header == "referer"
                or header == "x-devtools-emulate-network-conditions-client-id"
            ):  # noqa: E501
                continue
            _hash["headers"][header] = headerValue
    return json.dumps(_hash)


class SecurityDetails(object):
    """Class represents responses which are received by page."""

    def __init__(
        self, subjectName: str, issuer: str, validFrom: int, validTo: int, protocol: str
    ) -> None:
        self.subjectName = subjectName
        self.issuer = issuer
        self.validFrom = validFrom
        self.validTo = validTo
        self.protocol = protocol


statusTexts = {
    "100": "Continue",
    "101": "Switching Protocols",
    "102": "Processing",
    "200": "OK",
    "201": "Created",
    "202": "Accepted",
    "203": "Non-Authoritative Information",
    "204": "No Content",
    "206": "Partial Content",
    "207": "Multi-Status",
    "208": "Already Reported",
    "209": "IM Used",
    "300": "Multiple Choices",
    "301": "Moved Permanently",
    "302": "Found",
    "303": "See Other",
    "304": "Not Modified",
    "305": "Use Proxy",
    "306": "Switch Proxy",
    "307": "Temporary Redirect",
    "308": "Permanent Redirect",
    "400": "Bad Request",
    "401": "Unauthorized",
    "402": "Payment Required",
    "403": "Forbidden",
    "404": "Not Found",
    "405": "Method Not Allowed",
    "406": "Not Acceptable",
    "407": "Proxy Authentication Required",
    "408": "Request Timeout",
    "409": "Conflict",
    "410": "Gone",
    "411": "Length Required",
    "412": "Precondition Failed",
    "413": "Payload Too Large",
    "414": "URI Too Long",
    "415": "Unsupported Media Type",
    "416": "Range Not Satisfiable",
    "417": "Expectation Failed",
    "418": "I'm a teapot",
    "421": "Misdirected Request",
    "422": "Unprocessable Entity",
    "423": "Locked",
    "424": "Failed Dependency",
    "426": "Upgrade Required",
    "428": "Precondition Required",
    "429": "Too Many Requests",
    "431": "Request Header Fields Too Large",
    "451": "Unavailable For Legal Reasons",
    "500": "Internal Server Error",
    "501": "Not Implemented",
    "502": "Bad Gateway",
    "503": "Service Unavailable",
    "504": "Gateway Timeout",
    "505": "HTTP Version Not Supported",
    "506": "Variant Also Negotiates",
    "507": "Insufficient Storage",
    "508": "Loop Detected",
    "510": "Not Extended",
    "511": "Network Authentication Required",
}
