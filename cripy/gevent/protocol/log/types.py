from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.network import types as Network

__all__ = [
    "ViolationSetting",
    "LogEntry",
    "LOG_TYPE_TO_OBJECT"
]


class ViolationSetting(object):
    """
    Violation configuration setting.
    """

    __slots__ = ["name", "threshold"]

    def __init__(self, name, threshold):
        """
        :param name: Violation type.
        :type name: str
        :param threshold: Time threshold to trigger upon.
        :type threshold: float
        """
        super(ViolationSetting, self).__init__()
        self.name = name
        self.threshold = threshold

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.threshold is not None:
            repr_args.append("threshold={!r}".format(self.threshold))
        return "ViolationSetting(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ViolationSetting from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ViolationSetting
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ViolationSetting if creation did not fail
        :rtype: Optional[Union[dict, ViolationSetting]]
        """
        if init is not None:
            try:
                ourselves = ViolationSetting(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ViolationSettings from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ViolationSetting instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ViolationSetting instances if creation did not fail
        :rtype: Optional[List[Union[dict, ViolationSetting]]]
        """
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

    __slots__ = ["source", "level", "text", "timestamp", "url", "lineNumber", "stackTrace", "networkRequestId", "workerId", "args"]

    def __init__(self, source, level, text, timestamp, url=None, lineNumber=None, stackTrace=None, networkRequestId=None, workerId=None, args=None):
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
        super(LogEntry, self).__init__()
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

    def __repr__(self):
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
        return "LogEntry(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LogEntry from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LogEntry
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LogEntry if creation did not fail
        :rtype: Optional[Union[dict, LogEntry]]
        """
        if init is not None:
            try:
                ourselves = LogEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list LogEntrys from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LogEntry instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LogEntry instances if creation did not fail
        :rtype: Optional[List[Union[dict, LogEntry]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LogEntry.safe_create(it))
            return list_of_self
        else:
            return init


LOG_TYPE_TO_OBJECT = {
    "ViolationSetting": ViolationSetting,
    "LogEntry": LogEntry,
}
