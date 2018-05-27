from typing import Optional


class Parameter(object):
    pass


class ReturnType(object):
    pass


class Command(object):

    def __init__(self, command: dict) -> None:
        self.name: str = command["name"]
        self.description: Optional[str] = command.get("description", None)
        params = command.get("parameters", [])
        self.arity: int = len(params)
        print(command)
