from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

SecurityState = TypeVar("SecurityState", str, str) # The security level of a page or resource.

MixedContentType = TypeVar("MixedContentType", str, str) # A description of mixed content (HTTP resources on HTTPS pages), as defined by https://www.w3.org/TR/mixed-content/#categories

CertificateId = TypeVar("CertificateId", int, int) # An internal certificate ID value.

CertificateErrorAction = TypeVar("CertificateErrorAction", str, str) # The action to take when a certificate error occurs. continue will continue processing the request and cancel will cancel the request.


class SecurityStateExplanation(ProtocolType):
    """
    An explanation of an factor contributing to the security state.
    """

    def __init__(self, securityState: SecurityState, title: str, summary: str, description: str, mixedContentType: MixedContentType, certificate: List[str]) -> None:
        """
        :param securityState: Security state representing the severity of the factor being explained.
        :type securityState: str
        :param title: Title describing the type of factor.
        :type title: str
        :param summary: Short phrase describing the type of factor.
        :type summary: str
        :param description: Full text explanation of the factor.
        :type description: str
        :param mixedContentType: The type of mixed content described by the explanation.
        :type mixedContentType: str
        :param certificate: Page certificate.
        :type certificate: List[str]
        """
        super().__init__()
        self.securityState = securityState
        self.title = title
        self.summary = summary
        self.description = description
        self.mixedContentType = mixedContentType
        self.certificate = certificate

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['SecurityStateExplanation']:
        if init is not None:
            return SecurityStateExplanation(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['SecurityStateExplanation']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityStateExplanation(**it))
            return list_of_self
        else:
            return init


class InsecureContentStatus(ProtocolType):
    """
    Information about insecure content on the page.
    """

    def __init__(self, ranMixedContent: bool, displayedMixedContent: bool, containedMixedForm: bool, ranContentWithCertErrors: bool, displayedContentWithCertErrors: bool, ranInsecureContentStyle: SecurityState, displayedInsecureContentStyle: SecurityState) -> None:
        """
        :param ranMixedContent: True if the page was loaded over HTTPS and ran mixed (HTTP) content such as scripts.
        :type ranMixedContent: bool
        :param displayedMixedContent: True if the page was loaded over HTTPS and displayed mixed (HTTP) content such as images.
        :type displayedMixedContent: bool
        :param containedMixedForm: True if the page was loaded over HTTPS and contained a form targeting an insecure url.
        :type containedMixedForm: bool
        :param ranContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and ran content such as scripts that were loaded with certificate errors.
        :type ranContentWithCertErrors: bool
        :param displayedContentWithCertErrors: True if the page was loaded over HTTPS without certificate errors, and displayed content such as images that were loaded with certificate errors.
        :type displayedContentWithCertErrors: bool
        :param ranInsecureContentStyle: Security state representing a page that ran insecure content.
        :type ranInsecureContentStyle: str
        :param displayedInsecureContentStyle: Security state representing a page that displayed insecure content.
        :type displayedInsecureContentStyle: str
        """
        super().__init__()
        self.ranMixedContent = ranMixedContent
        self.displayedMixedContent = displayedMixedContent
        self.containedMixedForm = containedMixedForm
        self.ranContentWithCertErrors = ranContentWithCertErrors
        self.displayedContentWithCertErrors = displayedContentWithCertErrors
        self.ranInsecureContentStyle = ranInsecureContentStyle
        self.displayedInsecureContentStyle = displayedInsecureContentStyle

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InsecureContentStatus']:
        if init is not None:
            return InsecureContentStatus(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InsecureContentStatus']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InsecureContentStatus(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SecurityStateExplanation": SecurityStateExplanation,
    "InsecureContentStatus": InsecureContentStatus,
}
