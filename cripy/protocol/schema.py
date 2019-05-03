"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Schema"]


class Schema:
    """
    This domain is deprecated.
    Status: Deprecated
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Schema`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Schema

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def getDomains(self) -> Awaitable[Dict]:
        """
        Returns supported domains.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Schema#method-getDomains`

        :return: The results of the command
        """
        return self.client.send("Schema.getDomains", {})
