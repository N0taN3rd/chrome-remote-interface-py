"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Testing"]


class Testing:
    """
    Testing domain is a dumping ground for the capabilities requires for browser or app testing that do not fit other
domains.
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        self.client: Union["ConnectionType", "SessionType"] = client

    def generateTestReport(
        self, message: str, group: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Generates a report for testing.

        :param message: Message to be displayed in the report.
        :type message: str
        :param group: Specifies the endpoint group to deliver the report to.
        :type group: Optional[str]
        """
        msg_dict = {}
        if message is not None:
            msg_dict["message"] = message
        if group is not None:
            msg_dict["group"] = group
        return self.client.send("Testing.generateTestReport", msg_dict)
