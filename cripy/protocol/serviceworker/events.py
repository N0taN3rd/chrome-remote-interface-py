from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class WorkerErrorReportedEvent(BaseEvent):

    event: str = "ServiceWorker.workerErrorReported"

    def __init__(self) -> None:
        """
        :param ServiceWorkerErrorMessage errorMessage: The errorMessage
        :type errorMessage: ServiceWorkerErrorMessage
        """
        super().__init__()


class WorkerRegistrationUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerRegistrationUpdated"

    def __init__(self) -> None:
        """
        :param array registrations: The registrations
        :type registrations: array
        """
        super().__init__()


class WorkerVersionUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerVersionUpdated"

    def __init__(self) -> None:
        """
        :param array versions: The versions
        :type versions: array
        """
        super().__init__()


EVENT_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

