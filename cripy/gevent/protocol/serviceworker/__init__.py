from cripy.gevent.protocol.serviceworker import events as Events
from cripy.gevent.protocol.serviceworker import types as Types

__all__ = ["ServiceWorker"] + Events.__all__ + Types.__all__


class ServiceWorker(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def deliverPushMessage(self, origin, registrationId, data):
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
        wres = self.chrome.send("ServiceWorker.deliverPushMessage", msg_dict)
        return wres.get()

    def disable(self):
        wres = self.chrome.send("ServiceWorker.disable")
        return wres.get()

    def dispatchSyncEvent(self, origin, registrationId, tag, lastChance):
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
        wres = self.chrome.send("ServiceWorker.dispatchSyncEvent", msg_dict)
        return wres.get()

    def enable(self):
        wres = self.chrome.send("ServiceWorker.enable")
        return wres.get()

    def inspectWorker(self, versionId):
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        wres = self.chrome.send("ServiceWorker.inspectWorker", msg_dict)
        return wres.get()

    def setForceUpdateOnPageLoad(self, forceUpdateOnPageLoad):
        """
        :param forceUpdateOnPageLoad: The forceUpdateOnPageLoad
        :type forceUpdateOnPageLoad: bool
        """
        msg_dict = dict()
        if forceUpdateOnPageLoad is not None:
            msg_dict["forceUpdateOnPageLoad"] = forceUpdateOnPageLoad
        wres = self.chrome.send("ServiceWorker.setForceUpdateOnPageLoad", msg_dict)
        return wres.get()

    def skipWaiting(self, scopeURL):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        wres = self.chrome.send("ServiceWorker.skipWaiting", msg_dict)
        return wres.get()

    def startWorker(self, scopeURL):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        wres = self.chrome.send("ServiceWorker.startWorker", msg_dict)
        return wres.get()

    def stopAllWorkers(self):
        wres = self.chrome.send("ServiceWorker.stopAllWorkers")
        return wres.get()

    def stopWorker(self, versionId):
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict["versionId"] = versionId
        wres = self.chrome.send("ServiceWorker.stopWorker", msg_dict)
        return wres.get()

    def unregister(self, scopeURL):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        wres = self.chrome.send("ServiceWorker.unregister", msg_dict)
        return wres.get()

    def updateRegistration(self, scopeURL):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict["scopeURL"] = scopeURL
        wres = self.chrome.send("ServiceWorker.updateRegistration", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
