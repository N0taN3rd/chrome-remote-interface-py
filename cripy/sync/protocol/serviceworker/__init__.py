from cripy.sync.protocol.serviceworker import events as Events
from cripy.sync.protocol.serviceworker import types as Types

__all__ = ["ServiceWorker"] + Events.__all__ + Types.__all__ 


class ServiceWorker(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def deliverPushMessage(self, origin, registrationId, data, cb=None):
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
            msg_dict['origin'] = origin
        if registrationId is not None:
            msg_dict['registrationId'] = registrationId
        if data is not None:
            msg_dict['data'] = data
        self.chrome.send('ServiceWorker.deliverPushMessage', params=msg_dict)


    def disable(self, cb=None):
        self.chrome.send('ServiceWorker.disable')


    def dispatchSyncEvent(self, origin, registrationId, tag, lastChance, cb=None):
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
            msg_dict['origin'] = origin
        if registrationId is not None:
            msg_dict['registrationId'] = registrationId
        if tag is not None:
            msg_dict['tag'] = tag
        if lastChance is not None:
            msg_dict['lastChance'] = lastChance
        self.chrome.send('ServiceWorker.dispatchSyncEvent', params=msg_dict)


    def enable(self, cb=None):
        self.chrome.send('ServiceWorker.enable')


    def inspectWorker(self, versionId, cb=None):
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict['versionId'] = versionId
        self.chrome.send('ServiceWorker.inspectWorker', params=msg_dict)


    def setForceUpdateOnPageLoad(self, forceUpdateOnPageLoad, cb=None):
        """
        :param forceUpdateOnPageLoad: The forceUpdateOnPageLoad
        :type forceUpdateOnPageLoad: bool
        """
        msg_dict = dict()
        if forceUpdateOnPageLoad is not None:
            msg_dict['forceUpdateOnPageLoad'] = forceUpdateOnPageLoad
        self.chrome.send('ServiceWorker.setForceUpdateOnPageLoad', params=msg_dict)


    def skipWaiting(self, scopeURL, cb=None):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict['scopeURL'] = scopeURL
        self.chrome.send('ServiceWorker.skipWaiting', params=msg_dict)


    def startWorker(self, scopeURL, cb=None):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict['scopeURL'] = scopeURL
        self.chrome.send('ServiceWorker.startWorker', params=msg_dict)


    def stopAllWorkers(self, cb=None):
        self.chrome.send('ServiceWorker.stopAllWorkers')


    def stopWorker(self, versionId, cb=None):
        """
        :param versionId: The versionId
        :type versionId: str
        """
        msg_dict = dict()
        if versionId is not None:
            msg_dict['versionId'] = versionId
        self.chrome.send('ServiceWorker.stopWorker', params=msg_dict)


    def unregister(self, scopeURL, cb=None):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict['scopeURL'] = scopeURL
        self.chrome.send('ServiceWorker.unregister', params=msg_dict)


    def updateRegistration(self, scopeURL, cb=None):
        """
        :param scopeURL: The scopeURL
        :type scopeURL: str
        """
        msg_dict = dict()
        if scopeURL is not None:
            msg_dict['scopeURL'] = scopeURL
        self.chrome.send('ServiceWorker.updateRegistration', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

