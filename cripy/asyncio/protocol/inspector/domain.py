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
        mayberes = await self.chrome.send('Inspector.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables inspector domain notifications.
        """
        mayberes = await self.chrome.send('Inspector.enable')
        return mayberes

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

