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
        :type str:
        :param scopeURL: The scopeURL
        :type str:
        :param isDeleted: The isDeleted
        :type bool:
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
        :type str:
        :param registrationId: The registrationId
        :type str:
        :param scriptURL: The scriptURL
        :type str:
        :param runningStatus: The runningStatus
        :type ServiceWorkerVersionRunningStatus:
        :param status: The status
        :type ServiceWorkerVersionStatus:
        :param scriptLastModified: The Last-Modified header value of the main script.
        :type float:
        :param scriptResponseTime: The time at which the response headers of the main script were received from the
        server. For cached script it is the last time the cache entry was validated.
        :type float:
        :param controlledClients: The controlledClients
        :type array:
        :param targetId: The targetId
        :type Target.TargetID:
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
        :type str:
        :param registrationId: The registrationId
        :type str:
        :param versionId: The versionId
        :type str:
        :param sourceURL: The sourceURL
        :type str:
        :param lineNumber: The lineNumber
        :type int:
        :param columnNumber: The columnNumber
        :type int:
        """
        super().__init__()
        self.errorMessage: str = errorMessage
        self.registrationId: str = registrationId
        self.versionId: str = versionId
        self.sourceURL: str = sourceURL
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


