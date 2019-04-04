"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["BackgroundService"]


class BackgroundService:
    """
    Defines events for background web platform features.
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of BackgroundService

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def startObserving(self, service: str) -> Awaitable[Dict]:
        """
        Enables event updates for the service.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#method-startObserving`

        :param service: The service
        :return: The results of the command
        """
        return self.client.send(
            "BackgroundService.startObserving", {"service": service}
        )

    def stopObserving(self, service: str) -> Awaitable[Dict]:
        """
        Disables event updates for the service.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#method-stopObserving`

        :param service: The service
        :return: The results of the command
        """
        return self.client.send("BackgroundService.stopObserving", {"service": service})

    def setRecording(self, shouldRecord: bool, service: str) -> Awaitable[Dict]:
        """
        Set the recording state for the service.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#method-setRecording`

        :param shouldRecord: The shouldRecord
        :param service: The service
        :return: The results of the command
        """
        return self.client.send(
            "BackgroundService.setRecording",
            {"shouldRecord": shouldRecord, "service": service},
        )

    def clearEvents(self, service: str) -> Awaitable[Dict]:
        """
        Clears all stored data for the service.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#method-clearEvents`

        :param service: The service
        :return: The results of the command
        """
        return self.client.send("BackgroundService.clearEvents", {"service": service})

    def recordingStateChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called when the recording state for the service has been updated.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#event-recordingStateChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "BackgroundService.recordingStateChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def backgroundServiceEventReceived(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Called with all existing backgroundServiceEvents when enabled, and all new
        events afterwards if enabled and recording.

        See `https://chromedevtools.github.io/devtools-protocol/tot/BackgroundService#event-backgroundServiceEventReceived`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "BackgroundService.backgroundServiceEventReceived"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
