from typing import List, Optional, Set, Union

import textwrap

from .shared import FRefCollector
from .ptype import Type

Enum = Optional[List[str]]

Items = Optional[Union[List[Type], Type]]


def cstring_mapper(t: Type) -> Union[str, Type]:
    if not t.is_pytype and not t.is_array:
        return f"'{t}'"
    return t


def clean_string(s: str) -> str:
    print(s)
    return s.rstrip(" ").lstrip(" ")


class Property(FRefCollector):

    def __init__(self, owner: str, prop: dict) -> None:
        super().__init__()
        self.owner: str = owner
        self.name: str = prop["name"]
        self.scoped_name: str = f"{self.owner}.{self.name}"
        self.description: Optional[str] = prop.get("description", None)
        self.type: Type = Type(prop)
        self._if_foreign_ref_add(self.type)
        self.enum: Enum = prop.get("enum", None)
        self.optional: bool = prop.get("optional", False)
        self.items: Items = self._build_items(prop.get("items", None))
        self._oprop = prop

    def _wrap_if_optional(self, to_wrap: Union[str, Type]) -> str:
        if self.optional:
            return f"Optional[{to_wrap}]"
        return to_wrap

    def _wrap_if_optionalc(self, to_wrap: Union[str, Type]) -> str:
        if self.optional:
            return f"Optional[{to_wrap}] = None"
        return to_wrap

    @property
    def nice_description(self) -> str:
        return ' '.join(self.description.split('\n'))

    @property
    def tinfo_str(self) -> str:
        if self.is_array:
            ars = ",".join(self.items) if isinstance(self.items, list) else self.items
            ts = self._wrap_if_optional(f"List[{ars}]")
        else:
            ts = self._wrap_if_optional(self.type)
        return f"{self.name}: {ts}"

    @property
    def constructor_string(self) -> str:
        if self.is_array:
            if isinstance(self.items, list):
                ars = ",".join(map(cstring_mapper, self.items))
            else:
                ars = f"'{self.items}'"
            ts = self._wrap_if_optionalc(f"List[{ars}]")
        else:
            if not self.type.is_pytype and not self.type.is_array:
                ts_ = f"'{self.type}'"
            else:
                ts_ = self.type
            ts = self._wrap_if_optionalc(ts_)
        return f"{self.name}: {ts}"

    @property
    def foreign_ref(self) -> str:
        return self.type.foreign_ref

    @property
    def is_foreign_ref(self) -> bool:
        return self.type.is_ref and self.type.is_foreign_ref

    @property
    def is_enum(self) -> bool:
        return self.enum is not None

    @property
    def is_array(self) -> bool:
        return self.type.is_array

    def _build_items(self, item_list: Optional[Union[dict, List[dict]]]) -> Items:
        if item_list is None or not self.is_array:
            return None
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
