from asyncio import AbstractEventLoop, Future
from typing import Optional

__all__ = ["CDPResultFuture"]


class CDPResultFuture(Future):
    """A subclass of asyncio.Future to make linting happy about adding method to it"""

    def __init__(self, method: str, loop: Optional[AbstractEventLoop] = None) -> None:
        super().__init__(loop=loop)
        self.method: str = method
