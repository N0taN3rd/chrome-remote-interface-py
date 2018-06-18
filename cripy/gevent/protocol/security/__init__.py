from cripy.gevent.protocol.security import events as Events
from cripy.gevent.protocol.security import types as Types

__all__ = ["Security"] + Events.__all__ + Types.__all__


class Security(object):
    """
    Security
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Security.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Security.enable")
        return wres.get()

    def setIgnoreCertificateErrors(self, ignore):
        """
        :param ignore: If true, all certificate errors will be ignored.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict["ignore"] = ignore
        wres = self.chrome.send("Security.setIgnoreCertificateErrors", msg_dict)
        return wres.get()

    def handleCertificateError(self, eventId, action):
        """
        :param eventId: The ID of the event.
        :type eventId: int
        :param action: The action to take on the certificate error.
        :type action: str
        """
        msg_dict = dict()
        if eventId is not None:
            msg_dict["eventId"] = eventId
        if action is not None:
            msg_dict["action"] = action
        wres = self.chrome.send("Security.handleCertificateError", msg_dict)
        return wres.get()

    def setOverrideCertificateErrors(self, override):
        """
        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        msg_dict = dict()
        if override is not None:
            msg_dict["override"] = override
        wres = self.chrome.send("Security.setOverrideCertificateErrors", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
