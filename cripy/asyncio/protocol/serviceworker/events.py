from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.serviceworker.types import *

__all__ = [
    "WorkerErrorReportedEvent",
    "WorkerRegistrationUpdatedEvent",
    "WorkerVersionUpdatedEvent",
    "SERVICEWORKER_EVENTS_TO_CLASS",
    "SERVICEWORKER_EVENTS_NS"
]

class WorkerErrorReportedEvent(object):

    event = "ServiceWorker.workerErrorReported"

    __slots__ = ["errorMessage"]

    def __init__(self, errorMessage: Union[ServiceWorkerErrorMessage, dict]) -> None:
        """
        Create a new instance of WorkerErrorReportedEvent

        :param errorMessage: The errorMessage
        :type errorMessage: dict
        """
        super().__init__()
        self.errorMessage = ServiceWorkerErrorMessage.safe_create(errorMessage)

    def __repr__(self) -> str:
        repr_args = []
        if self.errorMessage is not None:
            repr_args.append("errorMessage={!r}".format(self.errorMessage))
        return "WorkerErrorReportedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerErrorReportedEvent', dict]]:
        """
        Safely create WorkerErrorReportedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WorkerErrorReportedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WorkerErrorReportedEvent if creation did not fail
        :rtype: Optional[Union[dict, WorkerErrorReportedEvent]]
        """
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
        """
        Safely create a new list WorkerErrorReportedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WorkerErrorReportedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WorkerErrorReportedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WorkerErrorReportedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerErrorReportedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WorkerRegistrationUpdatedEvent(object):

    event = "ServiceWorker.workerRegistrationUpdated"

    __slots__ = ["registrations"]

    def __init__(self, registrations: List[Union[ServiceWorkerRegistration, dict]]) -> None:
        """
        Create a new instance of WorkerRegistrationUpdatedEvent

        :param registrations: The registrations
        :type registrations: List[dict]
        """
        super().__init__()
        self.registrations = ServiceWorkerRegistration.safe_create_from_list(registrations)

    def __repr__(self) -> str:
        repr_args = []
        if self.registrations is not None:
            repr_args.append("registrations={!r}".format(self.registrations))
        return "WorkerRegistrationUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerRegistrationUpdatedEvent', dict]]:
        """
        Safely create WorkerRegistrationUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WorkerRegistrationUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WorkerRegistrationUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, WorkerRegistrationUpdatedEvent]]
        """
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
        """
        Safely create a new list WorkerRegistrationUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WorkerRegistrationUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WorkerRegistrationUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WorkerRegistrationUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerRegistrationUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WorkerVersionUpdatedEvent(object):

    event = "ServiceWorker.workerVersionUpdated"

    __slots__ = ["versions"]

    def __init__(self, versions: List[Union[ServiceWorkerVersion, dict]]) -> None:
        """
        Create a new instance of WorkerVersionUpdatedEvent

        :param versions: The versions
        :type versions: List[dict]
        """
        super().__init__()
        self.versions = ServiceWorkerVersion.safe_create_from_list(versions)

    def __repr__(self) -> str:
        repr_args = []
        if self.versions is not None:
            repr_args.append("versions={!r}".format(self.versions))
        return "WorkerVersionUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['WorkerVersionUpdatedEvent', dict]]:
        """
        Safely create WorkerVersionUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WorkerVersionUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WorkerVersionUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, WorkerVersionUpdatedEvent]]
        """
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
        """
        Safely create a new list WorkerVersionUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WorkerVersionUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WorkerVersionUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WorkerVersionUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WorkerVersionUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


SERVICEWORKER_EVENTS_TO_CLASS = {
   "ServiceWorker.workerErrorReported": WorkerErrorReportedEvent,
   "ServiceWorker.workerRegistrationUpdated": WorkerRegistrationUpdatedEvent,
   "ServiceWorker.workerVersionUpdated": WorkerVersionUpdatedEvent,
}

ServiceWorkerNS = namedtuple("ServiceWorkerNS", ["WorkerErrorReported", "WorkerRegistrationUpdated", "WorkerVersionUpdated"])

SERVICEWORKER_EVENTS_NS = ServiceWorkerNS(
  WorkerErrorReported="ServiceWorker.workerErrorReported",
  WorkerRegistrationUpdated="ServiceWorker.workerRegistrationUpdated",
  WorkerVersionUpdated="ServiceWorker.workerVersionUpdated",
)
