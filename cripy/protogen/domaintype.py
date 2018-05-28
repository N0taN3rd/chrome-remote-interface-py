from typing import Optional, List, Dict
from collections import OrderedDict

from .shared import FRefCollector
from .property import Property
from .ptype import Type


Props = Optional[List[Property]]


class DomainType(FRefCollector):

    def __init__(self, domain: str, dt: dict) -> None:
        super().__init__()
        self.domain = domain
        self.id: str = dt["id"]
        self.scoped_name: str = f"{self.domain}.{self.id}"
        self.description: Optional[str] = dt.get("description", None)
        self.type: Type = Type(dt)
        self.experimental: bool = dt.get("experimental", False)
        self.properties: Props = self._build_props(dt.get("properties", None))

    @property
    def code_description(self) -> str:
        return " ".join(self.description.split("\n"))

    @property
    def is_array(self) -> bool:
        return self.type.is_array

    @property
    def is_object(self) -> bool:
        return self.type.is_object

    @property
    def has_properties(self):
        return self.properties is not None

    @property
    def properties_dict(self) -> Optional[Dict[str, Property]]:
        if not self.has_properties:
            return None
        pdict = OrderedDict()
        for prop in self.properties:
            pdict[prop.name] = prop
        return pdict

    @property
    def constructor_string(self) -> str:
        if self.type.is_object:
            if self.has_properties:
                optionals = []
                notoptional = []
                for prop in self.properties:
                    if prop.optional:
                        optionals.append(
                            prop.constructor_string.replace("'Any'", "Any")
                        )
                    else:
                        notoptional.append(
                            prop.constructor_string.replace("'Any'", "Any")
                        )
                return ", ".join(notoptional + optionals)
            else:
                return ""
        else:
            return ""

    def _build_props(self, props_list: Optional[List[dict]]) -> Props:
        if props_list is None:
            return props_list
        props = []
        for aprop in props_list:
            prop = Property(self.id, aprop)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props

    def __str__(self) -> str:
        if self.type.is_array:
            return f"{self.id}[]"
        elif self.type.is_object:
            if self.has_properties:
                ps = (
                    "\n "
                    + "\n ".join([prop.tinfo_str for prop in self.properties])
                    + "\n"
                )
            else:
                ps = ""
            return f"{self.id}" + " {%s}" % ps
        else:
            return f"{self.id}<{self.type}>"

    def __repr__(self) -> str:
        return self.__str__()
