import re
from typing import Any, DefaultDict, Dict, List, Optional, Pattern, Tuple, Union


__all__ = ["CDPType", "Command", "Domain", "Event", "Param", "Property", "ReturnValue"]

CDPTS = Union[str, "CDPType"]
OptStr = Optional[str]
OptParams = Optional[List["Param"]]
OptReturns = Optional[List["ReturnValue"]]
OptType = Optional["CDPType"]
OptTypeS = Optional[Union[str, "CDPType"]]
OptEvents = Optional[List["Event"]]
OptCommands = Optional[List["Command"]]
OptTypes = Optional[List["CDPType"]]
OptItems = Optional[Union[Dict[str, str], "CDPType"]]
OptDeps = Optional[List[str]]
OptEnum = Optional[List[str]]


remove_ptag: Pattern = re.compile("</p>", re.IGNORECASE)
split_nl: Pattern = re.compile("\n", re.IGNORECASE)
split_periods: Pattern = re.compile("[.]", re.IGNORECASE)


class PTPYT(Dict[str, str]):
    def __missing__(self, key) -> str:
        return "Any"


CDPT_PYT = PTPYT(
    binary="str",
    object="Dict[str, Any]",
    string="str",
    integer="int",
    number="Union[int, float]",
    boolean="bool",
    any="Any",
)


def prop_converters(props: Optional[List[Dict]]) -> Optional[Dict[str, "Property"]]:
    if props is None:
        return props
    converted: Dict[str, Property] = {}
    for prop in props:
        if "$ref" in prop:
            prop["ref"] = prop["$ref"]
            del prop["$ref"]
        converted[prop.get("name")] = Property(**prop)
    return converted


def correct_ref_name(type_obj: Dict) -> Dict:
    ref = type_obj.get("$ref")
    if ref:
        type_obj["ref"] = ref
        del type_obj["$ref"]

    items = type_obj.get("items")
    if items and "$ref" in items:
        items["ref"] = items["$ref"]
        del items["$ref"]
    return type_obj


def get_type_for_ref(
    ref: str,
    domain_types: Dict[str, "CDPType"],
    domains_types: DefaultDict[str, Dict[str, "CDPType"]],
) -> "CDPType":
    ref_type = domain_types.get(ref)
    if ref_type is None:
        domain, type_ = ref.split(".")
        other_domain_types = domains_types.get(domain)
        ref_type = other_domain_types.get(type_)
    return ref_type


def maybe_optional_type(optional: bool, type_str: str) -> str:
    if optional:
        return f"Optional[{type_str}] = None"
    return type_str


def clean_string(sting: str) -> str:
    return sting.rstrip().lstrip()


class Param:
    __slots__ = [
        "deprecated",
        "description",
        "enum",
        "experimental",
        "items",
        "name",
        "optional",
        "type",
    ]

    @classmethod
    def create(
        cls,
        cdp_param: Dict,
        our_types: Dict[str, "CDPType"],
        domain_types: DefaultDict[str, Dict[str, "CDPType"]],
    ) -> "Param":
        param = correct_ref_name(cdp_param)
        ref = param.get("ref")
        if ref:
            param_ref_type = get_type_for_ref(ref, our_types, domain_types)
            param["type"] = param_ref_type
            del param["ref"]
        items = param.get("items")
        if items:
            items = correct_ref_name(items)
            ref = items.get("ref")
            if ref:
                items_type = get_type_for_ref(ref, our_types, domain_types)
            else:
                items_type = items.get("type")
            param["items"] = items_type
        return cls(**param)

    def __init__(
        self,
        name: str,
        type: Union[str, "CDPType"],
        items: OptType = None,
        enum: OptEnum = None,
        description: OptStr = None,
        optional: bool = False,
        experimental: bool = False,
        deprecated: bool = False,
        **kwargs: Any,
    ) -> None:
        self.name: str = name
        self.type: Union[str, CDPType] = type
        self.items: OptType = items
        self.enum: OptEnum = enum
        self.description: OptStr = description
        self.optional: bool = optional
        self.experimental: bool = experimental
        self.deprecated: bool = deprecated

    def command_arg_string(self) -> str:
        if self.type == "array":
            if isinstance(self.items, CDPType):
                type_str = f"List[{self.items.py_typing()}]"
            else:
                type_str = f"List[{CDPT_PYT[self.items]}]"
        elif isinstance(self.type, CDPType):
            type_str = self.type.py_typing()
        else:
            type_str = CDPT_PYT[self.type]
        return f"{self.name}: {maybe_optional_type(self.optional, type_str)}"

    def doc_string(self) -> str:
        if self.description is not None:
            if "\n" in self.description:
                description_str = "\n         ".join(
                    split_nl.split(clean_string(self.description))
                )
            else:
                description_str = clean_string(self.description)
        else:
            description_str = f"The {self.name}"
        return f":param {self.name}: {description_str}"

    def __str__(self) -> str:
        return f"Param(name={self.name})"

    def __repr__(self) -> str:
        return self.__str__()


