from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class Domain(ChromeTypeBase):

    def __init__(self, name: str, version: str) -> None:
        super().__init__()
        self.name: str = name
        self.version: str = version
