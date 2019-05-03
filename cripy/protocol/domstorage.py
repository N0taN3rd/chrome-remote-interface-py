"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOMStorage"]


class DOMStorage:
    """
    Query and modify DOM storage.
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of DOMStorage

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clear(self, storageId: Dict[str, Any]) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-clear`

        :param storageId: The storageId
        :return: The results of the command
        """
        return self.client.send("DOMStorage.clear", {"storageId": storageId})

    def disable(self) -> Awaitable[Dict]:
        """
        Disables storage tracking, prevents storage events from being sent to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-disable`

        :return: The results of the command
        """
        return self.client.send("DOMStorage.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables storage tracking, storage events will now be delivered to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-enable`

        :return: The results of the command
        """
        return self.client.send("DOMStorage.enable", {})

    def getDOMStorageItems(self, storageId: Dict[str, Any]) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-getDOMStorageItems`

        :param storageId: The storageId
        :return: The results of the command
        """
        return self.client.send(
            "DOMStorage.getDOMStorageItems", {"storageId": storageId}
        )

    def removeDOMStorageItem(
        self, storageId: Dict[str, Any], key: str
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-removeDOMStorageItem`

        :param storageId: The storageId
        :param key: The key
        :return: The results of the command
        """
        return self.client.send(
            "DOMStorage.removeDOMStorageItem", {"storageId": storageId, "key": key}
        )

    def setDOMStorageItem(
        self, storageId: Dict[str, Any], key: str, value: str
    ) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#method-setDOMStorageItem`

        :param storageId: The storageId
        :param key: The key
        :param value: The value
        :return: The results of the command
        """
        return self.client.send(
            "DOMStorage.setDOMStorageItem",
            {"storageId": storageId, "key": key, "value": value},
        )

    def domStorageItemAdded(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#event-domStorageItemAdded`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOMStorage.domStorageItemAdded"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def domStorageItemRemoved(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#event-domStorageItemRemoved`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOMStorage.domStorageItemRemoved"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def domStorageItemUpdated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#event-domStorageItemUpdated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOMStorage.domStorageItemUpdated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def domStorageItemsCleared(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMStorage#event-domStorageItemsCleared`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "DOMStorage.domStorageItemsCleared"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