class Property:
    __slots__ = [
        "name",
        "description",
        "optional",
        "ref",
        "type",
        "items",
        "enum",
        "experimental",
    ]

    def __init__(
        self,
        name: str,
        description: OptStr = None,
        optional: bool = False,
        experimental: bool = False,
        ref: OptType = None,
        type: OptTypeS = None,
        items: OptItems = None,
        enum: OptEnum = None,
        **kwargs: Any,
    ) -> None:
        self.name: str = name
        self.description: OptStr = description
        self.ref: OptType = ref
        self.type: OptTypeS = type
        self.items: OptItems = items
        self.enum: OptEnum = enum
        self.optional: bool = optional
        self.experimental: bool = experimental

    @property
    def is_ref(self) -> bool:
        if self.ref is not None:
            return True
        if self.items is not None:
            return "ref" in self.items
        return False

    def py_typing(self) -> str:
        if isinstance(self.type, str):
            if self.type == "array":
                if isinstance(self.items, CDPType):
                    ptyping = f"List[{self.items.py_typing()}]"
                else:
                    ptyping = f"List[{CDPT_PYT[self.items.get('type')]}]"
            else:
                ptyping = CDPT_PYT[self.type]
            if self.optional:
                return f"Optional[{ptyping}]"
            return ptyping
        if self.type is not None:
            return self.type.py_typing()
        return self.ref.py_typing()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Property(name={self.name})"


class ReturnValue:
    __slots__ = ["description", "experimental", "items", "name", "optional", "type"]

    def __init__(
        self,
        name: str,
        type: Union[str, "CDPType"],
        description: OptStr = None,
        items: OptType = None,
        optional: bool = False,
        experimental: bool = False,
        **kwargs: Any,
    ) -> None:
        self.name: str = name
        self.type: Union[str, "CDPType"] = type
        self.description: OptStr = description
        self.items: OptType = items
        self.optional: bool = optional
        self.experimental: bool = experimental

    def py_typing(self) -> str:
        print(self.name)
        return ""

    def __str__(self) -> str:
        return f"ReturnValue(name={self.name})"

    def __repr__(self) -> str:
        return self.__str__()


class CDPType:
    __slots__ = [
        "deprecated",
        "description",
        "domain",
        "enum",
        "experimental",
        "items",
        "name",
        "optional",
        "properties",
        "refs",
        "type",
    ]

    @classmethod
    def create(cls, domain: str, cdp_type: Dict) -> "CDPType":
        name = cdp_type.get("id")
        cdp_type["name"] = name
        del cdp_type["id"]
        props = cdp_type.get("properties")
        refs = {}
        if props is not None:
            properties = {}
            for prop in props:
                _prop = Property(**correct_ref_name(prop))
                if _prop.is_ref:
                    refs[_prop.name] = _prop
                properties[_prop.name] = _prop
            cdp_type["properties"] = properties
        items = cdp_type.get("items")
        if items is not None:
            cdp_type["items"] = correct_ref_name(items)
        return cls(domain=domain, refs=refs, **cdp_type)

    def __init__(
        self,
        domain: str,
        refs: Dict[str, Any],
        name: str,
        type: str,
        items: Optional[Dict] = None,
        properties: Optional[Dict[str, Property]] = None,
        description: OptStr = None,
        enum: OptEnum = None,
        experimental: bool = False,
        deprecated: bool = False,
        optional: bool = False,
        **kwargs: Any,
    ) -> None:
        self.domain: str = domain
        self.refs: Dict[str, Any] = refs
        self.name: str = name
        self.type: str = type
        self.items: Optional[Dict] = items
        self.properties: Optional[Dict[str, Property]] = properties
        self.description: OptStr = description
        self.enum: OptEnum = enum
        self.experimental: bool = experimental
        self.deprecated: bool = deprecated
        self.optional: bool = optional

    @property
    def has_refs(self) -> bool:
        if self.items and "ref" in self.items:
            return True
        return len(self.refs) > 0

    def py_typing(self) -> str:
        if self.type == "array":
            type_str = f"List[{CDPT_PYT[self.items['type']]}]"
        else:
            type_str = CDPT_PYT[self.type]
        return maybe_optional_type(self.optional, type_str)

    def qualify_types(
        self, domain_to_types: DefaultDict[str, Dict[str, "CDPType"]]
    ) -> None:
        dtt_items = domain_to_types.items
        own_types = domain_to_types.get(self.domain, {})
        if self.items and "ref" in self.items:
            item_ref: str = self.items.get("ref")
            for domain, dts in dtt_items():
                if item_ref in dts:
                    self.items["ref"] = dts[item_ref]
                    break
        need_refs = len(self.refs)
        if need_refs > 0:
            prop_refs = set(self.refs.values())
            for prop in prop_refs:
                for domain, dts in dtt_items():
                    if prop.ref in dts:
                        prop.ref = dts[prop.ref]
                        need_refs -= 1
                        break
                if need_refs == 0:
                    break
        if self.properties:
            for prop in self.properties.values():
                if isinstance(prop.ref, str):
                    domain, domain_type = prop.ref.split(".")
                    dt = domain_to_types.get(domain, {}).get(domain_type)
                    prop.type = dt
                if prop.items and "ref" in prop.items:
                    prop_ref = prop.items.get("ref")
                    pt = own_types.get(prop_ref)
                    if pt:
                        prop.items = pt
                    else:
                        domain, domain_type = prop_ref.split(".")
                        dt = domain_to_types.get(domain, {}).get(domain_type)
                        if dt:
                            prop.items = dt

    def __str__(self) -> str:
        return f"CDPType(name={self.name}, domain={self.domain}, type={self.type})"

    def __repr__(self) -> str:
        return self.__str__()


