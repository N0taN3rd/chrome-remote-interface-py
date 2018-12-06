"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Inspector"]


@attr.dataclass(slots=True, cmp=False)
class Inspector(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Dict]:
        """
        Disables inspector domain notifications.
        """
        return self.client.send("Inspector.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables inspector domain notifications.
        """
        return self.client.send("Inspector.enable")

    def detached(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when remote debugging connection is about to be terminated. Contains detach reason.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Inspector.detached", _cb)

            return future

        self.client.on("Inspector.detached", cb)
        return lambda: self.client.remove_listener("Inspector.detached", cb)

    def targetCrashed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when debugging target has crashed
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Inspector.targetCrashed", _cb)

            return future

        self.client.on("Inspector.targetCrashed", cb)
        return lambda: self.client.remove_listener("Inspector.targetCrashed", cb)

    def targetReloadedAfterCrash(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Fired when debugging target has reloaded after crash
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Inspector.targetReloadedAfterCrash", _cb)

            return future

        self.client.on("Inspector.targetReloadedAfterCrash", cb)
        return lambda: self.client.remove_listener(
            "Inspector.targetReloadedAfterCrash", cb
        )
