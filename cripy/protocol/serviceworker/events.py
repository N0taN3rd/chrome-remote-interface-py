from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.serviceworker.types import *
except ImportError:
    pass


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
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerErrorReportedEvent', dict]]:
        if init is not None:
            try:
                ourselves = WorkerErrorReportedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WorkerErrorReportedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerErrorReportedEvent.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerRegistrationUpdatedEvent', dict]]:
        if init is not None:
            try:
                ourselves = WorkerRegistrationUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WorkerRegistrationUpdatedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerRegistrationUpdatedEvent.safe_create(it))
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
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerVersionUpdatedEvent', dict]]:
        if init is not None:
            try:
                ourselves = WorkerVersionUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WorkerVersionUpdatedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerVersionUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

