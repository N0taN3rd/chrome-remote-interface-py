from typing import List, Optional
from stringcase import pascalcase

from .property import Property
from .shared import FRefCollector

PropertyList = Optional[List[Property]]

__all__ = ["Event"]


class Event(FRefCollector):
    def __init__(self, domain: str, event: dict) -> None:
        super().__init__()
        self.domain: str = domain
        self.name: str = event["name"]
        self.scoped_name: str = f"{self.domain}.{self.name}"
        self.description: Optional[str] = self._get_description(event)
        self.parameters: PropertyList = self._build_parameters(
            event.get("parameters", None)
        )
        self._event = event

    @property
    def constructor_string(self) -> str:
        if self.has_parameters:
            optionals = []
            notoptional = []
            for prop in self.parameters:
                if prop.optional:
                    optionals.append(prop.constructor_string.replace("'", ""))
                else:
                    notoptional.append(prop.constructor_string.replace("'", ""))
            return ", ".join(notoptional + optionals)
        else:
            return ""

    @property
    def constructor_string_no_type(self) -> str:
        if self.has_parameters:
            optionals = []
            notoptional = []
            for prop in self.parameters:
                if prop.optional:
                    optionals.append(prop.constructor_string_no_type)
                else:
                    notoptional.append(prop.constructor_string_no_type)
            return ", ".join(notoptional + optionals)
        else:
            return ""

    def _get_description(self, event: dict) -> Optional[List[str]]:
        des = event.get("description", None)
        if des is not None:
            d = []
            for l in des.split("\n"):
                d.append(l.strip())
            return d
        return des

    @property
    def class_name(self) -> str:
        return f"{pascalcase(self.name)}Event"

    @property
    def has_parameters(self):
        return self.parameters is not None

    def _build_parameters(self, plist: Optional[List[dict]]) -> PropertyList:
        if plist is None:
            return plist
        props: List[Property] = list()
        for p in plist:
            prop = Property(self.scoped_name, p)
            prop.domain = self.domain
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props
