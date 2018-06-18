from typing import Optional

PT_PYT = dict(
    object="dict",
    string="str",
    integer="int",
    number="float",
    boolean="bool",
    any="Any",
)


class Type(object):

    def __init__(self, t: dict) -> None:
        _type = t.get("type", None)
        if _type is not None:
            self.type: str = _type
            self.is_ref: bool = False
        else:
            self.type = t["$ref"]
            self.is_ref: bool = True

    @property
    def safe_type(self) -> str:
        if self.is_array:
            return "list"
        else:
            return self.pytype

    @property
    def pytype(self) -> str:
        return PT_PYT[self.type]

    @property
    def pytype_safe(self) -> Optional[str]:
        return PT_PYT.get(self.type, None)

    @property
    def is_pytype(self) -> bool:
        return PT_PYT.get(self.type, None) is not None

    @property
    def is_array(self) -> bool:
        return self.type == "array"

    @property
    def is_object(self) -> bool:
        return self.type == "object"

    @property
    def is_primitive(self) -> bool:
        return not self.is_array and not self.is_object and self.is_pytype

    @property
    def is_foreign_ref(self) -> bool:
        return "." in self.type

    @property
    def foreign_ref(self) -> str:
        return self.type.split(".")[0]

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.type == other
        elif isinstance(other, Type):
            return self.type == other.type and self.is_ref == self.is_ref
        else:
            return False

    def __str__(self) -> str:
        if self.is_pytype:
            return f"{self.pytype}"
        return f"{self.type}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self):
        return self.__str__().__hash__()
