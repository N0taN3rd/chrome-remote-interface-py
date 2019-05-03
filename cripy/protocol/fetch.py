"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Fetch"]


class Fetch:
    """
    A domain for letting clients substitute browser's network layer with client code.
     
    Domain Dependencies: 
      * Network
      * IO
      * Page
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Fetch

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the fetch domain.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-disable`

        :return: The results of the command
        """
        return self.client.send("Fetch.disable", {})

    def enable(
        self,
        patterns: Optional[List[Dict[str, Any]]] = None,
        handleAuthRequests: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Enables issuing of requestPaused events. A request will be paused until client
        calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-enable`

        :param patterns: If specified, only requests matching any of these patterns will produce
         fetchRequested event and will be paused until clients response. If not set,
         all requests will be affected.
        :param handleAuthRequests: If true, authRequired events will be issued and requests will be paused
         expecting a call to continueWithAuth.
        :return: The results of the command
        """
        msg = {}
        if patterns is not None:
            msg["patterns"] = patterns
        if handleAuthRequests is not None:
            msg["handleAuthRequests"] = handleAuthRequests
        return self.client.send("Fetch.enable", msg)

    def failRequest(self, requestId: str, errorReason: str) -> Awaitable[Dict]:
        """
        Causes the request to fail with specified reason.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-failRequest`

        :param requestId: An id the client received in requestPaused event.
        :param errorReason: Causes the request to fail with the given reason.
        :return: The results of the command
        """
        return self.client.send(
            "Fetch.failRequest", {"requestId": requestId, "errorReason": errorReason}
        )

    def fulfillRequest(
        self,
        requestId: str,
        responseCode: int,
        responseHeaders: List[Dict[str, Any]],
        body: Optional[str] = None,
        responsePhrase: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Provides response to the request.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-fulfillRequest`

        :param requestId: An id the client received in requestPaused event.
        :param responseCode: An HTTP response code.
        :param responseHeaders: Response headers.
        :param body: A response body.
        :param responsePhrase: A textual representation of responseCode.
         If absent, a standard phrase mathcing responseCode is used.
        :return: The results of the command
        """
        msg = {
            "requestId": requestId,
            "responseCode": responseCode,
            "responseHeaders": responseHeaders,
        }
        if body is not None:
            msg["body"] = body
        if responsePhrase is not None:
            msg["responsePhrase"] = responsePhrase
        return self.client.send("Fetch.fulfillRequest", msg)

    def continueRequest(
        self,
        requestId: str,
        url: Optional[str] = None,
        method: Optional[str] = None,
        postData: Optional[str] = None,
        headers: Optional[List[Dict[str, Any]]] = None,
    ) -> Awaitable[Dict]:
        """
        Continues the request, optionally modifying some of its parameters.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-continueRequest`

        :param requestId: An id the client received in requestPaused event.
        :param url: If set, the request url will be modified in a way that's not observable by page.
        :param method: If set, the request method is overridden.
        :param postData: If set, overrides the post data in the request.
        :param headers: If set, overrides the request headrts.
        :return: The results of the command
        """
        msg = {"requestId": requestId}
        if url is not None:
            msg["url"] = url
        if method is not None:
            msg["method"] = method
        if postData is not None:
            msg["postData"] = postData
        if headers is not None:
            msg["headers"] = headers
        return self.client.send("Fetch.continueRequest", msg)

    def continueWithAuth(
        self, requestId: str, authChallengeResponse: Dict[str, Any]
    ) -> Awaitable[Dict]:
        """
        Continues a request supplying authChallengeResponse following authRequired event.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-continueWithAuth`

        :param requestId: An id the client received in authRequired event.
        :param authChallengeResponse: Response to  with an authChallenge.
        :return: The results of the command
        """
        return self.client.send(
            "Fetch.continueWithAuth",
            {"requestId": requestId, "authChallengeResponse": authChallengeResponse},
        )

    def getResponseBody(self, requestId: str) -> Awaitable[Dict]:
        """
        Causes the body of the response to be received from the server and
        returned as a single string. May only be issued for a request that
        is paused in the Response stage and is mutually exclusive with
        takeResponseBodyForInterceptionAsStream. Calling other methods that
        affect the request or disabling fetch domain before body is received
        results in an undefined behavior.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-getResponseBody`

        :param requestId: Identifier for the intercepted request to get body for.
        :return: The results of the command
        """
        return self.client.send("Fetch.getResponseBody", {"requestId": requestId})

    def takeResponseBodyAsStream(self, requestId: str) -> Awaitable[Dict]:
        """
        Returns a handle to the stream representing the response body.
        The request must be paused in the HeadersReceived stage.
        Note that after this command the request can't be continued
        as is -- client either needs to cancel it or to provide the
        response body.
        The stream only supports sequential read, IO.read will fail if the position
        is specified.
        This method is mutually exclusive with getResponseBody.
        Calling other methods that affect the request or disabling fetch
        domain before body is received results in an undefined behavior.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#method-takeResponseBodyAsStream`

        :param requestId: The requestId
        :return: The results of the command
        """
        return self.client.send(
            "Fetch.takeResponseBodyAsStream", {"requestId": requestId}
        )

    def requestPaused(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when the domain is enabled and the request URL matches the
        specified filter. The request is paused until the client responds
        with one of continueRequest, failRequest or fulfillRequest.
        The stage of the request can be determined by presence of responseErrorReason
        and responseStatusCode -- the request is at the response stage if either
        of these fields is present and in the request stage otherwise.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#event-requestPaused`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Fetch.requestPaused"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def authRequired(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when the domain is enabled with handleAuthRequests set to true.
        The request is paused until client responds with continueWithAuth.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Fetch#event-authRequired`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Fetch.authRequired"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
