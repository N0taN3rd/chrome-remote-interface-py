from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.security.types import *
except ImportError:
    pass


class CertificateErrorEvent(BaseEvent):
    """
    There is a certificate error.
	If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command.
	Note: this event does not fire if the certificate error has been allowed internally.
	Only one client per target should override certificate errors at the same time.
    """

    event = "Security.certificateError"

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
        self.eventId = eventId
        self.errorType = errorType
        self.requestURL = requestURL

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CertificateErrorEvent', dict]]:
        if init is not None:
            try:
                ourselves = CertificateErrorEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['CertificateErrorEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CertificateErrorEvent.safe_create(it))
            return list_of_self
        else:
            return init


class SecurityStateChangedEvent(BaseEvent):
    """
    The security state of the page changed.
    """

    event = "Security.securityStateChanged"

    def __init__(self, securityState: str, schemeIsCryptographic: bool, explanations: List[Union[SecurityStateExplanation, dict]], insecureContentStatus: Union[InsecureContentStatus, dict], summary: Optional[str] = None) -> None:
        """
        :param securityState: Security state.
        :type securityState: str
        :param schemeIsCryptographic: True if the page was loaded over cryptographic transport such as HTTPS.
        :type schemeIsCryptographic: bool
        :param explanations: List of explanations for the security state. If the overall security state is `insecure` or `warning`, at least one corresponding explanation should be included.
        :type explanations: List[dict]
        :param insecureContentStatus: Information about insecure content on the page.
        :type insecureContentStatus: dict
        :param summary: Overrides user-visible description of the state.
        :type summary: Optional[str]
        """
        super().__init__()
        self.securityState = securityState
        self.schemeIsCryptographic = schemeIsCryptographic
        self.explanations = SecurityStateExplanation.safe_create_from_list(explanations)
        self.insecureContentStatus = InsecureContentStatus.safe_create(insecureContentStatus)
        self.summary = summary

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SecurityStateChangedEvent', dict]]:
        if init is not None:
            try:
                ourselves = SecurityStateChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['SecurityStateChangedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityStateChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Security.certificateError": CertificateErrorEvent,
   "Security.securityStateChanged": SecurityStateChangedEvent,
}

