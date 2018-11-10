__all__ = ["NetworkError", "ClientError"]


class NetworkError(Exception):
    """Network/Protocol related exception."""


class ClientError(Exception):
    """Client specific exception."""
