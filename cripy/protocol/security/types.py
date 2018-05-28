from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# An internal certificate ID value.
CertificateId = int

# A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories
MixedContentType = str

# The security level of a page or resource.
SecurityState = str

# The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request.
CertificateErrorAction = str


class SecurityStateExplanation(ChromeTypeBase):
    """An explanation of an factor contributing to the security state."""

    def __init__(self, securityState: 'SecurityState', title: str, summary: str, description: str, mixedContentType: 'MixedContentType', certificate: List['str']) -> None:
        """
        :param securityState: Security state representing the severity of the factor being explained.
        :type SecurityState:
        :param title: Title describing the type of factor.
        :type str:
        :param summary: Short phrase describing the type of factor.
        :type str:
        :param description: Full text explanation of the factor.
        :type str:
        :param mixedContentType: The type of mixed content described by the explanation.
        :type MixedContentType:
        :param certificate: Page certificate.
        :type array:
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

    def __init__(self, ranMixedContent: bool, displayedMixedContent: bool, containedMixedForm: bool, ranContentWithCertErrors: bool, displayedContentWithCertErrors: bool, ranInsecureContentStyle: 'SecurityState', displayedInsecureContentStyle: 'SecurityState') -> None:
        """
        :param ranMixedContent: True if the page was loaded over HTTPS and ran mixed (HTTP) content such as scripts.
        :type bool:
        :param displayedMixedContent: True if the page was loaded over HTTPS and displayed mixed (HTTP) content such as
        images.
        :type bool:
        :param containedMixedForm: True if the page was loaded over HTTPS and contained a form targeting an insecure
        url.
        :type bool:
        :param ranContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and ran content
        such as scripts that were loaded with certificate errors.
        :type bool:
        :param displayedContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and displayed
        content such as images that were loaded with certificate errors.
        :type bool:
        :param ranInsecureContentStyle: Security state representing a page that ran insecure content.
        :type SecurityState:
        :param displayedInsecureContentStyle: Security state representing a page that displayed insecure content.
        :type SecurityState:
        """
        super().__init__()
        self.ranMixedContent: bool = ranMixedContent
        self.displayedMixedContent: bool = displayedMixedContent
        self.containedMixedForm: bool = containedMixedForm
        self.ranContentWithCertErrors: bool = ranContentWithCertErrors
        self.displayedContentWithCertErrors: bool = displayedContentWithCertErrors
        self.ranInsecureContentStyle: SecurityState = ranInsecureContentStyle
        self.displayedInsecureContentStyle: SecurityState = displayedInsecureContentStyle


