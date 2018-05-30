from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.target import types as Target

ServiceWorkerVersionStatus = TypeVar("ServiceWorkerVersionStatus", str, str) # 

ServiceWorkerVersionRunningStatus = TypeVar("ServiceWorkerVersionRunningStatus", str, str) # 


class ServiceWorkerVersion(ProtocolType):
    """
    ServiceWorker version.
    """

    def __init__(self, versionId: str, registrationId: str, scriptURL: str, runningStatus: ServiceWorkerVersionRunningStatus, status: ServiceWorkerVersionStatus, scriptLastModified: Optional[float] = None, scriptResponseTime: Optional[float] = None, controlledClients: Optional[List[Target.TargetID]] = None, targetId: Optional[Target.TargetID] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ServiceWorkerVersion']:
        if init is not None:
            return ServiceWorkerVersion(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ServiceWorkerVersion']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerVersion(**it))
            return list_of_self
        else:
            return init


class ServiceWorkerRegistration(ProtocolType):
    """
    ServiceWorker registration.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ServiceWorkerRegistration']:
        if init is not None:
            return ServiceWorkerRegistration(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ServiceWorkerRegistration']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerRegistration(**it))
            return list_of_self
        else:
            return init


class ServiceWorkerErrorMessage(ProtocolType):
    """
    ServiceWorker error message.
    """

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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ServiceWorkerErrorMessage']:
        if init is not None:
            return ServiceWorkerErrorMessage(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ServiceWorkerErrorMessage']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ServiceWorkerErrorMessage(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ServiceWorkerVersion": ServiceWorkerVersion,
    "ServiceWorkerRegistration": ServiceWorkerRegistration,
    "ServiceWorkerErrorMessage": ServiceWorkerErrorMessage,
}
