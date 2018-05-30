from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class ConsoleMessage(ProtocolType):
    """
    Console message.
    """

    def __init__(self, source: str, level: str, text: str, url: Optional[str] = None, line: Optional[int] = None, column: Optional[int] = None) -> None:
        """
        :param source: Message source.
        :type source: str
        :param level: Message severity.
        :type level: str
        :param text: Message text.
        :type text: str
        :param url: URL of the message origin.
        :type url: Optional[str]
        :param line: Line number in the resource that generated this message (1-based).
        :type line: Optional[int]
        :param column: Column number in the resource that generated this message (1-based).
        :type column: Optional[int]
        """
        super().__init__()
        self.source = source
        self.level = level
        self.text = text
        self.url = url
        self.line = line
        self.column = column

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleMessage', dict]]:
        if init is not None:
             try:
                ourselves = ConsoleMessage(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ConsoleMessage', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleMessage.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ConsoleMessage": ConsoleMessage,
}
