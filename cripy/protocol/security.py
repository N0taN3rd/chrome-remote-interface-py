"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Security"]


@attr.dataclass(slots=True, cmp=False)
class Security(object):
    """
    Security
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Dict]:
        """
        Disables tracking security state changes.
        """
        return self.client.send("Security.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables tracking security state changes.
        """
        return self.client.send("Security.enable")

    def setIgnoreCertificateErrors(self, ignore: bool) -> Awaitable[Dict]:
        """
        Enable/disable whether all certificate errors should be ignored.

        :param ignore: If true, all certificate errors will be ignored.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict["ignore"] = ignore
        return self.client.send("Security.setIgnoreCertificateErrors", msg_dict)

    def handleCertificateError(self, eventId: int, action: str) -> Awaitable[Dict]:
        """
        Handles a certificate error that fired a certificateError event.

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
        return self.client.send("Security.handleCertificateError", msg_dict)

    def setOverrideCertificateErrors(self, override: bool) -> Awaitable[Dict]:
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
be handled by the DevTools client and should be answered with `handleCertificateError` commands.

        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        msg_dict = dict()
        if override is not None:
            msg_dict["override"] = override
        return self.client.send("Security.setOverrideCertificateErrors", msg_dict)

    def certificateError(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        There is a certificate error. If overriding certificate errors is enabled, then it should be
        handled with the `handleCertificateError` command. Note: this event does not fire if the
        certificate error has been allowed internally. Only one client per target should override
        certificate errors at the same time.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Security.certificateError", _cb)

            return future

        self.client.on("Security.certificateError", cb)
        return lambda: self.client.remove_listener("Security.certificateError", cb)

    def securityStateChanged(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        The security state of the page changed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Security.securityStateChanged", _cb)

            return future

        self.client.on("Security.securityStateChanged", cb)
        return lambda: self.client.remove_listener("Security.securityStateChanged", cb)
