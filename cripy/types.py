from typing import Union

from .client import Client, TargetSession
from .connection import Connection, CDPSession

__all__ = ["ConnectionType", "SessionType"]

ConnectionType = Union[Client, Connection]
SessionType = Union[TargetSession, CDPSession]
