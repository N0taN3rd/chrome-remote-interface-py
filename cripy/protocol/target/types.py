from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

TargetID = str

SessionID = str

BrowserContextID = str


class TargetInfo(ChromeTypeBase):

    def __init__(
        self,
        targetId: "TargetID",
        type: str,
        title: str,
        url: str,
        attached: bool,
        openerId: Optional["TargetID"] = None,
        browserContextId: Optional["BrowserContextID"] = None,
    ) -> None:
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
        super().__init__()
        self.host: str = host
        self.port: int = port
