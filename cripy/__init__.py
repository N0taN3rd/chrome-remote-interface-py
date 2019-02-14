from typing import Union

from .cdp import CDP, connect, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_URL
from .client import Client, TargetSession
from .connection import Connection, CDPSession
from .errors import ClientError, ConnectionClosedError, NetworkError
from .events import ConnectionEvents, SessionEvents

ConnectionType = Union[Client, Connection]
SessionType = Union[TargetSession, CDPSession]

__all__ = [
    "CDP",
    "CDPSession",
    "Client",
    "ClientError",
    "Connection",
    "ConnectionClosedError",
    "ConnectionEvents",
    "ConnectionType",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "NetworkError",
    "SessionEvents",
    "SessionType",
    "TargetSession",
    "connect",
]
