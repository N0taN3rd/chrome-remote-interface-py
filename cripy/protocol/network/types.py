from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.security import types as Security
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.page import types as Page

TimeSinceEpoch = TypeVar("TimeSinceEpoch", float, float) # UTC time in seconds, counted from January 1, 1970.

ResourcePriority = TypeVar("ResourcePriority", str, str) # Loading priority of a resource request.

RequestId = TypeVar("RequestId", str, str) # Unique request identifier.

MonotonicTime = TypeVar("MonotonicTime", float, float) # Monotonically increasing time in seconds since an arbitrary point in the past.

LoaderId = TypeVar("LoaderId", str, str) # Unique loader identifier.

InterceptionStage = TypeVar("InterceptionStage", str, str) # Stages of the interception to begin intercepting. Request will intercept before the request is sent. Response will intercept after the response is received.

InterceptionId = TypeVar("InterceptionId", str, str) # Unique intercepted request identifier.

ErrorReason = TypeVar("ErrorReason", str, str) # Network level fetch failure reason.

CookieSameSite = TypeVar("CookieSameSite", str, str) # Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies

ConnectionType = TypeVar("ConnectionType", str, str) # The underlying connection technology that the browser is supposedly using.

CertificateTransparencyCompliance = TypeVar("CertificateTransparencyCompliance", str, str) # Whether the request complied with Certificate Transparency policy.

BlockedReason = TypeVar("BlockedReason", str, str) # The reason why request was blocked.


