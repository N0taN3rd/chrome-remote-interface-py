from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class ApplicationCacheStatusUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.applicationCacheStatusUpdated"

    def __init__(self) -> None:
        """
        :param frameId: Identifier of the frame containing document whose application cache updated status.
        :type Page.FrameId:
        :param manifestURL: Manifest URL.
        :type str:
        :param status: Updated application cache status.
        :type int:
        """
        super().__init__()


class NetworkStateUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.networkStateUpdated"

    def __init__(self) -> None:
        """
        :param isNowOnline: The isNowOnline
        :type bool:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "ApplicationCache.applicationCacheStatusUpdated": ApplicationCacheStatusUpdatedEvent,
   "ApplicationCache.networkStateUpdated": NetworkStateUpdatedEvent,
}

