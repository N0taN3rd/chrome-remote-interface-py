from typing import Optional, List

from .shared_typings import ForeignRefs
from .property import Property
from .protocol_type import Type

Props = Optional[List[Property]]


class DomainType(object):

    def __init__(self, dt: dict) -> None:
        self.id: str = dt["id"]
        self.description: Optional[str] = dt.get("description", None)
        self.type: Type = Type(dt)
        self.experimental: bool = dt.get("experimental", False)
        self.foreign_refs: ForeignRefs = None
        props = dt.get("properties", None)
        self.properties: Props = self._build_props(
            props
        ) if props is not None else props

    @property
    def has_foreign_refs(self) -> None:
        return self.foreign_refs is not None

    @property
    def has_properties(self):
        return self.properties is not None

    def _build_props(self, props_list: List[dict]) -> Props:
        props = []
        for aprop in props_list:
            prop = Property(self.id, aprop)
            self._if_prop_foreign_ref_add(prop)
            props.append(prop)
        return props

    def _if_prop_foreign_ref_add(self, prop: Property) -> None:
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if prop.is_foreign_ref:
            self.foreign_refs.add(prop.foreign_ref)
        if prop.has_foreign_refs:
            self.foreign_refs.update(prop.foreign_refs)
