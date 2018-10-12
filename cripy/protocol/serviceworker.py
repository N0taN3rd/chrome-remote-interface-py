# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["ServiceWorker"]


class ServiceWorker(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def deliverPushMessage(
        self, origin: str, registrationId: str, data: str
    ) -> Optional[dict]:
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
        res = await self.client.send("ServiceWorker.deliverPushMessage", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.client.send("ServiceWorker.disable")
        return res

    async def dispatchSyncEvent(
        self, origin: str, registrationId: str, tag: str, lastChance: bool
    ) -> Optional[dict]:
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
        res = await self.client.send("ServiceWorker.dispatchSyncEvent", msg_dict)
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.client.send("ServiceWorker.enable")
        return res

    async def inspectWorker(self, versionId: str) -> Optional[dict]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        res = await self.client.send("ServiceWorker.inspectWorker", msg_dict)
        return res

    async def setForceUpdateOnPageLoad(
        self, forceUpdateOnPageLoad: bool
    ) -> Optional[dict]:
        """
        :param forceUpdateOnPageLoad: The forceUpdateOnPageLoad
        :type forceUpdateOnPageLoad: bool
        """
        msg_dict = dict()
        if forceUpdateOnPageLoad is not None:
            msg_dict["forceUpdateOnPageLoad"] = forceUpdateOnPageLoad
        res = await self.client.send("ServiceWorker.setForceUpdateOnPageLoad", msg_dict)
        return res

    async def skipWaiting(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        res = await self.client.send("ServiceWorker.skipWaiting", msg_dict)
        return res

    async def startWorker(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        res = await self.client.send("ServiceWorker.startWorker", msg_dict)
        return res

    async def stopAllWorkers(self) -> Optional[dict]:
        res = await self.client.send("ServiceWorker.stopAllWorkers")
        return res

    async def stopWorker(self, versionId: str) -> Optional[dict]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        res = await self.client.send("ServiceWorker.stopWorker", msg_dict)
        return res

    async def unregister(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        res = await self.client.send("ServiceWorker.unregister", msg_dict)
        return res

    async def updateRegistration(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        res = await self.client.send("ServiceWorker.updateRegistration", msg_dict)
        return res

    def workerErrorReported(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("ServiceWorker.workerErrorReported", fn)
        else:
            self.client.on("ServiceWorker.workerErrorReported", fn)

    def workerRegistrationUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        if once:
            self.client.once("ServiceWorker.workerRegistrationUpdated", fn)
        else:
            self.client.on("ServiceWorker.workerRegistrationUpdated", fn)

    def workerVersionUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("ServiceWorker.workerVersionUpdated", fn)
        else:
            self.client.on("ServiceWorker.workerVersionUpdated", fn)

    def __repr__(self):
        return f"ServiceWorker()"
