__all__ = ["Security"]


class Security(object):
    """
    Security
    """

    def __init__(self, chrome):
        """
        Construct a new Security object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables tracking security state changes.
        """
        wres = self.chrome.send('Security.disable')
        return wres.get()

    def enable(self):
        """
        Enables tracking security state changes.
        """
        wres = self.chrome.send('Security.enable')
        return wres.get()

    def setIgnoreCertificateErrors(self, ignore):
        """
        Enable/disable whether all certificate errors should be ignored.

        :param ignore: If true, all certificate errors will be ignored.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict['ignore'] = ignore
        wres = self.chrome.send('Security.setIgnoreCertificateErrors', msg_dict)
        return wres.get()

    def handleCertificateError(self, eventId, action):
        """
        Handles a certificate error that fired a certificateError event.

        :param eventId: The ID of the event.
        :type eventId: int
        :param action: The action to take on the certificate error.
        :type action: str
        """
        msg_dict = dict()
        if eventId is not None:
            msg_dict['eventId'] = eventId
        if action is not None:
            msg_dict['action'] = action
        wres = self.chrome.send('Security.handleCertificateError', msg_dict)
        return wres.get()

    def setOverrideCertificateErrors(self, override):
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
be handled by the DevTools client and should be answered with `handleCertificateError` commands.

        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        msg_dict = dict()
        if override is not None:
            msg_dict['override'] = override
        wres = self.chrome.send('Security.setOverrideCertificateErrors', msg_dict)
        return wres.get()

    def certificateError(self, fn, once=False):
        """
        There is a certificate error. If overriding certificate errors is enabled, then it should be
        handled with the `handleCertificateError` command. Note: this event does not fire if the
        certificate error has been allowed internally. Only one client per target should override
        certificate errors at the same time.
        """
        self.chrome.on("Security.certificateError", fn, once=once)

    def securityStateChanged(self, fn, once=False):
        """
        The security state of the page changed.
        """
        self.chrome.on("Security.securityStateChanged", fn, once=once)


