from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.runtime.types import *
except ImportError:
    pass


class ConsoleAPICalledEvent(BaseEvent):
    """
    Issued when console API was called.
    """

    event = "Runtime.consoleAPICalled"

    def __init__(self, type: str, args: List[Union[RemoteObject, dict]], executionContextId: ExecutionContextId, timestamp: Timestamp, stackTrace: Optional[Union[StackTrace, dict]] = None, context: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ConsoleAPICalledEvent']:
        if init is not None:
            return ConsoleAPICalledEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ConsoleAPICalledEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleAPICalledEvent(**it))
            return list_of_self
        else:
            return init


class ExceptionRevokedEvent(BaseEvent):
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExceptionRevokedEvent']:
        if init is not None:
            return ExceptionRevokedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExceptionRevokedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionRevokedEvent(**it))
            return list_of_self
        else:
            return init


class ExceptionThrownEvent(BaseEvent):
    """
    Issued when exception was thrown and unhandled.
    """

    event = "Runtime.exceptionThrown"

    def __init__(self, timestamp: Timestamp, exceptionDetails: Union[ExceptionDetails, dict]) -> None:
        """
        :param timestamp: Timestamp of the exception.
        :type timestamp: float
        :param exceptionDetails: The exceptionDetails
        :type exceptionDetails: dict
        """
        super().__init__()
        self.timestamp = timestamp
        self.exceptionDetails = ExceptionDetails.safe_create(exceptionDetails)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExceptionThrownEvent']:
        if init is not None:
            return ExceptionThrownEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExceptionThrownEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExceptionThrownEvent(**it))
            return list_of_self
        else:
            return init


class ExecutionContextCreatedEvent(BaseEvent):
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExecutionContextCreatedEvent']:
        if init is not None:
            return ExecutionContextCreatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExecutionContextCreatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextCreatedEvent(**it))
            return list_of_self
        else:
            return init


class ExecutionContextDestroyedEvent(BaseEvent):
    """
    Issued when execution context is destroyed.
    """

    event = "Runtime.executionContextDestroyed"

    def __init__(self, executionContextId: ExecutionContextId) -> None:
        """
        :param executionContextId: Id of the destroyed context
        :type executionContextId: int
        """
        super().__init__()
        self.executionContextId = executionContextId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExecutionContextDestroyedEvent']:
        if init is not None:
            return ExecutionContextDestroyedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExecutionContextDestroyedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextDestroyedEvent(**it))
            return list_of_self
        else:
            return init


class ExecutionContextsClearedEvent(BaseEvent, dict):
    """
    Issued when all executionContexts were cleared in browser
    """

    event = "Runtime.executionContextsCleared"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ExecutionContextsClearedEvent']:
        if init is not None:
            return ExecutionContextsClearedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ExecutionContextsClearedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ExecutionContextsClearedEvent(**it))
            return list_of_self
        else:
            return init


class InspectRequestedEvent(BaseEvent):
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InspectRequestedEvent']:
        if init is not None:
            return InspectRequestedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InspectRequestedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InspectRequestedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Runtime.consoleAPICalled": ConsoleAPICalledEvent,
   "Runtime.exceptionRevoked": ExceptionRevokedEvent,
   "Runtime.exceptionThrown": ExceptionThrownEvent,
   "Runtime.executionContextCreated": ExecutionContextCreatedEvent,
   "Runtime.executionContextDestroyed": ExecutionContextDestroyedEvent,
   "Runtime.executionContextsCleared": ExecutionContextsClearedEvent,
   "Runtime.inspectRequested": InspectRequestedEvent,
}

