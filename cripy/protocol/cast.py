"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Cast"]


class Cast:
    """
    A domain for interacting with Cast, Presentation API, and Remote Playback API
    functionalities.
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Cast`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Cast

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def enable(self, presentationUrl: Optional[str] = None) -> Awaitable[Dict]:
        """
        Starts observing for sinks that can be used for tab mirroring, and if set,
        sinks compatible with |presentationUrl| as well. When sinks are found, a
        |sinksUpdated| event is fired.
        Also starts observing for issue messages. When an issue is added or removed,
        an |issueUpdated| event is fired.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#method-enable`

        :param presentationUrl: The presentationUrl
        :return: The results of the command
        """
        msg = {}
        if presentationUrl is not None:
            msg["presentationUrl"] = presentationUrl
        return self.client.send("Cast.enable", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Stops observing for sinks and issues.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#method-disable`

        :return: The results of the command
        """
        return self.client.send("Cast.disable", {})

    def setSinkToUse(self, sinkName: str) -> Awaitable[Dict]:
        """
        Sets a sink to be used when the web page requests the browser to choose a
        sink via Presentation API, Remote Playback API, or Cast SDK.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#method-setSinkToUse`

        :param sinkName: The sinkName
        :return: The results of the command
        """
        return self.client.send("Cast.setSinkToUse", {"sinkName": sinkName})

    def startTabMirroring(self, sinkName: str) -> Awaitable[Dict]:
        """
        Starts mirroring the tab to the sink.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#method-startTabMirroring`

        :param sinkName: The sinkName
        :return: The results of the command
        """
        return self.client.send("Cast.startTabMirroring", {"sinkName": sinkName})

    def stopCasting(self, sinkName: str) -> Awaitable[Dict]:
        """
        Stops the active Cast session on the sink.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#method-stopCasting`

        :param sinkName: The sinkName
        :return: The results of the command
        """
        return self.client.send("Cast.stopCasting", {"sinkName": sinkName})

    def sinksUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        This is fired whenever the list of available sinks changes. A sink is a
        device or a software surface that you can cast to.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#event-sinksUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Cast.sinksUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def issueUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        This is fired whenever the outstanding issue/error message changes.
        |issueMessage| is empty if there is no issue.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Cast#event-issueUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Cast.issueUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
