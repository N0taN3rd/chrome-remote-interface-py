import subprocess
import traceback
from pathlib import Path

import ujson

from cripy.protogen import generate_protocol_clazzs


def gen() -> None:
    cwd = Path.cwd()
    with (cwd / "data" / "protocol.json").open("r") as pin:
        proto_data = ujson.load(pin)
    generate_protocol_clazzs(proto_data["domains"], cwd / "cripy" / "protocol")
    try:
        from cripy.client import Client

        c = Client("")
    except Exception:
        print("Client failed")
        traceback.print_exc()
    else:
        print("Client appears good")
    subprocess.run(["black", "cripy/"])


if __name__ == "__main__":
    gen()
