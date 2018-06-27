from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.security import types as Security
from cripy.gevent.protocol.runtime import types as Runtime

__all__ = [
    "WebSocketResponse",
    "WebSocketRequest",
    "WebSocketFrame",
    "SignedExchangeSignature",
    "SignedExchangeInfo",
    "SignedExchangeHeader",
    "SignedCertificateTimestamp",
    "SecurityDetails",
    "Response",
    "ResourceTiming",
    "RequestPattern",
    "Request",
    "Initiator",
    "Headers",
    "CookieParam",
    "Cookie",
    "CachedResource",
    "AuthChallengeResponse",
    "AuthChallenge",
    "NETWORK_TYPE_TO_OBJECT"
]


class WebSocketResponse(object):
    """
    WebSocket response data.
    """

    __slots__ = ["status", "statusText", "headers", "headersText", "requestHeaders", "requestHeadersText"]

    def __init__(self, status, statusText, headers, headersText=None, requestHeaders=None, requestHeadersText=None):
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
        super(WebSocketResponse, self).__init__()
        self.status = status
        self.statusText = statusText
        self.headers = Headers.safe_create(headers)
        self.headersText = headersText
        self.requestHeaders = Headers.safe_create(requestHeaders)
        self.requestHeadersText = requestHeadersText

    def __repr__(self):
        repr_args = []
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        if self.statusText is not None:
            repr_args.append("statusText={!r}".format(self.statusText))
        if self.headers is not None:
            repr_args.append("headers={!r}".format(self.headers))
        if self.headersText is not None:
            repr_args.append("headersText={!r}".format(self.headersText))
        if self.requestHeaders is not None:
            repr_args.append("requestHeaders={!r}".format(self.requestHeaders))
        if self.requestHeadersText is not None:
            repr_args.append("requestHeadersText={!r}".format(self.requestHeadersText))
        return "WebSocketResponse(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create WebSocketResponse from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketResponse
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketResponse if creation did not fail
        :rtype: Optional[Union[dict, WebSocketResponse]]
        """
        if init is not None:
            try:
                ourselves = WebSocketResponse(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list WebSocketResponses from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketResponse instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketResponse instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketResponse]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketResponse.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketRequest(object):
    """
    WebSocket request data.
    """

    __slots__ = ["headers"]

    def __init__(self, headers):
        """
        :param headers: HTTP request headers.
        :type headers: dict
        """
        super(WebSocketRequest, self).__init__()
        self.headers = Headers.safe_create(headers)

    def __repr__(self):
        repr_args = []
        if self.headers is not None:
            repr_args.append("headers={!r}".format(self.headers))
        return "WebSocketRequest(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create WebSocketRequest from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketRequest
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketRequest if creation did not fail
        :rtype: Optional[Union[dict, WebSocketRequest]]
        """
        if init is not None:
            try:
                ourselves = WebSocketRequest(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list WebSocketRequests from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketRequest instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketRequest instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketRequest]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketRequest.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketFrame(object):
    """
    WebSocket frame data.
    """

    __slots__ = ["opcode", "mask", "payloadData"]

    def __init__(self, opcode, mask, payloadData):
        """
        :param opcode: WebSocket frame opcode.
        :type opcode: float
        :param mask: WebSocke frame mask.
        :type mask: bool
        :param payloadData: WebSocke frame payload data.
        :type payloadData: str
        """
        super(WebSocketFrame, self).__init__()
        self.opcode = opcode
        self.mask = mask
        self.payloadData = payloadData

    def __repr__(self):
        repr_args = []
        if self.opcode is not None:
            repr_args.append("opcode={!r}".format(self.opcode))
        if self.mask is not None:
            repr_args.append("mask={!r}".format(self.mask))
        if self.payloadData is not None:
            repr_args.append("payloadData={!r}".format(self.payloadData))
        return "WebSocketFrame(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create WebSocketFrame from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketFrame
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketFrame if creation did not fail
        :rtype: Optional[Union[dict, WebSocketFrame]]
        """
        if init is not None:
            try:
                ourselves = WebSocketFrame(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list WebSocketFrames from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketFrame instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketFrame instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketFrame]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrame.safe_create(it))
            return list_of_self
        else:
            return init


class SignedExchangeSignature(object):
    """
    Information about a signed exchange signature.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1
    """

    __slots__ = ["label", "integrity", "certUrl", "validityUrl", "date", "expires"]

    def __init__(self, label, integrity, certUrl, validityUrl, date, expires):
        """
        :param label: Signed exchange signature label.
        :type label: str
        :param integrity: Signed exchange signature integrity.
        :type integrity: str
        :param certUrl: Signed exchange signature cert Url.
        :type certUrl: str
        :param validityUrl: Signed exchange signature validity Url.
        :type validityUrl: str
        :param date: Signed exchange signature date.
        :type date: int
        :param expires: Signed exchange signature expires.
        :type expires: int
        """
        super(SignedExchangeSignature, self).__init__()
        self.label = label
        self.integrity = integrity
        self.certUrl = certUrl
        self.validityUrl = validityUrl
        self.date = date
        self.expires = expires

    def __repr__(self):
        repr_args = []
        if self.label is not None:
            repr_args.append("label={!r}".format(self.label))
        if self.integrity is not None:
            repr_args.append("integrity={!r}".format(self.integrity))
        if self.certUrl is not None:
            repr_args.append("certUrl={!r}".format(self.certUrl))
        if self.validityUrl is not None:
            repr_args.append("validityUrl={!r}".format(self.validityUrl))
        if self.date is not None:
            repr_args.append("date={!r}".format(self.date))
        if self.expires is not None:
            repr_args.append("expires={!r}".format(self.expires))
        return "SignedExchangeSignature(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SignedExchangeSignature from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SignedExchangeSignature
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SignedExchangeSignature if creation did not fail
        :rtype: Optional[Union[dict, SignedExchangeSignature]]
        """
        if init is not None:
            try:
                ourselves = SignedExchangeSignature(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SignedExchangeSignatures from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SignedExchangeSignature instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SignedExchangeSignature instances if creation did not fail
        :rtype: Optional[List[Union[dict, SignedExchangeSignature]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeSignature.safe_create(it))
            return list_of_self
        else:
            return init


class SignedExchangeInfo(object):
    """
    Information about a signed exchange response.
    """

    __slots__ = ["outerResponse", "header", "securityDetails", "errors"]

    def __init__(self, outerResponse, header=None, securityDetails=None, errors=None):
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
        super(SignedExchangeInfo, self).__init__()
        self.outerResponse = Response.safe_create(outerResponse)
        self.header = SignedExchangeHeader.safe_create(header)
        self.securityDetails = SecurityDetails.safe_create(securityDetails)
        self.errors = errors

    def __repr__(self):
        repr_args = []
        if self.outerResponse is not None:
            repr_args.append("outerResponse={!r}".format(self.outerResponse))
        if self.header is not None:
            repr_args.append("header={!r}".format(self.header))
        if self.securityDetails is not None:
            repr_args.append("securityDetails={!r}".format(self.securityDetails))
        if self.errors is not None:
            repr_args.append("errors={!r}".format(self.errors))
        return "SignedExchangeInfo(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SignedExchangeInfo from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SignedExchangeInfo
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SignedExchangeInfo if creation did not fail
        :rtype: Optional[Union[dict, SignedExchangeInfo]]
        """
        if init is not None:
            try:
                ourselves = SignedExchangeInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SignedExchangeInfos from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SignedExchangeInfo instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SignedExchangeInfo instances if creation did not fail
        :rtype: Optional[List[Union[dict, SignedExchangeInfo]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeInfo.safe_create(it))
            return list_of_self
        else:
            return init


class SignedExchangeHeader(object):
    """
    Information about a signed exchange header.
https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation
    """

    __slots__ = ["requestUrl", "requestMethod", "responseCode", "responseHeaders", "signatures"]

    def __init__(self, requestUrl, requestMethod, responseCode, responseHeaders, signatures):
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
        super(SignedExchangeHeader, self).__init__()
        self.requestUrl = requestUrl
        self.requestMethod = requestMethod
        self.responseCode = responseCode
        self.responseHeaders = Headers.safe_create(responseHeaders)
        self.signatures = SignedExchangeSignature.safe_create_from_list(signatures)

    def __repr__(self):
        repr_args = []
        if self.requestUrl is not None:
            repr_args.append("requestUrl={!r}".format(self.requestUrl))
        if self.requestMethod is not None:
            repr_args.append("requestMethod={!r}".format(self.requestMethod))
        if self.responseCode is not None:
            repr_args.append("responseCode={!r}".format(self.responseCode))
        if self.responseHeaders is not None:
            repr_args.append("responseHeaders={!r}".format(self.responseHeaders))
        if self.signatures is not None:
            repr_args.append("signatures={!r}".format(self.signatures))
        return "SignedExchangeHeader(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SignedExchangeHeader from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SignedExchangeHeader
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SignedExchangeHeader if creation did not fail
        :rtype: Optional[Union[dict, SignedExchangeHeader]]
        """
        if init is not None:
            try:
                ourselves = SignedExchangeHeader(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SignedExchangeHeaders from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SignedExchangeHeader instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SignedExchangeHeader instances if creation did not fail
        :rtype: Optional[List[Union[dict, SignedExchangeHeader]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeHeader.safe_create(it))
            return list_of_self
        else:
            return init


class SignedCertificateTimestamp(object):
    """
    Details of a signed certificate timestamp (SCT).
    """

    __slots__ = ["status", "origin", "logDescription", "logId", "timestamp", "hashAlgorithm", "signatureAlgorithm", "signatureData"]

    def __init__(self, status, origin, logDescription, logId, timestamp, hashAlgorithm, signatureAlgorithm, signatureData):
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
        super(SignedCertificateTimestamp, self).__init__()
        self.status = status
        self.origin = origin
        self.logDescription = logDescription
        self.logId = logId
        self.timestamp = timestamp
        self.hashAlgorithm = hashAlgorithm
        self.signatureAlgorithm = signatureAlgorithm
        self.signatureData = signatureData

    def __repr__(self):
        repr_args = []
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.logDescription is not None:
            repr_args.append("logDescription={!r}".format(self.logDescription))
        if self.logId is not None:
            repr_args.append("logId={!r}".format(self.logId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.hashAlgorithm is not None:
            repr_args.append("hashAlgorithm={!r}".format(self.hashAlgorithm))
        if self.signatureAlgorithm is not None:
            repr_args.append("signatureAlgorithm={!r}".format(self.signatureAlgorithm))
        if self.signatureData is not None:
            repr_args.append("signatureData={!r}".format(self.signatureData))
        return "SignedCertificateTimestamp(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SignedCertificateTimestamp from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SignedCertificateTimestamp
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SignedCertificateTimestamp if creation did not fail
        :rtype: Optional[Union[dict, SignedCertificateTimestamp]]
        """
        if init is not None:
            try:
                ourselves = SignedCertificateTimestamp(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SignedCertificateTimestamps from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SignedCertificateTimestamp instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SignedCertificateTimestamp instances if creation did not fail
        :rtype: Optional[List[Union[dict, SignedCertificateTimestamp]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedCertificateTimestamp.safe_create(it))
            return list_of_self
        else:
            return init


class SecurityDetails(object):
    """
    Security details about a request.
    """

    __slots__ = ["protocol", "keyExchange", "keyExchangeGroup", "cipher", "mac", "certificateId", "subjectName", "sanList", "issuer", "validFrom", "validTo", "signedCertificateTimestampList", "certificateTransparencyCompliance"]

    def __init__(self, protocol, keyExchange, cipher, certificateId, subjectName, sanList, issuer, validFrom, validTo, signedCertificateTimestampList, certificateTransparencyCompliance, keyExchangeGroup=None, mac=None):
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
        super(SecurityDetails, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.protocol is not None:
            repr_args.append("protocol={!r}".format(self.protocol))
        if self.keyExchange is not None:
            repr_args.append("keyExchange={!r}".format(self.keyExchange))
        if self.keyExchangeGroup is not None:
            repr_args.append("keyExchangeGroup={!r}".format(self.keyExchangeGroup))
        if self.cipher is not None:
            repr_args.append("cipher={!r}".format(self.cipher))
        if self.mac is not None:
            repr_args.append("mac={!r}".format(self.mac))
        if self.certificateId is not None:
            repr_args.append("certificateId={!r}".format(self.certificateId))
        if self.subjectName is not None:
            repr_args.append("subjectName={!r}".format(self.subjectName))
        if self.sanList is not None:
            repr_args.append("sanList={!r}".format(self.sanList))
        if self.issuer is not None:
            repr_args.append("issuer={!r}".format(self.issuer))
        if self.validFrom is not None:
            repr_args.append("validFrom={!r}".format(self.validFrom))
        if self.validTo is not None:
            repr_args.append("validTo={!r}".format(self.validTo))
        if self.signedCertificateTimestampList is not None:
            repr_args.append("signedCertificateTimestampList={!r}".format(self.signedCertificateTimestampList))
        if self.certificateTransparencyCompliance is not None:
            repr_args.append("certificateTransparencyCompliance={!r}".format(self.certificateTransparencyCompliance))
        return "SecurityDetails(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create SecurityDetails from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SecurityDetails
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SecurityDetails if creation did not fail
        :rtype: Optional[Union[dict, SecurityDetails]]
        """
        if init is not None:
            try:
                ourselves = SecurityDetails(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list SecurityDetailss from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SecurityDetails instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SecurityDetails instances if creation did not fail
        :rtype: Optional[List[Union[dict, SecurityDetails]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityDetails.safe_create(it))
            return list_of_self
        else:
            return init


class Response(object):
    """
    HTTP response data.
    """

    __slots__ = ["url", "status", "statusText", "headers", "headersText", "mimeType", "requestHeaders", "requestHeadersText", "connectionReused", "connectionId", "remoteIPAddress", "remotePort", "fromDiskCache", "fromServiceWorker", "encodedDataLength", "timing", "protocol", "securityState", "securityDetails"]

    def __init__(self, url, status, statusText, headers, mimeType, connectionReused, connectionId, encodedDataLength, securityState, headersText=None, requestHeaders=None, requestHeadersText=None, remoteIPAddress=None, remotePort=None, fromDiskCache=None, fromServiceWorker=None, timing=None, protocol=None, securityDetails=None):
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
        super(Response, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        if self.statusText is not None:
            repr_args.append("statusText={!r}".format(self.statusText))
        if self.headers is not None:
            repr_args.append("headers={!r}".format(self.headers))
        if self.headersText is not None:
            repr_args.append("headersText={!r}".format(self.headersText))
        if self.mimeType is not None:
            repr_args.append("mimeType={!r}".format(self.mimeType))
        if self.requestHeaders is not None:
            repr_args.append("requestHeaders={!r}".format(self.requestHeaders))
        if self.requestHeadersText is not None:
            repr_args.append("requestHeadersText={!r}".format(self.requestHeadersText))
        if self.connectionReused is not None:
            repr_args.append("connectionReused={!r}".format(self.connectionReused))
        if self.connectionId is not None:
            repr_args.append("connectionId={!r}".format(self.connectionId))
        if self.remoteIPAddress is not None:
            repr_args.append("remoteIPAddress={!r}".format(self.remoteIPAddress))
        if self.remotePort is not None:
            repr_args.append("remotePort={!r}".format(self.remotePort))
        if self.fromDiskCache is not None:
            repr_args.append("fromDiskCache={!r}".format(self.fromDiskCache))
        if self.fromServiceWorker is not None:
            repr_args.append("fromServiceWorker={!r}".format(self.fromServiceWorker))
        if self.encodedDataLength is not None:
            repr_args.append("encodedDataLength={!r}".format(self.encodedDataLength))
        if self.timing is not None:
            repr_args.append("timing={!r}".format(self.timing))
        if self.protocol is not None:
            repr_args.append("protocol={!r}".format(self.protocol))
        if self.securityState is not None:
            repr_args.append("securityState={!r}".format(self.securityState))
        if self.securityDetails is not None:
            repr_args.append("securityDetails={!r}".format(self.securityDetails))
        return "Response(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Response from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Response
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Response if creation did not fail
        :rtype: Optional[Union[dict, Response]]
        """
        if init is not None:
            try:
                ourselves = Response(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Responses from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Response instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Response instances if creation did not fail
        :rtype: Optional[List[Union[dict, Response]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Response.safe_create(it))
            return list_of_self
        else:
            return init


class ResourceTiming(object):
    """
    Timing information for the request.
    """

    __slots__ = ["requestTime", "proxyStart", "proxyEnd", "dnsStart", "dnsEnd", "connectStart", "connectEnd", "sslStart", "sslEnd", "workerStart", "workerReady", "sendStart", "sendEnd", "pushStart", "pushEnd", "receiveHeadersEnd"]

    def __init__(self, requestTime, proxyStart, proxyEnd, dnsStart, dnsEnd, connectStart, connectEnd, sslStart, sslEnd, workerStart, workerReady, sendStart, sendEnd, pushStart, pushEnd, receiveHeadersEnd):
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
        super(ResourceTiming, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.requestTime is not None:
            repr_args.append("requestTime={!r}".format(self.requestTime))
        if self.proxyStart is not None:
            repr_args.append("proxyStart={!r}".format(self.proxyStart))
        if self.proxyEnd is not None:
            repr_args.append("proxyEnd={!r}".format(self.proxyEnd))
        if self.dnsStart is not None:
            repr_args.append("dnsStart={!r}".format(self.dnsStart))
        if self.dnsEnd is not None:
            repr_args.append("dnsEnd={!r}".format(self.dnsEnd))
        if self.connectStart is not None:
            repr_args.append("connectStart={!r}".format(self.connectStart))
        if self.connectEnd is not None:
            repr_args.append("connectEnd={!r}".format(self.connectEnd))
        if self.sslStart is not None:
            repr_args.append("sslStart={!r}".format(self.sslStart))
        if self.sslEnd is not None:
            repr_args.append("sslEnd={!r}".format(self.sslEnd))
        if self.workerStart is not None:
            repr_args.append("workerStart={!r}".format(self.workerStart))
        if self.workerReady is not None:
            repr_args.append("workerReady={!r}".format(self.workerReady))
        if self.sendStart is not None:
            repr_args.append("sendStart={!r}".format(self.sendStart))
        if self.sendEnd is not None:
            repr_args.append("sendEnd={!r}".format(self.sendEnd))
        if self.pushStart is not None:
            repr_args.append("pushStart={!r}".format(self.pushStart))
        if self.pushEnd is not None:
            repr_args.append("pushEnd={!r}".format(self.pushEnd))
        if self.receiveHeadersEnd is not None:
            repr_args.append("receiveHeadersEnd={!r}".format(self.receiveHeadersEnd))
        return "ResourceTiming(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ResourceTiming from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ResourceTiming
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ResourceTiming if creation did not fail
        :rtype: Optional[Union[dict, ResourceTiming]]
        """
        if init is not None:
            try:
                ourselves = ResourceTiming(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ResourceTimings from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ResourceTiming instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ResourceTiming instances if creation did not fail
        :rtype: Optional[List[Union[dict, ResourceTiming]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResourceTiming.safe_create(it))
            return list_of_self
        else:
            return init


class RequestPattern(object):
    """
    Request pattern for interception.
    """

    __slots__ = ["urlPattern", "resourceType", "interceptionStage"]

    def __init__(self, urlPattern=None, resourceType=None, interceptionStage=None):
        """
        :param urlPattern: Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*".
        :type urlPattern: Optional[str]
        :param resourceType: If set, only requests for matching resource types will be intercepted.
        :type resourceType: Optional[str]
        :param interceptionStage: Stage at wich to begin intercepting requests. Default is Request.
        :type interceptionStage: Optional[str]
        """
        super(RequestPattern, self).__init__()
        self.urlPattern = urlPattern
        self.resourceType = resourceType
        self.interceptionStage = interceptionStage

    def __repr__(self):
        repr_args = []
        if self.urlPattern is not None:
            repr_args.append("urlPattern={!r}".format(self.urlPattern))
        if self.resourceType is not None:
            repr_args.append("resourceType={!r}".format(self.resourceType))
        if self.interceptionStage is not None:
            repr_args.append("interceptionStage={!r}".format(self.interceptionStage))
        return "RequestPattern(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create RequestPattern from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RequestPattern
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RequestPattern if creation did not fail
        :rtype: Optional[Union[dict, RequestPattern]]
        """
        if init is not None:
            try:
                ourselves = RequestPattern(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list RequestPatterns from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RequestPattern instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RequestPattern instances if creation did not fail
        :rtype: Optional[List[Union[dict, RequestPattern]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestPattern.safe_create(it))
            return list_of_self
        else:
            return init


class Request(object):
    """
    HTTP request data.
    """

    __slots__ = ["url", "method", "headers", "postData", "hasPostData", "mixedContentType", "initialPriority", "referrerPolicy", "isLinkPreload"]

    def __init__(self, url, method, headers, initialPriority, referrerPolicy, postData=None, hasPostData=None, mixedContentType=None, isLinkPreload=None):
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
        super(Request, self).__init__()
        self.url = url
        self.method = method
        self.headers = Headers.safe_create(headers)
        self.postData = postData
        self.hasPostData = hasPostData
        self.mixedContentType = mixedContentType
        self.initialPriority = initialPriority
        self.referrerPolicy = referrerPolicy
        self.isLinkPreload = isLinkPreload

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.method is not None:
            repr_args.append("method={!r}".format(self.method))
        if self.headers is not None:
            repr_args.append("headers={!r}".format(self.headers))
        if self.postData is not None:
            repr_args.append("postData={!r}".format(self.postData))
        if self.hasPostData is not None:
            repr_args.append("hasPostData={!r}".format(self.hasPostData))
        if self.mixedContentType is not None:
            repr_args.append("mixedContentType={!r}".format(self.mixedContentType))
        if self.initialPriority is not None:
            repr_args.append("initialPriority={!r}".format(self.initialPriority))
        if self.referrerPolicy is not None:
            repr_args.append("referrerPolicy={!r}".format(self.referrerPolicy))
        if self.isLinkPreload is not None:
            repr_args.append("isLinkPreload={!r}".format(self.isLinkPreload))
        return "Request(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Request from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Request
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Request if creation did not fail
        :rtype: Optional[Union[dict, Request]]
        """
        if init is not None:
            try:
                ourselves = Request(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Requests from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Request instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Request instances if creation did not fail
        :rtype: Optional[List[Union[dict, Request]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Request.safe_create(it))
            return list_of_self
        else:
            return init


class Initiator(object):
    """
    Information about the request initiator.
    """

    __slots__ = ["type", "stack", "url", "lineNumber"]

    def __init__(self, type, stack=None, url=None, lineNumber=None):
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
        super(Initiator, self).__init__()
        self.type = type
        self.stack = Runtime.StackTrace.safe_create(stack)
        self.url = url
        self.lineNumber = lineNumber

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.stack is not None:
            repr_args.append("stack={!r}".format(self.stack))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        return "Initiator(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Initiator from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Initiator
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Initiator if creation did not fail
        :rtype: Optional[Union[dict, Initiator]]
        """
        if init is not None:
            try:
                ourselves = Initiator(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Initiators from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Initiator instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Initiator instances if creation did not fail
        :rtype: Optional[List[Union[dict, Initiator]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Initiator.safe_create(it))
            return list_of_self
        else:
            return init


class Headers(dict):
    """
    Request / response headers as keys / values of JSON object.
    """


    def __repr__(self):
        return "Headers(dict)"

    @staticmethod
    def safe_create(init):
        """
        Safely create Headers from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Headers
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Headers if creation did not fail
        :rtype: Optional[Union[dict, Headers]]
        """
        if init is not None:
            try:
                ourselves = Headers(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Headerss from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Headers instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Headers instances if creation did not fail
        :rtype: Optional[List[Union[dict, Headers]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Headers.safe_create(it))
            return list_of_self
        else:
            return init


class CookieParam(object):
    """
    Cookie parameter object
    """

    __slots__ = ["name", "value", "url", "domain", "path", "secure", "httpOnly", "sameSite", "expires"]

    def __init__(self, name, value, url=None, domain=None, path=None, secure=None, httpOnly=None, sameSite=None, expires=None):
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
        super(CookieParam, self).__init__()
        self.name = name
        self.value = value
        self.url = url
        self.domain = domain
        self.path = path
        self.secure = secure
        self.httpOnly = httpOnly
        self.sameSite = sameSite
        self.expires = expires

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.domain is not None:
            repr_args.append("domain={!r}".format(self.domain))
        if self.path is not None:
            repr_args.append("path={!r}".format(self.path))
        if self.secure is not None:
            repr_args.append("secure={!r}".format(self.secure))
        if self.httpOnly is not None:
            repr_args.append("httpOnly={!r}".format(self.httpOnly))
        if self.sameSite is not None:
            repr_args.append("sameSite={!r}".format(self.sameSite))
        if self.expires is not None:
            repr_args.append("expires={!r}".format(self.expires))
        return "CookieParam(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create CookieParam from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CookieParam
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CookieParam if creation did not fail
        :rtype: Optional[Union[dict, CookieParam]]
        """
        if init is not None:
            try:
                ourselves = CookieParam(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list CookieParams from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CookieParam instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CookieParam instances if creation did not fail
        :rtype: Optional[List[Union[dict, CookieParam]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CookieParam.safe_create(it))
            return list_of_self
        else:
            return init


class Cookie(object):
    """
    Cookie object
    """

    __slots__ = ["name", "value", "domain", "path", "expires", "size", "httpOnly", "secure", "session", "sameSite"]

    def __init__(self, name, value, domain, path, expires, size, httpOnly, secure, session, sameSite=None):
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
        super(Cookie, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        if self.domain is not None:
            repr_args.append("domain={!r}".format(self.domain))
        if self.path is not None:
            repr_args.append("path={!r}".format(self.path))
        if self.expires is not None:
            repr_args.append("expires={!r}".format(self.expires))
        if self.size is not None:
            repr_args.append("size={!r}".format(self.size))
        if self.httpOnly is not None:
            repr_args.append("httpOnly={!r}".format(self.httpOnly))
        if self.secure is not None:
            repr_args.append("secure={!r}".format(self.secure))
        if self.session is not None:
            repr_args.append("session={!r}".format(self.session))
        if self.sameSite is not None:
            repr_args.append("sameSite={!r}".format(self.sameSite))
        return "Cookie(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Cookie from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Cookie
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Cookie if creation did not fail
        :rtype: Optional[Union[dict, Cookie]]
        """
        if init is not None:
            try:
                ourselves = Cookie(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Cookies from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Cookie instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Cookie instances if creation did not fail
        :rtype: Optional[List[Union[dict, Cookie]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Cookie.safe_create(it))
            return list_of_self
        else:
            return init


class CachedResource(object):
    """
    Information about the cached resource.
    """

    __slots__ = ["url", "type", "response", "bodySize"]

    def __init__(self, url, type, bodySize, response=None):
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
        super(CachedResource, self).__init__()
        self.url = url
        self.type = type
        self.response = Response.safe_create(response)
        self.bodySize = bodySize

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        if self.bodySize is not None:
            repr_args.append("bodySize={!r}".format(self.bodySize))
        return "CachedResource(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create CachedResource from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CachedResource
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CachedResource if creation did not fail
        :rtype: Optional[Union[dict, CachedResource]]
        """
        if init is not None:
            try:
                ourselves = CachedResource(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list CachedResources from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CachedResource instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CachedResource instances if creation did not fail
        :rtype: Optional[List[Union[dict, CachedResource]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CachedResource.safe_create(it))
            return list_of_self
        else:
            return init


class AuthChallengeResponse(object):
    """
    Response to an AuthChallenge.
    """

    __slots__ = ["response", "username", "password"]

    def __init__(self, response, username=None, password=None):
        """
        :param response: The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box.
        :type response: str
        :param username: The username to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type username: Optional[str]
        :param password: The password to provide, possibly empty. Should only be set if response is ProvideCredentials.
        :type password: Optional[str]
        """
        super(AuthChallengeResponse, self).__init__()
        self.response = response
        self.username = username
        self.password = password

    def __repr__(self):
        repr_args = []
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        if self.username is not None:
            repr_args.append("username={!r}".format(self.username))
        if self.password is not None:
            repr_args.append("password={!r}".format(self.password))
        return "AuthChallengeResponse(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AuthChallengeResponse from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AuthChallengeResponse
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AuthChallengeResponse if creation did not fail
        :rtype: Optional[Union[dict, AuthChallengeResponse]]
        """
        if init is not None:
            try:
                ourselves = AuthChallengeResponse(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AuthChallengeResponses from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AuthChallengeResponse instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AuthChallengeResponse instances if creation did not fail
        :rtype: Optional[List[Union[dict, AuthChallengeResponse]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AuthChallengeResponse.safe_create(it))
            return list_of_self
        else:
            return init


class AuthChallenge(object):
    """
    Authorization challenge for HTTP status code 401 or 407.
    """

    __slots__ = ["source", "origin", "scheme", "realm"]

    def __init__(self, origin, scheme, realm, source=None):
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
        super(AuthChallenge, self).__init__()
        self.source = source
        self.origin = origin
        self.scheme = scheme
        self.realm = realm

    def __repr__(self):
        repr_args = []
        if self.source is not None:
            repr_args.append("source={!r}".format(self.source))
        if self.origin is not None:
            repr_args.append("origin={!r}".format(self.origin))
        if self.scheme is not None:
            repr_args.append("scheme={!r}".format(self.scheme))
        if self.realm is not None:
            repr_args.append("realm={!r}".format(self.realm))
        return "AuthChallenge(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AuthChallenge from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AuthChallenge
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AuthChallenge if creation did not fail
        :rtype: Optional[Union[dict, AuthChallenge]]
        """
        if init is not None:
            try:
                ourselves = AuthChallenge(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AuthChallenges from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AuthChallenge instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AuthChallenge instances if creation did not fail
        :rtype: Optional[List[Union[dict, AuthChallenge]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AuthChallenge.safe_create(it))
            return list_of_self
        else:
            return init


NETWORK_TYPE_TO_OBJECT = {
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
