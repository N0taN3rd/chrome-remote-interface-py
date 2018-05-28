from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.page import types as Page
from cripy.protocol.network.types import (
    ErrorReason,
    LoaderId,
    Response,
    ResourcePriority,
    SignedExchangeInfo,
    WebSocketRequest,
    RequestId,
    InterceptionId,
    AuthChallenge,
    Initiator,
    WebSocketResponse,
    MonotonicTime,
    TimeSinceEpoch,
    WebSocketFrame,
    Request,
    Headers,
    BlockedReason,
)


class DataReceivedEvent(BaseEvent):
    """Fired when data chunk was received over the network."""

    event: str = "Network.dataReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, dataLength: int, encodedDataLength: int) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param dataLength: Data chunk length.
        :type dataLength: int
        :param encodedDataLength: Actual bytes received (might be less than dataLength for compressed encodings).
        :type encodedDataLength: int
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.dataLength: int = dataLength
        self.encodedDataLength: int = encodedDataLength


class EventSourceMessageReceivedEvent(BaseEvent):
    """Fired when EventSource message is received."""

    event: str = "Network.eventSourceMessageReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, eventName: str, eventId: str, data: str) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param eventName: Message type.
        :type eventName: str
        :param eventId: Message identifier.
        :type eventId: str
        :param data: Message content.
        :type data: str
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.eventName: str = eventName
        self.eventId: str = eventId
        self.data: str = data


class LoadingFailedEvent(BaseEvent):
    """Fired when HTTP request has failed to load."""

    event: str = "Network.loadingFailed"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, type: Page.ResourceType, errorText: str, canceled: Optional[bool] = None, blockedReason: Optional[BlockedReason] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param type: Resource type.
        :type type: Page.ResourceType
        :param errorText: User friendly error message.
        :type errorText: str
        :param canceled: True if loading was canceled.
        :type canceled: bool
        :param blockedReason: The reason why loading was blocked, if any.
        :type blockedReason: BlockedReason
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.type: Page.ResourceType = type
        self.errorText: str = errorText
        self.canceled: Optional[bool] = canceled
        self.blockedReason: Optional[BlockedReason] = blockedReason


class LoadingFinishedEvent(BaseEvent):
    """Fired when HTTP request has finished loading."""

    event: str = "Network.loadingFinished"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, encodedDataLength: float, blockedCrossSiteDocument: Optional[bool] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param encodedDataLength: Total number of bytes received for this request.
        :type encodedDataLength: float
        :param blockedCrossSiteDocument: Set when response was blocked due to being cross-site document response.
        :type blockedCrossSiteDocument: bool
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.encodedDataLength: float = encodedDataLength
        self.blockedCrossSiteDocument: Optional[bool] = blockedCrossSiteDocument


class RequestInterceptedEvent(BaseEvent):
    """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked."""

    event: str = "Network.requestIntercepted"

    def __init__(self, interceptionId: InterceptionId, request: Request, frameId: Page.FrameId, resourceType: Page.ResourceType, isNavigationRequest: bool, isDownload: Optional[bool] = None, redirectUrl: Optional[str] = None, authChallenge: Optional[AuthChallenge] = None, responseErrorReason: Optional[ErrorReason] = None, responseStatusCode: Optional[int] = None, responseHeaders: Optional[Headers] = None) -> None:
        """
        :param interceptionId: Each request the page makes will have a unique id, however if any redirects are encountered while processing that fetch, they will be reported with the same id as the original fetch. Likewise if HTTP authentication is needed then the same fetch id will be used.
        :type interceptionId: InterceptionId
        :param request: The request
        :type request: Request
        :param frameId: The id of the frame that initiated the request.
        :type frameId: Page.FrameId
        :param resourceType: How the requested resource will be used.
        :type resourceType: Page.ResourceType
        :param isNavigationRequest: Whether this is a navigation request, which can abort the navigation completely.
        :type isNavigationRequest: bool
        :param isDownload: Set if the request is a navigation that will result in a download. Only present after response is received from the server (i.e. HeadersReceived stage).
        :type isDownload: bool
        :param redirectUrl: Redirect location, only sent if a redirect was intercepted.
        :type redirectUrl: str
        :param authChallenge: Details of the Authorization Challenge encountered. If this is set then continueInterceptedRequest must contain an authChallengeResponse.
        :type authChallenge: AuthChallenge
        :param responseErrorReason: Response error if intercepted at response stage or if redirect occurred while intercepting request.
        :type responseErrorReason: ErrorReason
        :param responseStatusCode: Response code if intercepted at response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseStatusCode: int
        :param responseHeaders: Response headers if intercepted at the response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseHeaders: Headers
        """
        super().__init__()
        self.interceptionId: InterceptionId = interceptionId
        self.request: Request = request
        self.frameId: Page.FrameId = frameId
        self.resourceType: Page.ResourceType = resourceType
        self.isNavigationRequest: bool = isNavigationRequest
        self.isDownload: Optional[bool] = isDownload
        self.redirectUrl: Optional[str] = redirectUrl
        self.authChallenge: Optional[AuthChallenge] = authChallenge
        self.responseErrorReason: Optional[ErrorReason] = responseErrorReason
        self.responseStatusCode: Optional[int] = responseStatusCode
        self.responseHeaders: Optional[Headers] = responseHeaders


