from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.target import types as Target

ServiceWorkerVersionRunningStatus = str

ServiceWorkerVersionStatus = str


class ServiceWorkerRegistration(ChromeTypeBase):

    def __init__(self, registrationId: str, scopeURL: str, isDeleted: bool) -> None:
        super().__init__()
        self.registrationId: str = registrationId
        self.scopeURL: str = scopeURL
        self.isDeleted: bool = isDeleted


class ServiceWorkerVersion(ChromeTypeBase):

    def __init__(
        self,
        versionId: str,
        registrationId: str,
        scriptURL: str,
        runningStatus: "ServiceWorkerVersionRunningStatus",
        status: "ServiceWorkerVersionStatus",
        scriptLastModified: Optional[float] = None,
        scriptResponseTime: Optional[float] = None,
        controlledClients: Optional[List["Target.TargetID"]] = None,
        targetId: Optional["Target.TargetID"] = None,
    ) -> None:
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

    def __init__(
        self,
        errorMessage: str,
        registrationId: str,
        versionId: str,
        sourceURL: str,
        lineNumber: int,
        columnNumber: int,
    ) -> None:
        super().__init__()
        self.errorMessage: str = errorMessage
        self.registrationId: str = registrationId
        self.versionId: str = versionId
        self.sourceURL: str = sourceURL
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber
