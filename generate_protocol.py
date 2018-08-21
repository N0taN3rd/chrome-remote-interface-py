import ujson as json
import os.path
from pathlib import Path
from typing import Optional, List, Tuple

from jinja2 import Template
from protogen.domain import Domain
from protogen.typer import TYPER
from stringcase import pascalcase, snakecase

output_dir_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "cripy/asyncio/")
)
output_dirsync_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "cripy/gevent")
)

version_def_fp = (
    "full",
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data/70.0.3521.2-protocol.json")
    ),
)

browser_json_fp = (
    "browser",
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data/browser_protocol.json")
    ),
)
js_json_fp = (
    "js",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "data/js_protocol.json")),
)
test_script_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "check_generation.py")
)


PT_PYT = dict(
    object="dict",
    string="str",
    integer="int",
    number="float",
    boolean="bool",
    any="Any",
)


def read_json(fp: str) -> dict:
    with open(fp, "r") as iin:
        return json.load(iin)


def dtype_name(dt, dname) -> str:
    if dt == dname:
        return f"{dt}T"
    else:
        return dt


def slotgen(props) -> str:
    l = list()
    for prop in props:
        l.append(f'"{prop.name}"')
    return ", ".join(l)


def event_ns_init(values) -> str:
    l = list()
    for ename, _ in values:
        prop = pascalcase(ename.split(".")[1])
        l.append(f'"{prop}"')
    return ", ".join(l)


def generate_types(d, template, dp) -> None:
    if d.has_types:
        obj_types = []
        py_types = []
        timports = set()
        for dt in sorted(d.types, key=lambda t: t.id, reverse=True):
            dt.prune(set(d.domain))
            if dt.has_foreign_refs:
                timports.update(dt.foreign_refs)
            if dt.is_object:
                obj_types.append(dt)
            else:
                py_types.append(dt)


def generate_events(d: Domain, template, dp: Path) -> Optional[List[Tuple[str, str]]]:
    if d.has_events:
        event_to_clazz = []
        for e in d.events:
            event_to_clazz.append((e.scoped_name, e.class_name))
            return event_to_clazz
    return None


def generate_commands(d: Domain, template, dp: Path, events) -> None:
    if d.has_commands:
        eventsp = dp.joinpath(f"{d.domain.lower()}.py")
        with eventsp.open("w") as tout:
            timports = set()
            types = set()
            for e in d.commands:
                e.prune(set(e.domain))
                if e.has_foreign_refs:
                    timports.update(e.foreign_refs)
            timports.discard(d.domain)
            timports.discard("IO")
            tout.write(
                template.render(
                    d=d,
                    domain=d.domain,
                    description=d.description,
                    timports=timports,
                    types=types,
                    slotgen=slotgen,
                    events=events,
                    onEvent=onEvent,
                )
            )
    else:
        print(d)


def onEvent(fe):
    return fe.split(".")[1]


def generate_domain_init(d: Domain, template, dp: Path) -> None:
    init_p = dp.joinpath(f"{d.domain.lower()}.py")
    with init_p.open("w") as tout:
        tout.write(template.render(d=d))


def proto_gen_good() -> None:
    from cripy.asyncio.client import Client
    c = Client("")


def gen() -> None:
    with open("templates/simple/commands.async.py.j2", "r") as iin:
        command_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/simple/protocol_init.py.j2", "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

    domains = []
    mixin_imports = []
    allstrs = []
    for which, fp in [version_def_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            mixin_imports.append((domain["domain"].lower(), domain["domain"]))
            allstrs.append(f'"{domain["domain"]}"')
            domains.append(Domain(domain))
    for d in domains:
        dp = Path(output_dir_fp)
        events = []
        if d.has_events:
            for e in d.events:
                events.append((e.scoped_name, e.description))
        generate_commands(d, command_template, dp, events)
    proto_gen_good()


def gen_no_types() -> None:
    with open("templates/simple/commands.py.j2", "r") as iin:
        command_template_sync = Template(
            iin.read(), trim_blocks=True, lstrip_blocks=True
        )
    with open("templates/simple/protocol_init.py.j2", "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

    domains = []
    mixin_imports = []
    allstrs = []
    for which, fp in [version_def_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            mixin_imports.append((domain["domain"].lower(), domain["domain"]))
            allstrs.append(f'"{domain["domain"]}"')
            domains.append(Domain(domain))
    for d in domains:
        dp_sync = Path(output_dirsync_fp)
        if not dp_sync.exists():
            dp_sync.mkdir(parents=True)
        events = []
        if d.has_events:
            for e in d.events:
                events.append((e.scoped_name, e.description))
        generate_commands(d, command_template_sync, dp_sync, events)
    init = Path(output_dirsync_fp, "__init__.py")
    with init.open("w") as out:
        out.write(pinit.render(domains=mixin_imports, which="gevent"))
    from cripy.gevent.protocol import ProtocolMixin

    class IT(ProtocolMixin):
        pass


if __name__ == "__main__":
    gen()
    # gen_no_types()
