# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Security"]


class Security(object):
    """
    Security
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def disable(self) -> Optional[dict]:
        """
        Disables tracking security state changes.
        """
        res = await self.client.send("Security.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables tracking security state changes.
        """
        res = await self.client.send("Security.enable")
        return res

    async def setIgnoreCertificateErrors(self, ignore: bool) -> Optional[dict]:
        """
        Enable/disable whether all certificate errors should be ignored.

        :param ignore: If true, all certificate errors will be ignored.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict["ignore"] = ignore
        res = await self.client.send("Security.setIgnoreCertificateErrors", msg_dict)
        return res

    async def handleCertificateError(self, eventId: int, action: str) -> Optional[dict]:
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
        res = await self.client.send("Security.handleCertificateError", msg_dict)
        return res

    async def setOverrideCertificateErrors(self, override: bool) -> Optional[dict]:
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
be handled by the DevTools client and should be answered with `handleCertificateError` commands.

        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        msg_dict = dict()
        if override is not None:
            msg_dict["override"] = override
        res = await self.client.send("Security.setOverrideCertificateErrors", msg_dict)
        return res

    def certificateError(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        There is a certificate error. If overriding certificate errors is enabled, then it should be
        handled with the `handleCertificateError` command. Note: this event does not fire if the
        certificate error has been allowed internally. Only one client per target should override
        certificate errors at the same time.
        """
        if once:
            self.client.once("Security.certificateError", fn)
        else:
            self.client.on("Security.certificateError", fn)

    def securityStateChanged(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        The security state of the page changed.
        """
        if once:
            self.client.once("Security.securityStateChanged", fn)
        else:
            self.client.on("Security.securityStateChanged", fn)

    def __repr__(self):
        return f"Security()"
