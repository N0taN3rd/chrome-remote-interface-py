from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.async.protocol.runtime.types import *
except ImportError:
    pass


class BindingCalledEvent(object):
    """
    Notification is issued every time when binding is called.
    """

    event = "Runtime.bindingCalled"

    def __init__(self, name: str, payload: str, executionContextId: int) -> None:
        """
        :param name: The name
        :type name: str
        :param payload: The payload
        :type payload: str
        :param executionContextId: Identifier of the context where the call was made.
        :type executionContextId: int
        """
        super().__init__()
        self.name = name
        self.payload = payload
        self.executionContextId = executionContextId

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
        if self.payload is not None:
            repr_args.append("payload={!r}".format(self.payload))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        return "BindingCalledEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["BindingCalledEvent", dict]]:
        if init is not None:
            try:
                ourselves = BindingCalledEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["BindingCalledEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(BindingCalledEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ConsoleAPICalledEvent(object):
    """
    Issued when console API was called.
    """

    event = "Runtime.consoleAPICalled"

    def __init__(
        self,
        type: str,
        args: List[Union[RemoteObject, dict]],
        executionContextId: int,
        timestamp: float,
        stackTrace: Optional[Union[StackTrace, dict]] = None,
        context: Optional[str] = None,
    ) -> None:
        """
        :param type: Type of the call.
        :type type: str
        :param args: Call arguments.
        :type args: List[dict]
        :param executionContextId: Identifier of the context where the call was made.
        :type executionContextId: int
        :param timestamp: Call timestamp.
        :type timestamp: float
        :param stackTrace: Stack trace captured when the call was made.
        :type stackTrace: Optional[dict]
        :param context: Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context.
        :type context: Optional[str]
        """
        super().__init__()
        self.type = type
        self.args = RemoteObject.safe_create_from_list(args)
        self.executionContextId = executionContextId
        self.timestamp = timestamp
        self.stackTrace = StackTrace.safe_create(stackTrace)
        self.context = context

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.args is not None:
            repr_args.append("args={!r}".format(self.args))
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.stackTrace is not None:
            repr_args.append("stackTrace={!r}".format(self.stackTrace))
        if self.context is not None:
            repr_args.append("context={!r}".format(self.context))
        return "ConsoleAPICalledEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ConsoleAPICalledEvent", dict]]:
        if init is not None:
            try:
                ourselves = ConsoleAPICalledEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ConsoleAPICalledEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleAPICalledEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExceptionRevokedEvent(object):
    """
    Issued when unhandled exception was revoked.
    """

    event = "Runtime.exceptionRevoked"

    def __init__(self, reason: str, exceptionId: int) -> None:
        """
        :param reason: Reason describing why exception was revoked.
        :type reason: str
        :param exceptionId: The id of revoked exception, as reported in `exceptionThrown`.
        :type exceptionId: int
        """
        super().__init__()
        self.reason = reason
        self.exceptionId = exceptionId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        if self.exceptionId is not None:
            repr_args.append("exceptionId={!r}".format(self.exceptionId))
        return "ExceptionRevokedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ExceptionRevokedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ExceptionRevokedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ExceptionRevokedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionRevokedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExceptionThrownEvent(object):
    """
    Issued when exception was thrown and unhandled.
    """

    event = "Runtime.exceptionThrown"

    def __init__(
        self, timestamp: float, exceptionDetails: Union[ExceptionDetails, dict]
    ) -> None:
        """
        :param timestamp: Timestamp of the exception.
        :type timestamp: float
        :param exceptionDetails: The exceptionDetails
        :type exceptionDetails: dict
        """
        super().__init__()
        self.timestamp = timestamp
        self.exceptionDetails = ExceptionDetails.safe_create(exceptionDetails)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        if self.exceptionDetails is not None:
            repr_args.append("exceptionDetails={!r}".format(self.exceptionDetails))
        return "ExceptionThrownEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ExceptionThrownEvent", dict]]:
        if init is not None:
            try:
                ourselves = ExceptionThrownEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ExceptionThrownEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionThrownEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextCreatedEvent(object):
    """
    Issued when new execution context is created.
    """

    event = "Runtime.executionContextCreated"

    def __init__(self, context: Union[ExecutionContextDescription, dict]) -> None:
        """
        :param context: A newly created execution context.
        :type context: dict
        """
        super().__init__()
        self.context = ExecutionContextDescription.safe_create(context)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.context is not None:
            repr_args.append("context={!r}".format(self.context))
        return "ExecutionContextCreatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ExecutionContextCreatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ExecutionContextCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ExecutionContextCreatedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextDestroyedEvent(object):
    """
    Issued when execution context is destroyed.
    """

    event = "Runtime.executionContextDestroyed"

    def __init__(self, executionContextId: int) -> None:
        """
        :param executionContextId: Id of the destroyed context
        :type executionContextId: int
        """
        super().__init__()
        self.executionContextId = executionContextId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.executionContextId is not None:
            repr_args.append("executionContextId={!r}".format(self.executionContextId))
        return "ExecutionContextDestroyedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ExecutionContextDestroyedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ExecutionContextDestroyedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ExecutionContextDestroyedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextDestroyedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ExecutionContextsClearedEvent(dict):
    """
    Issued when all executionContexts were cleared in browser
    """

    event = "Runtime.executionContextsCleared"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "ExecutionContextsClearedEvent(dict)"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["ExecutionContextsClearedEvent", dict]]:
        if init is not None:
            try:
                ourselves = ExecutionContextsClearedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["ExecutionContextsClearedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextsClearedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class InspectRequestedEvent(object):
    """
    Issued when object should be inspected (for example, as a result of inspect() command line API call).
    """

    event = "Runtime.inspectRequested"

    def __init__(self, object: Union[RemoteObject, dict], hints: dict) -> None:
        """
        :param object: The object
        :type object: dict
        :param hints: The hints
        :type hints: dict
        """
        super().__init__()
        self.object = RemoteObject.safe_create(object)
        self.hints = hints

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.object is not None:
            repr_args.append("object={!r}".format(self.object))
        if self.hints is not None:
            repr_args.append("hints={!r}".format(self.hints))
        return "InspectRequestedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["InspectRequestedEvent", dict]]:
        if init is not None:
            try:
                ourselves = InspectRequestedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["InspectRequestedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InspectRequestedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Runtime.bindingCalled": BindingCalledEvent,
    "Runtime.consoleAPICalled": ConsoleAPICalledEvent,
    "Runtime.exceptionRevoked": ExceptionRevokedEvent,
    "Runtime.exceptionThrown": ExceptionThrownEvent,
    "Runtime.executionContextCreated": ExecutionContextCreatedEvent,
    "Runtime.executionContextDestroyed": ExecutionContextDestroyedEvent,
    "Runtime.executionContextsCleared": ExecutionContextsClearedEvent,
    "Runtime.inspectRequested": InspectRequestedEvent,
}

EVENT_NS = SimpleNamespace(
    BindingCalled="Runtime.bindingCalled",
    ConsoleAPICalled="Runtime.consoleAPICalled",
    ExceptionRevoked="Runtime.exceptionRevoked",
    ExceptionThrown="Runtime.exceptionThrown",
    ExecutionContextCreated="Runtime.executionContextCreated",
    ExecutionContextDestroyed="Runtime.executionContextDestroyed",
    ExecutionContextsCleared="Runtime.executionContextsCleared",
    InspectRequested="Runtime.inspectRequested",
)
