from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.target import types as Target

# 
ServiceWorkerVersionRunningStatus = str

# 
ServiceWorkerVersionStatus = str


class ServiceWorkerRegistration(ChromeTypeBase):
    """ServiceWorker registration."""
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
        self.registrationId: str = registrationId
        self.scopeURL: str = scopeURL
        self.isDeleted: bool = isDeleted


class ServiceWorkerVersion(ChromeTypeBase):
    """ServiceWorker version."""
    def __init__(self, versionId: str, registrationId: str, scriptURL: str, runningStatus: 'ServiceWorkerVersionRunningStatus', status: 'ServiceWorkerVersionStatus', scriptLastModified: Optional[float] = None, scriptResponseTime: Optional[float] = None, controlledClients: Optional[List['Target.TargetID']] = None, targetId: Optional['Target.TargetID'] = None) -> None:
        """
        :param versionId: The versionId
        :type versionId: str
        :param registrationId: The registrationId
        :type registrationId: str
        :param scriptURL: The scriptURL
        :type scriptURL: str
        :param runningStatus: The runningStatus
        :type runningStatus: ServiceWorkerVersionRunningStatus
        :param status: The status
        :type status: ServiceWorkerVersionStatus
        :param scriptLastModified: The Last-Modified header value of the main script.
        :type scriptLastModified: float
        :param scriptResponseTime: The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated.
        :type scriptResponseTime: float
        :param controlledClients: The controlledClients
        :type controlledClients: array
        :param targetId: The targetId
        :type targetId: Target.TargetID
        """
        super().__init__()
        self.versionId: str = versionId
        self.registrationId: str = registrationId
        self.scriptURL: str = scriptURL
        self.runningStatus: ServiceWorkerVersionRunningStatus = runningStatus
        self.status: ServiceWorkerVersionStatus = status
        self.scriptLastModified: Optional[float] = scriptLastModified
        self.scriptResponseTime: Optional[float] = scriptResponseTime
        self.controlledClients: Optional[List[Target.TargetID]] = controlledClients
        self.targetId: Optional[Target.TargetID] = targetId


class ServiceWorkerErrorMessage(ChromeTypeBase):
    """ServiceWorker error message."""
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
        self.errorMessage: str = errorMessage
        self.registrationId: str = registrationId
        self.versionId: str = versionId
        self.sourceURL: str = sourceURL
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


