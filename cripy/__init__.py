from typing import Union

from .client import (
    Client,
    TargetSession,
    connect,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_URL,
)
from .connection import Connection, CDPSession, ConnectionEvents
from .errors import ClientError, NetworkError

ConnectionType = Union[Client, Connection]
SessionType = Union[TargetSession, CDPSession]

__all__ = [
    "Connection",
    "Client",
    "CDPSession",
    "TargetSession",
    "ConnectionEvents",
    "connect",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "NetworkError",
    "ClientError",
    "ConnectionType",
    "SessionType",
]
