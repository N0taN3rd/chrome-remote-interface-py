from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DataReceivedEvent(BaseEvent):
    """Fired when data chunk was received over the network."""

    event: str = "Network.dataReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param int dataLength: Data chunk length.
        :param int encodedDataLength: Actual bytes received (might be less than dataLength for compressed encodings).
        """
        super().__init__()


class EventSourceMessageReceivedEvent(BaseEvent):
    """Fired when EventSource message is received."""

    event: str = "Network.eventSourceMessageReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param str eventName: Message type.
        :param str eventId: Message identifier.
        :param str data: Message content.
        """
        super().__init__()


class LoadingFailedEvent(BaseEvent):
    """Fired when HTTP request has failed to load."""

    event: str = "Network.loadingFailed"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param Page.ResourceType type: Resource type.
        :param str errorText: User friendly error message.
        :param bool canceled: True if loading was canceled.
        :param BlockedReason blockedReason: The reason why loading was blocked, if any.
        """
        super().__init__()


class LoadingFinishedEvent(BaseEvent):
    """Fired when HTTP request has finished loading."""

    event: str = "Network.loadingFinished"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param float encodedDataLength: Total number of bytes received for this request.
        :param bool blockedCrossSiteDocument: Set when response was blocked due to being cross-site document response.
        """
        super().__init__()


class RequestInterceptedEvent(BaseEvent):
    """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked."""

    event: str = "Network.requestIntercepted"

    def __init__(self) -> None:
        """
        :param InterceptionId interceptionId: Each request the page makes will have a unique id, however if any redirects are encountered while processing that fetch, they will be reported with the same id as the original fetch. Likewise if HTTP authentication is needed then the same fetch id will be used.
        :param Request request: The request
        :param Page.FrameId frameId: The id of the frame that initiated the request.
        :param Page.ResourceType resourceType: How the requested resource will be used.
        :param bool isNavigationRequest: Whether this is a navigation request, which can abort the navigation completely.
        :param bool isDownload: Set if the request is a navigation that will result in a download. Only present after response is received from the server (i.e. HeadersReceived stage).
        :param str redirectUrl: Redirect location, only sent if a redirect was intercepted.
        :param AuthChallenge authChallenge: Details of the Authorization Challenge encountered. If this is set then continueInterceptedRequest must contain an authChallengeResponse.
        :param ErrorReason responseErrorReason: Response error if intercepted at response stage or if redirect occurred while intercepting request.
        :param int responseStatusCode: Response code if intercepted at response stage or if redirect occurred while intercepting request or auth retry occurred.
        :param Headers responseHeaders: Response headers if intercepted at the response stage or if redirect occurred while intercepting request or auth retry occurred.
        """
        super().__init__()


class RequestServedFromCacheEvent(BaseEvent):
    """Fired if request ended up loading from cache."""

    event: str = "Network.requestServedFromCache"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        """
        super().__init__()


class RequestWillBeSentEvent(BaseEvent):
    """Fired when page is about to send HTTP request."""

    event: str = "Network.requestWillBeSent"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param LoaderId loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :param str documentURL: URL of the document this request is loaded for.
        :param Request request: Request data.
        :param MonotonicTime timestamp: Timestamp.
        :param TimeSinceEpoch wallTime: Timestamp.
        :param Initiator initiator: Request initiator.
        :param Response redirectResponse: Redirect response data.
        :param Page.ResourceType type: Type of this resource.
        :param Page.FrameId frameId: Frame identifier.
        :param bool hasUserGesture: Whether the request is initiated by a user gesture. Defaults to false.
        """
        super().__init__()


class ResourceChangedPriorityEvent(BaseEvent):
    """Fired when resource loading priority is changed"""

    event: str = "Network.resourceChangedPriority"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param ResourcePriority newPriority: New priority
        :param MonotonicTime timestamp: Timestamp.
        """
        super().__init__()


class SignedExchangeReceivedEvent(BaseEvent):
    """Fired when a signed exchange was received over the network"""

    event: str = "Network.signedExchangeReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param SignedExchangeInfo info: Information about the signed exchange response.
        """
        super().__init__()


class ResponseReceivedEvent(BaseEvent):
    """Fired when HTTP response is available."""

    event: str = "Network.responseReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param LoaderId loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :param MonotonicTime timestamp: Timestamp.
        :param Page.ResourceType type: Resource type.
        :param Response response: Response data.
        :param Page.FrameId frameId: Frame identifier.
        """
        super().__init__()


class WebSocketClosedEvent(BaseEvent):
    """Fired when WebSocket is closed."""

    event: str = "Network.webSocketClosed"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        """
        super().__init__()


class WebSocketCreatedEvent(BaseEvent):
    """Fired upon WebSocket creation."""

    event: str = "Network.webSocketCreated"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param str url: WebSocket request URL.
        :param Initiator initiator: Request initiator.
        """
        super().__init__()


class WebSocketFrameErrorEvent(BaseEvent):
    """Fired when WebSocket frame error occurs."""

    event: str = "Network.webSocketFrameError"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param str errorMessage: WebSocket frame error message.
        """
        super().__init__()


class WebSocketFrameReceivedEvent(BaseEvent):
    """Fired when WebSocket frame is received."""

    event: str = "Network.webSocketFrameReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param WebSocketFrame response: WebSocket response data.
        """
        super().__init__()


class WebSocketFrameSentEvent(BaseEvent):
    """Fired when WebSocket frame is sent."""

    event: str = "Network.webSocketFrameSent"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param WebSocketFrame response: WebSocket response data.
        """
        super().__init__()


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):
    """Fired when WebSocket handshake response becomes available."""

    event: str = "Network.webSocketHandshakeResponseReceived"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param WebSocketResponse response: WebSocket response data.
        """
        super().__init__()


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):
    """Fired when WebSocket is about to initiate handshake."""

    event: str = "Network.webSocketWillSendHandshakeRequest"

    def __init__(self) -> None:
        """
        :param RequestId requestId: Request identifier.
        :param MonotonicTime timestamp: Timestamp.
        :param TimeSinceEpoch wallTime: UTC Timestamp.
        :param WebSocketRequest request: WebSocket request data.
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

