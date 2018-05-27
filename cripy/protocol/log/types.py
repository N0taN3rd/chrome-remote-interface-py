from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.network import types as Network
from cripy.protocol.runtime import types as Runtime


class LogEntry(ChromeTypeBase):

    def __init__(
        self,
        source: str,
        level: str,
        text: str,
        timestamp: "Runtime.Timestamp",
        url: Optional[str] = None,
        lineNumber: Optional[int] = None,
        stackTrace: Optional["Runtime.StackTrace"] = None,
        networkRequestId: Optional["Network.RequestId"] = None,
        workerId: Optional[str] = None,
        args: Optional[List["Runtime.RemoteObject"]] = None,
    ) -> None:
        super().__init__()
        self.source: str = source
        self.level: str = level
        self.text: str = text
        self.timestamp: Runtime.Timestamp = timestamp
        self.url: Optional[str] = url
        self.lineNumber: Optional[int] = lineNumber
        self.stackTrace: Optional[Runtime.StackTrace] = stackTrace
        self.networkRequestId: Optional[Network.RequestId] = networkRequestId
        self.workerId: Optional[str] = workerId
        self.args: Optional[List[Runtime.RemoteObject]] = args


class ViolationSetting(ChromeTypeBase):

    def __init__(self, name: str, threshold: float) -> None:
        super().__init__()
        self.name: str = name
        self.threshold: float = threshold
