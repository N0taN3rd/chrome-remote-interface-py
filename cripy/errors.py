from typing import Dict

__all__ = ["ClientError", "NetworkError", "ProtocolError"]


class NetworkError(Exception):
    """Network related exception."""


class ClientError(Exception):
    """Client specific exception."""


class ProtocolError(Exception):
    """Exception used to indicate that a CDP command has received an error"""


def create_protocol_error(method: str, msg: Dict) -> ProtocolError:
    error = msg["error"]
    data = error.get("data")
    data_m = f" {data}" if data is not None else ""
    return ProtocolError(f"Protocol Error ({method}): {error.get('message')}{data_m}")