class RequestServedFromCacheEvent(BaseEvent):
    """Fired if request ended up loading from cache."""

    event: str = "Network.requestServedFromCache"

    def __init__(self, requestId: RequestId) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        """
        super().__init__()
        self.requestId: RequestId = requestId


class RequestWillBeSentEvent(BaseEvent):
    """Fired when page is about to send HTTP request."""

    event: str = "Network.requestWillBeSent"

    def __init__(self, requestId: RequestId, loaderId: LoaderId, documentURL: str, request: Request, timestamp: MonotonicTime, wallTime: TimeSinceEpoch, initiator: Initiator, redirectResponse: Optional[Response] = None, type: Optional[Page.ResourceType] = None, frameId: Optional[Page.FrameId] = None, hasUserGesture: Optional[bool] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: LoaderId
        :param documentURL: URL of the document this request is loaded for.
        :type documentURL: str
        :param request: Request data.
        :type request: Request
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param wallTime: Timestamp.
        :type wallTime: TimeSinceEpoch
        :param initiator: Request initiator.
        :type initiator: Initiator
        :param redirectResponse: Redirect response data.
        :type redirectResponse: Response
        :param type: Type of this resource.
        :type type: Page.ResourceType
        :param frameId: Frame identifier.
        :type frameId: Page.FrameId
        :param hasUserGesture: Whether the request is initiated by a user gesture. Defaults to false.
        :type hasUserGesture: bool
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.loaderId: LoaderId = loaderId
        self.documentURL: str = documentURL
        self.request: Request = request
        self.timestamp: MonotonicTime = timestamp
        self.wallTime: TimeSinceEpoch = wallTime
        self.initiator: Initiator = initiator
        self.redirectResponse: Optional[Response] = redirectResponse
        self.type: Optional[Page.ResourceType] = type
        self.frameId: Optional[Page.FrameId] = frameId
        self.hasUserGesture: Optional[bool] = hasUserGesture


class ResourceChangedPriorityEvent(BaseEvent):
    """Fired when resource loading priority is changed"""

    event: str = "Network.resourceChangedPriority"

    def __init__(self, requestId: RequestId, newPriority: ResourcePriority, timestamp: MonotonicTime) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param newPriority: New priority
        :type newPriority: ResourcePriority
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.newPriority: ResourcePriority = newPriority
        self.timestamp: MonotonicTime = timestamp


class SignedExchangeReceivedEvent(BaseEvent):
    """Fired when a signed exchange was received over the network"""

    event: str = "Network.signedExchangeReceived"

    def __init__(self, requestId: RequestId, info: SignedExchangeInfo) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param info: Information about the signed exchange response.
        :type info: SignedExchangeInfo
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.info: SignedExchangeInfo = info


class ResponseReceivedEvent(BaseEvent):
    """Fired when HTTP response is available."""

    event: str = "Network.responseReceived"

    def __init__(self, requestId: RequestId, loaderId: LoaderId, timestamp: MonotonicTime, type: Page.ResourceType, response: Response, frameId: Optional[Page.FrameId] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: LoaderId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param type: Resource type.
        :type type: Page.ResourceType
        :param response: Response data.
        :type response: Response
        :param frameId: Frame identifier.
        :type frameId: Page.FrameId
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.loaderId: LoaderId = loaderId
        self.timestamp: MonotonicTime = timestamp
        self.type: Page.ResourceType = type
        self.response: Response = response
        self.frameId: Optional[Page.FrameId] = frameId


class WebSocketClosedEvent(BaseEvent):
    """Fired when WebSocket is closed."""

    event: str = "Network.webSocketClosed"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp


class WebSocketCreatedEvent(BaseEvent):
    """Fired upon WebSocket creation."""

    event: str = "Network.webSocketCreated"

    def __init__(self, requestId: RequestId, url: str, initiator: Optional[Initiator] = None) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param url: WebSocket request URL.
        :type url: str
        :param initiator: Request initiator.
        :type initiator: Initiator
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.url: str = url
        self.initiator: Optional[Initiator] = initiator


class WebSocketFrameErrorEvent(BaseEvent):
    """Fired when WebSocket frame error occurs."""

    event: str = "Network.webSocketFrameError"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, errorMessage: str) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param errorMessage: WebSocket frame error message.
        :type errorMessage: str
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.errorMessage: str = errorMessage


class WebSocketFrameReceivedEvent(BaseEvent):
    """Fired when WebSocket frame is received."""

    event: str = "Network.webSocketFrameReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: WebSocketFrame) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param response: WebSocket response data.
        :type response: WebSocketFrame
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.response: WebSocketFrame = response


class WebSocketFrameSentEvent(BaseEvent):
    """Fired when WebSocket frame is sent."""

    event: str = "Network.webSocketFrameSent"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: WebSocketFrame) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param response: WebSocket response data.
        :type response: WebSocketFrame
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.response: WebSocketFrame = response


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):
    """Fired when WebSocket handshake response becomes available."""

    event: str = "Network.webSocketHandshakeResponseReceived"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, response: WebSocketResponse) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param response: WebSocket response data.
        :type response: WebSocketResponse
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.response: WebSocketResponse = response


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):
    """Fired when WebSocket is about to initiate handshake."""

    event: str = "Network.webSocketWillSendHandshakeRequest"

    def __init__(self, requestId: RequestId, timestamp: MonotonicTime, wallTime: TimeSinceEpoch, request: WebSocketRequest) -> None:
        """
        :param requestId: Request identifier.
        :type requestId: RequestId
        :param timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param wallTime: UTC Timestamp.
        :type wallTime: TimeSinceEpoch
        :param request: WebSocket request data.
        :type request: WebSocketRequest
        """
        super().__init__()
        self.requestId: RequestId = requestId
        self.timestamp: MonotonicTime = timestamp
        self.wallTime: TimeSinceEpoch = wallTime
        self.request: WebSocketRequest = request


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

