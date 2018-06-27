from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.inspector import events as Events

__all__ = ["Inspector"]


class Inspector(object):
    events = Events.INSPECTOR_EVENTS_NS

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

    def detached(self, fn, once=False):
        if once:
            self.chrome.once("Inspector.detached", fn)
        else:
            self.chrome.on("Inspector.detached", fn)

    def targetCrashed(self, fn, once=False):
        if once:
            self.chrome.once("Inspector.targetCrashed", fn)
        else:
            self.chrome.on("Inspector.targetCrashed", fn)

    def targetReloadedAfterCrash(self, fn, once=False):
        if once:
            self.chrome.once("Inspector.targetReloadedAfterCrash", fn)
        else:
            self.chrome.on("Inspector.targetReloadedAfterCrash", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.INSPECTOR_EVENTS_TO_CLASS

