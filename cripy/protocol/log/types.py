from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.network import types as Network
from cripy.protocol.runtime import types as Runtime


class ViolationSetting(object):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.threshold is not None:
            repr_args.append("threshold={!r}".format(self.threshold))
        return "ViolationSetting(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["ViolationSetting", dict]]:
        if init is not None:
            try:
                ourselves = ViolationSetting(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ViolationSetting", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ViolationSetting.safe_create(it))
            return list_of_self
        else:
            return init


class LogEntry(object):
    """
    Log entry.
    """

    def __init__(
        self,
        source: str,
        level: str,
        text: str,
        timestamp: float,
        url: Optional[str] = None,
        lineNumber: Optional[int] = None,
        stackTrace: Optional[Union["Runtime.StackTrace", dict]] = None,
        networkRequestId: Optional[str] = None,
        workerId: Optional[str] = None,
        args: Optional[List[Union["Runtime.RemoteObject", dict]]] = None,
    ) -> None:
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.source is not None:
            repr_args.append("source={!r}".format(self.source))
        if self.level is not None:
            repr_args.append("level={!r}".format(self.level))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        if self.networkRequestId is not None:
            repr_args.append("networkRequestId={!r}".format(self.networkRequestId))
        if self.workerId is not None:
            repr_args.append("workerId={!r}".format(self.workerId))
        if self.args is not None:
            repr_args.append("args={!r}".format(self.args))
        return "LogEntry(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["LogEntry", dict]]:
        if init is not None:
            try:
                ourselves = LogEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["LogEntry", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LogEntry.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"ViolationSetting": ViolationSetting, "LogEntry": LogEntry}
