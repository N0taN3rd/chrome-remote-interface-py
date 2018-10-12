# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["ApplicationCache"]


class ApplicationCache(object):
    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def enable(self) -> Optional[dict]:
        """
        Enables application cache domain notifications.
        """
        res = await self.client.send("ApplicationCache.enable")
        return res

    async def getApplicationCacheForFrame(self, frameId: str) -> Optional[dict]:
        """
        Returns relevant application cache data for the document in given frame.

        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        res = await self.client.send(
            "ApplicationCache.getApplicationCacheForFrame", msg_dict
        )
        return res

    async def getFramesWithManifests(self) -> Optional[dict]:
        """
        Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
        """
        res = await self.client.send("ApplicationCache.getFramesWithManifests")
        return res

    async def getManifestForFrame(self, frameId: str) -> Optional[dict]:
        """
        Returns manifest URL for document in the given frame.

        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        res = await self.client.send("ApplicationCache.getManifestForFrame", msg_dict)
        return res

    def applicationCacheStatusUpdated(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        if once:
            self.client.once("ApplicationCache.applicationCacheStatusUpdated", fn)
        else:
            self.client.on("ApplicationCache.applicationCacheStatusUpdated", fn)

    def networkStateUpdated(self, fn: Callable[..., Any], once: bool = False) -> None:
        if once:
            self.client.once("ApplicationCache.networkStateUpdated", fn)
        else:
            self.client.on("ApplicationCache.networkStateUpdated", fn)

    def __repr__(self):
        return f"ApplicationCache()"
