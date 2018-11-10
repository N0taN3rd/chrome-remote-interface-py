# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOMStorage"]


@attr.dataclass(slots=True, cmp=False)
class DOMStorage(object):
    """
    Query and modify DOM storage.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def clear(self, storageId: dict) -> Awaitable[Optional[dict]]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        return self.client.send("DOMStorage.clear", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables storage tracking, prevents storage events from being sent to the client.
        """
        return self.client.send("DOMStorage.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables storage tracking, storage events will now be delivered to the client.
        """
        return self.client.send("DOMStorage.enable")

    def getDOMStorageItems(self, storageId: dict) -> Awaitable[Optional[dict]]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        return self.client.send("DOMStorage.getDOMStorageItems", msg_dict)

    def removeDOMStorageItem(
        self, storageId: dict, key: str
    ) -> Awaitable[Optional[dict]]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        if key is not None:
            msg_dict["key"] = key
        return self.client.send("DOMStorage.removeDOMStorageItem", msg_dict)

    def setDOMStorageItem(
        self, storageId: dict, key: str, value: str
    ) -> Awaitable[Optional[dict]]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param value: The value
        :type value: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict["storageId"] = storageId
        if key is not None:
            msg_dict["key"] = key
        if value is not None:
            msg_dict["value"] = value
        return self.client.send("DOMStorage.setDOMStorageItem", msg_dict)

    def domStorageItemAdded(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("DOMStorage.domStorageItemAdded", _cb)

            return future

        self.client.on("DOMStorage.domStorageItemAdded", cb)

    def domStorageItemRemoved(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("DOMStorage.domStorageItemRemoved", _cb)

            return future

        self.client.on("DOMStorage.domStorageItemRemoved", cb)

    def domStorageItemUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("DOMStorage.domStorageItemUpdated", _cb)

            return future

        self.client.on("DOMStorage.domStorageItemUpdated", cb)

    def domStorageItemsCleared(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("DOMStorage.domStorageItemsCleared", _cb)

            return future

        self.client.on("DOMStorage.domStorageItemsCleared", cb)
