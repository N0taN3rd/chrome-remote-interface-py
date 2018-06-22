import ujson as json
import os.path
from pathlib import Path

from jinja2 import Template
from protogen.domain import Domain
from protogen.typer import TYPER
from stringcase import pascalcase

output_dir_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "cripy/asyncio/protocol/")
)
output_dirsync_fp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "cripy/gevent/protocol")
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

with open("templates/domain_init.py.j2", "r") as iin:
    DOMAIN_INIT = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

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
        typep = dp.joinpath("types.py")
        with typep.open("w") as tout:
            tout.write(
                template.render(
                    py_types=py_types,
                    obj_types=obj_types,
                    timports=timports,
                    domain=d.domain,
                    slotgen=slotgen,
                    dtype_name=dtype_name,
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
            timports.discard('IO')
            tout.write(
                template.render(
                    pascalcase=pascalcase,
                    dhastype=d.has_types,
                    events=d.events,
                    domain=d.domain,
                    event_to_clazz=event_to_clazz,
                    timports=timports,
                    types=types,
                    slotgen=slotgen,
                    event_ns_init=event_ns_init,
                )
            )


def generate_commands(d: Domain, template, dp: Path) -> None:
    if d.has_commands:
        eventsp = dp.joinpath("domain.py")
        with eventsp.open("w") as tout:
            timports = set()
            types = set()
            for e in d.commands:
                e.prune(set(e.domain))
                if e.has_foreign_refs:
                    timports.update(e.foreign_refs)
            timports.discard(d.domain)
            timports.discard('IO')
            tout.write(
                template.render(
                    d=d,
                    domain=d.domain,
                    description=d.description,
                    timports=timports,
                    types=types,
                    slotgen=slotgen,
                )
            )
    else:
        print(d)


def generate_domain_init(d: Domain, template, dp: Path) -> None:
    init_p = dp.joinpath("__init__.py")
    with init_p.open("w") as tout:
        tout.write(template.render(d=d))


def proto_gen_good() -> None:
    from cripy.asyncio.protocol import ProtocolMixin

    class IT(ProtocolMixin):
        pass


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
    allstrs = []
    for which, fp in [js_json_fp, browser_json_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            mixin_imports.append((domain["domain"].lower(), domain["domain"]))
            allstrs.append(f'"{domain["domain"]}"')
            domains.append(Domain(domain))
    for d in domains:
        dp = Path(output_dir_fp, d.domain.lower())
        if not dp.exists():
            dp.mkdir(parents=True)
        generate_types(d, domain_template, dp)
        generate_events(d, event_template, dp)
        generate_commands(d, command_template, dp)
        generate_domain_init(d, DOMAIN_INIT, dp)
    init = Path(output_dir_fp, "__init__.py")
    with init.open("w") as out:
        out.write(pinit.render(domains=mixin_imports, which="asyncio"))
    proto_gen_good()


def gen_no_types() -> None:
    with open("templates/domain_typent.py.j2", "r") as iin:
        domain_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/eventsnt.py.j2", "r") as iin:
        event_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/commands.py.j2", "r") as iin:
        command_template_sync = Template(
            iin.read(), trim_blocks=True, lstrip_blocks=True
        )
    with open("templates/protocol_init.py.j2", "r") as iin:
        pinit = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

    domains = []
    mixin_imports = []
    allstrs = []
    for which, fp in [js_json_fp, browser_json_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            mixin_imports.append((domain["domain"].lower(), domain["domain"]))
            allstrs.append(f'"{domain["domain"]}"')
            domains.append(Domain(domain))
    for d in domains:
        dp_sync = Path(output_dirsync_fp, d.domain.lower())
        if not dp_sync.exists():
            dp_sync.mkdir(parents=True)
        generate_types(d, domain_template, dp_sync)
        generate_events(d, event_template, dp_sync)
        generate_commands(d, command_template_sync, dp_sync)
        generate_domain_init(d, DOMAIN_INIT, dp_sync)
    init = Path(output_dirsync_fp, "__init__.py")
    with init.open("w") as out:
        out.write(pinit.render(domains=mixin_imports, which="gevent"))
    from cripy.gevent.protocol import ProtocolMixin

    class IT(ProtocolMixin):
        pass

    print(IT().protocol_events)


if __name__ == "__main__":
    gen()
    gen_no_types()
