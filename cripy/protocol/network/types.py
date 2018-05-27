from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.page import types as Page
from cripy.protocol.security import types as Security

LoaderId = str

RequestId = str

InterceptionId = str

ErrorReason = str

TimeSinceEpoch = float

MonotonicTime = float

ConnectionType = str

CookieSameSite = str

ResourcePriority = str

CertificateTransparencyCompliance = str

BlockedReason = str

InterceptionStage = str


class Headers(ChromeTypeBase):

    def __init__(self,) -> None:
        super().__init__()


class ResourceTiming(ChromeTypeBase):

    def __init__(
        self,
        requestTime: float,
        proxyStart: float,
        proxyEnd: float,
        dnsStart: float,
        dnsEnd: float,
        connectStart: float,
        connectEnd: float,
        sslStart: float,
        sslEnd: float,
        workerStart: float,
        workerReady: float,
        sendStart: float,
        sendEnd: float,
        pushStart: float,
        pushEnd: float,
        receiveHeadersEnd: float,
    ) -> None:
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

    def __init__(
        self,
        url: str,
        method: str,
        headers: "Headers",
        initialPriority: "ResourcePriority",
        referrerPolicy: str,
        postData: Optional[str] = None,
        hasPostData: Optional[bool] = None,
        mixedContentType: Optional["Security.MixedContentType"] = None,
        isLinkPreload: Optional[bool] = None,
    ) -> None:
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

    def __init__(
        self,
        status: str,
        origin: str,
        logDescription: str,
        logId: str,
        timestamp: "TimeSinceEpoch",
        hashAlgorithm: str,
        signatureAlgorithm: str,
        signatureData: str,
    ) -> None:
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

    def __init__(
        self,
        protocol: str,
        keyExchange: str,
        cipher: str,
        certificateId: "Security.CertificateId",
        subjectName: str,
        sanList: List["str"],
        issuer: str,
        validFrom: "TimeSinceEpoch",
        validTo: "TimeSinceEpoch",
        signedCertificateTimestampList: List["SignedCertificateTimestamp"],
        certificateTransparencyCompliance: "CertificateTransparencyCompliance",
        keyExchangeGroup: Optional[str] = None,
        mac: Optional[str] = None,
    ) -> None:
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
        self.signedCertificateTimestampList: List[
            SignedCertificateTimestamp
        ] = signedCertificateTimestampList
        self.certificateTransparencyCompliance: CertificateTransparencyCompliance = certificateTransparencyCompliance


class Response(ChromeTypeBase):

    def __init__(
        self,
        url: str,
        status: int,
        statusText: str,
        headers: "Headers",
        mimeType: str,
        connectionReused: bool,
        connectionId: float,
        encodedDataLength: float,
        securityState: "Security.SecurityState",
        headersText: Optional[str] = None,
        requestHeaders: Optional["Headers"] = None,
        requestHeadersText: Optional[str] = None,
        remoteIPAddress: Optional[str] = None,
        remotePort: Optional[int] = None,
        fromDiskCache: Optional[bool] = None,
        fromServiceWorker: Optional[bool] = None,
        timing: Optional["ResourceTiming"] = None,
        protocol: Optional[str] = None,
        securityDetails: Optional["SecurityDetails"] = None,
    ) -> None:
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

    def __init__(self, headers: "Headers") -> None:
        super().__init__()
        self.headers: Headers = headers


