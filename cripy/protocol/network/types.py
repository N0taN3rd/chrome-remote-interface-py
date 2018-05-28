from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.security import types as Security
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.page import types as Page

# Unique loader identifier.
LoaderId = str

# Unique request identifier.
RequestId = str

# Unique intercepted request identifier.
InterceptionId = str

# Network level fetch failure reason.
ErrorReason = str

# UTC time in seconds, counted from January 1, 1970.
TimeSinceEpoch = float

# Monotonically increasing time in seconds since an arbitrary point in the past.
MonotonicTime = float

# The underlying connection technology that the browser is supposedly using.
ConnectionType = str

# Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies
CookieSameSite = str

# Loading priority of a resource request.
ResourcePriority = str

# Whether the request complied with Certificate Transparency policy.
CertificateTransparencyCompliance = str

# The reason why request was blocked.
BlockedReason = str

# Stages of the interception to begin intercepting. Request will intercept before the request is sent. Response will intercept after the response is received.
InterceptionStage = str


class Headers(ChromeTypeBase, dict):
    """Request / response headers as keys / values of JSON object."""


class ResourceTiming(ChromeTypeBase):
    """Timing information for the request."""
    def __init__(self, requestTime: float, proxyStart: float, proxyEnd: float, dnsStart: float, dnsEnd: float, connectStart: float, connectEnd: float, sslStart: float, sslEnd: float, workerStart: float, workerReady: float, sendStart: float, sendEnd: float, pushStart: float, pushEnd: float, receiveHeadersEnd: float) -> None:
        """
        :param requestTime: Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime.
        :type requestTime: float
        :param proxyStart: Started resolving proxy.
        :type proxyStart: float
        :param proxyEnd: Finished resolving proxy.
        :type proxyEnd: float
        :param dnsStart: Started DNS address resolve.
        :type dnsStart: float
        :param dnsEnd: Finished DNS address resolve.
        :type dnsEnd: float
        :param connectStart: Started connecting to the remote host.
        :type connectStart: float
        :param connectEnd: Connected to the remote host.
        :type connectEnd: float
        :param sslStart: Started SSL handshake.
        :type sslStart: float
        :param sslEnd: Finished SSL handshake.
        :type sslEnd: float
        :param workerStart: Started running ServiceWorker.
        :type workerStart: float
        :param workerReady: Finished Starting ServiceWorker.
        :type workerReady: float
        :param sendStart: Started sending request.
        :type sendStart: float
        :param sendEnd: Finished sending request.
        :type sendEnd: float
        :param pushStart: Time the server started pushing request.
        :type pushStart: float
        :param pushEnd: Time the server finished pushing request.
        :type pushEnd: float
        :param receiveHeadersEnd: Finished receiving response headers.
        :type receiveHeadersEnd: float
        """
        super().__init__()
        self.requestTime: float = requestTime
        self.proxyStart: float = proxyStart
        self.proxyEnd: float = proxyEnd
        self.dnsStart: float = dnsStart
        self.dnsEnd: float = dnsEnd
        self.connectStart: float = connectStart
        self.connectEnd: float = connectEnd
        self.sslStart: float = sslStart
        self.sslEnd: float = sslEnd
        self.workerStart: float = workerStart
        self.workerReady: float = workerReady
        self.sendStart: float = sendStart
        self.sendEnd: float = sendEnd
        self.pushStart: float = pushStart
        self.pushEnd: float = pushEnd
        self.receiveHeadersEnd: float = receiveHeadersEnd


class Request(ChromeTypeBase):
    """HTTP request data."""
    def __init__(self, url: str, method: str, headers: 'Headers', initialPriority: 'ResourcePriority', referrerPolicy: str, postData: Optional[str] = None, hasPostData: Optional[bool] = None, mixedContentType: Optional['Security.MixedContentType'] = None, isLinkPreload: Optional[bool] = None) -> None:
        """
        :param url: Request URL.
        :type url: str
        :param method: HTTP request method.
        :type method: str
        :param headers: HTTP request headers.
        :type headers: Headers
        :param postData: HTTP POST request data.
        :type postData: str
        :param hasPostData: True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.
        :type hasPostData: bool
        :param mixedContentType: The mixed content type of the request.
        :type mixedContentType: Security.MixedContentType
        :param initialPriority: Priority of the resource request at the time request is sent.
        :type initialPriority: ResourcePriority
        :param referrerPolicy: The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/
        :type referrerPolicy: str
        :param isLinkPreload: Whether is loaded via link preload.
        :type isLinkPreload: bool
        """
        super().__init__()
        self.url: str = url
        self.method: str = method
        self.headers: Headers = headers
        self.postData: Optional[str] = postData
        self.hasPostData: Optional[bool] = hasPostData
        self.mixedContentType: Optional[Security.MixedContentType] = mixedContentType
        self.initialPriority: ResourcePriority = initialPriority
        self.referrerPolicy: str = referrerPolicy
        self.isLinkPreload: Optional[bool] = isLinkPreload


