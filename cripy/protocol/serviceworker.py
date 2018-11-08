# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["ServiceWorker"]


@attr.dataclass(slots=True, cmp=False)
class ServiceWorker(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def deliverPushMessage(
        self, origin: str, registrationId: str, data: str
    ) -> Awaitable[Optional[dict]]:
        """
        :param origin: The origin
        :type origin: str
        :param registrationId: The registrationId
        :type registrationId: str
        :param data: The data
        :type data: str
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if registrationId is not None:
            msg_dict["registrationId"] = registrationId
        if data is not None:
            msg_dict["data"] = data
        return self.client.send("ServiceWorker.deliverPushMessage", msg_dict)

    def disable(self) -> Awaitable[Optional[dict]]:
        return self.client.send("ServiceWorker.disable")

    def dispatchSyncEvent(
        self, origin: str, registrationId: str, tag: str, lastChance: bool
    ) -> Awaitable[Optional[dict]]:
        """
        :param origin: The origin
        :type origin: str
        :param registrationId: The registrationId
        :type registrationId: str
        :param tag: The tag
        :type tag: str
        :param lastChance: The lastChance
        :type lastChance: bool
        """
        msg_dict = dict()
        if origin is not None:
            msg_dict["origin"] = origin
        if registrationId is not None:
            msg_dict["registrationId"] = registrationId
        if tag is not None:
            msg_dict["tag"] = tag
        if lastChance is not None:
            msg_dict["lastChance"] = lastChance
        return self.client.send("ServiceWorker.dispatchSyncEvent", msg_dict)

    def enable(self) -> Awaitable[Optional[dict]]:
        return self.client.send("ServiceWorker.enable")

    def inspectWorker(self, versionId: str) -> Awaitable[Optional[dict]]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        return self.client.send("ServiceWorker.inspectWorker", msg_dict)

    def setForceUpdateOnPageLoad(
        self, forceUpdateOnPageLoad: bool
    ) -> Awaitable[Optional[dict]]:
        """
        :param forceUpdateOnPageLoad: The forceUpdateOnPageLoad
        :type forceUpdateOnPageLoad: bool
        """
        msg_dict = dict()
        if forceUpdateOnPageLoad is not None:
            msg_dict["forceUpdateOnPageLoad"] = forceUpdateOnPageLoad
        return self.client.send("ServiceWorker.setForceUpdateOnPageLoad", msg_dict)

    def skipWaiting(self, scopeURL: str) -> Awaitable[Optional[dict]]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        return self.client.send("ServiceWorker.skipWaiting", msg_dict)

    def startWorker(self, scopeURL: str) -> Awaitable[Optional[dict]]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        return self.client.send("ServiceWorker.startWorker", msg_dict)

    def stopAllWorkers(self) -> Awaitable[Optional[dict]]:
        return self.client.send("ServiceWorker.stopAllWorkers")

    def stopWorker(self, versionId: str) -> Awaitable[Optional[dict]]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        return self.client.send("ServiceWorker.stopWorker", msg_dict)

    def unregister(self, scopeURL: str) -> Awaitable[Optional[dict]]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        return self.client.send("ServiceWorker.unregister", msg_dict)

    def updateRegistration(self, scopeURL: str) -> Awaitable[Optional[dict]]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        return self.client.send("ServiceWorker.updateRegistration", msg_dict)

    def workerErrorReported(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("ServiceWorker.workerErrorReported", _cb)

            return future

        self.client.on("ServiceWorker.workerErrorReported", cb)

    def workerRegistrationUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("ServiceWorker.workerRegistrationUpdated", _cb)

            return future

        self.client.on("ServiceWorker.workerRegistrationUpdated", cb)

    def workerVersionUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("ServiceWorker.workerVersionUpdated", _cb)

            return future

        self.client.on("ServiceWorker.workerVersionUpdated", cb)
