from collections import namedtuple

__all__ = ["make_namespace"]


def make_namespace(name, events):
    fields = []
    for field in events.keys():
        fields.append(field)
    clz = namedtuple(name, fields)
    return clz(**events)
