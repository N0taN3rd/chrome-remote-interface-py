from pathlib import Path
from types import ModuleType
from typing import List, Dict, Tuple, Any

import aiofiles
from jinja2 import Template

from .domain import Domain
from .typer import TYPER
from ..templates import SIMPLE_PROTO_INIT_PATH, SIMPLE_COMMANDS_PATH


__all__ = [
    "onEvent",
    "create_domains",
    "get_default_templates",
    "generate_domain",
    "dynamically_generate_domains",
]


def onEvent(fe):
    return fe.split(".")[1]


def create_domains(protocol_info: Dict) -> List[Domain]:
    domains = []
    for domain in protocol_info["domains"]:
        domains.append(Domain(domain))
    return domains


def generate_domain(d: Domain, template, dp: Path) -> None:
    if d.has_commands:
        domain_sp = dp.joinpath(f"{d.domain.lower()}.py")
        events = []
        if d.has_events:
            for e in d.events:
                events.append((e.scoped_name, e.description))
        with domain_sp.open("w") as tout:
            tout.write(
                template.render(
                    d=d,
                    domain=d.domain,
                    description=d.description,
                    events=events,
                    onEvent=onEvent,
                )
            )


async def dynamically_generate_domains(protocol_info: Dict) -> Dict[str, Any]:
    async with aiofiles.open(SIMPLE_COMMANDS_PATH, "r") as iin:
        command_template = Template(
            await iin.read(), trim_blocks=True, lstrip_blocks=True
        )
    domains = create_domains(protocol_info)
    domain_classes = {}
    for d in domains:
        events = []
        if d.has_events:
            for e in d.events:
                events.append((e.scoped_name, e.description))
        code = compile(
            command_template.render(
                d=d,
                domain=d.domain,
                description=d.description,
                events=events,
                onEvent=onEvent,
            ),
            f"cripy/protocoldyn/{d.domain.lower()}.py",
            "exec",
        )
        module = ModuleType(f"cripy.protocoldyn.{d.domain.lower()}")
        exec(code, module.__dict__)
        name = code.co_names[-1]
        domain_classes[name] = getattr(module, d.domain)
    TYPER.clear()
    return domain_classes


def get_default_templates() -> Tuple[Template, Template]:
    with open(SIMPLE_COMMANDS_PATH, "r") as iin:
        command_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open(SIMPLE_PROTO_INIT_PATH, "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    return command_template, pinit
