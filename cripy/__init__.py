from typing import Union

from .cdp import CDP, connect, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_URL
from .client import Client, TargetSession
from .connection import Connection, CDPSession, ConnectionEvents, SessionEvents
from .errors import ClientError, NetworkError

ConnectionType = Union[Client, Connection]
SessionType = Union[TargetSession, CDPSession]

__all__ = [
    "CDP",
    "connect",
    "Connection",
    "Client",
    "CDPSession",
    "TargetSession",
    "ConnectionEvents",
    "SessionEvents",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "NetworkError",
    "ClientError",
    "ConnectionType",
    "SessionType",
]
