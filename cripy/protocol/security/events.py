from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.security.types import *
except ImportError:
    pass


class CertificateErrorEvent(object):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.eventId is not None:
            repr_args.append("eventId={!r}".format(self.eventId))
        if self.errorType is not None:
            repr_args.append("errorType={!r}".format(self.errorType))
        if self.requestURL is not None:
            repr_args.append("requestURL={!r}".format(self.requestURL))
        return "CertificateErrorEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["CertificateErrorEvent", dict]]:
        if init is not None:
            try:
                ourselves = CertificateErrorEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CertificateErrorEvent", dict]]]:
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

    def __init__(
        self,
        securityState: str,
        schemeIsCryptographic: bool,
        explanations: List[Union[SecurityStateExplanation, dict]],
        insecureContentStatus: Union[InsecureContentStatus, dict],
        summary: Optional[str] = None,
    ) -> None:
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
        self.insecureContentStatus = InsecureContentStatus.safe_create(
            insecureContentStatus
        )
        self.summary = summary

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.securityState is not None:
            repr_args.append("securityState={!r}".format(self.securityState))
        if self.schemeIsCryptographic is not None:
            repr_args.append(
                "schemeIsCryptographic={!r}".format(self.schemeIsCryptographic)
            )
        if self.explanations is not None:
            repr_args.append("explanations={!r}".format(self.explanations))
        if self.insecureContentStatus is not None:
            repr_args.append(
                "insecureContentStatus={!r}".format(self.insecureContentStatus)
            )
        if self.summary is not None:
            repr_args.append("summary={!r}".format(self.summary))
        return "SecurityStateChangedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["SecurityStateChangedEvent", dict]]:
        if init is not None:
            try:
                ourselves = SecurityStateChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["SecurityStateChangedEvent", dict]]]:
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

EVENT_NS = SimpleNamespace(
    CertificateError="Security.certificateError",
    SecurityStateChanged="Security.securityStateChanged",
)