class Command:
    __slots__ = [
        "deprecated",
        "description",
        "domain",
        "experimental",
        "name",
        "parameters",
        "redirect",
        "returns",
    ]

    @classmethod
    def create(
        cls,
        domain: str,
        cdp_command: Dict,
        domain_types: DefaultDict[str, Dict[str, "CDPType"]],
    ) -> "Command":
        params = []
        return_values = []
        add_param = params.append
        add_return = return_values.append
        create_param = Param.create

        our_types = domain_types.get(domain, {})

        for param in cdp_command.get("parameters", []):
            add_param(create_param(param, our_types, domain_types))

        for returns in cdp_command.get("returns", []):
            correct_ref_name(returns)
            items = returns.get("items")
            if items:
                ref = items.get("ref")
                if ref:
                    items_type = get_type_for_ref(ref, our_types, domain_types)
                else:
                    items_type = items.get("type")
                returns["items"] = items_type
            ref = returns.get("ref")
            if ref:
                returns["type"] = get_type_for_ref(ref, our_types, domain_types)
                del returns["ref"]
            add_return(ReturnValue(**returns))
        if params:
            cdp_command["parameters"] = params
        if return_values:
            cdp_command["returns"] = return_values
        return cls(domain=domain, **cdp_command)

    def __init__(
        self,
        domain: str,
        name: str,
        experimental: bool = False,
        deprecated: bool = False,
        parameters: OptParams = None,
        returns: OptReturns = None,
        description: OptStr = None,
        redirect: OptStr = None,
        **kwargs: Any,
    ) -> None:
        self.domain: str = domain
        self.name: str = name
        self.experimental: bool = experimental
        self.deprecated: bool = deprecated
        self.parameters: OptParams = parameters
        self.returns: OptReturns = returns
        self.description: OptStr = description
        self.redirect: OptStr = redirect

    @property
    def has_parameters(self) -> bool:
        return self.parameters is not None

    @property
    def has_description(self) -> bool:
        return self.description is not None

    @property
    def has_description_and_params(self) -> bool:
        return self.has_parameters and self.has_parameters

    @property
    def is_deprecation_or_experimental(self) -> bool:
        return self.deprecated or self.experimental

    def description_parts(self) -> List[str]:
        if self.description is None:
            return []
        return split_nl.split(self.description)

    def command_arg_string(self) -> str:
        if self.parameters is None:
            return ""
        return ", ".join([param.command_arg_string() for param in self.parameters])

    def command_sig(self) -> str:
        arg_str = f", {self.command_arg_string()}" if self.has_parameters else ""
        return f"def {self.name}(self{arg_str}) -> Awaitable[Dict]:"

    def command_link(self) -> str:
        url_domain = (
            f"https://chromedevtools.github.io/devtools-protocol/tot/{self.domain}"
        )
        return f"See `{url_domain}#method-{self.name}`"

    def deprecation_experimental_status(self) -> str:
        if self.deprecated and self.experimental:
            return "Status: Deprecated and Experimental"
        if self.deprecated:
            return "Status: Deprecated"
        if self.experimental:
            return "Status: Experimental"

    def required_optional_params(self) -> Tuple[OptStr, List[str]]:
        required = []
        optional = []
        add_req = required.append
        add_opt = optional.append
        for param in self.parameters:
            if param.optional:
                add_opt(param.name)
            else:
                add_req(f'"{param.name}": {param.name}')
        if required:
            return f"{{{', '.join(required)}}}", optional
        return None, optional

    def __str__(self) -> str:
        return f"Command(name={self.name}, domain={self.domain})"

    def __repr__(self) -> str:
        return self.__str__()


