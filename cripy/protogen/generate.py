from asyncio import AbstractEventLoop, get_event_loop
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from types import ModuleType
from typing import Any, DefaultDict, Dict, Generator, List, Optional, Tuple

import aiofiles
from jinja2 import Template

from .cdp import CDPType, Command, Domain, Event
from ..templates import SIMPLE_COMMANDS_PATH, SIMPLE_PROTO_INIT_PATH

__all__ = [
    "dynamically_generate_domains",
    "generate_domains",
    "generate_protocol_clazzs",
    "get_default_templates",
]


def generate_domains(cdp_domains: List[Dict]) -> Generator[Domain, None, None]:
    domain_types: DefaultDict[str, Dict[str, CDPType]] = defaultdict(dict)
    types_: List[CDPType] = []
    add_type = types_.append
    create_type = CDPType.create
    create_command = Command.create
    create_event = Event.create

    for cdp_domain in cdp_domains:
        types = cdp_domain.get("types")
        if types is not None:
            dname = cdp_domain.get("domain")
            for domain_type in cdp_domain.get("types"):
                t = create_type(dname, domain_type)
                domain_types[dname][t.name] = t
                add_type(t)

    for dt in types_:
        dt.qualify_types(domain_types)

    for cdp_domain in cdp_domains:
        domain_name = cdp_domain.get("domain")
        cdp_domain["types"] = domain_types.get(domain_name)

        cdp_commands: Optional[List[Dict]] = cdp_domain.get("commands")
        if cdp_commands:
            commands: List[Command] = []
            add_command = commands.append
            for command in cdp_commands:
                add_command(create_command(domain_name, command, domain_types))
            cdp_domain["commands"] = commands

        cdp_events: Optional[List[Dict]] = cdp_domain.get("events")
        if cdp_events:
            events: List[Event] = []
            add_event = events.append
            for event in cdp_events:
                add_event(create_event(domain_name, event, domain_types))
            cdp_domain["events"] = events

        yield Domain(**cdp_domain)


def generate_protocol_clazzs(cdp_domains: List[Dict], protocol_dir: Path) -> None:
    with open(SIMPLE_COMMANDS_PATH, "r") as iin:
        command_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open(SIMPLE_PROTO_INIT_PATH, "r") as iin:
        init_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    render_clazz = command_template.render
    inits = []
    add_init = inits.append
    for domain in generate_domains(cdp_domains):
        name = domain.name
        name_lower = name.lower()
        with (protocol_dir / f"{name_lower}.py").open("w") as out:
            out.write(render_clazz(d=domain))
            add_init((name_lower, name))
    with (protocol_dir / "__init__.py").open("w") as out:
        out.write(init_template.render(domains=sorted(inits, key=lambda x: x[1])))


async def dynamically_generate_domains(
    protocol_info: Dict, loop: Optional[AbstractEventLoop] = None
) -> Dict[str, Any]:
    if loop is None:
        loop = get_event_loop()
    async with aiofiles.open(SIMPLE_COMMANDS_PATH, mode="r", loop=loop) as iin:
        command_template = Template(
            await iin.read(), trim_blocks=True, lstrip_blocks=True
        )
    make_class = command_template.render
    domain_classes = {}
    domains = deepcopy(protocol_info["domains"])
    for domain in generate_domains(domains):
        domain_name = domain.domain.lower()
        code = compile(
            make_class(d=domain), f"cripy/protocoldyn/{domain_name}.py", "exec"
        )
        module = ModuleType(f"cripy.protocoldyn.{domain_name}")
        exec(code, module.__dict__)
        name = code.co_names[-1]
        domain_classes[name] = getattr(module, domain.domain)
    return domain_classes


def get_default_templates() -> Tuple[Template, Template]:
    with open(SIMPLE_COMMANDS_PATH, "r") as iin:
        command_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open(SIMPLE_PROTO_INIT_PATH, "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    return command_template, pinit
