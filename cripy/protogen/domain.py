from typing import List, Optional, Set

from .domaintype import DomainType
from .command import Command


class Domain(object):

    def __init__(self, domain: dict) -> None:
        self.types: List[DomainType] = self._build_dtypes(domain)
        self.commands: List[Command] = self._build_commands(domain)
        self.deprefs: Set[str] = set(domain.get("dependencies", []))

    def _build_dtypes(self, domain: dict) -> List[DomainType]:
        domain_types: List[DomainType] = []
        for t in domain.get("types", []):
            dt = DomainType(t)
            domain_types.append(dt)
        return domain_types

    def _build_commands(self, domain: dict) -> List[Command]:
        commands: List[Command] = []
        for c in domain.get("commands", []):
            commands.append(Command(c))
        return commands
