from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.console.types import *

__all__ = [
    "MessageAddedEvent",
    "CONSOLE_EVENTS_TO_CLASS",
    "CONSOLE_EVENTS_NS"
]

class MessageAddedEvent(object):
    """
    Issued when new console message is added.
    """

    event = "Console.messageAdded"

    __slots__ = ["message"]

    def __init__(self, message: Union[ConsoleMessage, dict]) -> None:
        """
        Create a new instance of MessageAddedEvent

        :param message: Console message that has been added.
        :type message: dict
        """
        super().__init__()
        self.message = ConsoleMessage.safe_create(message)

    def __repr__(self) -> str:
        repr_args = []
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        return "MessageAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['MessageAddedEvent', dict]]:
        """
        Safely create MessageAddedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of MessageAddedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of MessageAddedEvent if creation did not fail
        :rtype: Optional[Union[dict, MessageAddedEvent]]
        """
        if init is not None:
            try:
                ourselves = MessageAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['MessageAddedEvent', dict]]]:
        """
        Safely create a new list MessageAddedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list MessageAddedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of MessageAddedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, MessageAddedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MessageAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


CONSOLE_EVENTS_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

ConsoleNS = namedtuple("ConsoleNS", ["MessageAdded"])

CONSOLE_EVENTS_NS = ConsoleNS(
  MessageAdded="Console.messageAdded",
)
