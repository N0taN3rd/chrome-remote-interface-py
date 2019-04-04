from typing import ClassVar

__all__ = ["ConnectionEvents", "SessionEvents"]


class ConnectionEvents:
    Disconnected: ClassVar[str] = "Connection.Disconnected"
    Ready: ClassVar[str] = "Connection.Ready"
    AllMessages: ClassVar[str] = "Connection.AllMessages"


class SessionEvents:
    Disconnected: ClassVar[str] = "Session.Disconnected"
