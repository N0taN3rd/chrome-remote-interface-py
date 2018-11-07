# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["ApplicationCache"]


@attr.dataclass(slots=True)
class ApplicationCache(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables application cache domain notifications.
        """
        return self.client.send("ApplicationCache.enable")

    def getApplicationCacheForFrame(self, frameId: str) -> Awaitable[Optional[dict]]:
        """
        Returns relevant application cache data for the document in given frame.

        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        return self.client.send(
            "ApplicationCache.getApplicationCacheForFrame", msg_dict
        )

    def getFramesWithManifests(self) -> Awaitable[Optional[dict]]:
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
        """
        return self.client.send("ApplicationCache.getFramesWithManifests")

    def getManifestForFrame(self, frameId: str) -> Awaitable[Optional[dict]]:
        """
        Returns manifest URL for document in the given frame.

        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        return self.client.send("ApplicationCache.getManifestForFrame", msg_dict)

    def applicationCacheStatusUpdated(
        self, cb: Optional[Callable[..., Any]] = None
    ) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("ApplicationCache.applicationCacheStatusUpdated", _cb)

            return future

        self.client.on("ApplicationCache.applicationCacheStatusUpdated", cb)

    def networkStateUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("ApplicationCache.networkStateUpdated", _cb)

            return future

        self.client.on("ApplicationCache.networkStateUpdated", cb)
