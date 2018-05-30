from typing import List, Optional, Union, Iterator

from .shared import FRefCollector
from .property import Property
from .returns import Returns
from .typer import TYPER


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

    def _argstr(self, arg: Property) -> str:
        return f"{arg.name}={arg.name}"

    def stringify_thy_args(self) -> Iterator[str]:
        for parm in self.parameters:
            yield (f"if {arg.name} is not None")
        if len(self.parameters) > 0:
            dict_body = ", ".join(map(self._argstr, self.parameters))
            return f", dict({dict_body})"
        else:
            return ""

    @property
    def has_parameters(self) -> bool:
        return len(self.parameters) > 0

    @property
    def returns_something(self) -> bool:
        return self.returns is not None

    @property
    def returns_str(self) -> str:
        if self.returns is not None:
            return self.returns.returns_string
        else:
            return "None"

    @property
    def param_string(self) -> str:
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
    def command_arg_string(self) -> str:
        if self.has_parameters:
            optionals = []
            notoptional = []
            for prop in self.parameters:
                if prop.optional:
                    optionals.append(prop.command_arg_string(self.domain))
                else:
                    notoptional.append(prop.command_arg_string(self.domain))
            return ", ".join(notoptional + optionals)
        else:
            return ""

    @property
    def class_name(self) -> str:
        return self.name

    def _build_params(self, param_list: List[dict]) -> List[Property]:
        params = []
        for param in param_list:
            para = Property(self.name, param)
            self._if_foreign_ref_add(para)
            params.append(para)
        return params

    def _build_returns(self, command) -> Optional[Returns]:
        rt = command.get("returns", None)
        if rt is not None:
            returns = Returns(self.domain, self.name, rt)
            self._if_foreign_ref_add(returns)
            return returns
        else:
            return rt
