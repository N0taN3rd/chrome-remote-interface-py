from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.network import types as Network


class LogEntry(ChromeTypeBase):
    """Log entry."""
    def __init__(self, source: str, level: str, text: str, timestamp: 'Runtime.Timestamp', url: Optional[str] = None, lineNumber: Optional[int] = None, stackTrace: Optional['Runtime.StackTrace'] = None, networkRequestId: Optional['Network.RequestId'] = None, workerId: Optional[str] = None, args: Optional[List['Runtime.RemoteObject']] = None) -> None:
        """
        :param str source: Log entry source.
        :param str level: Log entry severity.
        :param str text: Logged text.
        :param Runtime.Timestamp timestamp: Timestamp when this entry was added.
        :param str url: URL of the resource if known.
        :param int lineNumber: Line number in the resource.
        :param Runtime.StackTrace stackTrace: JavaScript stack trace.
        :param Network.RequestId networkRequestId: Identifier of the network request associated with this entry.
        :param str workerId: Identifier of the worker associated with this entry.
        :param array args: Call arguments.
        """
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
    """Violation configuration setting."""
    def __init__(self, name: str, threshold: float) -> None:
        """
        :param str name: Violation type.
        :param float threshold: Time threshold to trigger upon.
        """
        super().__init__()
        self.name: str = name
        self.threshold: float = threshold


