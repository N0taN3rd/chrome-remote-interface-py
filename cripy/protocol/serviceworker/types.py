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
        :param str registrationId: The registrationId
        :param str scopeURL: The scopeURL
        :param bool isDeleted: The isDeleted
        """
        super().__init__()
        self.registrationId: str = registrationId
        self.scopeURL: str = scopeURL
        self.isDeleted: bool = isDeleted


class ServiceWorkerVersion(ChromeTypeBase):
    """ServiceWorker version."""
    def __init__(self, versionId: str, registrationId: str, scriptURL: str, runningStatus: 'ServiceWorkerVersionRunningStatus', status: 'ServiceWorkerVersionStatus', scriptLastModified: Optional[float] = None, scriptResponseTime: Optional[float] = None, controlledClients: Optional[List['Target.TargetID']] = None, targetId: Optional['Target.TargetID'] = None) -> None:
        """
        :param str versionId: The versionId
        :param str registrationId: The registrationId
        :param str scriptURL: The scriptURL
        :param ServiceWorkerVersionRunningStatus runningStatus: The runningStatus
        :param ServiceWorkerVersionStatus status: The status
        :param float scriptLastModified: The Last-Modified header value of the main script.
        :param float scriptResponseTime: The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated.
        :param array controlledClients: The controlledClients
        :param Target.TargetID targetId: The targetId
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
        :param str errorMessage: The errorMessage
        :param str registrationId: The registrationId
        :param str versionId: The versionId
        :param str sourceURL: The sourceURL
        :param int lineNumber: The lineNumber
        :param int columnNumber: The columnNumber
        """
        super().__init__()
        self.errorMessage: str = errorMessage
        self.registrationId: str = registrationId
        self.versionId: str = versionId
        self.sourceURL: str = sourceURL
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


