"""Exceptions for pyppeteer package."""

import asyncio


class CripyError(Exception):  # noqa: D204
    """Base exception for pyppeteer."""
    pass


class BrowserError(Exception):  # noqa: D204
    """Exception raised from browser."""
    pass


class ElementHandleError(Exception):  # noqa: D204
    """ElementHandle related exception."""
    pass


class NetworkError(Exception):  # noqa: D204
    """Network/Protocol related exception."""
    pass


class PageError(Exception):  # noqa: D204
    """Page/Frame related exception."""
    pass


class TimeoutError(asyncio.TimeoutError):  # noqa: D204
    """Timeout Error class."""
    pass
