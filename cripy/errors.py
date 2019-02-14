__all__ = ["ClientError", "ConnectionClosedError", "NetworkError"]


class NetworkError(Exception):
    """Network/Protocol related exception."""


class ClientError(Exception):
    """Client specific exception."""


class ConnectionClosedError(Exception):
    """Exception used to indicate that the underlying connection has closed"""
