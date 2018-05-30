import ujson as json
import os.path
from pathlib import Path

from jinja2 import Template

from cripy.protogen.domain import Domain


protocol_template = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "data/protocol.py.j2")
)
init_template = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "data/protocol_init.py.j2")
)
output_dir_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "cripy/protocol/")
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
        typep = dp.joinpath("types.py")
        with typep.open("w") as tout:
            tout.write(
                template.render(
                    py_types=py_types, obj_types=obj_types, timports=timports
                )
            )


def generate_events(d: Domain, template, dp: Path) -> None:
    if d.has_events:
        eventsp = dp.joinpath("events.py")
        with eventsp.open("w") as tout:
            event_to_clazz = []
            timports = set()
            types = set()
            for e in d.events:
                e.prune(set(e.domain))
                if e.has_foreign_refs:
                    timports.update(e.foreign_refs)
                if e.has_parameters:
                    for param in e.parameters:
                        if param.type.is_ref and not param.type.is_foreign_ref:
                            types.add(param.type)
                event_to_clazz.append((e.scoped_name, e.class_name))
            tout.write(
                template.render(
                    events=d.events,
                    domain=d.domain,
                    event_to_clazz=event_to_clazz,
                    timports=timports,
                    types=types,
                )
            )


def generate_commands(d: Domain, template, dp: Path) -> None:
    if d.has_commands:
        eventsp = dp.joinpath("__init__.py")
        with eventsp.open("w") as tout:
            timports = set()
            types = set()
            for e in d.commands:
                e.prune(set(e.domain))
                if e.has_foreign_refs:
                    timports.update(e.foreign_refs)
            timports.discard(d.domain)
            tout.write(
                template.render(
                    d=d,
                    domain=d.domain,
                    description=d.description,
                    timports=timports,
                    types=types,
                )
            )
    else:
        print(d)


def gen() -> None:
    with open("templates/domain_type.py.j2", "r") as iin:
        domain_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/events.py.j2", "r") as iin:
        event_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/commands.async.py.j2", "r") as iin:
        command_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/protocol_init.py.j2", "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

    domains = []
    mixin_imports = []
    for which, fp in [js_json_fp, browser_json_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            mixin_imports.append((domain['domain'].lower(), domain['domain']))
            domains.append(Domain(domain))
    for d in domains:
        dp = Path(output_dir_fp, d.domain.lower())
        if not dp.exists():
            dp.mkdir()
        generate_types(d, domain_template, dp)
        generate_events(d, event_template, dp)
        generate_commands(d, command_template, dp)
    init = Path(output_dir_fp, '__init__.py')
    with init.open('w') as out:
        out.write(pinit.render(domains=mixin_imports))
    from cripy.protocol import ProtocolMixin
    class IT(ProtocolMixin):
        pass
    print(IT().protocol_events)

if __name__ == "__main__":
    gen()
