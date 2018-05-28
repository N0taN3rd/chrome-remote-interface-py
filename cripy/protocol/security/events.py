from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class CertificateErrorEvent(BaseEvent):
    """There is a certificate error.
	If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command.
	Note: this event does not fire if the certificate error has been allowed internally.
	Only one client per target should override certificate errors at the same time."""

    event: str = "Security.certificateError"

    def __init__(self) -> None:
        """
        :param int eventId: The ID of the event.
        :type eventId: int
        :param str errorType: The type of the error.
        :type errorType: str
        :param str requestURL: The url that was requested.
        :type requestURL: str
        """
        super().__init__()


class SecurityStateChangedEvent(BaseEvent):
    """The security state of the page changed."""

    event: str = "Security.securityStateChanged"

    def __init__(self) -> None:
        """
        :param SecurityState securityState: Security state.
        :type securityState: SecurityState
        :param bool schemeIsCryptographic: True if the page was loaded over cryptographic transport such as HTTPS.
        :type schemeIsCryptographic: bool
        :param array explanations: List of explanations for the security state. If the overall security state is `insecure` or `warning`, at least one corresponding explanation should be included.
        :type explanations: array
        :param InsecureContentStatus insecureContentStatus: Information about insecure content on the page.
        :type insecureContentStatus: InsecureContentStatus
        :param str summary: Overrides user-visible description of the state.
        :type summary: str
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Security.certificateError": CertificateErrorEvent,
   "Security.securityStateChanged": SecurityStateChangedEvent,
}

