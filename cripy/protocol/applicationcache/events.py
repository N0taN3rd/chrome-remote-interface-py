from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.page import types as Page
try:
    from cripy.protocol.applicationcache.types import *
except ImportError:
    pass


class ApplicationCacheStatusUpdatedEvent(BaseEvent):

    event = "ApplicationCache.applicationCacheStatusUpdated"

    def __init__(self, frameId: str, manifestURL: str, status: int) -> None:
        """
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ApplicationCacheStatusUpdatedEvent', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheStatusUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class NetworkStateUpdatedEvent(BaseEvent):

    event = "ApplicationCache.networkStateUpdated"

    def __init__(self, isNowOnline: bool) -> None:
        """
        :param isNowOnline: The isNowOnline
        :type isNowOnline: bool
        """
        super().__init__()
        self.isNowOnline = isNowOnline

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['NetworkStateUpdatedEvent', dict]]:
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NetworkStateUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "ApplicationCache.applicationCacheStatusUpdated": ApplicationCacheStatusUpdatedEvent,
   "ApplicationCache.networkStateUpdated": NetworkStateUpdatedEvent,
}

