from typing import List

from .shared import FRefCollector
from .property import Property


class Returns(FRefCollector):

    def __init__(self, owner: str, rt: List[dict]) -> None:
        super().__init__()
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
