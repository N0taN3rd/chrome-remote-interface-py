__all__ = ["ClientError", "NetworkError", "ProtocolError"]


class NetworkError(Exception):
    """Network related exception."""


class ClientError(Exception):
    """Client specific exception."""


class ProtocolError(Exception):
    """Exception used to indicate that a CDP command has received an error"""
