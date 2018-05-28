from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class ConsoleAPICalledEvent(BaseEvent):
    """Issued when console API was called."""

    event: str = "Runtime.consoleAPICalled"

    def __init__(self) -> None:
        """
        :param str type: Type of the call.
        :param array args: Call arguments.
        :param ExecutionContextId executionContextId: Identifier of the context where the call was made.
        :param Timestamp timestamp: Call timestamp.
        :param StackTrace stackTrace: Stack trace captured when the call was made.
        :param str context: Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context.
        """
        super().__init__()


class ExceptionRevokedEvent(BaseEvent):
    """Issued when unhandled exception was revoked."""

    event: str = "Runtime.exceptionRevoked"

    def __init__(self) -> None:
        """
        :param str reason: Reason describing why exception was revoked.
        :param int exceptionId: The id of revoked exception, as reported in `exceptionThrown`.
        """
        super().__init__()


class ExceptionThrownEvent(BaseEvent):
    """Issued when exception was thrown and unhandled."""

    event: str = "Runtime.exceptionThrown"

    def __init__(self) -> None:
        """
        :param Timestamp timestamp: Timestamp of the exception.
        :param ExceptionDetails exceptionDetails: The exceptionDetails
        """
        super().__init__()


class ExecutionContextCreatedEvent(BaseEvent):
    """Issued when new execution context is created."""

    event: str = "Runtime.executionContextCreated"

    def __init__(self) -> None:
        """
        :param ExecutionContextDescription context: A newly created execution context.
        """
        super().__init__()


class ExecutionContextDestroyedEvent(BaseEvent):
    """Issued when execution context is destroyed."""

    event: str = "Runtime.executionContextDestroyed"

    def __init__(self) -> None:
        """
        :param ExecutionContextId executionContextId: Id of the destroyed context
        """
        super().__init__()


class ExecutionContextsClearedEvent(BaseEvent):
    """Issued when all executionContexts were cleared in browser"""

    event: str = "Runtime.executionContextsCleared"

    def __init__(self) -> None:
        super().__init__()


class InspectRequestedEvent(BaseEvent):
    """Issued when object should be inspected (for example, as a result of inspect() command line API call)."""

    event: str = "Runtime.inspectRequested"

    def __init__(self) -> None:
        """
        :param RemoteObject object: The object
        :param dict hints: The hints
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Runtime.consoleAPICalled": ConsoleAPICalledEvent,
   "Runtime.exceptionRevoked": ExceptionRevokedEvent,
   "Runtime.exceptionThrown": ExceptionThrownEvent,
   "Runtime.executionContextCreated": ExecutionContextCreatedEvent,
   "Runtime.executionContextDestroyed": ExecutionContextDestroyedEvent,
   "Runtime.executionContextsCleared": ExecutionContextsClearedEvent,
   "Runtime.inspectRequested": InspectRequestedEvent,
}

