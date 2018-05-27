from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class Metric(ChromeTypeBase):

    def __init__(self, name: str, value: float) -> None:
        super().__init__()
        self.name: str = name
        self.value: float = value
