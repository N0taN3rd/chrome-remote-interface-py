from typing import Any, List, Optional, Union
from types import SimpleNamespace
from cripy.async.protocol.page import types as Page

try:
    from cripy.async.protocol.network.types import *
except ImportError:
    pass


class DataReceivedEvent(object):
    """
    Fired when data chunk was received over the network.
    """

    event = "Network.dataReceived"

    def __init__(
        self, requestId: str, timestamp: float, dataLength: int, encodedDataLength: int
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param dataLength: Data chunk length.
        :type dataLength: int
        :param encodedDataLength: Actual bytes received (might be less than dataLength for compressed encodings).
        :type encodedDataLength: int
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.dataLength = dataLength
        self.encodedDataLength = encodedDataLength

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.dataLength is not None:
            repr_args.append("dataLength={!r}".format(self.dataLength))
        if self.encodedDataLength is not None:
            repr_args.append("encodedDataLength={!r}".format(self.encodedDataLength))
        return "DataReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["DataReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = DataReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DataReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class EventSourceMessageReceivedEvent(object):
    """
    Fired when EventSource message is received.
    """

    event = "Network.eventSourceMessageReceived"

    def __init__(
        self, requestId: str, timestamp: float, eventName: str, eventId: str, data: str
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param eventName: Message type.
        :type eventName: str
        :param eventId: Message identifier.
        :type eventId: str
        :param data: Message content.
        :type data: str
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.eventName = eventName
        self.eventId = eventId
        self.data = data

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.eventName is not None:
            repr_args.append("eventName={!r}".format(self.eventName))
        if self.eventId is not None:
            repr_args.append("eventId={!r}".format(self.eventId))
        if self.data is not None:
            repr_args.append("data={!r}".format(self.data))
        return "EventSourceMessageReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["EventSourceMessageReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = EventSourceMessageReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["EventSourceMessageReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EventSourceMessageReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LoadingFailedEvent(object):
    """
    Fired when HTTP request has failed to load.
    """

    event = "Network.loadingFailed"

    def __init__(
        self,
        requestId: str,
        timestamp: float,
        type: str,
        errorText: str,
        canceled: Optional[bool] = None,
        blockedReason: Optional[str] = None,
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param type: Resource type.
        :type type: str
        :param errorText: User friendly error message.
        :type errorText: str
        :param canceled: True if loading was canceled.
        :type canceled: Optional[bool]
        :param blockedReason: The reason why loading was blocked, if any.
        :type blockedReason: Optional[str]
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.type = type
        self.errorText = errorText
        self.canceled = canceled
        self.blockedReason = blockedReason

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.errorText is not None:
            repr_args.append("errorText={!r}".format(self.errorText))
        if self.canceled is not None:
            repr_args.append("canceled={!r}".format(self.canceled))
        if self.blockedReason is not None:
            repr_args.append("blockedReason={!r}".format(self.blockedReason))
        return "LoadingFailedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["LoadingFailedEvent", dict]]:
        if init is not None:
            try:
                ourselves = LoadingFailedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["LoadingFailedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadingFailedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LoadingFinishedEvent(object):
    """
    Fired when HTTP request has finished loading.
    """

    event = "Network.loadingFinished"

    def __init__(
        self,
        requestId: str,
        timestamp: float,
        encodedDataLength: float,
        shouldReportCorbBlocking: Optional[bool] = None,
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param encodedDataLength: Total number of bytes received for this request.
        :type encodedDataLength: float
        :param shouldReportCorbBlocking: Set when 1) response was blocked by Cross-Origin Read Blocking and also 2) this needs to be reported to the DevTools console.
        :type shouldReportCorbBlocking: Optional[bool]
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.encodedDataLength = encodedDataLength
        self.shouldReportCorbBlocking = shouldReportCorbBlocking

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.encodedDataLength is not None:
            repr_args.append("encodedDataLength={!r}".format(self.encodedDataLength))
        if self.shouldReportCorbBlocking is not None:
            repr_args.append(
                "shouldReportCorbBlocking={!r}".format(self.shouldReportCorbBlocking)
            )
        return "LoadingFinishedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["LoadingFinishedEvent", dict]]:
        if init is not None:
            try:
                ourselves = LoadingFinishedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["LoadingFinishedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadingFinishedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class RequestInterceptedEvent(object):
    """
    Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked.
    """

    event = "Network.requestIntercepted"

    def __init__(
        self,
        interceptionId: str,
        request: Union[Request, dict],
        frameId: str,
        resourceType: str,
        isNavigationRequest: bool,
        isDownload: Optional[bool] = None,
        redirectUrl: Optional[str] = None,
        authChallenge: Optional[Union[AuthChallenge, dict]] = None,
        responseErrorReason: Optional[str] = None,
        responseStatusCode: Optional[int] = None,
        responseHeaders: Optional[Union[Headers, dict]] = None,
    ) -> None:
        """
        :param interceptionId: Each request the page makes will have a unique id, however if any redirects are encountered while processing that fetch, they will be reported with the same id as the original fetch. Likewise if HTTP authentication is needed then the same fetch id will be used.
        :type interceptionId: str
        :param request: The request
        :type request: dict
        :param frameId: The id of the frame that initiated the request.
        :type frameId: str
        :param resourceType: How the requested resource will be used.
        :type resourceType: str
        :param isNavigationRequest: Whether this is a navigation request, which can abort the navigation completely.
        :type isNavigationRequest: bool
        :param isDownload: Set if the request is a navigation that will result in a download. Only present after response is received from the server (i.e. HeadersReceived stage).
        :type isDownload: Optional[bool]
        :param redirectUrl: Redirect location, only sent if a redirect was intercepted.
        :type redirectUrl: Optional[str]
        :param authChallenge: Details of the Authorization Challenge encountered. If this is set then continueInterceptedRequest must contain an authChallengeResponse.
        :type authChallenge: Optional[dict]
        :param responseErrorReason: Response error if intercepted at response stage or if redirect occurred while intercepting request.
        :type responseErrorReason: Optional[str]
        :param responseStatusCode: Response code if intercepted at response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseStatusCode: Optional[int]
        :param responseHeaders: Response headers if intercepted at the response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseHeaders: Optional[dict]
        """
        super().__init__()
        self.interceptionId = interceptionId
        self.request = Request.safe_create(request)
        self.frameId = frameId
        self.resourceType = resourceType
        self.isNavigationRequest = isNavigationRequest
        self.isDownload = isDownload
        self.redirectUrl = redirectUrl
        self.authChallenge = AuthChallenge.safe_create(authChallenge)
        self.responseErrorReason = responseErrorReason
        self.responseStatusCode = responseStatusCode
        self.responseHeaders = Headers.safe_create(responseHeaders)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.interceptionId is not None:
            repr_args.append("interceptionId={!r}".format(self.interceptionId))
        if self.request is not None:
            repr_args.append("request={!r}".format(self.request))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.resourceType is not None:
            repr_args.append("resourceType={!r}".format(self.resourceType))
        if self.isNavigationRequest is not None:
            repr_args.append(
                "isNavigationRequest={!r}".format(self.isNavigationRequest)
            )
        if self.isDownload is not None:
            repr_args.append("isDownload={!r}".format(self.isDownload))
        if self.redirectUrl is not None:
            repr_args.append("redirectUrl={!r}".format(self.redirectUrl))
        if self.authChallenge is not None:
            repr_args.append("authChallenge={!r}".format(self.authChallenge))
        if self.responseErrorReason is not None:
            repr_args.append(
                "responseErrorReason={!r}".format(self.responseErrorReason)
            )
        if self.responseStatusCode is not None:
            repr_args.append("responseStatusCode={!r}".format(self.responseStatusCode))
        if self.responseHeaders is not None:
            repr_args.append("responseHeaders={!r}".format(self.responseHeaders))
        return "RequestInterceptedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["RequestInterceptedEvent", dict]]:
        if init is not None:
            try:
                ourselves = RequestInterceptedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["RequestInterceptedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestInterceptedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class RequestServedFromCacheEvent(object):
    """
    Fired if request ended up loading from cache.
    """

    event = "Network.requestServedFromCache"

    def __init__(self, requestId: str) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        """
        super().__init__()
        self.requestId = requestId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        return "RequestServedFromCacheEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["RequestServedFromCacheEvent", dict]]:
        if init is not None:
            try:
                ourselves = RequestServedFromCacheEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["RequestServedFromCacheEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestServedFromCacheEvent.safe_create(it))
            return list_of_self
        else:
            return init


class RequestWillBeSentEvent(object):
    """
    Fired when page is about to send HTTP request.
    """

    event = "Network.requestWillBeSent"

    def __init__(
        self,
        requestId: str,
        loaderId: str,
        documentURL: str,
        request: Union[Request, dict],
        timestamp: float,
        wallTime: float,
        initiator: Union[Initiator, dict],
        redirectResponse: Optional[Union[Response, dict]] = None,
        type: Optional[str] = None,
        frameId: Optional[str] = None,
        hasUserGesture: Optional[bool] = None,
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: str
        :param documentURL: URL of the document this request is loaded for.
        :type documentURL: str
        :param request: Request data.
        :type request: dict
        :param timestamp: Timestamp.
        :type timestamp: float
        :param wallTime: Timestamp.
        :type wallTime: float
        :param initiator: Request initiator.
        :type initiator: dict
        :param redirectResponse: Redirect response data.
        :type redirectResponse: Optional[dict]
        :param type: Type of this resource.
        :type type: Optional[str]
        :param frameId: Frame identifier.
        :type frameId: Optional[str]
        :param hasUserGesture: Whether the request is initiated by a user gesture. Defaults to false.
        :type hasUserGesture: Optional[bool]
        """
        super().__init__()
        self.requestId = requestId
        self.loaderId = loaderId
        self.documentURL = documentURL
        self.request = Request.safe_create(request)
        self.timestamp = timestamp
        self.wallTime = wallTime
        self.initiator = Initiator.safe_create(initiator)
        self.redirectResponse = Response.safe_create(redirectResponse)
        self.type = type
        self.frameId = frameId
        self.hasUserGesture = hasUserGesture

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.loaderId is not None:
            repr_args.append("loaderId={!r}".format(self.loaderId))
        if self.documentURL is not None:
            repr_args.append("documentURL={!r}".format(self.documentURL))
        if self.request is not None:
            repr_args.append("request={!r}".format(self.request))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.wallTime is not None:
            repr_args.append("wallTime={!r}".format(self.wallTime))
        if self.initiator is not None:
            repr_args.append("initiator={!r}".format(self.initiator))
        if self.redirectResponse is not None:
            repr_args.append("redirectResponse={!r}".format(self.redirectResponse))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.hasUserGesture is not None:
            repr_args.append("hasUserGesture={!r}".format(self.hasUserGesture))
        return "RequestWillBeSentEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["RequestWillBeSentEvent", dict]]:
        if init is not None:
            try:
                ourselves = RequestWillBeSentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["RequestWillBeSentEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestWillBeSentEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResourceChangedPriorityEvent(object):
    """
    Fired when resource loading priority is changed
    """

    event = "Network.resourceChangedPriority"

    def __init__(self, requestId: str, newPriority: str, timestamp: float) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param newPriority: New priority
        :type newPriority: str
        :param timestamp: Timestamp.
        :type timestamp: float
        """
        super().__init__()
        self.requestId = requestId
        self.newPriority = newPriority
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.newPriority is not None:
            repr_args.append("newPriority={!r}".format(self.newPriority))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "ResourceChangedPriorityEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ResourceChangedPriorityEvent", dict]]:
        if init is not None:
            try:
                ourselves = ResourceChangedPriorityEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ResourceChangedPriorityEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResourceChangedPriorityEvent.safe_create(it))
            return list_of_self
        else:
            return init


class SignedExchangeReceivedEvent(object):
    """
    Fired when a signed exchange was received over the network
    """

    event = "Network.signedExchangeReceived"

    def __init__(self, requestId: str, info: Union[SignedExchangeInfo, dict]) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param info: Information about the signed exchange response.
        :type info: dict
        """
        super().__init__()
        self.requestId = requestId
        self.info = SignedExchangeInfo.safe_create(info)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.info is not None:
            repr_args.append("info={!r}".format(self.info))
        return "SignedExchangeReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["SignedExchangeReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = SignedExchangeReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["SignedExchangeReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ResponseReceivedEvent(object):
    """
    Fired when HTTP response is available.
    """

    event = "Network.responseReceived"

    def __init__(
        self,
        requestId: str,
        loaderId: str,
        timestamp: float,
        type: str,
        response: Union[Response, dict],
        frameId: Optional[str] = None,
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param type: Resource type.
        :type type: str
        :param response: Response data.
        :type response: dict
        :param frameId: Frame identifier.
        :type frameId: Optional[str]
        """
        super().__init__()
        self.requestId = requestId
        self.loaderId = loaderId
        self.timestamp = timestamp
        self.type = type
        self.response = Response.safe_create(response)
        self.frameId = frameId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.loaderId is not None:
            repr_args.append("loaderId={!r}".format(self.loaderId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "ResponseReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ResponseReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ResponseReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ResponseReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResponseReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketClosedEvent(object):
    """
    Fired when WebSocket is closed.
    """

    event = "Network.webSocketClosed"

    def __init__(self, requestId: str, timestamp: float) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "WebSocketClosedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketClosedEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketClosedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketClosedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketClosedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketCreatedEvent(object):
    """
    Fired upon WebSocket creation.
    """

    event = "Network.webSocketCreated"

    def __init__(
        self,
        requestId: str,
        url: str,
        initiator: Optional[Union[Initiator, dict]] = None,
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param url: WebSocket request URL.
        :type url: str
        :param initiator: Request initiator.
        :type initiator: Optional[dict]
        """
        super().__init__()
        self.requestId = requestId
        self.url = url
        self.initiator = Initiator.safe_create(initiator)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.initiator is not None:
            repr_args.append("initiator={!r}".format(self.initiator))
        return "WebSocketCreatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketCreatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketCreatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketFrameErrorEvent(object):
    """
    Fired when WebSocket frame error occurs.
    """

    event = "Network.webSocketFrameError"

    def __init__(self, requestId: str, timestamp: float, errorMessage: str) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param errorMessage: WebSocket frame error message.
        :type errorMessage: str
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.errorMessage = errorMessage

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.errorMessage is not None:
            repr_args.append("errorMessage={!r}".format(self.errorMessage))
        return "WebSocketFrameErrorEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketFrameErrorEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketFrameErrorEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketFrameErrorEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameErrorEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketFrameReceivedEvent(object):
    """
    Fired when WebSocket frame is received.
    """

    event = "Network.webSocketFrameReceived"

    def __init__(
        self, requestId: str, timestamp: float, response: Union[WebSocketFrame, dict]
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param response: WebSocket response data.
        :type response: dict
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.response = WebSocketFrame.safe_create(response)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketFrameReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketFrameReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketFrameReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketFrameReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketFrameSentEvent(object):
    """
    Fired when WebSocket frame is sent.
    """

    event = "Network.webSocketFrameSent"

    def __init__(
        self, requestId: str, timestamp: float, response: Union[WebSocketFrame, dict]
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param response: WebSocket response data.
        :type response: dict
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.response = WebSocketFrame.safe_create(response)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketFrameSentEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketFrameSentEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketFrameSentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketFrameSentEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameSentEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketHandshakeResponseReceivedEvent(object):
    """
    Fired when WebSocket handshake response becomes available.
    """

    event = "Network.webSocketHandshakeResponseReceived"

    def __init__(
        self, requestId: str, timestamp: float, response: Union[WebSocketResponse, dict]
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param response: WebSocket response data.
        :type response: dict
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.response = WebSocketResponse.safe_create(response)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketHandshakeResponseReceivedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketHandshakeResponseReceivedEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketHandshakeResponseReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketHandshakeResponseReceivedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(
                    WebSocketHandshakeResponseReceivedEvent.safe_create(it)
                )
            return list_of_self
        else:
            return init


class WebSocketWillSendHandshakeRequestEvent(object):
    """
    Fired when WebSocket is about to initiate handshake.
    """

    event = "Network.webSocketWillSendHandshakeRequest"

    def __init__(
        self,
        requestId: str,
        timestamp: float,
        wallTime: float,
        request: Union[WebSocketRequest, dict],
    ) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param wallTime: UTC Timestamp.
        :type wallTime: float
        :param request: WebSocket request data.
        :type request: dict
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.wallTime = wallTime
        self.request = WebSocketRequest.safe_create(request)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.wallTime is not None:
            repr_args.append("wallTime={!r}".format(self.wallTime))
        if self.request is not None:
            repr_args.append("request={!r}".format(self.request))
        return "WebSocketWillSendHandshakeRequestEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["WebSocketWillSendHandshakeRequestEvent", dict]]:
        if init is not None:
            try:
                ourselves = WebSocketWillSendHandshakeRequestEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["WebSocketWillSendHandshakeRequestEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(
                    WebSocketWillSendHandshakeRequestEvent.safe_create(it)
                )
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Network.dataReceived": DataReceivedEvent,
    "Network.eventSourceMessageReceived": EventSourceMessageReceivedEvent,
    "Network.loadingFailed": LoadingFailedEvent,
    "Network.loadingFinished": LoadingFinishedEvent,
    "Network.requestIntercepted": RequestInterceptedEvent,
    "Network.requestServedFromCache": RequestServedFromCacheEvent,
    "Network.requestWillBeSent": RequestWillBeSentEvent,
    "Network.resourceChangedPriority": ResourceChangedPriorityEvent,
    "Network.signedExchangeReceived": SignedExchangeReceivedEvent,
    "Network.responseReceived": ResponseReceivedEvent,
    "Network.webSocketClosed": WebSocketClosedEvent,
    "Network.webSocketCreated": WebSocketCreatedEvent,
    "Network.webSocketFrameError": WebSocketFrameErrorEvent,
    "Network.webSocketFrameReceived": WebSocketFrameReceivedEvent,
    "Network.webSocketFrameSent": WebSocketFrameSentEvent,
    "Network.webSocketHandshakeResponseReceived": WebSocketHandshakeResponseReceivedEvent,
    "Network.webSocketWillSendHandshakeRequest": WebSocketWillSendHandshakeRequestEvent,
}

EVENT_NS = SimpleNamespace(
    DataReceived="Network.dataReceived",
    EventSourceMessageReceived="Network.eventSourceMessageReceived",
    LoadingFailed="Network.loadingFailed",
    LoadingFinished="Network.loadingFinished",
    RequestIntercepted="Network.requestIntercepted",
    RequestServedFromCache="Network.requestServedFromCache",
    RequestWillBeSent="Network.requestWillBeSent",
    ResourceChangedPriority="Network.resourceChangedPriority",
    SignedExchangeReceived="Network.signedExchangeReceived",
    ResponseReceived="Network.responseReceived",
    WebSocketClosed="Network.webSocketClosed",
    WebSocketCreated="Network.webSocketCreated",
    WebSocketFrameError="Network.webSocketFrameError",
    WebSocketFrameReceived="Network.webSocketFrameReceived",
    WebSocketFrameSent="Network.webSocketFrameSent",
    WebSocketHandshakeResponseReceived="Network.webSocketHandshakeResponseReceived",
    WebSocketWillSendHandshakeRequest="Network.webSocketWillSendHandshakeRequest",
)
