from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

DatabaseId = str


class Database(ChromeTypeBase):

    def __init__(self, id: "DatabaseId", domain: str, name: str, version: str) -> None:
        super().__init__()
        self.id: DatabaseId = id
        self.domain: str = domain
        self.name: str = name
        self.version: str = version


class Error(ChromeTypeBase):

    def __init__(self, message: str, code: int) -> None:
        super().__init__()
        self.message: str = message
        self.code: int = code
