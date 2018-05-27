from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

CertificateId = int

MixedContentType = str

SecurityState = str

CertificateErrorAction = str


class SecurityStateExplanation(ChromeTypeBase):

    def __init__(
        self,
        securityState: "SecurityState",
        title: str,
        summary: str,
        description: str,
        mixedContentType: "MixedContentType",
        certificate: List["str"],
    ) -> None:
        super().__init__()
        self.securityState: SecurityState = securityState
        self.title: str = title
        self.summary: str = summary
        self.description: str = description
        self.mixedContentType: MixedContentType = mixedContentType
        self.certificate: List[str] = certificate


class InsecureContentStatus(ChromeTypeBase):

    def __init__(
        self,
        ranMixedContent: bool,
        displayedMixedContent: bool,
        containedMixedForm: bool,
        ranContentWithCertErrors: bool,
        displayedContentWithCertErrors: bool,
        ranInsecureContentStyle: "SecurityState",
        displayedInsecureContentStyle: "SecurityState",
    ) -> None:
        super().__init__()
        self.ranMixedContent: bool = ranMixedContent
        self.displayedMixedContent: bool = displayedMixedContent
        self.containedMixedForm: bool = containedMixedForm
        self.ranContentWithCertErrors: bool = ranContentWithCertErrors
        self.displayedContentWithCertErrors: bool = displayedContentWithCertErrors
        self.ranInsecureContentStyle: SecurityState = ranInsecureContentStyle
        self.displayedInsecureContentStyle: SecurityState = displayedInsecureContentStyle
