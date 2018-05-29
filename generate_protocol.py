import ujson as json
import os.path
from pathlib import Path
import re
import sys

from jinja2 import Template

from cripy.protogen.domain import Domain
from cripy.protogen.shared import TYPER

# TODO: circular dependency below
# PACKAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
#
# sys.path.insert(0, PACKAGE_DIR)
#
# from chromewhip.helpers import camelize

FULL_CAP_WORDS = ["url", "dom", "css", "html"]


def camelize(string):
    words = string.split("_")
    result = words[0]
    for w in words[1:]:
        w = w.upper() if w in FULL_CAP_WORDS else w.title()
        result += w
    return result


camel_pat = re.compile(r"([A-Z]+)")

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

# https://stackoverflow.com/questions/17156078/converting-identifier-naming-between-camelcase-and-underscores-during-json-seria


JS_PYTHON_TYPES = {"string": "str", "number": "float", "integer": "int"}


def set_py_type(type_obj, type_ids_set):
    type_ = type_obj["type"]
    id_ = type_obj["id"]
    if re.match(r".*Id", id_) and id_[:2] in type_ids_set:
        new_type_ = "py_chrome_identifier"
    elif type_ == "array":
        item_type = type_obj["items"].get("$ref") or type_obj["items"].get("type")
        try:
            new_type_ = "[%s]" % JS_PYTHON_TYPES[item_type]
        except KeyError:
            new_type_ = "[%s]" % item_type
    elif type_ == "object":
        if not type_obj.get("properties"):
            new_type_ = "dict"
        else:
            new_type_ = "object"
    elif type_ in JS_PYTHON_TYPES.keys():
        new_type_ = JS_PYTHON_TYPES[type_]
    else:
        raise ValueError(
            'type "%s" is not recognised, check type data = %s' % (type_, type_obj)
        )
    type_obj["type"] = new_type_


# import autopep8


def collect_param_ref(params: list) -> set:
    collector = set()
    for param in params:
        pref = param.get("$ref", None)
        if pref is not None and "." in pref:
            collector.add(pref.split(".")[0])
        ptype = param.get("type", None)
        if ptype is not None and "array" in ptype:
            items = param.get("items")
            if isinstance(items, list):
                for itm in items:
                    iref = itm.get("$ref", None)
                    if iref is not None and "." in iref:
                        collector.add(iref.split(".")[0])
            elif isinstance(items, dict):
                iref = items.get("$ref", None)
                if iref is not None and "." in iref:
                    collector.add(iref.split(".")[0])
    return collector


def collect_deps_refs(domain: dict) -> list:
    depref = set()
    depref.update()
    for ddep in domain.get("dependencies", []):
        depref.add(ddep)
    for t in domain.get("types", []):
        tref = t.get("$ref", None)
        if tref is not None and "." in tref:
            depref.add(tref.split(".")[0])
        for tprop in t.get("properties", []):
            pref = tprop.get("$ref", None)
            if pref is not None and "." in pref:
                depref.add(pref.split(".")[0])
    for c in domain.get("commands", []):
        depref.update(collect_param_ref(c.get("parameters", [])))
        depref.update(collect_param_ref(c.get("returns", [])))
    for e in domain.get("events", []):
        depref.update(collect_param_ref(e.get("parameters", [])))
    return list(depref)


