from typing import List, Optional, Set, Union

from .shared_typings import ForeignRefs
from .protocol_type import Type

Enum = Optional[List[str]]

Items = Optional[Union[List[Type], Type]]


class Property(object):

    def __init__(self, owner: str, prop: dict) -> None:
        self.owner: str = owner
        self.name: str = prop["name"]
        self.description: Optional[str] = prop.get("description", None)
        self.foreign_refs: ForeignRefs = None
        self.type: Type = Type(prop)
        self._if_foreign_ref_add(self.type)
        self.enum: Enum = prop.get("enum", None)
        self.optional: bool = prop.get("optional", False)
        self.items: Items = self._build_items(
            prop["items"]
        ) if self.type.is_array else None

    @property
    def has_foreign_refs(self) -> None:
        return self.foreign_refs is not None

    @property
    def is_foreign_ref(self) -> bool:
        return self.type.is_ref and self.type.is_foreign_ref

    @property
    def foreign_ref(self) -> str:
        return self.type.foreign_ref

    @property
    def is_enum(self) -> bool:
        return self.enum is not None

    @property
    def is_array(self) -> bool:
        return self.type.is_array

    def _if_foreign_ref_add(self, t: Type) -> None:
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if t.is_foreign_ref:
            self.foreign_refs.add(t.foreign_ref)

    def _build_items(self, item_list: Union[dict, List]) -> Items:
        if isinstance(item_list, dict):
            t = Type(item_list)
            self._if_foreign_ref_add(t)
            return t
        elif isinstance(item_list, list):
            items = []
            for item in item_list:
                t = Type(item)
                self._if_foreign_ref_add(t)
                items.append(t)
                return item
        return None

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()
