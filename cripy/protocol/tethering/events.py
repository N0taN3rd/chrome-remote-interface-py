from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AcceptedEvent(BaseEvent):
    """Informs that port was successfully bound and got a specified connection id."""

    event: str = "Tethering.accepted"

    def __init__(self, port: int, connectionId: str) -> None:
        """
        :param port: Port number that was successfully bound.
        :type port: int
        :param connectionId: Connection id to be used.
        :type connectionId: str
        """
        super().__init__()
        self.port: int = port
        self.connectionId: str = connectionId


EVENT_TO_CLASS = {
   "Tethering.accepted": AcceptedEvent,
}

