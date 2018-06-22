from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.console import events as Events
from cripy.asyncio.protocol.console import types as Types

__all__ = ["Console"]


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ['Runtime']

    events = Events.CONSOLE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Console object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clearMessages(self) -> Optional[dict]:
        """
        Does nothing.
        """
        mayberes = await self.chrome.send('Console.clearMessages')
        return mayberes

    async def disable(self) -> Optional[dict]:
        """
        Disables console domain, prevents further console messages from being reported to the client.
        """
        mayberes = await self.chrome.send('Console.disable')
        return mayberes

    async def enable(self) -> Optional[dict]:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        mayberes = await self.chrome.send('Console.enable')
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
        return Events.CONSOLE_EVENTS_TO_CLASS