class WebSocketResponse(ChromeTypeBase):

    def __init__(
        self,
        status: int,
        statusText: str,
        headers: "Headers",
        headersText: Optional[str] = None,
        requestHeaders: Optional["Headers"] = None,
        requestHeadersText: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.status: int = status
        self.statusText: str = statusText
        self.headers: Headers = headers
        self.headersText: Optional[str] = headersText
        self.requestHeaders: Optional[Headers] = requestHeaders
        self.requestHeadersText: Optional[str] = requestHeadersText


class WebSocketFrame(ChromeTypeBase):

    def __init__(self, opcode: float, mask: bool, payloadData: str) -> None:
        super().__init__()
        self.opcode: float = opcode
        self.mask: bool = mask
        self.payloadData: str = payloadData


class CachedResource(ChromeTypeBase):

    def __init__(
        self,
        url: str,
        type: "Page.ResourceType",
        bodySize: float,
        response: Optional["Response"] = None,
    ) -> None:
        super().__init__()
        self.url: str = url
        self.type: Page.ResourceType = type
        self.response: Optional[Response] = response
        self.bodySize: float = bodySize


class Initiator(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        stack: Optional["Runtime.StackTrace"] = None,
        url: Optional[str] = None,
        lineNumber: Optional[float] = None,
    ) -> None:
        super().__init__()
        self.type: str = type
        self.stack: Optional[Runtime.StackTrace] = stack
        self.url: Optional[str] = url
        self.lineNumber: Optional[float] = lineNumber


class Cookie(ChromeTypeBase):

    def __init__(
        self,
        name: str,
        value: str,
        domain: str,
        path: str,
        expires: float,
        size: int,
        httpOnly: bool,
        secure: bool,
        session: bool,
        sameSite: Optional["CookieSameSite"] = None,
    ) -> None:
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

    def __init__(
        self,
        name: str,
        value: str,
        url: Optional[str] = None,
        domain: Optional[str] = None,
        path: Optional[str] = None,
        secure: Optional[bool] = None,
        httpOnly: Optional[bool] = None,
        sameSite: Optional["CookieSameSite"] = None,
        expires: Optional["TimeSinceEpoch"] = None,
    ) -> None:
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

    def __init__(
        self, origin: str, scheme: str, realm: str, source: Optional[str] = None
    ) -> None:
        super().__init__()
        self.source: Optional[str] = source
        self.origin: str = origin
        self.scheme: str = scheme
        self.realm: str = realm


class AuthChallengeResponse(ChromeTypeBase):

    def __init__(
        self,
        response: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.response: str = response
        self.username: Optional[str] = username
        self.password: Optional[str] = password


class RequestPattern(ChromeTypeBase):

    def __init__(
        self,
        urlPattern: Optional[str] = None,
        resourceType: Optional["Page.ResourceType"] = None,
        interceptionStage: Optional["InterceptionStage"] = None,
    ) -> None:
        super().__init__()
        self.urlPattern: Optional[str] = urlPattern
        self.resourceType: Optional[Page.ResourceType] = resourceType
        self.interceptionStage: Optional[InterceptionStage] = interceptionStage


class SignedExchangeSignature(ChromeTypeBase):

    def __init__(
        self,
        label: str,
        signature: str,
        integrity: str,
        validityUrl: str,
        date: int,
        expires: int,
        certUrl: Optional[str] = None,
        certSha256: Optional[str] = None,
        certificates: Optional[List["str"]] = None,
    ) -> None:
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

    def __init__(
        self,
        requestUrl: str,
        requestMethod: str,
        responseCode: int,
        responseHeaders: "Headers",
        signatures: List["SignedExchangeSignature"],
    ) -> None:
        super().__init__()
        self.requestUrl: str = requestUrl
        self.requestMethod: str = requestMethod
        self.responseCode: int = responseCode
        self.responseHeaders: Headers = responseHeaders
        self.signatures: List[SignedExchangeSignature] = signatures


class SignedExchangeInfo(ChromeTypeBase):

    def __init__(
        self,
        outerResponse: "Response",
        header: Optional["SignedExchangeHeader"] = None,
        securityDetails: Optional["SecurityDetails"] = None,
        errors: Optional[List["str"]] = None,
    ) -> None:
        super().__init__()
        self.outerResponse: Response = outerResponse
        self.header: Optional[SignedExchangeHeader] = header
        self.securityDetails: Optional[SecurityDetails] = securityDetails
        self.errors: Optional[List[str]] = errors
