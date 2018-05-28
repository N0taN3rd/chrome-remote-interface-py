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
        :param eventId: The ID of the event.
        :type int:
        :param errorType: The type of the error.
        :type str:
        :param requestURL: The url that was requested.
        :type str:
        """
        super().__init__()


class SecurityStateChangedEvent(BaseEvent):
    """The security state of the page changed."""

    event: str = "Security.securityStateChanged"

    def __init__(self) -> None:
        """
        :param securityState: Security state.
        :type SecurityState:
        :param schemeIsCryptographic: True if the page was loaded over cryptographic transport such as HTTPS.
        :type bool:
        :param explanations: List of explanations for the security state. If the overall security state is
        `insecure` or `warning`, at least one corresponding explanation should be included.
        :type array:
        :param insecureContentStatus: Information about insecure content on the page.
        :type InsecureContentStatus:
        :param summary: Overrides user-visible description of the state.
        :type str:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Security.certificateError": CertificateErrorEvent,
   "Security.securityStateChanged": SecurityStateChangedEvent,
}

