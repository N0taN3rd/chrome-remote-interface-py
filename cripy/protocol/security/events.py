from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.security.types import (
    InsecureContentStatus,
    SecurityState,
)


class CertificateErrorEvent(BaseEvent):
    """There is a certificate error.
	If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command.
	Note: this event does not fire if the certificate error has been allowed internally.
	Only one client per target should override certificate errors at the same time."""

    event: str = "Security.certificateError"

    def __init__(self, eventId: int, errorType: str, requestURL: str) -> None:
        """
        :param eventId: The ID of the event.
        :type eventId: int
        :param errorType: The type of the error.
        :type errorType: str
        :param requestURL: The url that was requested.
        :type requestURL: str
        """
        super().__init__()
        self.eventId: int = eventId
        self.errorType: str = errorType
        self.requestURL: str = requestURL


class SecurityStateChangedEvent(BaseEvent):
    """The security state of the page changed."""

    event: str = "Security.securityStateChanged"

    def __init__(self, securityState: SecurityState, schemeIsCryptographic: bool, explanations: List[SecurityStateExplanation], insecureContentStatus: InsecureContentStatus, summary: Optional[str] = None) -> None:
        """
        :param securityState: Security state.
        :type securityState: SecurityState
        :param schemeIsCryptographic: True if the page was loaded over cryptographic transport such as HTTPS.
        :type schemeIsCryptographic: bool
        :param explanations: List of explanations for the security state. If the overall security state is `insecure` or `warning`, at least one corresponding explanation should be included.
        :type explanations: array
        :param insecureContentStatus: Information about insecure content on the page.
        :type insecureContentStatus: InsecureContentStatus
        :param summary: Overrides user-visible description of the state.
        :type summary: str
        """
        super().__init__()
        self.securityState: SecurityState = securityState
        self.schemeIsCryptographic: bool = schemeIsCryptographic
        self.explanations: List[SecurityStateExplanation] = explanations
        self.insecureContentStatus: InsecureContentStatus = insecureContentStatus
        self.summary: Optional[str] = summary


EVENT_TO_CLASS = {
   "Security.certificateError": CertificateErrorEvent,
   "Security.securityStateChanged": SecurityStateChangedEvent,
}

