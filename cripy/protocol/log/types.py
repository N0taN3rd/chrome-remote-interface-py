from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.network import types as Network
from cripy.protocol.runtime import types as Runtime


class LogEntry(ChromeTypeBase):
    """Log entry."""

    def __init__(self, source: str, level: str, text: str, timestamp: 'Runtime.Timestamp', url: Optional[str] = None, lineNumber: Optional[int] = None, stackTrace: Optional['Runtime.StackTrace'] = None, networkRequestId: Optional['Network.RequestId'] = None, workerId: Optional[str] = None, args: Optional[List['Runtime.RemoteObject']] = None) -> None:
        """
        :param source: Log entry source.
        :type str:
        :param level: Log entry severity.
        :type str:
        :param text: Logged text.
        :type str:
        :param timestamp: Timestamp when this entry was added.
        :type Runtime.Timestamp:
        :param url: URL of the resource if known.
        :type str:
        :param lineNumber: Line number in the resource.
        :type int:
        :param stackTrace: JavaScript stack trace.
        :type Runtime.StackTrace:
        :param networkRequestId: Identifier of the network request associated with this entry.
        :type Network.RequestId:
        :param workerId: Identifier of the worker associated with this entry.
        :type str:
        :param args: Call arguments.
        :type array:
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
        :param name: Violation type.
        :type str:
        :param threshold: Time threshold to trigger upon.
        :type float:
        """
        super().__init__()
        self.name: str = name
        self.threshold: float = threshold


