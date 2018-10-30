from enum import Enum
from typing import Dict, List, Set, Union

from .ptype import Type

__all__ = ["InferredType", "Typer", "TYPER"]


PY_PRIMATIVES = {"str", "int", "float", "bool", "dict"}


class InferredType(Enum):
    OBJECT = "object"
    LIST = "list"
    ANYP = "any or primitive"


class Typer(object):
    def __init__(self) -> None:
        self.objects: Set[str] = set()
        self.primitives: Dict[str, str] = dict()
        self.lists: Set[str] = set()
        self.domain_types: dict = dict()
        self.domain_types_type_names: dict = dict()

    def clear(self):
        self.objects.clear()
        self.primitives.clear()
        self.lists.clear()
        self.domain_types.clear()
        self.domain_types_type_names.clear()

    def add_domain_type(self, dt) -> None:
        self.domain_types[dt.scoped_name] = dt
        self.domain_types_type_names[dt.id] = dt.type_name

    def constructor_sig(self, t: Union[List[Type], Type]) -> str:
        if isinstance(t, list):
            sigs = map(lambda x: self.constructor_sig(x), t)
            return ",".join(sigs)
        elif self.is_object(t):
            if str(t) in self.domain_types_type_names:
                return f"Union['{self.domain_types_type_names[str(t)]}', dict]"
            return f"Union['{t}', dict]"
        elif self.is_list(t):
            return "list"
        elif self.is_primitive_or_any(t):
            if not t.is_pytype:
                dt = self.domain_types.get(t)
                if dt is not None:
                    pts = dt.type.pytype_safe
                    if pts is not None:
                        return pts
                    else:
                        print("bbb", dt)
                else:
                    return self.primitives.get(t, f"'{t}'")
                return f"'{t}'"
            return f"{t}"
        return "Any"

    def command_sig(self, t: Union[List[Type], Type], domain) -> str:
        if isinstance(t, list):
            sigs = map(lambda x: self.command_sig(x, domain), t)
            return ",".join(sigs)
        elif self.is_object(t):
            return "dict"
        elif self.is_list(t):
            return "list"
        elif self.is_primitive_or_any(t):
            pt = t.pytype_safe
            if pt is not None:
                return pt
            dt = self.domain_types.get(t, self.domain_types.get(f"{domain}.{t}", None))
            if dt is not None:
                return dt.type
            if t.is_foreign_ref:
                res = f"{t}".replace(domain, "Types")
            else:
                if t.is_pytype:
                    res = f"{t}"
                else:
                    res = f"Types.{t}"
            return res

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
