from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

# 
TargetID = str

# Unique identifier of attached debugging session.
SessionID = str

# 
BrowserContextID = str


class TargetInfo(ChromeTypeBase):
    pass
    def __init__(self, targetId: 'TargetID', type: str, title: str, url: str, attached: bool, openerId: Optional['TargetID'] = None, browserContextId: Optional['BrowserContextID'] = None) -> None:
        """
        :param targetId: The targetId
        :type targetId: TargetID
        :param type: The type
        :type type: str
        :param title: The title
        :type title: str
        :param url: The url
        :type url: str
        :param attached: Whether the target has an attached client.
        :type attached: bool
        :param openerId: Opener target Id
        :type openerId: TargetID
        :param browserContextId: The browserContextId
        :type browserContextId: BrowserContextID
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
    pass
    def __init__(self, host: str, port: int) -> None:
        """
        :param host: The host
        :type host: str
        :param port: The port
        :type port: int
        """
        super().__init__()
        self.host: str = host
        self.port: int = port


