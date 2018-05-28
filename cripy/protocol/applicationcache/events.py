from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.page import types as Page


class ApplicationCacheStatusUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.applicationCacheStatusUpdated"

    def __init__(self, frameId: Page.FrameId, manifestURL: str, status: int) -> None:
        """
        :param frameId: Identifier of the frame containing document whose application cache updated status.
        :type frameId: Page.FrameId
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param status: Updated application cache status.
        :type status: int
        """
        super().__init__()
        self.frameId: Page.FrameId = frameId
        self.manifestURL: str = manifestURL
        self.status: int = status


class NetworkStateUpdatedEvent(BaseEvent):

    event: str = "ApplicationCache.networkStateUpdated"

    def __init__(self, isNowOnline: bool) -> None:
        """
        :param isNowOnline: The isNowOnline
        :type isNowOnline: bool
        """
        super().__init__()
        self.isNowOnline: bool = isNowOnline


EVENT_TO_CLASS = {
   "ApplicationCache.applicationCacheStatusUpdated": ApplicationCacheStatusUpdatedEvent,
   "ApplicationCache.networkStateUpdated": NetworkStateUpdatedEvent,
}

