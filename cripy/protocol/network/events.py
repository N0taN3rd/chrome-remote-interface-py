from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DataReceivedEvent(BaseEvent):
    """Fired when data chunk was received over the network."""

    event: str = "Network.dataReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param int dataLength: Data chunk length.
        :type dataLength: int
        :param int encodedDataLength: Actual bytes received (might be less than dataLength for compressed encodings).
        :type encodedDataLength: int
        """
        super().__init__()


class EventSourceMessageReceivedEvent(BaseEvent):
    """Fired when EventSource message is received."""

    event: str = "Network.eventSourceMessageReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param str eventName: Message type.
        :type eventName: str
        :param str eventId: Message identifier.
        :type eventId: str
        :param str data: Message content.
        :type data: str
        """
        super().__init__()


class LoadingFailedEvent(BaseEvent):
    """Fired when HTTP request has failed to load."""

    event: str = "Network.loadingFailed"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param Page.ResourceType type: Resource type.
        :type type: Page.ResourceType
        :param str errorText: User friendly error message.
        :type errorText: str
        :param bool canceled: True if loading was canceled.
        :type canceled: bool
        :param BlockedReason blockedReason: The reason why loading was blocked, if any.
        :type blockedReason: BlockedReason
        """
        super().__init__()


class LoadingFinishedEvent(BaseEvent):
    """Fired when HTTP request has finished loading."""

    event: str = "Network.loadingFinished"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param float encodedDataLength: Total number of bytes received for this request.
        :type encodedDataLength: float
        :param bool blockedCrossSiteDocument: Set when response was blocked due to being cross-site document response.
        :type blockedCrossSiteDocument: bool
        """
        super().__init__()


class RequestInterceptedEvent(BaseEvent):
    """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked."""

    event: str = "Network.requestIntercepted"

    def __init__(self) -> None:
        """
        :param InterceptionId interceptionId: Each request the page makes will have a unique id, however if any redirects are encountered while processing that fetch, they will be reported with the same id as the original fetch. Likewise if HTTP authentication is needed then the same fetch id will be used.
        :type interceptionId: InterceptionId
        :param Request request: The request
        :type request: Request
        :param Page.FrameId frameId: The id of the frame that initiated the request.
        :type frameId: Page.FrameId
        :param Page.ResourceType resourceType: How the requested resource will be used.
        :type resourceType: Page.ResourceType
        :param bool isNavigationRequest: Whether this is a navigation request, which can abort the navigation completely.
        :type isNavigationRequest: bool
        :param bool isDownload: Set if the request is a navigation that will result in a download. Only present after response is received from the server (i.e. HeadersReceived stage).
        :type isDownload: bool
        :param str redirectUrl: Redirect location, only sent if a redirect was intercepted.
        :type redirectUrl: str
        :param AuthChallenge authChallenge: Details of the Authorization Challenge encountered. If this is set then continueInterceptedRequest must contain an authChallengeResponse.
        :type authChallenge: AuthChallenge
        :param ErrorReason responseErrorReason: Response error if intercepted at response stage or if redirect occurred while intercepting request.
        :type responseErrorReason: ErrorReason
        :param int responseStatusCode: Response code if intercepted at response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseStatusCode: int
        :param Headers responseHeaders: Response headers if intercepted at the response stage or if redirect occurred while intercepting request or auth retry occurred.
        :type responseHeaders: Headers
        """
        super().__init__()


class RequestServedFromCacheEvent(BaseEvent):
    """Fired if request ended up loading from cache."""

    event: str = "Network.requestServedFromCache"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        """
        super().__init__()


class RequestWillBeSentEvent(BaseEvent):
    """Fired when page is about to send HTTP request."""

    event: str = "Network.requestWillBeSent"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param LoaderId loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: LoaderId
        :param str documentURL: URL of the document this request is loaded for.
        :type documentURL: str
        :param Request request: Request data.
        :type request: Request
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param TimeSinceEpoch wallTime: Timestamp.
        :type wallTime: TimeSinceEpoch
        :param Initiator initiator: Request initiator.
        :type initiator: Initiator
        :param Response redirectResponse: Redirect response data.
        :type redirectResponse: Response
        :param Page.ResourceType type: Type of this resource.
        :type type: Page.ResourceType
        :param Page.FrameId frameId: Frame identifier.
        :type frameId: Page.FrameId
        :param bool hasUserGesture: Whether the request is initiated by a user gesture. Defaults to false.
        :type hasUserGesture: bool
        """
        super().__init__()


class ResourceChangedPriorityEvent(BaseEvent):
    """Fired when resource loading priority is changed"""

    event: str = "Network.resourceChangedPriority"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param ResourcePriority newPriority: New priority
        :type newPriority: ResourcePriority
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        """
        super().__init__()


class SignedExchangeReceivedEvent(BaseEvent):
    """Fired when a signed exchange was received over the network"""

    event: str = "Network.signedExchangeReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param SignedExchangeInfo info: Information about the signed exchange response.
        :type info: SignedExchangeInfo
        """
        super().__init__()


class ResponseReceivedEvent(BaseEvent):
    """Fired when HTTP response is available."""

    event: str = "Network.responseReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param LoaderId loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: LoaderId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param Page.ResourceType type: Resource type.
        :type type: Page.ResourceType
        :param Response response: Response data.
        :type response: Response
        :param Page.FrameId frameId: Frame identifier.
        :type frameId: Page.FrameId
        """
        super().__init__()


class WebSocketClosedEvent(BaseEvent):
    """Fired when WebSocket is closed."""

    event: str = "Network.webSocketClosed"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        """
        super().__init__()


class WebSocketCreatedEvent(BaseEvent):
    """Fired upon WebSocket creation."""

    event: str = "Network.webSocketCreated"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param str url: WebSocket request URL.
        :type url: str
        :param Initiator initiator: Request initiator.
        :type initiator: Initiator
        """
        super().__init__()


class WebSocketFrameErrorEvent(BaseEvent):
    """Fired when WebSocket frame error occurs."""

    event: str = "Network.webSocketFrameError"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param str errorMessage: WebSocket frame error message.
        :type errorMessage: str
        """
        super().__init__()


class WebSocketFrameReceivedEvent(BaseEvent):
    """Fired when WebSocket frame is received."""

    event: str = "Network.webSocketFrameReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param WebSocketFrame response: WebSocket response data.
        :type response: WebSocketFrame
        """
        super().__init__()


class WebSocketFrameSentEvent(BaseEvent):
    """Fired when WebSocket frame is sent."""

    event: str = "Network.webSocketFrameSent"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param WebSocketFrame response: WebSocket response data.
        :type response: WebSocketFrame
        """
        super().__init__()


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):
    """Fired when WebSocket handshake response becomes available."""

    event: str = "Network.webSocketHandshakeResponseReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param WebSocketResponse response: WebSocket response data.
        :type response: WebSocketResponse
        """
        super().__init__()


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):
    """Fired when WebSocket is about to initiate handshake."""

    event: str = "Network.webSocketWillSendHandshakeRequest"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :type requestId: RequestId
        :param MonotonicTime timestamp: Timestamp.
        :type timestamp: MonotonicTime
        :param TimeSinceEpoch wallTime: UTC Timestamp.
        :type wallTime: TimeSinceEpoch
        :param WebSocketRequest request: WebSocket request data.
        :type request: WebSocketRequest
        """
        super().__init__()


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

