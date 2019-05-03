"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Security"]


class Security:
    """
    Security
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Security`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Security

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables tracking security state changes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#method-disable`

        :return: The results of the command
        """
        return self.client.send("Security.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables tracking security state changes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#method-enable`

        :return: The results of the command
        """
        return self.client.send("Security.enable", {})

    def setIgnoreCertificateErrors(self, ignore: bool) -> Awaitable[Dict]:
        """
        Enable/disable whether all certificate errors should be ignored.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#method-setIgnoreCertificateErrors`

        :param ignore: If true, all certificate errors will be ignored.
        :return: The results of the command
        """
        return self.client.send(
            "Security.setIgnoreCertificateErrors", {"ignore": ignore}
        )

    def handleCertificateError(self, eventId: int, action: str) -> Awaitable[Dict]:
        """
        Handles a certificate error that fired a certificateError event.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#method-handleCertificateError`

        :param eventId: The ID of the event.
        :param action: The action to take on the certificate error.
        :return: The results of the command
        """
        return self.client.send(
            "Security.handleCertificateError", {"eventId": eventId, "action": action}
        )

    def setOverrideCertificateErrors(self, override: bool) -> Awaitable[Dict]:
        """
        Enable/disable overriding certificate errors. If enabled, all certificate error events need to
        be handled by the DevTools client and should be answered with `handleCertificateError` commands.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#method-setOverrideCertificateErrors`

        :param override: If true, certificate errors will be overridden.
        :return: The results of the command
        """
        return self.client.send(
            "Security.setOverrideCertificateErrors", {"override": override}
        )

    def certificateError(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        There is a certificate error. If overriding certificate errors is enabled, then it should be
        handled with the `handleCertificateError` command. Note: this event does not fire if the
        certificate error has been allowed internally. Only one client per target should override
        certificate errors at the same time.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#event-certificateError`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Security.certificateError"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def securityStateChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        The security state of the page changed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Security#event-securityStateChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Security.securityStateChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
