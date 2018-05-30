from typing import Iterable, Dict, List, Optional, Set, Union
from enum import Enum

from cripy.protogen.ptype import Type

ForeignRefs = Optional[Set[str]]


class FRefCollector(object):

    def __init__(self) -> None:
        self.foreign_refs: Optional[Set[str]] = None

    def prune(self, remove_me: Iterable[str]) -> None:
        if self.has_foreign_refs:
            self.foreign_refs.difference_update(remove_me)
            if len(self.foreign_refs) == 0:
                self.foreign_refs = None

    @property
    def has_foreign_refs(self) -> bool:
        return self.foreign_refs is not None

    def _if_foreign_ref_add(self, it: Optional) -> None:
        if it is None:
            return
        if getattr(it, "is_foreign_ref", False):
            self._add_foreign_ref(it.foreign_ref)
        if getattr(it, "has_foreign_refs", False):
            self._add_foreign_ref(it.foreign_refs)

    def _add_foreign_ref(self, ref: Union[str, Iterable[str]]) -> None:
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if isinstance(ref, str):
            self.foreign_refs.add(ref)
        else:
            self.foreign_refs.update(ref)


PY_PRIMATIVES = {"str", "int", "float", "bool", "dict"}


class InferredType(Enum):
    OBJECT = "object"
    LIST = "list"
    ANYP = "any or primative"


class Typer(object):

    def __init__(self) -> None:
        self.objects: Set[str] = set()
        self.primitives: Dict[str, str] = dict()
        self.lists: Set[str] = set()

    def constructor_sig(self, t: Union[List[Type], Type]) -> str:
        if isinstance(t, list):
            sigs = map(lambda x: self.constructor_sig(x), t)
            return ",".join(sigs)
        elif self.is_object(t):
            return f"Union['{t}', dict]"
        elif self.is_list(t):
            return f"{t}"
        elif self.is_primitive_or_any(t):
            return f"{t}"
        print("wtf", t)

    def constructor_docstr(self, t: Union[List[Type], Type]) -> str:
        if isinstance(t, list):
            sigs = map(lambda x: self.constructor_sig(x), t)
            return ",".join(sigs)
        elif self.is_object(t):
            return "dict"
        elif self.is_primitive(t):
            ptype = t.pytype_safe
            if ptype is None:
                ptype = self.primitives.get(t.type, "Any")
            return ptype
        else:
            return "Any"

    def you_are_in(self, what: Union[str, Type]) -> InferredType:
        if self.is_object(what):
            return InferredType.OBJECT
        elif self.is_list(what):
            return InferredType.LIST
        else:
            return InferredType.ANYP

    def add_type(self, name: str, _type: Type) -> None:
        if _type.is_object:
            self.objects.add(name)
        elif _type.is_array:
            self.lists.add(name)
        else:
            self.primitives[name] = _type.pytype

    def is_object(self, what: Union[str, Type]) -> bool:
        if isinstance(what, Type):
            return str(what) in self.objects
        return what in self.objects

    def is_primitive(self, what: Union[str, Type]) -> bool:
        if isinstance(what, Type):
            t = str(what)
            return self.primitives.get(t, None) is not None or t in PY_PRIMATIVES
        return self.primitives.get(what, None) is not None or what in PY_PRIMATIVES

    def is_list(self, what: Union[str, Type]) -> bool:
        if isinstance(what, Type):
            return str(what) in self.lists
        return what in self.lists

    def is_primitive_or_any(self, what: Union[str, Type]) -> bool:
        if isinstance(what, Type):
            t = str(what)
        else:
            t = what
        if t == "Any":
            return True
        return self.is_primitive(t)


TYPER = Typer()
