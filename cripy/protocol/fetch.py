"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Fetch"]


@attr.dataclass(slots=True, cmp=False)
class Fetch(object):
    """
    A domain for letting clients substitute browser's network layer with client code.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the fetch domain.
        """
        return self.client.send("Fetch.disable")

    def enable(
        self,
        patterns: Optional[List[dict]] = None,
        handleAuthRequests: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Enables issuing of requestPaused events. A request will be paused until client
calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.

        :param patterns: If specified, only requests matching any of these patterns will produce fetchRequested event and will be paused until clients response. If not set, all requests will be affected.
        :type patterns: Optional[List[dict]]
        :param handleAuthRequests: If true, authRequired events will be issued and requests will be paused expecting a call to continueWithAuth.
        :type handleAuthRequests: Optional[bool]
        """
        msg_dict = dict()
        if patterns is not None:
            msg_dict["patterns"] = patterns
        if handleAuthRequests is not None:
            msg_dict["handleAuthRequests"] = handleAuthRequests
        return self.client.send("Fetch.enable", msg_dict)

    def failRequest(self, requestId: str, errorReason: str) -> Awaitable[Dict]:
        """
        Causes the request to fail with specified reason.

        :param requestId: An id the client received in requestPaused event.
        :type requestId: str
        :param errorReason: Causes the request to fail with the given reason.
        :type errorReason: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if errorReason is not None:
            msg_dict["errorReason"] = errorReason
        return self.client.send("Fetch.failRequest", msg_dict)

    def fulfillRequest(
        self,
        requestId: str,
        responseCode: int,
        responseHeaders: List[dict],
        body: Optional[str] = None,
        responsePhrase: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Provides response to the request.

        :param requestId: An id the client received in requestPaused event.
        :type requestId: str
        :param responseCode: An HTTP response code.
        :type responseCode: int
        :param responseHeaders: Response headers.
        :type responseHeaders: List[dict]
        :param body: A response body.
        :type body: Optional[str]
        :param responsePhrase: A textual representation of responseCode. If absent, a standard phrase mathcing responseCode is used.
        :type responsePhrase: Optional[str]
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if responseCode is not None:
            msg_dict["responseCode"] = responseCode
        if responseHeaders is not None:
            msg_dict["responseHeaders"] = responseHeaders
        if body is not None:
            msg_dict["body"] = body
        if responsePhrase is not None:
            msg_dict["responsePhrase"] = responsePhrase
        return self.client.send("Fetch.fulfillRequest", msg_dict)

    def continueRequest(
        self,
        requestId: str,
        url: Optional[str] = None,
        method: Optional[str] = None,
        postData: Optional[str] = None,
        headers: Optional[List[dict]] = None,
    ) -> Awaitable[Dict]:
        """
        Continues the request, optionally modifying some of its parameters.

        :param requestId: An id the client received in requestPaused event.
        :type requestId: str
        :param url: If set, the request url will be modified in a way that's not observable by page.
        :type url: Optional[str]
        :param method: If set, the request method is overridden.
        :type method: Optional[str]
        :param postData: If set, overrides the post data in the request.
        :type postData: Optional[str]
        :param headers: If set, overrides the request headrts.
        :type headers: Optional[List[dict]]
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if url is not None:
            msg_dict["url"] = url
        if method is not None:
            msg_dict["method"] = method
        if postData is not None:
            msg_dict["postData"] = postData
        if headers is not None:
            msg_dict["headers"] = headers
        return self.client.send("Fetch.continueRequest", msg_dict)

    def continueWithAuth(
        self, requestId: str, authChallengeResponse: dict
    ) -> Awaitable[Dict]:
        """
        Continues a request supplying authChallengeResponse following authRequired event.

        :param requestId: An id the client received in authRequired event.
        :type requestId: str
        :param authChallengeResponse: Response to  with an authChallenge.
        :type authChallengeResponse: dict
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if authChallengeResponse is not None:
            msg_dict["authChallengeResponse"] = authChallengeResponse
        return self.client.send("Fetch.continueWithAuth", msg_dict)

    def getResponseBody(self, requestId: str) -> Awaitable[Dict]:
        """
        Causes the body of the response to be received from the server and
returned as a single string. May only be issued for a request that
is paused in the Response stage and is mutually exclusive with
takeResponseBodyForInterceptionAsStream. Calling other methods that
affect the request or disabling fetch domain before body is received
results in an undefined behavior.

        :param requestId: Identifier for the intercepted request to get body for.
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        return self.client.send("Fetch.getResponseBody", msg_dict)

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

        :param requestId: The requestId
        :type requestId: str
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        return self.client.send("Fetch.takeResponseBodyAsStream", msg_dict)

    def requestPaused(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when the domain is enabled and the request URL matches the
        specified filter. The request is paused until the client responds
        with one of continueRequest, failRequest or fulfillRequest.
        The stage of the request can be determined by presence of responseErrorReason
        and responseStatusCode -- the request is at the response stage if either
        of these fields is present and in the request stage otherwise.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Fetch.requestPaused", _cb)

            return future

        self.client.on("Fetch.requestPaused", cb)
        return lambda: self.client.remove_listener("Fetch.requestPaused", cb)

    def authRequired(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when the domain is enabled with handleAuthRequests set to true.
        The request is paused until client responds with continueWithAuth.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Fetch.authRequired", _cb)

            return future

        self.client.on("Fetch.authRequired", cb)
        return lambda: self.client.remove_listener("Fetch.authRequired", cb)