class WebSocketResponse(ProtocolType):
    """
    WebSocket response data.
    """

    def __init__(self, status: int, statusText: str, headers: Union['Headers', dict], headersText: Optional[str] = None, requestHeaders: Optional[Union['Headers', dict]] = None, requestHeadersText: Optional[str] = None) -> None:
        """
        :param status: HTTP response status code.
        :type status: int
        :param statusText: HTTP response status text.
        :type statusText: str
        :param headers: HTTP response headers.
        :type headers: dict
        :param headersText: HTTP response headers text.
        :type headersText: Optional[str]
        :param requestHeaders: HTTP request headers.
        :type requestHeaders: Optional[dict]
        :param requestHeadersText: HTTP request headers text.
        :type requestHeadersText: Optional[str]
        """
        super().__init__()
        self.status = status
        self.statusText = statusText
        self.headers = Headers.safe_create(headers)
        self.headersText = headersText
        self.requestHeaders = Headers.safe_create(requestHeaders)
        self.requestHeadersText = requestHeadersText

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketResponse']:
        if init is not None:
            return WebSocketResponse(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketResponse']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketResponse(**it))
            return list_of_self
        else:
            return init


class WebSocketRequest(ProtocolType):
    """
    WebSocket request data.
    """

    def __init__(self, headers: Union['Headers', dict]) -> None:
        """
        :param headers: HTTP request headers.
        :type headers: dict
        """
        super().__init__()
        self.headers = Headers.safe_create(headers)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketRequest']:
        if init is not None:
            return WebSocketRequest(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketRequest']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketRequest(**it))
            return list_of_self
        else:
            return init


class WebSocketFrame(ProtocolType):
    """
    WebSocket frame data.
    """

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
        self.opcode = opcode
        self.mask = mask
        self.payloadData = payloadData

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketFrame']:
        if init is not None:
            return WebSocketFrame(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketFrame']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrame(**it))
            return list_of_self
        else:
            return init


class SignedExchangeSignature(ProtocolType):
    """
    Information about a signed exchange signature.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    def __init__(self, label: str, signature: str, integrity: str, validityUrl: str, date: int, expires: int, certUrl: Optional[str] = None, certSha256: Optional[str] = None, certificates: Optional[List[str]] = None) -> None:
        """
        :param label: Signed exchange signature label.
        :type label: str
        :param signature: The hex string of signed exchange signature.
        :type signature: str
        :param integrity: Signed exchange signature integrity.
        :type integrity: str
        :param certUrl: Signed exchange signature cert Url.
        :type certUrl: Optional[str]
        :param certSha256: The hex string of signed exchange signature cert sha256.
        :type certSha256: Optional[str]
        :param validityUrl: Signed exchange signature validity Url.
        :type validityUrl: str
        :param date: Signed exchange signature date.
        :type date: int
        :param expires: Signed exchange signature expires.
        :type expires: int
        :param certificates: The encoded certificates.
        :type certificates: Optional[List[str]]
        """
        super().__init__()
        self.label = label
        self.signature = signature
        self.integrity = integrity
        self.certUrl = certUrl
        self.certSha256 = certSha256
        self.validityUrl = validityUrl
        self.date = date
        self.expires = expires
        self.certificates = certificates

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SignedExchangeSignature']:
        if init is not None:
            return SignedExchangeSignature(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SignedExchangeSignature']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeSignature(**it))
            return list_of_self
        else:
            return init


class SignedExchangeInfo(ProtocolType):
    """
    Information about a signed exchange response.
    """

    def __init__(self, outerResponse: Union['Response', dict], header: Optional[Union['SignedExchangeHeader', dict]] = None, securityDetails: Optional[Union['SecurityDetails', dict]] = None, errors: Optional[List[str]] = None) -> None:
        """
        :param outerResponse: The outer response of signed HTTP exchange which was received from network.
        :type outerResponse: dict
        :param header: Information about the signed exchange header.
        :type header: Optional[dict]
        :param securityDetails: Security details for the signed exchange header.
        :type securityDetails: Optional[dict]
        :param errors: Errors occurred while handling the signed exchagne.
        :type errors: Optional[List[str]]
        """
        super().__init__()
        self.outerResponse = Response.safe_create(outerResponse)
        self.header = SignedExchangeHeader.safe_create(header)
        self.securityDetails = SecurityDetails.safe_create(securityDetails)
        self.errors = errors

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SignedExchangeInfo']:
        if init is not None:
            return SignedExchangeInfo(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SignedExchangeInfo']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeInfo(**it))
            return list_of_self
        else:
            return init


class SignedExchangeHeader(ProtocolType):
    """
    Information about a signed exchange header.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    def __init__(self, requestUrl: str, requestMethod: str, responseCode: int, responseHeaders: Union['Headers', dict], signatures: List[Union['SignedExchangeSignature', dict]]) -> None:
        """
        :param requestUrl: Signed exchange request URL.
        :type requestUrl: str
        :param requestMethod: Signed exchange request method.
        :type requestMethod: str
        :param responseCode: Signed exchange response code.
        :type responseCode: int
        :param responseHeaders: Signed exchange response headers.
        :type responseHeaders: dict
        :param signatures: Signed exchange response signature.
        :type signatures: List[dict]
        """
        super().__init__()
        self.requestUrl = requestUrl
        self.requestMethod = requestMethod
        self.responseCode = responseCode
        self.responseHeaders = Headers.safe_create(responseHeaders)
        self.signatures = SignedExchangeSignature.safe_create_from_list(signatures)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SignedExchangeHeader']:
        if init is not None:
            return SignedExchangeHeader(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SignedExchangeHeader']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeHeader(**it))
            return list_of_self
        else:
            return init


class SignedCertificateTimestamp(ProtocolType):
    """
    Details of a signed certificate timestamp (SCT).
    """

    def __init__(self, status: str, origin: str, logDescription: str, logId: str, timestamp: TimeSinceEpoch, hashAlgorithm: str, signatureAlgorithm: str, signatureData: str) -> None:
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
        :type timestamp: float
        :param hashAlgorithm: Hash algorithm.
        :type hashAlgorithm: str
        :param signatureAlgorithm: Signature algorithm.
        :type signatureAlgorithm: str
        :param signatureData: Signature data.
        :type signatureData: str
        """
        super().__init__()
        self.status = status
        self.origin = origin
        self.logDescription = logDescription
        self.logId = logId
        self.timestamp = timestamp
        self.hashAlgorithm = hashAlgorithm
        self.signatureAlgorithm = signatureAlgorithm
        self.signatureData = signatureData

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SignedCertificateTimestamp']:
        if init is not None:
            return SignedCertificateTimestamp(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SignedCertificateTimestamp']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedCertificateTimestamp(**it))
            return list_of_self
        else:
            return init


class SecurityDetails(ProtocolType):
    """
    Security details about a request.
    """

    def __init__(self, protocol: str, keyExchange: str, cipher: str, certificateId: Security.CertificateId, subjectName: str, sanList: List[str], issuer: str, validFrom: TimeSinceEpoch, validTo: TimeSinceEpoch, signedCertificateTimestampList: List[Union['SignedCertificateTimestamp', dict]], certificateTransparencyCompliance: CertificateTransparencyCompliance, keyExchangeGroup: Optional[str] = None, mac: Optional[str] = None) -> None:
        """
        :param protocol: Protocol name (e.g. "TLS 1.2" or "QUIC").
        :type protocol: str
        :param keyExchange: Key Exchange used by the connection, or the empty string if not applicable.
        :type keyExchange: str
        :param keyExchangeGroup: (EC)DH group used by the connection, if applicable.
        :type keyExchangeGroup: Optional[str]
        :param cipher: Cipher name.
        :type cipher: str
        :param mac: TLS MAC. Note that AEAD ciphers do not have separate MACs.
        :type mac: Optional[str]
        :param certificateId: Certificate ID value.
        :type certificateId: int
        :param subjectName: Certificate subject name.
        :type subjectName: str
        :param sanList: Subject Alternative Name (SAN) DNS names and IP addresses.
        :type sanList: List[str]
        :param issuer: Name of the issuing CA.
        :type issuer: str
        :param validFrom: Certificate valid from date.
        :type validFrom: float
        :param validTo: Certificate valid to (expiration) date
        :type validTo: float
        :param signedCertificateTimestampList: List of signed certificate timestamps (SCTs).
        :type signedCertificateTimestampList: List[dict]
        :param certificateTransparencyCompliance: Whether the request complied with Certificate Transparency policy
        :type certificateTransparencyCompliance: str
        """
        super().__init__()
        self.protocol = protocol
        self.keyExchange = keyExchange
        self.keyExchangeGroup = keyExchangeGroup
        self.cipher = cipher
        self.mac = mac
        self.certificateId = certificateId
        self.subjectName = subjectName
        self.sanList = sanList
        self.issuer = issuer
        self.validFrom = validFrom
        self.validTo = validTo
        self.signedCertificateTimestampList = SignedCertificateTimestamp.safe_create_from_list(signedCertificateTimestampList)
        self.certificateTransparencyCompliance = certificateTransparencyCompliance

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SecurityDetails']:
        if init is not None:
            return SecurityDetails(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SecurityDetails']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityDetails(**it))
            return list_of_self
        else:
            return init


class Response(ProtocolType):
    """
    HTTP response data.
    """

    def __init__(self, url: str, status: int, statusText: str, headers: Union['Headers', dict], mimeType: str, connectionReused: bool, connectionId: float, encodedDataLength: float, securityState: Security.SecurityState, headersText: Optional[str] = None, requestHeaders: Optional[Union['Headers', dict]] = None, requestHeadersText: Optional[str] = None, remoteIPAddress: Optional[str] = None, remotePort: Optional[int] = None, fromDiskCache: Optional[bool] = None, fromServiceWorker: Optional[bool] = None, timing: Optional[Union['ResourceTiming', dict]] = None, protocol: Optional[str] = None, securityDetails: Optional[Union['SecurityDetails', dict]] = None) -> None:
        """
        :param url: Response URL. This URL can be different from CachedResource.url in case of redirect.
        :type url: str
        :param status: HTTP response status code.
        :type status: int
        :param statusText: HTTP response status text.
        :type statusText: str
        :param headers: HTTP response headers.
        :type headers: dict
        :param headersText: HTTP response headers text.
        :type headersText: Optional[str]
        :param mimeType: Resource mimeType as determined by the browser.
        :type mimeType: str
        :param requestHeaders: Refined HTTP request headers that were actually transmitted over the network.
        :type requestHeaders: Optional[dict]
        :param requestHeadersText: HTTP request headers text.
        :type requestHeadersText: Optional[str]
        :param connectionReused: Specifies whether physical connection was actually reused for this request.
        :type connectionReused: bool
        :param connectionId: Physical connection id that was actually used for this request.
        :type connectionId: float
        :param remoteIPAddress: Remote IP address.
        :type remoteIPAddress: Optional[str]
        :param remotePort: Remote port.
        :type remotePort: Optional[int]
        :param fromDiskCache: Specifies that the request was served from the disk cache.
        :type fromDiskCache: Optional[bool]
        :param fromServiceWorker: Specifies that the request was served from the ServiceWorker.
        :type fromServiceWorker: Optional[bool]
        :param encodedDataLength: Total number of bytes received for this request so far.
        :type encodedDataLength: float
        :param timing: Timing information for the given request.
        :type timing: Optional[dict]
        :param protocol: Protocol used to fetch this request.
        :type protocol: Optional[str]
        :param securityState: Security state of the request resource.
        :type securityState: str
        :param securityDetails: Security details for the request.
        :type securityDetails: Optional[dict]
        """
        super().__init__()
        self.url = url
        self.status = status
        self.statusText = statusText
        self.headers = Headers.safe_create(headers)
        self.headersText = headersText
        self.mimeType = mimeType
        self.requestHeaders = Headers.safe_create(requestHeaders)
        self.requestHeadersText = requestHeadersText
        self.connectionReused = connectionReused
        self.connectionId = connectionId
        self.remoteIPAddress = remoteIPAddress
        self.remotePort = remotePort
        self.fromDiskCache = fromDiskCache
        self.fromServiceWorker = fromServiceWorker
        self.encodedDataLength = encodedDataLength
        self.timing = ResourceTiming.safe_create(timing)
        self.protocol = protocol
        self.securityState = securityState
        self.securityDetails = SecurityDetails.safe_create(securityDetails)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Response']:
        if init is not None:
            return Response(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Response']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Response(**it))
            return list_of_self
        else:
            return init


class ResourceTiming(ProtocolType):
    """
    Timing information for the request.
    """

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
        self.requestTime = requestTime
        self.proxyStart = proxyStart
        self.proxyEnd = proxyEnd
        self.dnsStart = dnsStart
        self.dnsEnd = dnsEnd
        self.connectStart = connectStart
        self.connectEnd = connectEnd
        self.sslStart = sslStart
        self.sslEnd = sslEnd
        self.workerStart = workerStart
        self.workerReady = workerReady
        self.sendStart = sendStart
        self.sendEnd = sendEnd
        self.pushStart = pushStart
        self.pushEnd = pushEnd
        self.receiveHeadersEnd = receiveHeadersEnd

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ResourceTiming']:
        if init is not None:
            return ResourceTiming(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ResourceTiming']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResourceTiming(**it))
            return list_of_self
        else:
            return init


class RequestPattern(ProtocolType):
    """
    Request pattern for interception.
    """

    def __init__(self, urlPattern: Optional[str] = None, resourceType: Optional[Page.ResourceType] = None, interceptionStage: Optional[InterceptionStage] = None) -> None:
        """
        :param urlPattern: Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*".
        :type urlPattern: Optional[str]
        :param resourceType: If set, only requests for matching resource types will be intercepted.
        :type resourceType: Optional[str]
        :param interceptionStage: Stage at wich to begin intercepting requests. Default is Request.
        :type interceptionStage: Optional[str]
        """
        super().__init__()
        self.urlPattern = urlPattern
        self.resourceType = resourceType
        self.interceptionStage = interceptionStage

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RequestPattern']:
        if init is not None:
            return RequestPattern(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RequestPattern']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestPattern(**it))
            return list_of_self
        else:
            return init


class Request(ProtocolType):
    """
    HTTP request data.
    """

    def __init__(self, url: str, method: str, headers: Union['Headers', dict], initialPriority: ResourcePriority, referrerPolicy: str, postData: Optional[str] = None, hasPostData: Optional[bool] = None, mixedContentType: Optional[Security.MixedContentType] = None, isLinkPreload: Optional[bool] = None) -> None:
        """
        :param url: Request URL.
        :type url: str
        :param method: HTTP request method.
        :type method: str
        :param headers: HTTP request headers.
        :type headers: dict
        :param postData: HTTP POST request data.
        :type postData: Optional[str]
        :param hasPostData: True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long.
        :type hasPostData: Optional[bool]
        :param mixedContentType: The mixed content type of the request.
        :type mixedContentType: Optional[str]
        :param initialPriority: Priority of the resource request at the time request is sent.
        :type initialPriority: str
        :param referrerPolicy: The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/
        :type referrerPolicy: str
        :param isLinkPreload: Whether is loaded via link preload.
        :type isLinkPreload: Optional[bool]
        """
        super().__init__()
        self.url = url
        self.method = method
        self.headers = Headers.safe_create(headers)
        self.postData = postData
        self.hasPostData = hasPostData
        self.mixedContentType = mixedContentType
        self.initialPriority = initialPriority
        self.referrerPolicy = referrerPolicy
        self.isLinkPreload = isLinkPreload

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Request']:
        if init is not None:
            return Request(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Request']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Request(**it))
            return list_of_self
        else:
            return init


class Initiator(ProtocolType):
    """
    Information about the request initiator.
    """

    def __init__(self, type: str, stack: Optional[Union['Runtime.StackTrace', dict]] = None, url: Optional[str] = None, lineNumber: Optional[float] = None) -> None:
        """
        :param type: Type of this initiator.
        :type type: str
        :param stack: Initiator JavaScript stack trace, set for Script only.
        :type stack: Optional[dict]
        :param url: Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type.
        :type url: Optional[str]
        :param lineNumber: Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based).
        :type lineNumber: Optional[float]
        """
        super().__init__()
        self.type = type
        self.stack = Runtime.StackTrace.safe_create(stack)
        self.url = url
        self.lineNumber = lineNumber

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Initiator']:
        if init is not None:
            return Initiator(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Initiator']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Initiator(**it))
            return list_of_self
        else:
            return init


class Headers(ProtocolType, dict):
    """
    Request / response headers as keys / values of JSON object.
    """

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Headers']:
        if init is not None:
            return Headers(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Headers']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Headers(**it))
            return list_of_self
        else:
            return init


class CookieParam(ProtocolType):
    """
    Cookie parameter object
    """

    def __init__(self, name: str, value: str, url: Optional[str] = None, domain: Optional[str] = None, path: Optional[str] = None, secure: Optional[bool] = None, httpOnly: Optional[bool] = None, sameSite: Optional[CookieSameSite] = None, expires: Optional[TimeSinceEpoch] = None) -> None:
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
        super().__init__()
        self.name = name
        self.value = value
        self.url = url
        self.domain = domain
        self.path = path
        self.secure = secure
        self.httpOnly = httpOnly
        self.sameSite = sameSite
        self.expires = expires

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CookieParam']:
        if init is not None:
            return CookieParam(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CookieParam']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CookieParam(**it))
            return list_of_self
        else:
            return init


class Cookie(ProtocolType):
    """
    Cookie object
    """

    def __init__(self, name: str, value: str, domain: str, path: str, expires: float, size: int, httpOnly: bool, secure: bool, session: bool, sameSite: Optional[CookieSameSite] = None) -> None:
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
        :type sameSite: Optional[str]
        """
        super().__init__()
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.expires = expires
        self.size = size
        self.httpOnly = httpOnly
        self.secure = secure
        self.session = session
        self.sameSite = sameSite

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['Cookie']:
        if init is not None:
            return Cookie(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Cookie']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Cookie(**it))
            return list_of_self
        else:
            return init


class CachedResource(ProtocolType):
    """
    Information about the cached resource.
    """

    def __init__(self, url: str, type: Page.ResourceType, bodySize: float, response: Optional[Union['Response', dict]] = None) -> None:
        """
        :param url: Resource URL. This is the url of the original network request.
        :type url: str
        :param type: Type of this resource.
        :type type: str
        :param response: Cached response data.
        :type response: Optional[dict]
        :param bodySize: Cached response body size.
        :type bodySize: float
        """
        super().__init__()
        self.url = url
        self.type = type
        self.response = Response.safe_create(response)
        self.bodySize = bodySize

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['CachedResource']:
        if init is not None:
            return CachedResource(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['CachedResource']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CachedResource(**it))
            return list_of_self
        else:
            return init


class AuthChallengeResponse(ProtocolType):
    """
    Response to an AuthChallenge.
    """

    def __init__(self, response: str, username: Optional[str] = None, password: Optional[str] = None) -> None:
        """
        :param response: The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box.
        :type response: str
        :param username: The username to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type username: Optional[str]
        :param password: The password to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type password: Optional[str]
        """
        super().__init__()
        self.response = response
        self.username = username
        self.password = password

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AuthChallengeResponse']:
        if init is not None:
            return AuthChallengeResponse(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AuthChallengeResponse']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AuthChallengeResponse(**it))
            return list_of_self
        else:
            return init


class AuthChallenge(ProtocolType):
    """
    Authorization challenge for HTTP status code 401 or 407.
    """

    def __init__(self, origin: str, scheme: str, realm: str, source: Optional[str] = None) -> None:
        """
        :param source: Source of the authentication challenge.
        :type source: Optional[str]
        :param origin: Origin of the challenger.
        :type origin: str
        :param scheme: The authentication scheme used, such as basic or digest
        :type scheme: str
        :param realm: The realm of the challenge. May be empty.
        :type realm: str
        """
        super().__init__()
        self.source = source
        self.origin = origin
        self.scheme = scheme
        self.realm = realm

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AuthChallenge']:
        if init is not None:
            return AuthChallenge(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AuthChallenge']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AuthChallenge(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "WebSocketResponse": WebSocketResponse,
    "WebSocketRequest": WebSocketRequest,
    "WebSocketFrame": WebSocketFrame,
    "SignedExchangeSignature": SignedExchangeSignature,
    "SignedExchangeInfo": SignedExchangeInfo,
    "SignedExchangeHeader": SignedExchangeHeader,
    "SignedCertificateTimestamp": SignedCertificateTimestamp,
    "SecurityDetails": SecurityDetails,
    "Response": Response,
    "ResourceTiming": ResourceTiming,
    "RequestPattern": RequestPattern,
    "Request": Request,
    "Initiator": Initiator,
    "Headers": Headers,
    "CookieParam": CookieParam,
    "Cookie": Cookie,
    "CachedResource": CachedResource,
    "AuthChallengeResponse": AuthChallengeResponse,
    "AuthChallenge": AuthChallenge,
}
