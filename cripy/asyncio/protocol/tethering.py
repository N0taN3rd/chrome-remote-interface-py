from typing import Any, List, Optional, Union


__all__ = ["Tethering"]


class Tethering(object):
    """
    The Tethering domain defines methods and events for browser port binding.
    """


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
        res = await self.chrome.send('Tethering.bind', msg_dict)
        return res

    async def unbind(self, port: int) -> Optional[dict]:
        """
        Request browser port unbinding.

        :param port: Port number to unbind.
        :type port: int
        """
        msg_dict = dict()
        if port is not None:
            msg_dict['port'] = port
        res = await self.chrome.send('Tethering.unbind', msg_dict)
        return res

    def accepted(self, fn, once=False) -> None:
        """
        Informs that port was successfully bound and got a specified connection id.
        """
        if once:
            self.chrome.once("Tethering.accepted", fn)
        else:
            self.chrome.on("Tethering.accepted", fn)



