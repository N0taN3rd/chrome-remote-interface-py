from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# 
TargetID = str

# Unique identifier of attached debugging session.
SessionID = str

# 
BrowserContextID = str


class TargetInfo(ChromeTypeBase):

    def __init__(self, targetId: 'TargetID', type: str, title: str, url: str, attached: bool, openerId: Optional['TargetID'] = None, browserContextId: Optional['BrowserContextID'] = None) -> None:
        """
        :param targetId: The targetId
        :type TargetID:
        :param type: The type
        :type str:
        :param title: The title
        :type str:
        :param url: The url
        :type str:
        :param attached: Whether the target has an attached client.
        :type bool:
        :param openerId: Opener target Id
        :type TargetID:
        :param browserContextId: The browserContextId
        :type BrowserContextID:
        """
        super().__init__()
        self.targetId: TargetID = targetId
        self.type: str = type
        self.title: str = title
        self.url: str = url
        self.attached: bool = attached
        self.openerId: Optional[TargetID] = openerId
        self.browserContextId: Optional[BrowserContextID] = browserContextId


class RemoteLocation(ChromeTypeBase):

    def __init__(self, host: str, port: int) -> None:
        """
        :param host: The host
        :type str:
        :param port: The port
        :type int:
        """
        super().__init__()
        self.host: str = host
        self.port: int = port


