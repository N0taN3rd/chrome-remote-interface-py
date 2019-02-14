from typing import List, Callable, Tuple, Dict, Union, Any, Optional

import attr
from pyee2 import EventEmitter

from cripy import Connection, Client, CDP

__all__ = [
    "Cleaner",
    "evaluation_result",
    "make_target_selector",
    "get_target_from_list",
]

EEListener = Dict[str, Union[str, EventEmitter, Callable]]


@attr.dataclass(slots=True)
class Cleaner(object):
    listeners: List[EEListener] = attr.ib(init=False, factory=list)
    disposables: List[Any] = attr.ib(init=False, factory=list)

    def addEventListener(
        self, emitter: EventEmitter, eventName: str, handler: Callable
    ) -> None:
        emitter.on(eventName, handler)
        self.listeners.append(
            dict(emitter=emitter, eventName=eventName, handler=handler)
        )

    def addEventListeners(
        self, emitter: EventEmitter, eventsHandlers: List[Tuple[str, Callable]]
    ) -> None:
        for eventName, handler in eventsHandlers:
            self.addEventListener(emitter, eventName, handler)

    def add_disposable(self, disposable: Any) -> None:
        self.disposables.append(disposable)

    async def clean_up(self) -> None:
        for listener in self.listeners:
            emitter = listener["emitter"]
            eventName = listener["eventName"]
            handler = listener["handler"]
            emitter.remove_listener(eventName, handler)
        self.listeners.clear()

        for disposable in self.disposables:
            if isinstance(disposable, EventEmitter):
                disposable.remove_all_listeners()
            await disposable.dispose()
        self.disposables.clear()


DefaultEvalArgs = dict(includeCommandLineAPI=True, awaitPromise=True, userGesture=True)


def merge_dicts(*dicts: Dict) -> Dict:
    merged: Dict = dict()
    for d in dicts:
        merged.update(d)
    return merged


async def evaluation_result(
    cdp_client: Union[Connection, Client], expression: str, **kwargs: Any
) -> Tuple[Any, Any]:
    args = merge_dicts(DefaultEvalArgs, kwargs)
    args["expression"] = expression
    if isinstance(cdp_client, Connection):
        result = await cdp_client.send("Runtime.evaluate", args)
    else:
        result = await cdp_client.Runtime.evaluate(**args)
    res = result.get("result")
    return res.get("type"), res.get("value")


def make_target_selector(which: str) -> Callable[[List[Dict[str, str]]], Any]:
    def target_selector(targets: List[Dict[str, str]]) -> Any:
        for idx, target in enumerate(targets):
            if target["type"] == "page":
                if which == "dict":
                    return target
                elif which == "idx":
                    return idx
                elif which == "str":
                    return target["webSocketDebuggerUrl"]

    return target_selector


async def get_target_from_list(
    return_what: str
) -> Optional[Union[Dict[str, str], str]]:
    targets = await CDP.List()
    for target in targets:
        if target["type"] == "page":
            if return_what == "target":
                return target
            elif return_what == "wsurl":
                return target["webSocketDebuggerUrl"]
            elif return_what == "id":
                return target["id"]
    return None
