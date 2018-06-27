from typing import List

from .shared import FRefCollector
from .property import Property
from .typer import TYPER

__all__ = ["Returns"]


class Returns(FRefCollector):
    def __init__(self, domain, owner: str, rt: List[dict]) -> None:
        super().__init__()
        self.domain: str = domain
        self.owner: str = owner
        self.pytype: str = "dict"
        self.properties: List[Property] = self._build_properties(rt)

    def _build_properties(self, rt: List[dict]) -> List[Property]:
        props = []
        for aprop in rt:
            prop = Property(self.owner, aprop)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props

    def yield_result_trans(self):
        # print(f"yield_result_trans for {self.owner}")
        for p in self.properties:
            if TYPER.is_object(p.type):
                if p.type.is_foreign_ref:
                    t = p.type
                else:
                    t = f"Types.{p.type}"
                if p.name == "cssKeyframesRules":
                    print(p, p.type, t)
                yield f"res['{p.name}'] = {t}.safe_create(res['{p.name}'])"
            else:
                if p.type.is_array:
                    itms = p.items
                    scoped = f"{self.domain}.{itms.type}"
                    dt = TYPER.domain_types.get(scoped, None)
                    if dt is not None:
                        ts = f"{itms.type}"
                        if self.domain in ts:
                            scoped = f"Types.{ts}"
                        else:
                            scoped = scoped.replace(self.domain, "Types")
                        if dt.type.is_object:
                            yield (
                                f"res['{p.name}'] = "
                                f"{scoped}.safe_create_from_list(res['{p.name}'])"
                            )
                    else:
                        dt = TYPER.domain_types.get(itms.type)
                        if dt is not None:
                            if dt.type.is_object:
                                yield (
                                    f"res['{p.name}'] = "
                                    f"{dt.scoped_name}.safe_create_from_list(res['{p.name}'])"
                                )
                else:
                    scoped = f"{self.domain}.{p.type}"
                    dt = TYPER.domain_types.get(scoped, None)
                    if dt is not None:
                        if dt.type.is_object:
                            print(scoped.replace(self.domain, "Types"))
                            yield (
                                f"res['{p.name}'] = "
                                f"{scoped.replace(self.domain,'Types')}.safe_create_from_list(res['{p.name}'])"
                            )
                    else:
                        dt = TYPER.domain_types.get(p.type)
                        if dt is not None:
                            if dt.type.is_object:
                                yield (
                                    f"res['{p.name}'] = "
                                    f"{dt.scoped_name}.safe_create_from_list(res['{p.name}'])"
                                )

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