class SignedCertificateTimestamp(ChromeTypeBase):
    """Details of a signed certificate timestamp (SCT)."""
    def __init__(self, status: str, origin: str, logDescription: str, logId: str, timestamp: 'TimeSinceEpoch', hashAlgorithm: str, signatureAlgorithm: str, signatureData: str) -> None:
        """
        :param status: Validation status.
        :type status: str
        :param origin: Origin.
        :type origin: str
        :param logDescription: Log name / description.
        :type logDescription: str
        :param logId: Log ID.
        :type logId: str
        :param timestamp: Issuance date.
        :type timestamp: TimeSinceEpoch
        :param hashAlgorithm: Hash algorithm.
        :type hashAlgorithm: str
        :param signatureAlgorithm: Signature algorithm.
        :type signatureAlgorithm: str
        :param signatureData: Signature data.
        :type signatureData: str
        """
        super().__init__()
        self.status: str = status
        self.origin: str = origin
        self.logDescription: str = logDescription
        self.logId: str = logId
        self.timestamp: TimeSinceEpoch = timestamp
        self.hashAlgorithm: str = hashAlgorithm
        self.signatureAlgorithm: str = signatureAlgorithm
        self.signatureData: str = signatureData


class SecurityDetails(ChromeTypeBase):
    """Security details about a request."""
    def __init__(self, protocol: str, keyExchange: str, cipher: str, certificateId: 'Security.CertificateId', subjectName: str, sanList: List['str'], issuer: str, validFrom: 'TimeSinceEpoch', validTo: 'TimeSinceEpoch', signedCertificateTimestampList: List['SignedCertificateTimestamp'], certificateTransparencyCompliance: 'CertificateTransparencyCompliance', keyExchangeGroup: Optional[str] = None, mac: Optional[str] = None) -> None:
        """
        :param protocol: Protocol name (e.g. "TLS 1.2" or "QUIC").
        :type protocol: str
        :param keyExchange: Key Exchange used by the connection, or the empty string if not applicable.
        :type keyExchange: str
        :param keyExchangeGroup: (EC)DH group used by the connection, if applicable.
        :type keyExchangeGroup: str
        :param cipher: Cipher name.
        :type cipher: str
        :param mac: TLS MAC. Note that AEAD ciphers do not have separate MACs.
        :type mac: str
        :param certificateId: Certificate ID value.
        :type certificateId: Security.CertificateId
        :param subjectName: Certificate subject name.
        :type subjectName: str
        :param sanList: Subject Alternative Name (SAN) DNS names and IP addresses.
        :type sanList: array
        :param issuer: Name of the issuing CA.
        :type issuer: str
        :param validFrom: Certificate valid from date.
        :type validFrom: TimeSinceEpoch
        :param validTo: Certificate valid to (expiration) date
        :type validTo: TimeSinceEpoch
        :param signedCertificateTimestampList: List of signed certificate timestamps (SCTs).
        :type signedCertificateTimestampList: array
        :param certificateTransparencyCompliance: Whether the request complied with Certificate Transparency policy
        :type certificateTransparencyCompliance: CertificateTransparencyCompliance
        """
        super().__init__()
        self.protocol: str = protocol
        self.keyExchange: str = keyExchange
        self.keyExchangeGroup: Optional[str] = keyExchangeGroup
        self.cipher: str = cipher
        self.mac: Optional[str] = mac
        self.certificateId: Security.CertificateId = certificateId
        self.subjectName: str = subjectName
        self.sanList: List[str] = sanList
        self.issuer: str = issuer
        self.validFrom: TimeSinceEpoch = validFrom
        self.validTo: TimeSinceEpoch = validTo
        self.signedCertificateTimestampList: List[SignedCertificateTimestamp] = signedCertificateTimestampList
        self.certificateTransparencyCompliance: CertificateTransparencyCompliance = certificateTransparencyCompliance


