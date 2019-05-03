from typing import Union

from .cdp import CDP, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_URL, connect
from .cdp_session import CDPSession
from .client import Client, ClientDynamic
from .connection import Connection
from .errors import ClientError, NetworkError, ProtocolError
from .events import ConnectionEvents, SessionEvents
from .target_session import TargetSession, TargetSessionDynamic

ConnectionType = Union[Client, Connection, ClientDynamic]
SessionType = Union[TargetSession, CDPSession, TargetSessionDynamic]

__all__ = [
    "CDP",
    "CDPSession",
    "Client",
    "ClientDynamic",
    "ClientError",
    "connect",
    "Connection",
    "ConnectionEvents",
    "ConnectionType",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "NetworkError",
    "ProtocolError",
    "SessionEvents",
    "SessionType",
    "TargetSession",
    "TargetSessionDynamic",
]
