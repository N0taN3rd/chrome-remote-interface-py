from typing import Optional, Any


def make_repr(class_name: str, *args: Any, **kwargs: Any) -> str:
    """Shamelessly stolen from PyFilesystem https://github.com/PyFilesystem/pyfilesystem2"""
    arguments = []
    for arg in args:
        arguments.append(repr(arg))
    for name, (value, default) in kwargs.items():
        if value != default:
            arguments.append("{}={!r}".format(name, value))
    return f"{class_name}({', '.join(arguments)})"


class ProtocolType:
    """
    Shamelessly stolen from chromewhip geenrate_protocol.py
    MIT Licence Copyright 2017 Robert Charles Smith (https://github.com/chuckus)
    """

    def to_dict(self):
        return self.__dict__
