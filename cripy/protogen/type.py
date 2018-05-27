
PT_PYT = dict(
    object="dict", string="str", integer="int", number="float", boolean="bool"
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
    def is_pytype(self) -> bool:
        return PT_PYT.get(self.type, None) is not None

    @property
    def pytype(self) -> str:
        return PT_PYT[self.type]

    @property
    def is_array(self) -> bool:
        return self.type == "array"

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
        return f"{self.type}"

    def __repr__(self) -> str:
        return self.__str__()
