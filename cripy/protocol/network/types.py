from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.page import types as Page
from cripy.protocol.security import types as Security

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
        :param float requestTime: Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime.
        :param float proxyStart: Started resolving proxy.
        :param float proxyEnd: Finished resolving proxy.
        :param float dnsStart: Started DNS address resolve.
        :param float dnsEnd: Finished DNS address resolve.
        :param float connectStart: Started connecting to the remote host.
        :param float connectEnd: Connected to the remote host.
        :param float sslStart: Started SSL handshake.
        :param float sslEnd: Finished SSL handshake.
        :param float workerStart: Started running ServiceWorker.
        :param float workerReady: Finished Starting ServiceWorker.
        :param float sendStart: Started sending request.
        :param float sendEnd: Finished sending request.
        :param float pushStart: Time the server started pushing request.
        :param float pushEnd: Time the server finished pushing request.
        :param float receiveHeadersEnd: Finished receiving response headers.
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
        :param str url: Request URL.
        :param str method: HTTP request method.
        :param Headers headers: HTTP request headers.
        :param str postData: HTTP POST request data.
        :param bool hasPostData: True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.
        :param Security.MixedContentType mixedContentType: The mixed content type of the request.
        :param ResourcePriority initialPriority: Priority of the resource request at the time request is sent.
        :param str referrerPolicy: The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/
        :param bool isLinkPreload: Whether is loaded via link preload.
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
        :param str status: Validation status.
        :param str origin: Origin.
        :param str logDescription: Log name / description.
        :param str logId: Log ID.
        :param TimeSinceEpoch timestamp: Issuance date.
        :param str hashAlgorithm: Hash algorithm.
        :param str signatureAlgorithm: Signature algorithm.
        :param str signatureData: Signature data.
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
        :param str protocol: Protocol name (e.g. "TLS 1.2" or "QUIC").
        :param str keyExchange: Key Exchange used by the connection, or the empty string if not applicable.
        :param str keyExchangeGroup: (EC)DH group used by the connection, if applicable.
        :param str cipher: Cipher name.
        :param str mac: TLS MAC. Note that AEAD ciphers do not have separate MACs.
        :param Security.CertificateId certificateId: Certificate ID value.
        :param str subjectName: Certificate subject name.
        :param array sanList: Subject Alternative Name (SAN) DNS names and IP addresses.
        :param str issuer: Name of the issuing CA.
        :param TimeSinceEpoch validFrom: Certificate valid from date.
        :param TimeSinceEpoch validTo: Certificate valid to (expiration) date
        :param array signedCertificateTimestampList: List of signed certificate timestamps (SCTs).
        :param CertificateTransparencyCompliance certificateTransparencyCompliance: Whether the request complied with Certificate Transparency policy
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
        :param str url: Response URL. This URL can be different from CachedResource.url in case of redirect.
        :param int status: HTTP response status code.
        :param str statusText: HTTP response status text.
        :param Headers headers: HTTP response headers.
        :param str headersText: HTTP response headers text.
        :param str mimeType: Resource mimeType as determined by the browser.
        :param Headers requestHeaders: Refined HTTP request headers that were actually transmitted over the network.
        :param str requestHeadersText: HTTP request headers text.
        :param bool connectionReused: Specifies whether physical connection was actually reused for this request.
        :param float connectionId: Physical connection id that was actually used for this request.
        :param str remoteIPAddress: Remote IP address.
        :param int remotePort: Remote port.
        :param bool fromDiskCache: Specifies that the request was served from the disk cache.
        :param bool fromServiceWorker: Specifies that the request was served from the ServiceWorker.
        :param float encodedDataLength: Total number of bytes received for this request so far.
        :param ResourceTiming timing: Timing information for the given request.
        :param str protocol: Protocol used to fetch this request.
        :param Security.SecurityState securityState: Security state of the request resource.
        :param SecurityDetails securityDetails: Security details for the request.
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
        :param Headers headers: HTTP request headers.
        """
        super().__init__()
        self.headers: Headers = headers


class WebSocketResponse(ChromeTypeBase):
    """WebSocket response data."""
    def __init__(self, status: int, statusText: str, headers: 'Headers', headersText: Optional[str] = None, requestHeaders: Optional['Headers'] = None, requestHeadersText: Optional[str] = None) -> None:
        """
        :param int status: HTTP response status code.
        :param str statusText: HTTP response status text.
        :param Headers headers: HTTP response headers.
        :param str headersText: HTTP response headers text.
        :param Headers requestHeaders: HTTP request headers.
        :param str requestHeadersText: HTTP request headers text.
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
        :param float opcode: WebSocket frame opcode.
        :param bool mask: WebSocke frame mask.
        :param str payloadData: WebSocke frame payload data.
        """
        super().__init__()
        self.opcode: float = opcode
        self.mask: bool = mask
        self.payloadData: str = payloadData


class CachedResource(ChromeTypeBase):
    """Information about the cached resource."""
    def __init__(self, url: str, type: 'Page.ResourceType', bodySize: float, response: Optional['Response'] = None) -> None:
        """
        :param str url: Resource URL. This is the url of the original network request.
        :param Page.ResourceType type: Type of this resource.
        :param Response response: Cached response data.
        :param float bodySize: Cached response body size.
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
        :param str type: Type of this initiator.
        :param Runtime.StackTrace stack: Initiator JavaScript stack trace, set for Script only.
        :param str url: Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.
        :param float lineNumber: Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based).
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
        :param str name: Cookie name.
        :param str value: Cookie value.
        :param str domain: Cookie domain.
        :param str path: Cookie path.
        :param float expires: Cookie expiration date as the number of seconds since the UNIX epoch.
        :param int size: Cookie size.
        :param bool httpOnly: True if cookie is http-only.
        :param bool secure: True if cookie is secure.
        :param bool session: True in case of session cookie.
        :param CookieSameSite sameSite: Cookie SameSite type.
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
        :param str name: Cookie name.
        :param str value: Cookie value.
        :param str url: The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
        :param str domain: Cookie domain.
        :param str path: Cookie path.
        :param bool secure: True if cookie is secure.
        :param bool httpOnly: True if cookie is http-only.
        :param CookieSameSite sameSite: Cookie SameSite type.
        :param TimeSinceEpoch expires: Cookie expiration date, session cookie if not set
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
        :param str source: Source of the authentication challenge.
        :param str origin: Origin of the challenger.
        :param str scheme: The authentication scheme used, such as basic or digest
        :param str realm: The realm of the challenge. May be empty.
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
        :param str response: The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box.
        :param str username: The username to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :param str password: The password to provide, possibly empty. Should only be set if response is ProvideCredentials.
        """
        super().__init__()
        self.response: str = response
        self.username: Optional[str] = username
        self.password: Optional[str] = password


class RequestPattern(ChromeTypeBase):
    """Request pattern for interception."""
    def __init__(self, urlPattern: Optional[str] = None, resourceType: Optional['Page.ResourceType'] = None, interceptionStage: Optional['InterceptionStage'] = None) -> None:
        """
        :param str urlPattern: Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*".
        :param Page.ResourceType resourceType: If set, only requests for matching resource types will be intercepted.
        :param InterceptionStage interceptionStage: Stage at wich to begin intercepting requests. Default is Request.
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
        :param str label: Signed exchange signature label.
        :param str signature: The hex string of signed exchange signature.
        :param str integrity: Signed exchange signature integrity.
        :param str certUrl: Signed exchange signature cert Url.
        :param str certSha256: The hex string of signed exchange signature cert sha256.
        :param str validityUrl: Signed exchange signature validity Url.
        :param int date: Signed exchange signature date.
        :param int expires: Signed exchange signature expires.
        :param array certificates: The encoded certificates.
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
        :param str requestUrl: Signed exchange request URL.
        :param str requestMethod: Signed exchange request method.
        :param int responseCode: Signed exchange response code.
        :param Headers responseHeaders: Signed exchange response headers.
        :param array signatures: Signed exchange response signature.
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
        :param Response outerResponse: The outer response of signed HTTP exchange which was received from network.
        :param SignedExchangeHeader header: Information about the signed exchange header.
        :param SecurityDetails securityDetails: Security details for the signed exchange header.
        :param array errors: Errors occurred while handling the signed exchagne.
        """
        super().__init__()
        self.outerResponse: Response = outerResponse
        self.header: Optional[SignedExchangeHeader] = header
        self.securityDetails: Optional[SecurityDetails] = securityDetails
        self.errors: Optional[List[str]] = errors


