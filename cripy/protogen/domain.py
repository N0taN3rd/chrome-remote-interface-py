from typing import List, Optional

from .command import Command
from .domaintype import DomainType
from .event import Event
from .shared import FRefCollector


class Domain(FRefCollector):

    def __init__(self, domain: dict) -> None:
        super().__init__()
        self.domain: str = domain["domain"]
        self.types: List[DomainType] = self._build_dtypes(domain)
        self.commands: List[Command] = self._build_commands(domain)
        self.events: List[Event] = self._build_events(domain)
        self.dependencies: List[str] = domain.get("dependencies", [])
        self.description: Optional[str] = domain.get("description", None)
        self.prune(self.dependencies)
        self._domain = domain

    @property
    def has_deps(self) -> bool:
        return len(self.dependencies) > 0

    @property
    def dep_list_str(self) -> str:
        nice = map(lambda x: f"'{x}'", self.dependencies)
        return f"dependencies = [{', '.join(nice)}]"

    @property
    def has_types(self) -> bool:
        return len(self.types) > 0

    @property
    def has_events(self) -> bool:
        return len(self.events) > 0

    @property
    def has_commands(self) -> bool:
        return len(self.commands) > 0

    def _build_dtypes(self, domain: dict) -> List[DomainType]:
        domain_types: List[DomainType] = []
        for t in domain.get("types", []):
            dt = DomainType(self.domain, t)
            self._if_foreign_ref_add(dt)
            domain_types.append(dt)
        return domain_types

    def _build_commands(self, domain: dict) -> List[Command]:
        commands: List[Command] = []
        for c in domain.get("commands", []):
            comnd = Command(self.domain, c)
            self._if_foreign_ref_add(comnd)
            commands.append(comnd)
        return commands

    def _build_events(self, domain: dict) -> List[Event]:
        events: List[Event] = []
        for e in domain.get("events", []):
            event = Event(self.domain, e)
            self._if_foreign_ref_add(event)
            events.append(event)
        return events
