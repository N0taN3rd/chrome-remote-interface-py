from typing import List, Callable, Tuple, Dict, Union, Any

import attr
from pyee import EventEmitter

__all__ = ["Cleaner"]

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
