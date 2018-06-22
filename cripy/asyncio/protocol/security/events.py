from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.security.types import *

__all__ = [
    "CertificateErrorEvent",
    "SecurityStateChangedEvent",
    "SECURITY_EVENTS_TO_CLASS",
    "SECURITY_EVENTS_NS"
]

class CertificateErrorEvent(object):
    """
    There is a certificate error.
	If overriding certificate errors is enabled, then it should be handled with the `handleCertificateError` command.
	Note: this event does not fire if the certificate error has been allowed internally.
	Only one client per target should override certificate errors at the same time.
    """

    event = "Security.certificateError"

    __slots__ = ["eventId", "errorType", "requestURL"]

    def __init__(self, eventId: int, errorType: str, requestURL: str) -> None:
        """
        Create a new instance of CertificateErrorEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.eventId is not None:
            repr_args.append("eventId={!r}".format(self.eventId))
        if self.errorType is not None:
            repr_args.append("errorType={!r}".format(self.errorType))
        if self.requestURL is not None:
            repr_args.append("requestURL={!r}".format(self.requestURL))
        return "CertificateErrorEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['CertificateErrorEvent', dict]]:
        """
        Safely create CertificateErrorEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of CertificateErrorEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of CertificateErrorEvent if creation did not fail
        :rtype: Optional[Union[dict, CertificateErrorEvent]]
        """
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
        """
        Safely create a new list CertificateErrorEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list CertificateErrorEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of CertificateErrorEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, CertificateErrorEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CertificateErrorEvent.safe_create(it))
            return list_of_self
        else:
            return init


class SecurityStateChangedEvent(object):
    """
    The security state of the page changed.
    """

    event = "Security.securityStateChanged"

    __slots__ = ["securityState", "schemeIsCryptographic", "explanations", "insecureContentStatus", "summary"]

    def __init__(self, securityState: str, schemeIsCryptographic: bool, explanations: List[Union[SecurityStateExplanation, dict]], insecureContentStatus: Union[InsecureContentStatus, dict], summary: Optional[str] = None) -> None:
        """
        Create a new instance of SecurityStateChangedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.securityState is not None:
            repr_args.append("securityState={!r}".format(self.securityState))
        if self.schemeIsCryptographic is not None:
            repr_args.append("schemeIsCryptographic={!r}".format(self.schemeIsCryptographic))
        if self.explanations is not None:
            repr_args.append("explanations={!r}".format(self.explanations))
        if self.insecureContentStatus is not None:
            repr_args.append("insecureContentStatus={!r}".format(self.insecureContentStatus))
        if self.summary is not None:
            repr_args.append("summary={!r}".format(self.summary))
        return "SecurityStateChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['SecurityStateChangedEvent', dict]]:
        """
        Safely create SecurityStateChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of SecurityStateChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of SecurityStateChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, SecurityStateChangedEvent]]
        """
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
        """
        Safely create a new list SecurityStateChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list SecurityStateChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of SecurityStateChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, SecurityStateChangedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityStateChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


SECURITY_EVENTS_TO_CLASS = {
   "Security.certificateError": CertificateErrorEvent,
   "Security.securityStateChanged": SecurityStateChangedEvent,
}

SecurityNS = namedtuple("SecurityNS", ["CertificateError", "SecurityStateChanged"])

SECURITY_EVENTS_NS = SecurityNS(
  CertificateError="Security.certificateError",
  SecurityStateChanged="Security.securityStateChanged",
)