def main() -> None:
    domain_deprefs = {}
    for fpd in [js_json_fp, browser_json_fp]:
        pname, fp = fpd
        with open(fp) as jsonIN:
            data = json.load(jsonIN)
            for domain in data["domains"]:
                domain_deprefs[domain["domain"]] = collect_deps_refs(domain)
    processed_data = {}
    hashable_objs_per_prot = {}
    for fpd in [js_json_fp, browser_json_fp]:
        pname, fp = fpd
        with open(fp) as jsonIN:
            data = json.load(jsonIN)
        # first run
        hashable_objs = set()
        for domain in data["domains"]:

            for event in domain.get("events", []):
                event["py_class_name"] = (
                    event["name"][0].upper() + camelize(event["name"][1:]) + "Event"
                )

            # 12 Jul 9:37am - wont need this for now as have enhanced Id type
            # for cmd in domain.get('commands', []):
            #     for r in cmd.get('returns', []):
            #         # convert to non id
            #         if r.get('$ref', ''):
            #             r['$ref'] = re.sub(r'Id$', '', r['$ref'])

            for type_obj in domain.get("types", []):
                # we assume all type ids that contain `Id` are an alias for a built in type
                if any(
                    filter(lambda p: p["name"] == "id", type_obj.get("properties", []))
                ):
                    hashable_objs.add(type_obj["id"])

            # shorten references to drop domain if part of same module
            # for command in domain.get('commands', []):
            #     for parameter in command.get('parameters', []):
            #         ref = parameter.get('$ref')
            #         if ref and ref.split('.')[0] == domain['name']:
            #             print('modifying command "%s"' % '.'.join([domain['name'], command['name']]))
            #             ref

        hashable_objs_per_prot[pname] = hashable_objs
        processed_data[pname] = data
    # second run
    for k, v in processed_data.items():
        hashable_objs = hashable_objs_per_prot[k]
        for domain in v["domains"]:
            for type_obj in domain.get("types", []):
                # convert to richer, Python compatible types
                set_py_type(type_obj, hashable_objs)

            for event in domain.get("events", []):
                p_names = [p["name"] for p in event.get("parameters", [])]
                p_refs = [
                    (p["name"], p["$ref"])
                    for p in event.get("parameters", [])
                    if p.get("$ref")
                ]
                h_names = set(filter(lambda n: "id" in n or "Id" in n, p_names))
                for pn, pr in p_refs:
                    if pr in hashable_objs:
                        h_names.add(pn + "Id")
                event["hashable"] = list(h_names)
                event["is_hashable"] = len(event["hashable"]) > 0
    # finally write to file
    init_d = []
    with open(test_script_fp, "w") as testscript, open(protocol_template, "r") as pt:
        t = Template(pt.read(), trim_blocks=True, lstrip_blocks=True)
        for prot in processed_data.values():
            for domain in prot["domains"]:
                name = domain["domain"].lower()
                domain["dependencies"] = domain_deprefs[domain["domain"]]
                print(name, domain.get("dependencies", "nothing"))
                # if name == 'page':
                # domain['dependencies'].extend(['Runtime', 'Emulation'])

                init_d.append((name, domain["domain"]))
                with open(os.path.join(output_dir_fp, "%s.py" % name), "w") as f:
                    output = t.render(domain=domain)
                    f.write(output)
                    testscript.write("import cripy.protocol.%s\n" % name)

    init_p = os.path.join(output_dir_fp, "__init__.py")
    with open(init_p, "w") as init_out, open(init_template, "r") as it:
        t = Template(it.read(), trim_blocks=True, lstrip_blocks=True)
        output = t.render(domains=init_d)
        init_out.write(output)


def read_json(fp: str) -> dict:
    with open(fp, "r") as iin:
        return json.load(iin)


PT_PYT = dict(
    object="dict",
    string="str",
    integer="int",
    number="float",
    boolean="bool",
    any="Any",
)


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
            tout.write(template.render(events=d.events, domain=d.domain, event_to_clazz=event_to_clazz, timports=timports, types=types))


if __name__ == "__main__":
    with open("templates/domain_type.py.j2", "r") as iin:
        domain_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)
    with open("templates/events.py.j2", "r") as iin:
        event_template = Template(iin.read(), trim_blocks=True, lstrip_blocks=True)

    domains = []
    for which, fp in [js_json_fp, browser_json_fp]:
        data = read_json(fp)
        for domain in data["domains"]:
            domains.append(Domain(domain))
    for d in domains:
        dp = Path(output_dir_fp, d.domain.lower())
        if not dp.exists():
            dp.mkdir()
        generate_types(d, domain_template, dp)
        generate_events(d, event_template, dp)
