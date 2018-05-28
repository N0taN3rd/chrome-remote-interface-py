from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class WorkerErrorReportedEvent(BaseEvent):

    event: str = "ServiceWorker.workerErrorReported"

    def __init__(self) -> None:
        """
        :param errorMessage: The errorMessage
        :type ServiceWorkerErrorMessage:
        """
        super().__init__()


class WorkerRegistrationUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerRegistrationUpdated"

    def __init__(self) -> None:
        """
        :param registrations: The registrations
        :type array:
        """
        super().__init__()


class WorkerVersionUpdatedEvent(BaseEvent):

    event: str = "ServiceWorker.workerVersionUpdated"

    def __init__(self) -> None:
        """
        :param versions: The versions
        :type array:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

