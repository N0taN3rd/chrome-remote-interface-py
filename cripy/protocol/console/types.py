from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class ConsoleMessage(ChromeTypeBase):
    """Console message."""

    def __init__(self, source: str, level: str, text: str, url: Optional[str] = None, line: Optional[int] = None, column: Optional[int] = None) -> None:
        """
        :param source: Message source.
        :type str:
        :param level: Message severity.
        :type str:
        :param text: Message text.
        :type str:
        :param url: URL of the message origin.
        :type str:
        :param line: Line number in the resource that generated this message (1-based).
        :type int:
        :param column: Column number in the resource that generated this message (1-based).
        :type int:
        """
        super().__init__()
        self.source: str = source
        self.level: str = level
        self.text: str = text
        self.url: Optional[str] = url
        self.line: Optional[int] = line
        self.column: Optional[int] = column