class Event:
    __slots__ = [
        "deprecated",
        "description",
        "domain",
        "experimental",
        "name",
        "parameters",
    ]

    @classmethod
    def create(
        cls,
        domain: str,
        cdp_event: Dict,
        domain_types: DefaultDict[str, Dict[str, "CDPType"]],
    ) -> "Event":
        cdp_params = cdp_event.get("parameters")
        our_types = domain_types.get(domain, {})
        if cdp_params:
            params = []
            add_param = params.append
            create_param = Param.create
            for param in cdp_params:
                add_param(create_param(param, our_types, domain_types))
            cdp_event["parameters"] = params
        return cls(domain=domain, **cdp_event)

    def __init__(
        self,
        name: str,
        domain: str,
        description: OptStr = None,
        parameters: OptParams = None,
        experimental: bool = False,
        deprecated: bool = False,
        **kwargs: Any,
    ) -> None:
        self.name: str = name
        self.domain: str = domain
        self.description: OptStr = description
        self.parameters: OptParams = parameters
        self.experimental: bool = experimental
        self.deprecated: bool = deprecated

    @property
    def has_description(self) -> bool:
        return self.description is not None

    def description_parts(self) -> List[str]:
        if not self.has_description:
            return []
        return split_nl.split(self.description)

    def event_sig(self) -> str:
        if self.parameters is not None:
            return "Dict[str, Any]"
        return "Any"

    def event_link(self) -> str:
        url_domain = (
            f"https://chromedevtools.github.io/devtools-protocol/tot/{self.domain}"
        )
        return f"See `{url_domain}#event-{self.name}`"

    def __str__(self) -> str:
        return f"Event(name={self.name}, domain={self.domain})"

    def __repr__(self) -> str:
        return self.__str__()


class Domain:
    __slots__ = [
        "commands",
        "dependencies",
        "deprecated",
        "description",
        "domain",
        "events",
        "experimental",
        "types",
    ]

    def __init__(
        self,
        domain: str,
        description: OptStr = None,
        events: OptEvents = None,
        commands: OptCommands = None,
        types: OptTypes = None,
        dependencies: OptDeps = None,
        experimental: bool = False,
        deprecated: bool = False,
        **kwargs: Any,
    ) -> None:
        self.domain: str = domain
        self.description: OptStr = description
        self.events: OptEvents = events
        self.commands: OptCommands = commands
        self.types: OptTypes = types
        self.dependencies: OptDeps = dependencies
        self.experimental: bool = experimental
        self.deprecated: bool = deprecated

    @property
    def has_dependencies(self) -> bool:
        return self.dependencies is not None

    @property
    def has_description(self) -> bool:
        return self.description is not None

    @property
    def has_commands(self) -> bool:
        return self.commands is not None

    @property
    def has_events(self) -> bool:
        return self.events is not None

    @property
    def has_types(self) -> bool:
        return self.events is not None

    @property
    def name(self) -> str:
        return self.domain

    def description_parts(self) -> List[List[str]]:
        parts = []
        if self.description is not None:
            if "\n" in self.description:
                parts.append(
                    ["\n    ".join(split_nl.split(clean_string(self.description)))]
                )
            else:
                parts.append([clean_string(self.description)])
        if self.dependencies is not None:
            if len(parts) != 0:
                parts.append([" "])
            dep_strs = ["Domain Dependencies: "]
            add_depstr = dep_strs.append
            for dep in self.dependencies:
                add_depstr(f"  * {dep}")
            parts.append(dep_strs)
        if self.deprecated and self.experimental:
            parts.append([f"Status: Deprecated and Experimental"])
        elif self.deprecated:
            parts.append([f"Status: Deprecated"])
        elif self.experimental:
            parts.append([f"Status: Experimental"])
        if len(parts) != 0:
            parts.append([" "])
        parts.append(
            [
                f"See `https://chromedevtools.github.io/devtools-protocol/tot/{self.domain}`"
            ]
        )
        return parts

    def __str__(self) -> str:
        return f"Domain(name={self.domain})"

    def __repr__(self) -> str:
        return self.__str__()
