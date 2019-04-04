"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["WebAudio"]


class WebAudio:
    """
    This domain allows inspection of Web Audio API.
    https://webaudio.github.io/web-audio-api/
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of WebAudio

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def enable(self) -> Awaitable[Dict]:
        """
        Enables the WebAudio domain and starts sending context lifetime events.

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#method-enable`

        :return: The results of the command
        """
        return self.client.send("WebAudio.enable", {})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the WebAudio domain.

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#method-disable`

        :return: The results of the command
        """
        return self.client.send("WebAudio.disable", {})

    def getRealtimeData(self, contextId: str) -> Awaitable[Dict]:
        """
        Fetch the realtime data from the registered contexts.

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#method-getRealtimeData`

        :param contextId: The contextId
        :return: The results of the command
        """
        return self.client.send("WebAudio.getRealtimeData", {"contextId": contextId})

    def contextCreated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Notifies that a new BaseAudioContext has been created.

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#event-contextCreated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "WebAudio.contextCreated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def contextDestroyed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Notifies that existing BaseAudioContext has been destroyed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#event-contextDestroyed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "WebAudio.contextDestroyed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def contextChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Notifies that existing BaseAudioContext has changed some properties (id stays the same)..

        See `https://chromedevtools.github.io/devtools-protocol/tot/WebAudio#event-contextChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "WebAudio.contextChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
