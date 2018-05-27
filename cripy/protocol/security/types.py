from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

CertificateId = int

MixedContentType = str

SecurityState = str

CertificateErrorAction = str


class SecurityStateExplanation(ChromeTypeBase):
    """An explanation of an factor contributing to the security state."""

    def __init__(
        self,
        securityState: "SecurityState",
        title: str,
        summary: str,
        description: str,
        mixedContentType: "MixedContentType",
        certificate: List["str"],
    ) -> None:
        """
        :param securityState: Security state representing the severity of the factor being explained.
        :param title: Title describing the type of factor.
        :param summary: Short phrase describing the type of factor.
        :param description: Full text explanation of the factor.
        :param mixedContentType: The type of mixed content described by the explanation.
        :param certificate: Page certificate.
        """
        super().__init__()
        self.securityState: SecurityState = securityState
        self.title: str = title
        self.summary: str = summary
        self.description: str = description
        self.mixedContentType: MixedContentType = mixedContentType
        self.certificate: List[str] = certificate


class InsecureContentStatus(ChromeTypeBase):
    """Information about insecure content on the page."""

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
        """
        :param ranMixedContent: True if the page was loaded over HTTPS and ran mixed (HTTP) content such as scripts.
        :param displayedMixedContent: True if the page was loaded over HTTPS and displayed mixed (HTTP) content such as images.
        :param containedMixedForm: True if the page was loaded over HTTPS and contained a form targeting an insecure url.
        :param ranContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and ran content such as
scripts that were loaded with certificate errors.
        :param displayedContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and displayed content
such as images that were loaded with certificate errors.
        :param ranInsecureContentStyle: Security state representing a page that ran insecure content.
        :param displayedInsecureContentStyle: Security state representing a page that displayed insecure content.
        """
        super().__init__()
        self.ranMixedContent: bool = ranMixedContent
        self.displayedMixedContent: bool = displayedMixedContent
        self.containedMixedForm: bool = containedMixedForm
        self.ranContentWithCertErrors: bool = ranContentWithCertErrors
        self.displayedContentWithCertErrors: bool = displayedContentWithCertErrors
        self.ranInsecureContentStyle: SecurityState = ranInsecureContentStyle
        self.displayedInsecureContentStyle: SecurityState = displayedInsecureContentStyle
