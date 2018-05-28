from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.runtime.types import (
    ExecutionContextId,
    RemoteObject,
    ExceptionDetails,
    StackTrace,
    Timestamp,
    ExecutionContextDescription,
)


class ConsoleAPICalledEvent(BaseEvent):
    """Issued when console API was called."""

    event: str = "Runtime.consoleAPICalled"

    def __init__(self, type: str, args: List[RemoteObject], executionContextId: ExecutionContextId, timestamp: Timestamp, stackTrace: Optional[StackTrace] = None, context: Optional[str] = None) -> None:
        """
        :param type: Type of the call.
        :type type: str
        :param args: Call arguments.
        :type args: array
        :param executionContextId: Identifier of the context where the call was made.
        :type executionContextId: ExecutionContextId
        :param timestamp: Call timestamp.
        :type timestamp: Timestamp
        :param stackTrace: Stack trace captured when the call was made.
        :type stackTrace: StackTrace
        :param context: Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context.
        :type context: str
        """
        super().__init__()
        self.type: str = type
        self.args: List[RemoteObject] = args
        self.executionContextId: ExecutionContextId = executionContextId
        self.timestamp: Timestamp = timestamp
        self.stackTrace: Optional[StackTrace] = stackTrace
        self.context: Optional[str] = context


class ExceptionRevokedEvent(BaseEvent):
    """Issued when unhandled exception was revoked."""

    event: str = "Runtime.exceptionRevoked"

    def __init__(self, reason: str, exceptionId: int) -> None:
        """
        :param reason: Reason describing why exception was revoked.
        :type reason: str
        :param exceptionId: The id of revoked exception, as reported in `exceptionThrown`.
        :type exceptionId: int
        """
        super().__init__()
        self.reason: str = reason
        self.exceptionId: int = exceptionId


class ExceptionThrownEvent(BaseEvent):
    """Issued when exception was thrown and unhandled."""

    event: str = "Runtime.exceptionThrown"

    def __init__(self, timestamp: Timestamp, exceptionDetails: ExceptionDetails) -> None:
        """
        :param timestamp: Timestamp of the exception.
        :type timestamp: Timestamp
        :param exceptionDetails: The exceptionDetails
        :type exceptionDetails: ExceptionDetails
        """
        super().__init__()
        self.timestamp: Timestamp = timestamp
        self.exceptionDetails: ExceptionDetails = exceptionDetails


class ExecutionContextCreatedEvent(BaseEvent):
    """Issued when new execution context is created."""

    event: str = "Runtime.executionContextCreated"

    def __init__(self, context: ExecutionContextDescription) -> None:
        """
        :param context: A newly created execution context.
        :type context: ExecutionContextDescription
        """
        super().__init__()
        self.context: ExecutionContextDescription = context


class ExecutionContextDestroyedEvent(BaseEvent):
    """Issued when execution context is destroyed."""

    event: str = "Runtime.executionContextDestroyed"

    def __init__(self, executionContextId: ExecutionContextId) -> None:
        """
        :param executionContextId: Id of the destroyed context
        :type executionContextId: ExecutionContextId
        """
        super().__init__()
        self.executionContextId: ExecutionContextId = executionContextId


class ExecutionContextsClearedEvent(BaseEvent):
    """Issued when all executionContexts were cleared in browser"""

    event: str = "Runtime.executionContextsCleared"

    def __init__(self, ) -> None:
        super().__init__()


class InspectRequestedEvent(BaseEvent):
    """Issued when object should be inspected (for example, as a result of inspect() command line API call)."""

    event: str = "Runtime.inspectRequested"

    def __init__(self, object: RemoteObject, hints: dict) -> None:
        """
        :param object: The object
        :type object: RemoteObject
        :param hints: The hints
        :type hints: dict
        """
        super().__init__()
        self.object: RemoteObject = object
        self.hints: dict = hints


EVENT_TO_CLASS = {
   "Runtime.consoleAPICalled": ConsoleAPICalledEvent,
   "Runtime.exceptionRevoked": ExceptionRevokedEvent,
   "Runtime.exceptionThrown": ExceptionThrownEvent,
   "Runtime.executionContextCreated": ExecutionContextCreatedEvent,
   "Runtime.executionContextDestroyed": ExecutionContextDestroyedEvent,
   "Runtime.executionContextsCleared": ExecutionContextsClearedEvent,
   "Runtime.inspectRequested": InspectRequestedEvent,
}

