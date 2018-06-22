from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.target import types as Target

__all__ = [
    "ServiceWorkerVersion",
    "ServiceWorkerRegistration",
    "ServiceWorkerErrorMessage",
    "SERVICEWORKER_TYPES_TO_OBJECT"
]


class ServiceWorkerVersion(object):
    """
    ServiceWorker version.
    """

    __slots__ = ["versionId", "registrationId", "scriptURL", "runningStatus", "status", "scriptLastModified", "scriptResponseTime", "controlledClients", "targetId"]

    def __init__(self, versionId: str, registrationId: str, scriptURL: str, runningStatus: str, status: str, scriptLastModified: Optional[float] = None, scriptResponseTime: Optional[float] = None, controlledClients: Optional[List[str]] = None, targetId: Optional[str] = None) -> None:
        """
        :param versionId: The versionId
        :type versionId: str
        :param registrationId: The registrationId
        :type registrationId: str
        :param scriptURL: The scriptURL
        :type scriptURL: str
        :param runningStatus: The runningStatus
        :type runningStatus: str
        :param status: The status
        :type status: str
        :param scriptLastModified: The Last-Modified header value of the main script.
        :type scriptLastModified: Optional[float]
        :param scriptResponseTime: The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated.
        :type scriptResponseTime: Optional[float]
        :param controlledClients: The controlledClients
        :type controlledClients: Optional[List[str]]
        :param targetId: The targetId
        :type targetId: Optional[str]
        """
        super().__init__()
        self.versionId = versionId
        self.registrationId = registrationId
        self.scriptURL = scriptURL
        self.runningStatus = runningStatus
        self.status = status
        self.scriptLastModified = scriptLastModified
        self.scriptResponseTime = scriptResponseTime
        self.controlledClients = controlledClients
        self.targetId = targetId

    def __repr__(self) -> str:
        repr_args = []
        if self.versionId is not None:
            repr_args.append("versionId={!r}".format(self.versionId))
        if self.registrationId is not None:
            repr_args.append("registrationId={!r}".format(self.registrationId))
        if self.scriptURL is not None:
            repr_args.append("scriptURL={!r}".format(self.scriptURL))
        if self.runningStatus is not None:
            repr_args.append("runningStatus={!r}".format(self.runningStatus))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        if self.scriptLastModified is not None:
            repr_args.append("scriptLastModified={!r}".format(self.scriptLastModified))
        if self.scriptResponseTime is not None:
            repr_args.append("scriptResponseTime={!r}".format(self.scriptResponseTime))
        if self.controlledClients is not None:
            repr_args.append("controlledClients={!r}".format(self.controlledClients))
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        return "ServiceWorkerVersion(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ServiceWorkerVersion', dict]]:
        """
        Safely create ServiceWorkerVersion from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ServiceWorkerVersion
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ServiceWorkerVersion if creation did not fail
        :rtype: Optional[Union[dict, ServiceWorkerVersion]]
        """
        if init is not None:
            try:
                ourselves = ServiceWorkerVersion(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ServiceWorkerVersion', dict]]]:
        """
        Safely create a new list ServiceWorkerVersions from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ServiceWorkerVersion instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ServiceWorkerVersion instances if creation did not fail
        :rtype: Optional[List[Union[dict, ServiceWorkerVersion]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerVersion.safe_create(it))
            return list_of_self
        else:
            return init


class ServiceWorkerRegistration(object):
    """
    ServiceWorker registration.
    """

    __slots__ = ["registrationId", "scopeURL", "isDeleted"]

    def __init__(self, registrationId: str, scopeURL: str, isDeleted: bool) -> None:
        """
        :param registrationId: The registrationId
        :type registrationId: str
        :param scopeURL: The scopeURL
        :type scopeURL: str
        :param isDeleted: The isDeleted
        :type isDeleted: bool
        """
        super().__init__()
        self.registrationId = registrationId
        self.scopeURL = scopeURL
        self.isDeleted = isDeleted

    def __repr__(self) -> str:
        repr_args = []
        if self.registrationId is not None:
            repr_args.append("registrationId={!r}".format(self.registrationId))
        if self.scopeURL is not None:
            repr_args.append("scopeURL={!r}".format(self.scopeURL))
        if self.isDeleted is not None:
            repr_args.append("isDeleted={!r}".format(self.isDeleted))
        return "ServiceWorkerRegistration(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ServiceWorkerRegistration', dict]]:
        """
        Safely create ServiceWorkerRegistration from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ServiceWorkerRegistration
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ServiceWorkerRegistration if creation did not fail
        :rtype: Optional[Union[dict, ServiceWorkerRegistration]]
        """
        if init is not None:
            try:
                ourselves = ServiceWorkerRegistration(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ServiceWorkerRegistration', dict]]]:
        """
        Safely create a new list ServiceWorkerRegistrations from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ServiceWorkerRegistration instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ServiceWorkerRegistration instances if creation did not fail
        :rtype: Optional[List[Union[dict, ServiceWorkerRegistration]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerRegistration.safe_create(it))
            return list_of_self
        else:
            return init


class ServiceWorkerErrorMessage(object):
    """
    ServiceWorker error message.
    """

    __slots__ = ["errorMessage", "registrationId", "versionId", "sourceURL", "lineNumber", "columnNumber"]

    def __init__(self, errorMessage: str, registrationId: str, versionId: str, sourceURL: str, lineNumber: int, columnNumber: int) -> None:
        """
        :param errorMessage: The errorMessage
        :type errorMessage: str
        :param registrationId: The registrationId
        :type registrationId: str
        :param versionId: The versionId
        :type versionId: str
        :param sourceURL: The sourceURL
        :type sourceURL: str
        :param lineNumber: The lineNumber
        :type lineNumber: int
        :param columnNumber: The columnNumber
        :type columnNumber: int
        """
        super().__init__()
        self.errorMessage = errorMessage
        self.registrationId = registrationId
        self.versionId = versionId
        self.sourceURL = sourceURL
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

    def __repr__(self) -> str:
        repr_args = []
        if self.errorMessage is not None:
            repr_args.append("errorMessage={!r}".format(self.errorMessage))
        if self.registrationId is not None:
            repr_args.append("registrationId={!r}".format(self.registrationId))
        if self.versionId is not None:
            repr_args.append("versionId={!r}".format(self.versionId))
        if self.sourceURL is not None:
            repr_args.append("sourceURL={!r}".format(self.sourceURL))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        return "ServiceWorkerErrorMessage(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ServiceWorkerErrorMessage', dict]]:
        """
        Safely create ServiceWorkerErrorMessage from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ServiceWorkerErrorMessage
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ServiceWorkerErrorMessage if creation did not fail
        :rtype: Optional[Union[dict, ServiceWorkerErrorMessage]]
        """
        if init is not None:
            try:
                ourselves = ServiceWorkerErrorMessage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ServiceWorkerErrorMessage', dict]]]:
        """
        Safely create a new list ServiceWorkerErrorMessages from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ServiceWorkerErrorMessage instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ServiceWorkerErrorMessage instances if creation did not fail
        :rtype: Optional[List[Union[dict, ServiceWorkerErrorMessage]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerErrorMessage.safe_create(it))
            return list_of_self
        else:
            return init


SERVICEWORKER_TYPES_TO_OBJECT = {
    "ServiceWorkerVersion": ServiceWorkerVersion,
    "ServiceWorkerRegistration": ServiceWorkerRegistration,
    "ServiceWorkerErrorMessage": ServiceWorkerErrorMessage,
}
