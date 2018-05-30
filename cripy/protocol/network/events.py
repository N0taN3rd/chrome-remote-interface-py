from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.page import types as Page
try:
    from cripy.protocol.network.types import *
except ImportError:
    pass


class DataReceivedEvent(BaseEvent):
    """
    Fired when data chunk was received over the network.
    """

    event = "Network.dataReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, dataLength: int, encodedDataLength: int) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DataReceivedEvent']:
        if init is not None:
            return DataReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DataReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataReceivedEvent(**it))
            return list_of_self
        else:
            return init


class EventSourceMessageReceivedEvent(BaseEvent):
    """
    Fired when EventSource message is received.
    """

    event = "Network.eventSourceMessageReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, eventName: str, eventId: str, data: str) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['EventSourceMessageReceivedEvent']:
        if init is not None:
            return EventSourceMessageReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['EventSourceMessageReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EventSourceMessageReceivedEvent(**it))
            return list_of_self
        else:
            return init


class LoadingFailedEvent(BaseEvent):
    """
    Fired when HTTP request has failed to load.
    """

    event = "Network.loadingFailed"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, type: Page.ResourceType, errorText: str, canceled: Optional[bool] = None, blockedReason: Optional[BlockedReason] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LoadingFailedEvent']:
        if init is not None:
            return LoadingFailedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LoadingFailedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadingFailedEvent(**it))
            return list_of_self
        else:
            return init


class LoadingFinishedEvent(BaseEvent):
    """
    Fired when HTTP request has finished loading.
    """

    event = "Network.loadingFinished"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, encodedDataLength: float, blockedCrossSiteDocument: Optional[bool] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        :param encodedDataLength: Total number of bytes received for this request.
        :type encodedDataLength: float
        :param blockedCrossSiteDocument: Set when response was blocked due to being cross-site document response.
        :type blockedCrossSiteDocument: Optional[bool]
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp
        self.encodedDataLength = encodedDataLength
        self.blockedCrossSiteDocument = blockedCrossSiteDocument

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LoadingFinishedEvent']:
        if init is not None:
            return LoadingFinishedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LoadingFinishedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadingFinishedEvent(**it))
            return list_of_self
        else:
            return init


class RequestInterceptedEvent(BaseEvent):
    """
    Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked.
    """

    event = "Network.requestIntercepted"

    def __init__(self, interceptionId: InterceptionId, request: Union[Request, dict], frameId: Page.FrameId, resourceType: Page.ResourceType, isNavigationRequest: bool, isDownload: Optional[bool] = None, redirectUrl: Optional[str] = None, authChallenge: Optional[Union[AuthChallenge, dict]] = None, responseErrorReason: Optional[ErrorReason] = None, responseStatusCode: Optional[int] = None, responseHeaders: Optional[Union[Headers, dict]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RequestInterceptedEvent']:
        if init is not None:
            return RequestInterceptedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RequestInterceptedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestInterceptedEvent(**it))
            return list_of_self
        else:
            return init


class RequestServedFromCacheEvent(BaseEvent):
    """
    Fired if request ended up loading from cache.
    """

    event = "Network.requestServedFromCache"

    def __init__(self, requestId: RequestId) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        """
        super().__init__()
        self.requestId = requestId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RequestServedFromCacheEvent']:
        if init is not None:
            return RequestServedFromCacheEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RequestServedFromCacheEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestServedFromCacheEvent(**it))
            return list_of_self
        else:
            return init


class RequestWillBeSentEvent(BaseEvent):
    """
    Fired when page is about to send HTTP request.
    """

    event = "Network.requestWillBeSent"

    def __init__(self, requestId: RequestId, loaderId: LoaderId, documentURL: str, request: Union[Request, dict], timestamp: MonotonicTime, wallTime: TimeSinceEpoch, initiator: Union[Initiator, dict], redirectResponse: Optional[Union[Response, dict]] = None, type: Optional[Page.ResourceType] = None, frameId: Optional[Page.FrameId] = None, hasUserGesture: Optional[bool] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['RequestWillBeSentEvent']:
        if init is not None:
            return RequestWillBeSentEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RequestWillBeSentEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RequestWillBeSentEvent(**it))
            return list_of_self
        else:
            return init


class ResourceChangedPriorityEvent(BaseEvent):
    """
    Fired when resource loading priority is changed
    """

    event = "Network.resourceChangedPriority"

    def __init__(self, requestId: RequestId, newPriority: ResourcePriority, timestamp: MonotonicTime) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ResourceChangedPriorityEvent']:
        if init is not None:
            return ResourceChangedPriorityEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ResourceChangedPriorityEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResourceChangedPriorityEvent(**it))
            return list_of_self
        else:
            return init


class SignedExchangeReceivedEvent(BaseEvent):
    """
    Fired when a signed exchange was received over the network
    """

    event = "Network.signedExchangeReceived"

    def __init__(self, requestId: RequestId, info: Union[SignedExchangeInfo, dict]) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param info: Information about the signed exchange response.
        :type info: dict
        """
        super().__init__()
        self.requestId = requestId
        self.info = SignedExchangeInfo.safe_create(info)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SignedExchangeReceivedEvent']:
        if init is not None:
            return SignedExchangeReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SignedExchangeReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SignedExchangeReceivedEvent(**it))
            return list_of_self
        else:
            return init


