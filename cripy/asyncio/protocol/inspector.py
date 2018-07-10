from typing import Any, List, Optional, Union


__all__ = ["Inspector"]


class Inspector(object):

    def __init__(self, chrome):
        """
        Construct a new Inspector object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        """
        Disables inspector domain notifications.
        """
        res = await self.chrome.send('Inspector.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables inspector domain notifications.
        """
        res = await self.chrome.send('Inspector.enable')
        return res

    def detached(self, fn, once=False) -> None:
        """
        Fired when remote debugging connection is about to be terminated. Contains detach reason.
        """
        if once:
            self.chrome.once("Inspector.detached", fn)
        else:
            self.chrome.on("Inspector.detached", fn)

    def targetCrashed(self, fn, once=False) -> None:
        """
        Fired when debugging target has crashed
        """
        if once:
            self.chrome.once("Inspector.targetCrashed", fn)
        else:
            self.chrome.on("Inspector.targetCrashed", fn)

    def targetReloadedAfterCrash(self, fn, once=False) -> None:
        """
        Fired when debugging target has reloaded after crash
        """
        if once:
            self.chrome.once("Inspector.targetReloadedAfterCrash", fn)
        else:
            self.chrome.on("Inspector.targetReloadedAfterCrash", fn)



