from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.serviceworker.types import (
    ServiceWorkerErrorMessage,
)


class WorkerErrorReportedEvent(BaseEvent):

    event: str = "ServiceWorker.workerErrorReported"

    def __init__(self, errorMessage: ServiceWorkerErrorMessage) -> None:
        """
        :param errorMessage: The errorMessage
        :type errorMessage: ServiceWorkerErrorMessage
        """
        super().__init__()
        self.errorMessage: ServiceWorkerErrorMessage = errorMessage


class WorkerRegistrationUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerRegistrationUpdated"

    def __init__(self, registrations: List[ServiceWorkerRegistration]) -> None:
        """
        :param registrations: The registrations
        :type registrations: array
        """
        super().__init__()
        self.registrations: List[ServiceWorkerRegistration] = registrations


class WorkerVersionUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerVersionUpdated"

    def __init__(self, versions: List[ServiceWorkerVersion]) -> None:
        """
        :param versions: The versions
        :type versions: array
        """
        super().__init__()
        self.versions: List[ServiceWorkerVersion] = versions


EVENT_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

