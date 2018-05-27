from typing import List, Optional, Union

from .shared import FRefCollector
from .property import Property
from .returns import Returns


class Command(FRefCollector):

    def __init__(self, domain: str, command: dict) -> None:
        super().__init__()
        self.domain: str = domain
        self.name: str = command["name"]
        self.scoped_name: str = f"{self.domain}.{self.name}"
        self.description: Optional[str] = command.get("description", None)
        params = command.get("parameters", [])
        self.arity: int = len(params)
        self.parameters: List[Property] = self._build_params(params)
        self.returns: Optional[Returns] = self._build_returns(command)

    def _build_params(self, param_list: List[dict]) -> List[Property]:
        params = []
        for param in param_list:
            para = Property(self.name, param)
            self._if_foreign_ref_add(para)
            params.append(para)
        return params

    def _build_returns(self, command) -> Optional[Returns]:
        rt = command.get("returns")
        if rt is not None:
            self.returns = Returns(self.name, rt)
            self._if_foreign_ref_add(rt)
        else:
            return rt
