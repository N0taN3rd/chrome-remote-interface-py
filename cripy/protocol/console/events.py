from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.console.types import *
except ImportError:
    pass


class MessageAddedEvent(BaseEvent):
    """
    Issued when new console message is added.
    """

    event = "Console.messageAdded"

    def __init__(self, message: Union[ConsoleMessage, dict]) -> None:
        """
        :param message: Console message that has been added.
        :type message: dict
        """
        super().__init__()
        self.message = ConsoleMessage.safe_create(message)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['MessageAddedEvent']:
        if init is not None:
            return MessageAddedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['MessageAddedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MessageAddedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

