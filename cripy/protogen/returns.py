from typing import List

from .shared import FRefCollector, TYPER
from .property import Property


class Returns(FRefCollector):

    def __init__(self, owner: str, rt: List[dict]) -> None:
        super().__init__()
        self.owner: str = owner
        self.pytype: str = "dict"
        self.properties: List[Property] = self._build_properties(rt)
        for p in self.properties:
            if TYPER.is_object(p.type):
                print(p.type)

    def _build_properties(self, rt: List[dict]) -> List[Property]:
        props = []
        for aprop in rt:
            prop = Property(self.owner, aprop)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props

    def yield_result_trans(self):
        for p in self.properties:
            if TYPER.is_object(p.type):
                if p.type.is_foreign_ref:
                    t = p.type
                else:
                    t = f"Types.{p.type}"
                yield f"raw_res['{p.name}'] = {t}.safe_create(raw_res['{p.name}'])"

    @property
    def returns_string(self) -> str:
        if self.properties:
            optionals = []
            notoptional = []
            for prop in self.properties:
                if prop.optional:
                    optionals.append(prop.constructor_string.replace("'", ""))
                else:
                    notoptional.append(prop.constructor_string.replace("'", ""))
            return ", ".join(notoptional + optionals)
        else:
            return ""
