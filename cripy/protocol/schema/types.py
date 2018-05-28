from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class Domain(ChromeTypeBase):
    """Description of the protocol domain."""

    def __init__(self, name: str, version: str) -> None:
        """
        :param name: Domain name.
        :type str:
        :param version: Domain version.
        :type str:
        """
        super().__init__()
        self.name: str = name
        self.version: str = version


