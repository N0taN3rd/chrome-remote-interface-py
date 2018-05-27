from typing import List, Optional, Union

from cripy.protogen.shared_typings import ForeignRefs
from .protocol_type import Type
from .property import Property


class Parameter(Property):
    pass


class Returns(object):

    def __init__(self, owner: str, rt: List[dict]) -> None:
        self.owner: str = owner
        self.pytype: str = "dict"
        self.foreign_refs: ForeignRefs = None
        self.properties: List[Property] = self._build_properties(rt)

    @property
    def has_foreign_refs(self) -> None:
        return self.foreign_refs is not None

    def _build_properties(self, rt: List[dict]) -> List[Property]:
        props = []
        for aprop in rt:
            prop = Property(self.owner, aprop)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props

    def _if_foreign_ref_add(self, p: Property) -> None:
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if p.is_foreign_ref:
            self.foreign_refs.add(p.foreign_ref)
        if p.has_foreign_refs:
            self.foreign_refs.update(p.foreign_refs)


class Command(object):

    def __init__(self, command: dict) -> None:
        self.name: str = command["name"]
        self.description: Optional[str] = command.get("description", None)
        params = command.get("parameters", [])
        self.foreign_refs: ForeignRefs = None
        self.arity: int = len(params)
        self.parameters: List[Parameter] = self._build_params(params)
        rt = command.get("returns")
        # print(command)
        self.returns: Optional[Returns] = Returns(
            self.name, rt
        ) if rt is not None else rt
        self._if_foreign_ref_add(self.returns)

    @property
    def has_foreign_refs(self) -> None:
        return self.foreign_refs is not None

    def _if_foreign_ref_add(self, p: Optional[Union[Property, Returns]]) -> None:
        if p is None:
            return
        if self.foreign_refs is None:
            self.foreign_refs = set()
        if isinstance(p, Property) and p.is_foreign_ref:
            self.foreign_refs.add(p.foreign_ref)
        if p.has_foreign_refs:
            self.foreign_refs.update(p.foreign_refs)

    def _build_params(self, param_list: List[dict]) -> List[Parameter]:
        params = []
        for param in param_list:
            para = Parameter(self.name, param)
            self._if_foreign_ref_add(para)
            params.append(para)
        return params
