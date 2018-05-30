from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.serviceworker.types import (
    ServiceWorkerErrorMessage,
)


class WorkerErrorReportedEvent(BaseEvent):

    event = "ServiceWorker.workerErrorReported"

    def __init__(self, errorMessage: Union[ServiceWorkerErrorMessage, dict]) -> None:
        """
        :param errorMessage: The errorMessage
        :type errorMessage: dict
        """
        super().__init__()
        self.errorMessage = ServiceWorkerErrorMessage.safe_create(errorMessage)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WorkerErrorReportedEvent']:
        if init is not None:
            return WorkerErrorReportedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WorkerErrorReportedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerErrorReportedEvent(**it))
            return list_of_self
        else:
            return init


class WorkerRegistrationUpdatedEvent(BaseEvent):

    event = "ServiceWorker.workerRegistrationUpdated"

    def __init__(self, registrations: List[Union[ServiceWorkerRegistration, dict]]) -> None:
        """
        :param registrations: The registrations
        :type registrations: List[dict]
        """
        super().__init__()
        self.registrations = ServiceWorkerRegistration.safe_create_from_list(registrations)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WorkerRegistrationUpdatedEvent']:
        if init is not None:
            return WorkerRegistrationUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WorkerRegistrationUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerRegistrationUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class WorkerVersionUpdatedEvent(BaseEvent):

    event = "ServiceWorker.workerVersionUpdated"

    def __init__(self, versions: List[Union[ServiceWorkerVersion, dict]]) -> None:
        """
        :param versions: The versions
        :type versions: List[dict]
        """
        super().__init__()
        self.versions = ServiceWorkerVersion.safe_create_from_list(versions)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WorkerVersionUpdatedEvent']:
        if init is not None:
            return WorkerVersionUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WorkerVersionUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerVersionUpdatedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

