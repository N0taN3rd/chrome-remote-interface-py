from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.applicationcache.types import *

__all__ = [
    "ApplicationCacheStatusUpdatedEvent",
    "NetworkStateUpdatedEvent",
    "APPLICATIONCACHE_EVENTS_TO_CLASS",
    "APPLICATIONCACHE_EVENTS_NS"
]

class ApplicationCacheStatusUpdatedEvent(object):

    event = "ApplicationCache.applicationCacheStatusUpdated"

    __slots__ = ["frameId", "manifestURL", "status"]

    def __init__(self, frameId: str, manifestURL: str, status: int) -> None:
        """
        Create a new instance of ApplicationCacheStatusUpdatedEvent

        :param frameId: Identifier of the frame containing document whose application cache updated status.
        :type frameId: str
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param status: Updated application cache status.
        :type status: int
        """
        super().__init__()
        self.frameId = frameId
        self.manifestURL = manifestURL
        self.status = status

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.manifestURL is not None:
            repr_args.append("manifestURL={!r}".format(self.manifestURL))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        return "ApplicationCacheStatusUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ApplicationCacheStatusUpdatedEvent', dict]]:
        """
        Safely create ApplicationCacheStatusUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ApplicationCacheStatusUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ApplicationCacheStatusUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, ApplicationCacheStatusUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = ApplicationCacheStatusUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ApplicationCacheStatusUpdatedEvent', dict]]]:
        """
        Safely create a new list ApplicationCacheStatusUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ApplicationCacheStatusUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ApplicationCacheStatusUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ApplicationCacheStatusUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheStatusUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class NetworkStateUpdatedEvent(object):

    event = "ApplicationCache.networkStateUpdated"

    __slots__ = ["isNowOnline"]

    def __init__(self, isNowOnline: bool) -> None:
        """
        Create a new instance of NetworkStateUpdatedEvent

        :param isNowOnline: The isNowOnline
        :type isNowOnline: bool
        """
        super().__init__()
        self.isNowOnline = isNowOnline

    def __repr__(self) -> str:
        repr_args = []
        if self.isNowOnline is not None:
            repr_args.append("isNowOnline={!r}".format(self.isNowOnline))
        return "NetworkStateUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['NetworkStateUpdatedEvent', dict]]:
        """
        Safely create NetworkStateUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NetworkStateUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NetworkStateUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, NetworkStateUpdatedEvent]]
        """
        if init is not None:
            try:
                ourselves = NetworkStateUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['NetworkStateUpdatedEvent', dict]]]:
        """
        Safely create a new list NetworkStateUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NetworkStateUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NetworkStateUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, NetworkStateUpdatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NetworkStateUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


APPLICATIONCACHE_EVENTS_TO_CLASS = {
   "ApplicationCache.applicationCacheStatusUpdated": ApplicationCacheStatusUpdatedEvent,
   "ApplicationCache.networkStateUpdated": NetworkStateUpdatedEvent,
}

ApplicationCacheNS = namedtuple("ApplicationCacheNS", ["ApplicationCacheStatusUpdated", "NetworkStateUpdated"])

APPLICATIONCACHE_EVENTS_NS = ApplicationCacheNS(
  ApplicationCacheStatusUpdated="ApplicationCache.applicationCacheStatusUpdated",
  NetworkStateUpdated="ApplicationCache.networkStateUpdated",
)