class Response(ChromeTypeBase):
    """HTTP response data."""
    def __init__(self, url: str, status: int, statusText: str, headers: 'Headers', mimeType: str, connectionReused: bool, connectionId: float, encodedDataLength: float, securityState: 'Security.SecurityState', headersText: Optional[str] = None, requestHeaders: Optional['Headers'] = None, requestHeadersText: Optional[str] = None, remoteIPAddress: Optional[str] = None, remotePort: Optional[int] = None, fromDiskCache: Optional[bool] = None, fromServiceWorker: Optional[bool] = None, timing: Optional['ResourceTiming'] = None, protocol: Optional[str] = None, securityDetails: Optional['SecurityDetails'] = None) -> None:
        """
        :param url: Response URL. This URL can be different from CachedResource.url in case of redirect.
        :type url: str
        :param status: HTTP response status code.
        :type status: int
        :param statusText: HTTP response status text.
        :type statusText: str
        :param headers: HTTP response headers.
        :type headers: Headers
        :param headersText: HTTP response headers text.
        :type headersText: str
        :param mimeType: Resource mimeType as determined by the browser.
        :type mimeType: str
        :param requestHeaders: Refined HTTP request headers that were actually transmitted over the network.
        :type requestHeaders: Headers
        :param requestHeadersText: HTTP request headers text.
        :type requestHeadersText: str
        :param connectionReused: Specifies whether physical connection was actually reused for this request.
        :type connectionReused: bool
        :param connectionId: Physical connection id that was actually used for this request.
        :type connectionId: float
        :param remoteIPAddress: Remote IP address.
        :type remoteIPAddress: str
        :param remotePort: Remote port.
        :type remotePort: int
        :param fromDiskCache: Specifies that the request was served from the disk cache.
        :type fromDiskCache: bool
        :param fromServiceWorker: Specifies that the request was served from the ServiceWorker.
        :type fromServiceWorker: bool
        :param encodedDataLength: Total number of bytes received for this request so far.
        :type encodedDataLength: float
        :param timing: Timing information for the given request.
        :type timing: ResourceTiming
        :param protocol: Protocol used to fetch this request.
        :type protocol: str
        :param securityState: Security state of the request resource.
        :type securityState: Security.SecurityState
        :param securityDetails: Security details for the request.
        :type securityDetails: SecurityDetails
        """
        super().__init__()
        self.url: str = url
        self.status: int = status
        self.statusText: str = statusText
        self.headers: Headers = headers
        self.headersText: Optional[str] = headersText
        self.mimeType: str = mimeType
        self.requestHeaders: Optional[Headers] = requestHeaders
        self.requestHeadersText: Optional[str] = requestHeadersText
        self.connectionReused: bool = connectionReused
        self.connectionId: float = connectionId
        self.remoteIPAddress: Optional[str] = remoteIPAddress
        self.remotePort: Optional[int] = remotePort
        self.fromDiskCache: Optional[bool] = fromDiskCache
        self.fromServiceWorker: Optional[bool] = fromServiceWorker
        self.encodedDataLength: float = encodedDataLength
        self.timing: Optional[ResourceTiming] = timing
        self.protocol: Optional[str] = protocol
        self.securityState: Security.SecurityState = securityState
        self.securityDetails: Optional[SecurityDetails] = securityDetails


class WebSocketRequest(ChromeTypeBase):
    """WebSocket request data."""
    def __init__(self, headers: 'Headers') -> None:
        """
        :param headers: HTTP request headers.
        :type headers: Headers
        """
        super().__init__()
        self.headers: Headers = headers


class WebSocketResponse(ChromeTypeBase):
    """WebSocket response data."""
    def __init__(self, status: int, statusText: str, headers: 'Headers', headersText: Optional[str] = None, requestHeaders: Optional['Headers'] = None, requestHeadersText: Optional[str] = None) -> None:
        """
        :param status: HTTP response status code.
        :type status: int
        :param statusText: HTTP response status text.
        :type statusText: str
        :param headers: HTTP response headers.
        :type headers: Headers
        :param headersText: HTTP response headers text.
        :type headersText: str
        :param requestHeaders: HTTP request headers.
        :type requestHeaders: Headers
        :param requestHeadersText: HTTP request headers text.
        :type requestHeadersText: str
        """
        super().__init__()
        self.status: int = status
        self.statusText: str = statusText
        self.headers: Headers = headers
        self.headersText: Optional[str] = headersText
        self.requestHeaders: Optional[Headers] = requestHeaders
        self.requestHeadersText: Optional[str] = requestHeadersText


class WebSocketFrame(ChromeTypeBase):
    """WebSocket frame data."""
    def __init__(self, opcode: float, mask: bool, payloadData: str) -> None:
        """
        :param opcode: WebSocket frame opcode.
        :type opcode: float
        :param mask: WebSocke frame mask.
        :type mask: bool
        :param payloadData: WebSocke frame payload data.
        :type payloadData: str
        """
        super().__init__()
        self.opcode: float = opcode
        self.mask: bool = mask
        self.payloadData: str = payloadData


