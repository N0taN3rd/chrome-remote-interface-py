from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class ApplicationCacheStatusUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.applicationCacheStatusUpdated"

    def __init__(self) -> None:
        """
        :param Page.FrameId frameId: Identifier of the frame containing document whose application cache updated status.
        :type frameId: Page.FrameId
        :param str manifestURL: Manifest URL.
        :type manifestURL: str
        :param int status: Updated application cache status.
        :type status: int
        """
        super().__init__()


class NetworkStateUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.networkStateUpdated"

    def __init__(self) -> None:
        """
        :param bool isNowOnline: The isNowOnline
        :type isNowOnline: bool
        """
        super().__init__()


EVENT_TO_CLASS = {
   "ApplicationCache.applicationCacheStatusUpdated": ApplicationCacheStatusUpdatedEvent,
   "ApplicationCache.networkStateUpdated": NetworkStateUpdatedEvent,
}

