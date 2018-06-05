from typing import Any, List, Optional, Union
from cripy.protocol.serviceworker import events as Events
from cripy.protocol.serviceworker import types as Types


class ServiceWorker(object):

    def __init__(self, chrome):
        self.chrome = chrome

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
        mayberes = await self.chrome.send("ServiceWorker.deliverPushMessage", msg_dict)
        return mayberes

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("ServiceWorker.disable")
        return mayberes

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
        mayberes = await self.chrome.send("ServiceWorker.dispatchSyncEvent", msg_dict)
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("ServiceWorker.enable")
        return mayberes

    async def inspectWorker(self, versionId: str) -> Optional[dict]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        mayberes = await self.chrome.send("ServiceWorker.inspectWorker", msg_dict)
        return mayberes

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
        mayberes = await self.chrome.send(
            "ServiceWorker.setForceUpdateOnPageLoad", msg_dict
        )
        return mayberes

    async def skipWaiting(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        mayberes = await self.chrome.send("ServiceWorker.skipWaiting", msg_dict)
        return mayberes

    async def startWorker(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        mayberes = await self.chrome.send("ServiceWorker.startWorker", msg_dict)
        return mayberes

    async def stopAllWorkers(self) -> Optional[dict]:
        mayberes = await self.chrome.send("ServiceWorker.stopAllWorkers")
        return mayberes

    async def stopWorker(self, versionId: str) -> Optional[dict]:
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        mayberes = await self.chrome.send("ServiceWorker.stopWorker", msg_dict)
        return mayberes

    async def unregister(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        mayberes = await self.chrome.send("ServiceWorker.unregister", msg_dict)
        return mayberes

    async def updateRegistration(self, scopeURL: str) -> Optional[dict]:
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        mayberes = await self.chrome.send("ServiceWorker.updateRegistration", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