class CachedResource(ChromeTypeBase):
    """Information about the cached resource."""
    def __init__(self, url: str, type: 'Page.ResourceType', bodySize: float, response: Optional['Response'] = None) -> None:
        """
        :param url: Resource URL. This is the url of the original network request.
        :type url: str
        :param type: Type of this resource.
        :type type: Page.ResourceType
        :param response: Cached response data.
        :type response: Response
        :param bodySize: Cached response body size.
        :type bodySize: float
        """
        super().__init__()
        self.url: str = url
        self.type: Page.ResourceType = type
        self.response: Optional[Response] = response
        self.bodySize: float = bodySize


class Initiator(ChromeTypeBase):
    """Information about the request initiator."""
    def __init__(self, type: str, stack: Optional['Runtime.StackTrace'] = None, url: Optional[str] = None, lineNumber: Optional[float] = None) -> None:
        """
        :param type: Type of this initiator.
        :type type: str
        :param stack: Initiator JavaScript stack trace, set for Script only.
        :type stack: Runtime.StackTrace
        :param url: Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.
        :type url: str
        :param lineNumber: Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based).
        :type lineNumber: float
        """
        super().__init__()
        self.type: str = type
        self.stack: Optional[Runtime.StackTrace] = stack
        self.url: Optional[str] = url
        self.lineNumber: Optional[float] = lineNumber


class Cookie(ChromeTypeBase):
    """Cookie object"""
    def __init__(self, name: str, value: str, domain: str, path: str, expires: float, size: int, httpOnly: bool, secure: bool, session: bool, sameSite: Optional['CookieSameSite'] = None) -> None:
        """
        :param name: Cookie name.
        :type name: str
        :param value: Cookie value.
        :type value: str
        :param domain: Cookie domain.
        :type domain: str
        :param path: Cookie path.
        :type path: str
        :param expires: Cookie expiration date as the number of seconds since the UNIX epoch.
        :type expires: float
        :param size: Cookie size.
        :type size: int
        :param httpOnly: True if cookie is http-only.
        :type httpOnly: bool
        :param secure: True if cookie is secure.
        :type secure: bool
        :param session: True in case of session cookie.
        :type session: bool
        :param sameSite: Cookie SameSite type.
        :type sameSite: CookieSameSite
        """
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.domain: str = domain
        self.path: str = path
        self.expires: float = expires
        self.size: int = size
        self.httpOnly: bool = httpOnly
        self.secure: bool = secure
        self.session: bool = session
        self.sameSite: Optional[CookieSameSite] = sameSite


class CookieParam(ChromeTypeBase):
    """Cookie parameter object"""
    def __init__(self, name: str, value: str, url: Optional[str] = None, domain: Optional[str] = None, path: Optional[str] = None, secure: Optional[bool] = None, httpOnly: Optional[bool] = None, sameSite: Optional['CookieSameSite'] = None, expires: Optional['TimeSinceEpoch'] = None) -> None:
        """
        :param name: Cookie name.
        :type name: str
        :param value: Cookie value.
        :type value: str
        :param url: The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
        :type url: str
        :param domain: Cookie domain.
        :type domain: str
        :param path: Cookie path.
        :type path: str
        :param secure: True if cookie is secure.
        :type secure: bool
        :param httpOnly: True if cookie is http-only.
        :type httpOnly: bool
        :param sameSite: Cookie SameSite type.
        :type sameSite: CookieSameSite
        :param expires: Cookie expiration date, session cookie if not set
        :type expires: TimeSinceEpoch
        """
        super().__init__()
        self.name: str = name
        self.value: str = value
        self.url: Optional[str] = url
        self.domain: Optional[str] = domain
        self.path: Optional[str] = path
        self.secure: Optional[bool] = secure
        self.httpOnly: Optional[bool] = httpOnly
        self.sameSite: Optional[CookieSameSite] = sameSite
        self.expires: Optional[TimeSinceEpoch] = expires


class AuthChallenge(ChromeTypeBase):
    """Authorization challenge for HTTP status code 401 or 407."""
    def __init__(self, origin: str, scheme: str, realm: str, source: Optional[str] = None) -> None:
        """
        :param source: Source of the authentication challenge.
        :type source: str
        :param origin: Origin of the challenger.
        :type origin: str
        :param scheme: The authentication scheme used, such as basic or digest
        :type scheme: str
        :param realm: The realm of the challenge. May be empty.
        :type realm: str
        """
        super().__init__()
        self.source: Optional[str] = source
        self.origin: str = origin
        self.scheme: str = scheme
        self.realm: str = realm


