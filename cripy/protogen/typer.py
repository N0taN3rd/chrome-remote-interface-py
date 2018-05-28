from typing import Any, Set


class Typer(object):

    def __init__(self) -> None:
        self.objects: Set[str] = set()
        self.primitives: Set[str] = set()
        self.lists: Set[str] = set()

    def add_type(self, what: Any) -> None:
        pass

    def is_object(self, what: str) -> bool:
        return what in self.objects

    def is_primitive(self, what: str) -> bool:
        return what in self.primitives

    def is_list(self, what: str) -> bool:
        return what in self.lists
