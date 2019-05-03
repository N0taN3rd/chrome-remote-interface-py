"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["ServiceWorker"]


class ServiceWorker:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of ServiceWorker

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def deliverPushMessage(
        self, origin: str, registrationId: str, data: str
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-deliverPushMessage`

        :param origin: The origin
        :param registrationId: The registrationId
        :param data: The data
        :return: The results of the command
        """
        return self.client.send(
            "ServiceWorker.deliverPushMessage",
            {"origin": origin, "registrationId": registrationId, "data": data},
        )

    def disable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-disable`

        :return: The results of the command
        """
        return self.client.send("ServiceWorker.disable", {})

    def dispatchSyncEvent(
        self, origin: str, registrationId: str, tag: str, lastChance: bool
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-dispatchSyncEvent`

        :param origin: The origin
        :param registrationId: The registrationId
        :param tag: The tag
        :param lastChance: The lastChance
        :return: The results of the command
        """
        return self.client.send(
            "ServiceWorker.dispatchSyncEvent",
            {
                "origin": origin,
                "registrationId": registrationId,
                "tag": tag,
                "lastChance": lastChance,
            },
        )

    def enable(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-enable`

        :return: The results of the command
        """
        return self.client.send("ServiceWorker.enable", {})

    def inspectWorker(self, versionId: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-inspectWorker`

        :param versionId: The versionId
        :return: The results of the command
        """
        return self.client.send("ServiceWorker.inspectWorker", {"versionId": versionId})

    def setForceUpdateOnPageLoad(self, forceUpdateOnPageLoad: bool) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-setForceUpdateOnPageLoad`

        :param forceUpdateOnPageLoad: The forceUpdateOnPageLoad
        :return: The results of the command
        """
        return self.client.send(
            "ServiceWorker.setForceUpdateOnPageLoad",
            {"forceUpdateOnPageLoad": forceUpdateOnPageLoad},
        )

    def skipWaiting(self, scopeURL: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-skipWaiting`

        :param scopeURL: The scopeURL
        :return: The results of the command
        """
        return self.client.send("ServiceWorker.skipWaiting", {"scopeURL": scopeURL})

    def startWorker(self, scopeURL: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-startWorker`

        :param scopeURL: The scopeURL
        :return: The results of the command
        """
        return self.client.send("ServiceWorker.startWorker", {"scopeURL": scopeURL})

    def stopAllWorkers(self) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-stopAllWorkers`

        :return: The results of the command
        """
        return self.client.send("ServiceWorker.stopAllWorkers", {})

    def stopWorker(self, versionId: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-stopWorker`

        :param versionId: The versionId
        :return: The results of the command
        """
        return self.client.send("ServiceWorker.stopWorker", {"versionId": versionId})

    def unregister(self, scopeURL: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-unregister`

        :param scopeURL: The scopeURL
        :return: The results of the command
        """
        return self.client.send("ServiceWorker.unregister", {"scopeURL": scopeURL})

    def updateRegistration(self, scopeURL: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#method-updateRegistration`

        :param scopeURL: The scopeURL
        :return: The results of the command
        """
        return self.client.send(
            "ServiceWorker.updateRegistration", {"scopeURL": scopeURL}
        )

    def workerErrorReported(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#event-workerErrorReported`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "ServiceWorker.workerErrorReported"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def workerRegistrationUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#event-workerRegistrationUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "ServiceWorker.workerRegistrationUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def workerVersionUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/ServiceWorker#event-workerVersionUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "ServiceWorker.workerVersionUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
