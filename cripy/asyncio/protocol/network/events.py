from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.network.types import *

__all__ = [
    "DataReceivedEvent",
    "EventSourceMessageReceivedEvent",
    "LoadingFailedEvent",
    "LoadingFinishedEvent",
    "RequestInterceptedEvent",
    "RequestServedFromCacheEvent",
    "RequestWillBeSentEvent",
    "ResourceChangedPriorityEvent",
    "SignedExchangeReceivedEvent",
    "ResponseReceivedEvent",
    "WebSocketClosedEvent",
    "WebSocketCreatedEvent",
    "WebSocketFrameErrorEvent",
    "WebSocketFrameReceivedEvent",
    "WebSocketFrameSentEvent",
    "WebSocketHandshakeResponseReceivedEvent",
    "WebSocketWillSendHandshakeRequestEvent",
    "NETWORK_EVENTS_TO_CLASS",
    "NETWORK_EVENTS_NS"
]


class DataReceivedEvent(object):
    """
    Fired when data chunk was received over the network.
    """


    __slots__ = ["requestId", "timestamp", "dataLength", "encodedDataLength"]

    def __init__(self, requestId: str, timestamp: float, dataLength: int, encodedDataLength: int) -> None:
        """
        Create a new instance of DataReceivedEvent

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
        return "DataReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DataReceivedEvent', dict]]:
        """
        Safely create DataReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DataReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DataReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, DataReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = DataReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DataReceivedEvent', dict]]]:
        """
        Safely create a new list DataReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DataReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DataReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DataReceivedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "eventName", "eventId", "data"]

    def __init__(self, requestId: str, timestamp: float, eventName: str, eventId: str, data: str) -> None:
        """
        Create a new instance of EventSourceMessageReceivedEvent

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
        return "EventSourceMessageReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['EventSourceMessageReceivedEvent', dict]]:
        """
        Safely create EventSourceMessageReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of EventSourceMessageReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of EventSourceMessageReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, EventSourceMessageReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = EventSourceMessageReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['EventSourceMessageReceivedEvent', dict]]]:
        """
        Safely create a new list EventSourceMessageReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list EventSourceMessageReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of EventSourceMessageReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, EventSourceMessageReceivedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "type", "errorText", "canceled", "blockedReason"]

    def __init__(self, requestId: str, timestamp: float, type: str, errorText: str, canceled: Optional[bool] = None, blockedReason: Optional[str] = None) -> None:
        """
        Create a new instance of LoadingFailedEvent

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
        return "LoadingFailedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['LoadingFailedEvent', dict]]:
        """
        Safely create LoadingFailedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LoadingFailedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LoadingFailedEvent if creation did not fail
        :rtype: Optional[Union[dict, LoadingFailedEvent]]
        """
        if init is not None:
            try:
                ourselves = LoadingFailedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['LoadingFailedEvent', dict]]]:
        """
        Safely create a new list LoadingFailedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LoadingFailedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LoadingFailedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LoadingFailedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "encodedDataLength", "shouldReportCorbBlocking"]

    def __init__(self, requestId: str, timestamp: float, encodedDataLength: float, shouldReportCorbBlocking: Optional[bool] = None) -> None:
        """
        Create a new instance of LoadingFinishedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.encodedDataLength is not None:
            repr_args.append("encodedDataLength={!r}".format(self.encodedDataLength))
        if self.shouldReportCorbBlocking is not None:
            repr_args.append("shouldReportCorbBlocking={!r}".format(self.shouldReportCorbBlocking))
        return "LoadingFinishedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['LoadingFinishedEvent', dict]]:
        """
        Safely create LoadingFinishedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LoadingFinishedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LoadingFinishedEvent if creation did not fail
        :rtype: Optional[Union[dict, LoadingFinishedEvent]]
        """
        if init is not None:
            try:
                ourselves = LoadingFinishedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['LoadingFinishedEvent', dict]]]:
        """
        Safely create a new list LoadingFinishedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LoadingFinishedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LoadingFinishedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LoadingFinishedEvent]]]
        """
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


    __slots__ = ["interceptionId", "request", "frameId", "resourceType", "isNavigationRequest", "isDownload", "redirectUrl", "authChallenge", "responseErrorReason", "responseStatusCode", "responseHeaders"]

    def __init__(self, interceptionId: str, request: Union[Request, dict], frameId: str, resourceType: str, isNavigationRequest: bool, isDownload: Optional[bool] = None, redirectUrl: Optional[str] = None, authChallenge: Optional[Union[AuthChallenge, dict]] = None, responseErrorReason: Optional[str] = None, responseStatusCode: Optional[int] = None, responseHeaders: Optional[Union[Headers, dict]] = None) -> None:
        """
        Create a new instance of RequestInterceptedEvent

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
            repr_args.append("isNavigationRequest={!r}".format(self.isNavigationRequest))
        if self.isDownload is not None:
            repr_args.append("isDownload={!r}".format(self.isDownload))
        if self.redirectUrl is not None:
            repr_args.append("redirectUrl={!r}".format(self.redirectUrl))
        if self.authChallenge is not None:
            repr_args.append("authChallenge={!r}".format(self.authChallenge))
        if self.responseErrorReason is not None:
            repr_args.append("responseErrorReason={!r}".format(self.responseErrorReason))
        if self.responseStatusCode is not None:
            repr_args.append("responseStatusCode={!r}".format(self.responseStatusCode))
        if self.responseHeaders is not None:
            repr_args.append("responseHeaders={!r}".format(self.responseHeaders))
        return "RequestInterceptedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RequestInterceptedEvent', dict]]:
        """
        Safely create RequestInterceptedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RequestInterceptedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RequestInterceptedEvent if creation did not fail
        :rtype: Optional[Union[dict, RequestInterceptedEvent]]
        """
        if init is not None:
            try:
                ourselves = RequestInterceptedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['RequestInterceptedEvent', dict]]]:
        """
        Safely create a new list RequestInterceptedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RequestInterceptedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RequestInterceptedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, RequestInterceptedEvent]]]
        """
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


    __slots__ = ["requestId"]

    def __init__(self, requestId: str) -> None:
        """
        Create a new instance of RequestServedFromCacheEvent

        :param requestId: Request identifier.
        :type requestId: str
        """
        super().__init__()
        self.requestId = requestId

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        return "RequestServedFromCacheEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RequestServedFromCacheEvent', dict]]:
        """
        Safely create RequestServedFromCacheEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RequestServedFromCacheEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RequestServedFromCacheEvent if creation did not fail
        :rtype: Optional[Union[dict, RequestServedFromCacheEvent]]
        """
        if init is not None:
            try:
                ourselves = RequestServedFromCacheEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['RequestServedFromCacheEvent', dict]]]:
        """
        Safely create a new list RequestServedFromCacheEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RequestServedFromCacheEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RequestServedFromCacheEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, RequestServedFromCacheEvent]]]
        """
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


    __slots__ = ["requestId", "loaderId", "documentURL", "request", "timestamp", "wallTime", "initiator", "redirectResponse", "type", "frameId", "hasUserGesture"]

    def __init__(self, requestId: str, loaderId: str, documentURL: str, request: Union[Request, dict], timestamp: float, wallTime: float, initiator: Union[Initiator, dict], redirectResponse: Optional[Union[Response, dict]] = None, type: Optional[str] = None, frameId: Optional[str] = None, hasUserGesture: Optional[bool] = None) -> None:
        """
        Create a new instance of RequestWillBeSentEvent

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
        return "RequestWillBeSentEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RequestWillBeSentEvent', dict]]:
        """
        Safely create RequestWillBeSentEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RequestWillBeSentEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RequestWillBeSentEvent if creation did not fail
        :rtype: Optional[Union[dict, RequestWillBeSentEvent]]
        """
        if init is not None:
            try:
                ourselves = RequestWillBeSentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['RequestWillBeSentEvent', dict]]]:
        """
        Safely create a new list RequestWillBeSentEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RequestWillBeSentEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RequestWillBeSentEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, RequestWillBeSentEvent]]]
        """
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


    __slots__ = ["requestId", "newPriority", "timestamp"]

    def __init__(self, requestId: str, newPriority: str, timestamp: float) -> None:
        """
        Create a new instance of ResourceChangedPriorityEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.newPriority is not None:
            repr_args.append("newPriority={!r}".format(self.newPriority))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "ResourceChangedPriorityEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ResourceChangedPriorityEvent', dict]]:
        """
        Safely create ResourceChangedPriorityEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ResourceChangedPriorityEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ResourceChangedPriorityEvent if creation did not fail
        :rtype: Optional[Union[dict, ResourceChangedPriorityEvent]]
        """
        if init is not None:
            try:
                ourselves = ResourceChangedPriorityEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ResourceChangedPriorityEvent', dict]]]:
        """
        Safely create a new list ResourceChangedPriorityEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ResourceChangedPriorityEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ResourceChangedPriorityEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ResourceChangedPriorityEvent]]]
        """
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


    __slots__ = ["requestId", "info"]

    def __init__(self, requestId: str, info: Union[SignedExchangeInfo, dict]) -> None:
        """
        Create a new instance of SignedExchangeReceivedEvent

        :param requestId: Request identifier.
        :type requestId: str
        :param info: Information about the signed exchange response.
        :type info: dict
        """
        super().__init__()
        self.requestId = requestId
        self.info = SignedExchangeInfo.safe_create(info)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.info is not None:
            repr_args.append("info={!r}".format(self.info))
        return "SignedExchangeReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SignedExchangeReceivedEvent', dict]]:
        """
        Safely create SignedExchangeReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SignedExchangeReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SignedExchangeReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, SignedExchangeReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = SignedExchangeReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SignedExchangeReceivedEvent', dict]]]:
        """
        Safely create a new list SignedExchangeReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SignedExchangeReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SignedExchangeReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, SignedExchangeReceivedEvent]]]
        """
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


    __slots__ = ["requestId", "loaderId", "timestamp", "type", "response", "frameId"]

    def __init__(self, requestId: str, loaderId: str, timestamp: float, type: str, response: Union[Response, dict], frameId: Optional[str] = None) -> None:
        """
        Create a new instance of ResponseReceivedEvent

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
        return "ResponseReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ResponseReceivedEvent', dict]]:
        """
        Safely create ResponseReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ResponseReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ResponseReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, ResponseReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = ResponseReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ResponseReceivedEvent', dict]]]:
        """
        Safely create a new list ResponseReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ResponseReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ResponseReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ResponseReceivedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp"]

    def __init__(self, requestId: str, timestamp: float) -> None:
        """
        Create a new instance of WebSocketClosedEvent

        :param requestId: Request identifier.
        :type requestId: str
        :param timestamp: Timestamp.
        :type timestamp: float
        """
        super().__init__()
        self.requestId = requestId
        self.timestamp = timestamp

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "WebSocketClosedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketClosedEvent', dict]]:
        """
        Safely create WebSocketClosedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketClosedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketClosedEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketClosedEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketClosedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketClosedEvent', dict]]]:
        """
        Safely create a new list WebSocketClosedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketClosedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketClosedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketClosedEvent]]]
        """
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


    __slots__ = ["requestId", "url", "initiator"]

    def __init__(self, requestId: str, url: str, initiator: Optional[Union[Initiator, dict]] = None) -> None:
        """
        Create a new instance of WebSocketCreatedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.initiator is not None:
            repr_args.append("initiator={!r}".format(self.initiator))
        return "WebSocketCreatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketCreatedEvent', dict]]:
        """
        Safely create WebSocketCreatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketCreatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketCreatedEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketCreatedEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketCreatedEvent', dict]]]:
        """
        Safely create a new list WebSocketCreatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketCreatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketCreatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketCreatedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "errorMessage"]

    def __init__(self, requestId: str, timestamp: float, errorMessage: str) -> None:
        """
        Create a new instance of WebSocketFrameErrorEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.errorMessage is not None:
            repr_args.append("errorMessage={!r}".format(self.errorMessage))
        return "WebSocketFrameErrorEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketFrameErrorEvent', dict]]:
        """
        Safely create WebSocketFrameErrorEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketFrameErrorEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketFrameErrorEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketFrameErrorEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketFrameErrorEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketFrameErrorEvent', dict]]]:
        """
        Safely create a new list WebSocketFrameErrorEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketFrameErrorEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketFrameErrorEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketFrameErrorEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "response"]

    def __init__(self, requestId: str, timestamp: float, response: Union[WebSocketFrame, dict]) -> None:
        """
        Create a new instance of WebSocketFrameReceivedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketFrameReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketFrameReceivedEvent', dict]]:
        """
        Safely create WebSocketFrameReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketFrameReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketFrameReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketFrameReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketFrameReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketFrameReceivedEvent', dict]]]:
        """
        Safely create a new list WebSocketFrameReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketFrameReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketFrameReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketFrameReceivedEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "response"]

    def __init__(self, requestId: str, timestamp: float, response: Union[WebSocketFrame, dict]) -> None:
        """
        Create a new instance of WebSocketFrameSentEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketFrameSentEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketFrameSentEvent', dict]]:
        """
        Safely create WebSocketFrameSentEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketFrameSentEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketFrameSentEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketFrameSentEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketFrameSentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketFrameSentEvent', dict]]]:
        """
        Safely create a new list WebSocketFrameSentEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketFrameSentEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketFrameSentEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketFrameSentEvent]]]
        """
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


    __slots__ = ["requestId", "timestamp", "response"]

    def __init__(self, requestId: str, timestamp: float, response: Union[WebSocketResponse, dict]) -> None:
        """
        Create a new instance of WebSocketHandshakeResponseReceivedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.requestId is not None:
            repr_args.append("requestId={!r}".format(self.requestId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.response is not None:
            repr_args.append("response={!r}".format(self.response))
        return "WebSocketHandshakeResponseReceivedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketHandshakeResponseReceivedEvent', dict]]:
        """
        Safely create WebSocketHandshakeResponseReceivedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketHandshakeResponseReceivedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketHandshakeResponseReceivedEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketHandshakeResponseReceivedEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketHandshakeResponseReceivedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketHandshakeResponseReceivedEvent', dict]]]:
        """
        Safely create a new list WebSocketHandshakeResponseReceivedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketHandshakeResponseReceivedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketHandshakeResponseReceivedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketHandshakeResponseReceivedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketHandshakeResponseReceivedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WebSocketWillSendHandshakeRequestEvent(object):
    """
    Fired when WebSocket is about to initiate handshake.
    """


    __slots__ = ["requestId", "timestamp", "wallTime", "request"]

    def __init__(self, requestId: str, timestamp: float, wallTime: float, request: Union[WebSocketRequest, dict]) -> None:
        """
        Create a new instance of WebSocketWillSendHandshakeRequestEvent

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
        return "WebSocketWillSendHandshakeRequestEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WebSocketWillSendHandshakeRequestEvent', dict]]:
        """
        Safely create WebSocketWillSendHandshakeRequestEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WebSocketWillSendHandshakeRequestEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WebSocketWillSendHandshakeRequestEvent if creation did not fail
        :rtype: Optional[Union[dict, WebSocketWillSendHandshakeRequestEvent]]
        """
        if init is not None:
            try:
                ourselves = WebSocketWillSendHandshakeRequestEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WebSocketWillSendHandshakeRequestEvent', dict]]]:
        """
        Safely create a new list WebSocketWillSendHandshakeRequestEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WebSocketWillSendHandshakeRequestEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WebSocketWillSendHandshakeRequestEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WebSocketWillSendHandshakeRequestEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WebSocketWillSendHandshakeRequestEvent.safe_create(it))
            return list_of_self
        else:
            return init


NETWORK_EVENTS_TO_CLASS = {
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

NetworkNS = namedtuple("NetworkNS", ["DataReceived", "EventSourceMessageReceived", "LoadingFailed", "LoadingFinished", "RequestIntercepted", "RequestServedFromCache", "RequestWillBeSent", "ResourceChangedPriority", "SignedExchangeReceived", "ResponseReceived", "WebSocketClosed", "WebSocketCreated", "WebSocketFrameError", "WebSocketFrameReceived", "WebSocketFrameSent", "WebSocketHandshakeResponseReceived", "WebSocketWillSendHandshakeRequest"])

NETWORK_EVENTS_NS = NetworkNS(
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
