from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.network import types as Network


class ViolationSetting(ProtocolType):
    """
    Violation configuration setting.
    """

    def __init__(self, name: str, threshold: float) -> None:
        """
        :param name: Violation type.
        :type name: str
        :param threshold: Time threshold to trigger upon.
        :type threshold: float
        """
        super().__init__()
        self.name = name
        self.threshold = threshold

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ViolationSetting']:
        if init is not None:
            return ViolationSetting(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ViolationSetting']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ViolationSetting(**it))
            return list_of_self
        else:
            return init


class LogEntry(ProtocolType):
    """
    Log entry.
    """

    def __init__(self, source: str, level: str, text: str, timestamp: Runtime.Timestamp, url: Optional[str] = None, lineNumber: Optional[int] = None, stackTrace: Optional[Union['Runtime.StackTrace', dict]] = None, networkRequestId: Optional[Network.RequestId] = None, workerId: Optional[str] = None, args: Optional[List[Union['Runtime.RemoteObject', dict]]] = None) -> None:
        """
        :param source: Log entry source.
        :type source: str
        :param level: Log entry severity.
        :type level: str
        :param text: Logged text.
        :type text: str
        :param timestamp: Timestamp when this entry was added.
        :type timestamp: float
        :param url: URL of the resource if known.
        :type url: Optional[str]
        :param lineNumber: Line number in the resource.
        :type lineNumber: Optional[int]
        :param stackTrace: JavaScript stack trace.
        :type stackTrace: Optional[dict]
        :param networkRequestId: Identifier of the network request associated with this entry.
        :type networkRequestId: Optional[str]
        :param workerId: Identifier of the worker associated with this entry.
        :type workerId: Optional[str]
        :param args: Call arguments.
        :type args: Optional[List[dict]]
        """
        super().__init__()
        self.source = source
        self.level = level
        self.text = text
        self.timestamp = timestamp
        self.url = url
        self.lineNumber = lineNumber
        self.stackTrace = Runtime.StackTrace.safe_create(stackTrace)
        self.networkRequestId = networkRequestId
        self.workerId = workerId
        self.args = Runtime.RemoteObject.safe_create_from_list(args)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LogEntry']:
        if init is not None:
            return LogEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LogEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LogEntry(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ViolationSetting": ViolationSetting,
    "LogEntry": LogEntry,
}
