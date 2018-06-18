from typing import Any, List, Optional, Union, TypeVar


class SecurityStateExplanation(object):
    """
    An explanation of an factor contributing to the security state.
    """

    def __init__(
        self,
        securityState: str,
        title: str,
        summary: str,
        description: str,
        mixedContentType: str,
        certificate: List[str],
    ) -> None:
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
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        if self.summary is not None:
            repr_args.append("summary={!r}".format(self.summary))
        if self.description is not None:
            repr_args.append("description={!r}".format(self.description))
        if self.mixedContentType is not None:
            repr_args.append("mixedContentType={!r}".format(self.mixedContentType))
        if self.certificate is not None:
            repr_args.append("certificate={!r}".format(self.certificate))
        return "SecurityStateExplanation(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["SecurityStateExplanation", dict]]:
        if init is not None:
            try:
                ourselves = SecurityStateExplanation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["SecurityStateExplanation", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(SecurityStateExplanation.safe_create(it))
            return list_of_self
        else:
            return init


class InsecureContentStatus(object):
    """
    Information about insecure content on the page.
    """

    def __init__(
        self,
        ranMixedContent: bool,
        displayedMixedContent: bool,
        containedMixedForm: bool,
        ranContentWithCertErrors: bool,
        displayedContentWithCertErrors: bool,
        ranInsecureContentStyle: str,
        displayedInsecureContentStyle: str,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.ranMixedContent is not None:
            repr_args.append("ranMixedContent={!r}".format(self.ranMixedContent))
        if self.displayedMixedContent is not None:
            repr_args.append(
                "displayedMixedContent={!r}".format(self.displayedMixedContent)
            )
        if self.containedMixedForm is not None:
            repr_args.append("containedMixedForm={!r}".format(self.containedMixedForm))
        if self.ranContentWithCertErrors is not None:
            repr_args.append(
                "ranContentWithCertErrors={!r}".format(self.ranContentWithCertErrors)
            )
        if self.displayedContentWithCertErrors is not None:
            repr_args.append(
                "displayedContentWithCertErrors={!r}".format(
                    self.displayedContentWithCertErrors
                )
            )
        if self.ranInsecureContentStyle is not None:
            repr_args.append(
                "ranInsecureContentStyle={!r}".format(self.ranInsecureContentStyle)
            )
        if self.displayedInsecureContentStyle is not None:
            repr_args.append(
                "displayedInsecureContentStyle={!r}".format(
                    self.displayedInsecureContentStyle
                )
            )
        return "InsecureContentStatus(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["InsecureContentStatus", dict]]:
        if init is not None:
            try:
                ourselves = InsecureContentStatus(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["InsecureContentStatus", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InsecureContentStatus.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "SecurityStateExplanation": SecurityStateExplanation,
    "InsecureContentStatus": InsecureContentStatus,
}
