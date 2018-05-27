from typing import List, Optional

from .property import Property
from .shared import FRefCollector

PropertyList = Optional[List[Property]]


class Event(FRefCollector):

    def __init__(self, domain: str, event: dict) -> None:
        super().__init__()
        self.domain: str = domain
        self.name: str = event["name"]
        self.scoped_name: str = f"{self.domain}.{self.name}"
        self.description: Optional[str] = event.get("description", None)
        self.properties: PropertyList = self._build_properties(
            event.get("properties", None)
        )

    @property
    def has_properties(self):
        return self.properties is not None

    def _build_properties(self, plist: Optional[List[dict]]) -> PropertyList:
        if plist is None:
            return plist
        props: List[Property] = list()
        for p in plist:
            prop = Property(self.scoped_name, p)
            self._if_foreign_ref_add(prop)
            props.append(prop)
        return props
