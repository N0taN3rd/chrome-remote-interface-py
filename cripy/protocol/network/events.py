from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DataReceivedEvent(BaseEvent):
    """Fired when data chunk was received over the network."""

    event: str = "Network.dataReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param dataLength: Data chunk length.
        :type int:
        :param encodedDataLength: Actual bytes received (might be less than dataLength for compressed encodings).
        :type int:
        """
        super().__init__()


class EventSourceMessageReceivedEvent(BaseEvent):
    """Fired when EventSource message is received."""

    event: str = "Network.eventSourceMessageReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param eventName: Message type.
        :type str:
        :param eventId: Message identifier.
        :type str:
        :param data: Message content.
        :type str:
        """
        super().__init__()


class LoadingFailedEvent(BaseEvent):
    """Fired when HTTP request has failed to load."""

    event: str = "Network.loadingFailed"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param type: Resource type.
        :type Page.ResourceType:
        :param errorText: User friendly error message.
        :type str:
        :param canceled: True if loading was canceled.
        :type bool:
        :param blockedReason: The reason why loading was blocked, if any.
        :type BlockedReason:
        """
        super().__init__()


class LoadingFinishedEvent(BaseEvent):
    """Fired when HTTP request has finished loading."""

    event: str = "Network.loadingFinished"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param encodedDataLength: Total number of bytes received for this request.
        :type float:
        :param blockedCrossSiteDocument: Set when response was blocked due to being cross-site document response.
        :type bool:
        """
        super().__init__()


class RequestInterceptedEvent(BaseEvent):
    """Details of an intercepted HTTP request, which must be either allowed, blocked, modified or mocked."""

    event: str = "Network.requestIntercepted"

    def __init__(self) -> None:
        """
        :param interceptionId: Each request the page makes will have a unique id, however if any redirects are
        encountered while processing that fetch, they will be reported with the same id as
        the original fetch. Likewise if HTTP authentication is needed then the same fetch id
        will be used.
        :type InterceptionId:
        :param request: The request
        :type Request:
        :param frameId: The id of the frame that initiated the request.
        :type Page.FrameId:
        :param resourceType: How the requested resource will be used.
        :type Page.ResourceType:
        :param isNavigationRequest: Whether this is a navigation request, which can abort the navigation completely.
        :type bool:
        :param isDownload: Set if the request is a navigation that will result in a download. Only present after
        response is received from the server (i.e. HeadersReceived stage).
        :type bool:
        :param redirectUrl: Redirect location, only sent if a redirect was intercepted.
        :type str:
        :param authChallenge: Details of the Authorization Challenge encountered. If this is set then
        continueInterceptedRequest must contain an authChallengeResponse.
        :type AuthChallenge:
        :param responseErrorReason: Response error if intercepted at response stage or if redirect occurred while
        intercepting request.
        :type ErrorReason:
        :param responseStatusCode: Response code if intercepted at response stage or if redirect occurred while
        intercepting request or auth retry occurred.
        :type int:
        :param responseHeaders: Response headers if intercepted at the response stage or if redirect occurred while
        intercepting request or auth retry occurred.
        :type Headers:
        """
        super().__init__()


class RequestServedFromCacheEvent(BaseEvent):
    """Fired if request ended up loading from cache."""

    event: str = "Network.requestServedFromCache"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        """
        super().__init__()


class RequestWillBeSentEvent(BaseEvent):
    """Fired when page is about to send HTTP request."""

    event: str = "Network.requestWillBeSent"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type LoaderId:
        :param documentURL: URL of the document this request is loaded for.
        :type str:
        :param request: Request data.
        :type Request:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param wallTime: Timestamp.
        :type TimeSinceEpoch:
        :param initiator: Request initiator.
        :type Initiator:
        :param redirectResponse: Redirect response data.
        :type Response:
        :param type: Type of this resource.
        :type Page.ResourceType:
        :param frameId: Frame identifier.
        :type Page.FrameId:
        :param hasUserGesture: Whether the request is initiated by a user gesture. Defaults to false.
        :type bool:
        """
        super().__init__()


class ResourceChangedPriorityEvent(BaseEvent):
    """Fired when resource loading priority is changed"""

    event: str = "Network.resourceChangedPriority"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param newPriority: New priority
        :type ResourcePriority:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        """
        super().__init__()


class SignedExchangeReceivedEvent(BaseEvent):
    """Fired when a signed exchange was received over the network"""

    event: str = "Network.signedExchangeReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param info: Information about the signed exchange response.
        :type SignedExchangeInfo:
        """
        super().__init__()


class ResponseReceivedEvent(BaseEvent):
    """Fired when HTTP response is available."""

    event: str = "Network.responseReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type LoaderId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param type: Resource type.
        :type Page.ResourceType:
        :param response: Response data.
        :type Response:
        :param frameId: Frame identifier.
        :type Page.FrameId:
        """
        super().__init__()


class WebSocketClosedEvent(BaseEvent):
    """Fired when WebSocket is closed."""

    event: str = "Network.webSocketClosed"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        """
        super().__init__()


class WebSocketCreatedEvent(BaseEvent):
    """Fired upon WebSocket creation."""

    event: str = "Network.webSocketCreated"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param url: WebSocket request URL.
        :type str:
        :param initiator: Request initiator.
        :type Initiator:
        """
        super().__init__()


class WebSocketFrameErrorEvent(BaseEvent):
    """Fired when WebSocket frame error occurs."""

    event: str = "Network.webSocketFrameError"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param errorMessage: WebSocket frame error message.
        :type str:
        """
        super().__init__()


class WebSocketFrameReceivedEvent(BaseEvent):
    """Fired when WebSocket frame is received."""

    event: str = "Network.webSocketFrameReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param response: WebSocket response data.
        :type WebSocketFrame:
        """
        super().__init__()


class WebSocketFrameSentEvent(BaseEvent):
    """Fired when WebSocket frame is sent."""

    event: str = "Network.webSocketFrameSent"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param response: WebSocket response data.
        :type WebSocketFrame:
        """
        super().__init__()


class WebSocketHandshakeResponseReceivedEvent(BaseEvent):
    """Fired when WebSocket handshake response becomes available."""

    event: str = "Network.webSocketHandshakeResponseReceived"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param response: WebSocket response data.
        :type WebSocketResponse:
        """
        super().__init__()


class WebSocketWillSendHandshakeRequestEvent(BaseEvent):
    """Fired when WebSocket is about to initiate handshake."""

    event: str = "Network.webSocketWillSendHandshakeRequest"

    def __init__(self) -> None:
        """
        :param requestId: Request identifier.
        :type RequestId:
        :param timestamp: Timestamp.
        :type MonotonicTime:
        :param wallTime: UTC Timestamp.
        :type TimeSinceEpoch:
        :param request: WebSocket request data.
        :type WebSocketRequest:
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

