from typing import Any, List, Optional, Union
from cripy.protocol.tethering import events as Events


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    async def bind(self, port: int) -> Optional[dict]:
        """
        :param port: Port number to bind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        res = await self.chrome.send('Tethering.bind', msg_dict)
        return res

    async def unbind(self, port: int) -> Optional[dict]:
        """
        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        res = await self.chrome.send('Tethering.unbind', msg_dict)
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

