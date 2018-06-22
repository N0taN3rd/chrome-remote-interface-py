from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.tethering import events as Events

__all__ = ["Tethering"]


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """

    events = Events.TETHERING_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Tethering object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def bind(self, port: int) -> Optional[dict]:
        """
        Request browser port binding.

        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        mayberes = await self.chrome.send('Tethering.bind', msg_dict)
        return mayberes

    async def unbind(self, port: int) -> Optional[dict]:
        """
        Request browser port unbinding.

        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        mayberes = await self.chrome.send('Tethering.unbind', msg_dict)
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
        return Events.TETHERING_EVENTS_TO_CLASS

