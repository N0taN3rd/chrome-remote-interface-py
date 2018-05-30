from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.tethering.types import *
except ImportError:
    pass


class AcceptedEvent(BaseEvent):
    """
    Informs that port was successfully bound and got a specified connection id.
    """

    event = "Tethering.accepted"

    def __init__(self, port: int, connectionId: str) -> None:
        """
        :param port: Port number that was successfully bound.
        :type port: int
        :param connectionId: Connection id to be used.
        :type connectionId: str
        """
        super().__init__()
        self.port = port
        self.connectionId = connectionId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AcceptedEvent']:
        if init is not None:
            return AcceptedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AcceptedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AcceptedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Tethering.accepted": AcceptedEvent,
}

