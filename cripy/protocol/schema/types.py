from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class Domain(ChromeTypeBase):
    """Description of the protocol domain."""

    def __init__(self, name: str, version: str) -> None:
        """
        :param name: Domain name.
        :param version: Domain version.
        """
        super().__init__()
        self.name: str = name
        self.version: str = version
