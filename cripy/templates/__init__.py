import os.path

__all__ = ["SIMPLE_COMMANDS_PATH", "SIMPLE_PROTO_INIT_PATH"]

THIS_PATH = os.path.dirname(__file__)
SIMPLE_COMMANDS_PATH = os.path.join(THIS_PATH, "simple", "commands.async.py.j2")
SIMPLE_PROTO_INIT_PATH = os.path.join(THIS_PATH, "simple", "protocol_init.py.j2")
