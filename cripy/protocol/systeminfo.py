"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["SystemInfo"]


class SystemInfo:
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/SystemInfo`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of SystemInfo

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def getInfo(self) -> Awaitable[Dict]:
        """
        Returns information about the system.

        See `https://chromedevtools.github.io/devtools-protocol/tot/SystemInfo#method-getInfo`

        :return: The results of the command
        """
        return self.client.send("SystemInfo.getInfo", {})

    def getProcessInfo(self) -> Awaitable[Dict]:
        """
        Returns information about all running processes.

        See `https://chromedevtools.github.io/devtools-protocol/tot/SystemInfo#method-getProcessInfo`

        :return: The results of the command
        """
        return self.client.send("SystemInfo.getProcessInfo", {})
