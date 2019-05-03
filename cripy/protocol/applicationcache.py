"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["ApplicationCache"]


class ApplicationCache:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of ApplicationCache

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def enable(self) -> Awaitable[Dict]:
        """
        Enables application cache domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#method-enable`

        :return: The results of the command
        """
        return self.client.send("ApplicationCache.enable", {})

    def getApplicationCacheForFrame(self, frameId: str) -> Awaitable[Dict]:
        """
        Returns relevant application cache data for the document in given frame.

        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#method-getApplicationCacheForFrame`

        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :return: The results of the command
        """
        return self.client.send(
            "ApplicationCache.getApplicationCacheForFrame", {"frameId": frameId}
        )

    def getFramesWithManifests(self) -> Awaitable[Dict]:
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
        associated with some application cache.

        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#method-getFramesWithManifests`

        :return: The results of the command
        """
        return self.client.send("ApplicationCache.getFramesWithManifests", {})

    def getManifestForFrame(self, frameId: str) -> Awaitable[Dict]:
        """
        Returns manifest URL for document in the given frame.

        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#method-getManifestForFrame`

        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :return: The results of the command
        """
        return self.client.send(
            "ApplicationCache.getManifestForFrame", {"frameId": frameId}
        )

    def applicationCacheStatusUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#event-applicationCacheStatusUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "ApplicationCache.applicationCacheStatusUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def networkStateUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ApplicationCache#event-networkStateUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "ApplicationCache.networkStateUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