class ResponseReceivedEvent(BaseEvent):
    """
    Fired when HTTP response is available.
    """

    event = "Network.responseReceived"

    def __init__(self, requestId: RequestId, loaderId: LoaderId, timestamp: MonotonicTime, type: Page.ResourceType, response: Union[Response, dict], frameId: Optional[Page.FrameId] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ResponseReceivedEvent']:
        if init is not None:
            return ResponseReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ResponseReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ResponseReceivedEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketClosedEvent(BaseEvent):
    """
    Fired when WebSocket is closed.
    """

    event = "Network.webSocketClosed"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketClosedEvent']:
        if init is not None:
            return WebSocketClosedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketClosedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketClosedEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketCreatedEvent(BaseEvent):
    """
    Fired upon WebSocket creation.
    """

    event = "Network.webSocketCreated"

    def __init__(self, requestId: RequestId, url: str, initiator: Optional[Union[Initiator, dict]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketCreatedEvent']:
        if init is not None:
            return WebSocketCreatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketCreatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketCreatedEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketFrameErrorEvent(BaseEvent):
    """
    Fired when WebSocket frame error occurs.
    """

    event = "Network.webSocketFrameError"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, errorMessage: str) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketFrameErrorEvent']:
        if init is not None:
            return WebSocketFrameErrorEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketFrameErrorEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameErrorEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketFrameReceivedEvent(BaseEvent):
    """
    Fired when WebSocket frame is received.
    """

    event = "Network.webSocketFrameReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: Union[WebSocketFrame, dict]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketFrameReceivedEvent']:
        if init is not None:
            return WebSocketFrameReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketFrameReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameReceivedEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketFrameSentEvent(BaseEvent):
    """
    Fired when WebSocket frame is sent.
    """

    event = "Network.webSocketFrameSent"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: Union[WebSocketFrame, dict]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketFrameSentEvent']:
        if init is not None:
            return WebSocketFrameSentEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketFrameSentEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketFrameSentEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):
    """
    Fired when WebSocket handshake response becomes available.
    """

    event = "Network.webSocketHandshakeResponseReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: Union[WebSocketResponse, dict]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketHandshakeResponseReceivedEvent']:
        if init is not None:
            return WebSocketHandshakeResponseReceivedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketHandshakeResponseReceivedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketHandshakeResponseReceivedEvent(**it))
            return list_of_self
        else:
            return init


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):
    """
    Fired when WebSocket is about to initiate handshake.
    """

    event = "Network.webSocketWillSendHandshakeRequest"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, wallTime: TimeSinceEpoch, request: Union[WebSocketRequest, dict]) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WebSocketWillSendHandshakeRequestEvent']:
        if init is not None:
            return WebSocketWillSendHandshakeRequestEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WebSocketWillSendHandshakeRequestEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketWillSendHandshakeRequestEvent(**it))
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

