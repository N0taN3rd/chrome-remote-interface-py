from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class ConsoleMessage(ChromeTypeBase):

    def __init__(
        self,
        source: str,
        level: str,
        text: str,
        url: Optional[str] = None,
        line: Optional[int] = None,
        column: Optional[int] = None,
    ) -> None:
        super().__init__()
        self.source: str = source
        self.level: str = level
        self.text: str = text
        self.url: Optional[str] = url
        self.line: Optional[int] = line
        self.column: Optional[int] = column