class AuthChallengeResponse(ChromeTypeBase):
    """Response to an AuthChallenge."""
    def __init__(self, response: str, username: Optional[str] = None, password: Optional[str] = None) -> None:
        """
        :param response: The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box.
        :type response: str
        :param username: The username to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type username: str
        :param password: The password to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type password: str
        """
        super().__init__()
        self.response: str = response
        self.username: Optional[str] = username
        self.password: Optional[str] = password


class RequestPattern(ChromeTypeBase):
    """Request pattern for interception."""
    def __init__(self, urlPattern: Optional[str] = None, resourceType: Optional['Page.ResourceType'] = None, interceptionStage: Optional['InterceptionStage'] = None) -> None:
        """
        :param urlPattern: Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*".
        :type urlPattern: str
        :param resourceType: If set, only requests for matching resource types will be intercepted.
        :type resourceType: Page.ResourceType
        :param interceptionStage: Stage at wich to begin intercepting requests. Default is Request.
        :type interceptionStage: InterceptionStage
        """
        super().__init__()
        self.urlPattern: Optional[str] = urlPattern
        self.resourceType: Optional[Page.ResourceType] = resourceType
        self.interceptionStage: Optional[InterceptionStage] = interceptionStage


class SignedExchangeSignature(ChromeTypeBase):
    """Information about a signed exchange signature.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1"""
    def __init__(self, label: str, signature: str, integrity: str, validityUrl: str, date: int, expires: int, certUrl: Optional[str] = None, certSha256: Optional[str] = None, certificates: Optional[List['str']] = None) -> None:
        """
        :param label: Signed exchange signature label.
        :type label: str
        :param signature: The hex string of signed exchange signature.
        :type signature: str
        :param integrity: Signed exchange signature integrity.
        :type integrity: str
        :param certUrl: Signed exchange signature cert Url.
        :type certUrl: str
        :param certSha256: The hex string of signed exchange signature cert sha256.
        :type certSha256: str
        :param validityUrl: Signed exchange signature validity Url.
        :type validityUrl: str
        :param date: Signed exchange signature date.
        :type date: int
        :param expires: Signed exchange signature expires.
        :type expires: int
        :param certificates: The encoded certificates.
        :type certificates: array
        """
        super().__init__()
        self.label: str = label
        self.signature: str = signature
        self.integrity: str = integrity
        self.certUrl: Optional[str] = certUrl
        self.certSha256: Optional[str] = certSha256
        self.validityUrl: str = validityUrl
        self.date: int = date
        self.expires: int = expires
        self.certificates: Optional[List[str]] = certificates


class SignedExchangeHeader(ChromeTypeBase):
    """Information about a signed exchange header.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation"""
    def __init__(self, requestUrl: str, requestMethod: str, responseCode: int, responseHeaders: 'Headers', signatures: List['SignedExchangeSignature']) -> None:
        """
        :param requestUrl: Signed exchange request URL.
        :type requestUrl: str
        :param requestMethod: Signed exchange request method.
        :type requestMethod: str
        :param responseCode: Signed exchange response code.
        :type responseCode: int
        :param responseHeaders: Signed exchange response headers.
        :type responseHeaders: Headers
        :param signatures: Signed exchange response signature.
        :type signatures: array
        """
        super().__init__()
        self.requestUrl: str = requestUrl
        self.requestMethod: str = requestMethod
        self.responseCode: int = responseCode
        self.responseHeaders: Headers = responseHeaders
        self.signatures: List[SignedExchangeSignature] = signatures


class SignedExchangeInfo(ChromeTypeBase):
    """Information about a signed exchange response."""
    def __init__(self, outerResponse: 'Response', header: Optional['SignedExchangeHeader'] = None, securityDetails: Optional['SecurityDetails'] = None, errors: Optional[List['str']] = None) -> None:
        """
        :param outerResponse: The outer response of signed HTTP exchange which was received from network.
        :type outerResponse: Response
        :param header: Information about the signed exchange header.
        :type header: SignedExchangeHeader
        :param securityDetails: Security details for the signed exchange header.
        :type securityDetails: SecurityDetails
        :param errors: Errors occurred while handling the signed exchagne.
        :type errors: array
        """
        super().__init__()
        self.outerResponse: Response = outerResponse
        self.header: Optional[SignedExchangeHeader] = header
        self.securityDetails: Optional[SecurityDetails] = securityDetails
        self.errors: Optional[List[str]] = errors


