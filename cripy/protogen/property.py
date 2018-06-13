from typing import List, Optional, Set, Union

import textwrap

from .shared import FRefCollector
from .ptype import Type
from .typer import TYPER


Enum = Optional[List[str]]

Items = Optional[Union[List[Type], Type]]


def cstring_mapper(t: Type) -> Union[str, Type]:
    if not t.is_pytype and not t.is_array:
        return f"Union['{t}', dict]"
    return t


def clean_string(s: str) -> str:
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
        return " ".join(self.description.split("\n"))

    @property
    def tinfo_str(self) -> str:
        if self.is_array:
            ars = ",".join(self.items) if isinstance(self.items, list) else self.items
            ts = self._wrap_if_optional(f"List[{ars}]")
        else:
            ts = self._wrap_if_optional(self.type)
        return f"{self.name}: {ts}"

    @property
    def construct_thyself(self) -> str:
        if TYPER.is_object(self.type):
            return f"self.{self.name} = {self.type}.safe_create({self.name})"

        if self.type.is_array:
            if isinstance(self.items, list):
                print("we have multiple item types")
            else:
                if TYPER.is_primitive_or_any(self.items):
                    return f"self.{self.name} = {self.name}"
                else:
                    return f"self.{self.name} = {self.items.type}.safe_create_from_list({self.name})"
            # got

        return f"self.{self.name} = {self.name}"

    @property
    def construct_thyself_no_type(self) -> str:
        if TYPER.is_object(self.type):
            return f"self.{self.name} = {self.type}.safe_create({self.name})"
        return f"self.{self.name} = {self.name}"

    @property
    def constructor_string(self) -> str:
        if self.is_array:
            ars = TYPER.constructor_sig(self.items)
            if ars is None:
                print(
                    "wtf is_array",
                    self.name,
                    self.type,
                    self.items,
                    TYPER.you_are_in(self.items),
                )
            ts = self._wrap_if_optionalc(f"List[{ars}]")
        else:
            ars = TYPER.constructor_sig(self.type)
            if ars is None:
                print(
                    "wtf",
                    self.name,
                    self.type,
                    self.type.is_array,
                    self.items,
                    TYPER.you_are_in(self.items),
                )
            ts = self._wrap_if_optionalc(ars)
        return f"{self.name}: {ts}"

    @property
    def constructor_string_no_type(self) -> str:
        return f"{self.name}"

    def command_arg_string(self, domain) -> str:
        if self.is_array:
            ars = TYPER.command_sig(self.items, domain)
            if ars is None:
                print(
                    "wtf is_array",
                    self.name,
                    self.type,
                    self.items,
                    TYPER.you_are_in(self.items),
                )
            ts = self._wrap_if_optionalc(f"List[{ars}]")
        else:
            ars = TYPER.command_sig(self.type, domain)
            if ars is None:
                print(
                    "wtf",
                    self.name,
                    self.type,
                    self.type.is_array,
                    self.items,
                    TYPER.you_are_in(self.items),
                )
            ts = self._wrap_if_optionalc(ars)
        return f"{self.name}: {ts}"

    def command_arg_string_no_types(self, domain) -> str:
        return f"{self.name}"

    @property
    def constructor_docstr(self) -> str:
        if self.is_array:
            ars = TYPER.constructor_docstr(self.items)
            if ars is None:
                print(
                    "wtf constructor_docstr is_array",
                    self.name,
                    self.type,
                    self.items,
                    TYPER.you_are_in(self.items),
                )
            ts = self._wrap_if_optional(f"List[{ars}]")
        else:
            ts = self._wrap_if_optional(TYPER.constructor_docstr(self.type))
        return ts

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
