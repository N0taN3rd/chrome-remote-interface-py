import attr

__all__ = ["ConnectionEvents", "SessionEvents"]


@attr.dataclass(slots=True, frozen=True)
class ConnectionEvents(object):
    Disconnected: str = attr.ib(default="Connection.Disconnected")
    Ready: str = attr.ib(default="Connection.Ready")


@attr.dataclass(slots=True, frozen=True)
class SessionEvents(object):
    Disconnected: str = attr.ib(default="Session.Disconnected")
