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
        :param TargetID targetId: The targetId
        :param str type: The type
        :param str title: The title
        :param str url: The url
        :param bool attached: Whether the target has an attached client.
        :param TargetID openerId: Opener target Id
        :param BrowserContextID browserContextId: The browserContextId
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
        :param str host: The host
        :param int port: The port
        """
        super().__init__()
        self.host: str = host
        self.port: int = port


